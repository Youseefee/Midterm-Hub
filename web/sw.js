// Midterm Hub - Progressive Web App Service Worker (v6 - Network-First Always Fresh)
const CACHE_NAME = 'midterm-hub-v6';
const ASSETS_TO_CACHE = [
  '/',
  '/index.html',
  '/style.css?v=6',
  '/app.js?v=6',
  '/manifest.json',
  '/data/questions.js?v=6',
  '/data/summaries.js?v=6',
  '/icon-192.png',
  '/icon-512.png',
  '/icon-maskable-512.png',
  '/apple-touch-icon.png',
  '/favicon.ico'
];

// Strip redirected flag from responses so Service Worker navigation never throws ERR_FAILED
async function cleanResponse(response) {
  if (!response || !response.redirected) {
    return response;
  }
  const body = await response.blob();
  return new Response(body, {
    status: response.status,
    statusText: response.statusText,
    headers: response.headers
  });
}

self.addEventListener('install', (event) => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(async (cache) => {
      for (const asset of ASSETS_TO_CACHE) {
        try {
          const req = new Request(asset, { redirect: 'follow', cache: 'reload' });
          const res = await fetch(req);
          if (res && res.status === 200) {
            const cleanRes = await cleanResponse(res);
            await cache.put(asset, cleanRes);
          }
        } catch (err) {
          console.warn('Could not pre-cache asset:', asset, err);
        }
      }
    })
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  const url = new URL(event.request.url);
  if (url.protocol !== 'http:' && url.protocol !== 'https:') return;

  // Network-First for all requests so updates (questions, lectures, UI) appear immediately when online,
  // with full offline fallback to cached assets when offline.
  event.respondWith(
    fetch(event.request)
      .then(async (networkResponse) => {
        const cleanRes = await cleanResponse(networkResponse);
        if (cleanRes && cleanRes.status === 200 && cleanRes.type === 'basic') {
          const clone = cleanRes.clone();
          caches.open(CACHE_NAME).then((cache) => {
            cache.put(event.request, clone);
            if (event.request.mode === 'navigate') {
              cache.put('/', clone.clone());
            }
          });
        }
        return cleanRes;
      })
      .catch(async () => {
        const cache = await caches.open(CACHE_NAME);
        const exactMatch = await cache.match(event.request);
        if (exactMatch) return cleanResponse(exactMatch);

        const ignoreSearchMatch = await cache.match(event.request, { ignoreSearch: true });
        if (ignoreSearchMatch) return cleanResponse(ignoreSearchMatch);

        if (event.request.mode === 'navigate') {
          const cachedRoot = await cache.match('/');
          if (cachedRoot) return cleanResponse(cachedRoot);
          const cachedIndex = await cache.match('/index.html');
          if (cachedIndex) return cleanResponse(cachedIndex);
        }

        return new Response('Offline - Please check your connection.', {
          status: 503,
          headers: { 'Content-Type': 'text/plain; charset=utf-8' }
        });
      })
  );
});
