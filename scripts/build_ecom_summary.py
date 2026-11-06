import os, subprocess

css_shared = """
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');

@page {
    size: A4;
    margin: 15mm 15mm 18mm 15mm;
    @bottom-right {
        content: counter(page);
    }
}

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

body {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    color: #1e293b;
    line-height: 1.6;
    background: #ffffff;
    font-size: 13.5px;
    margin: 0;
    padding: 0;
}

body.ar {
    font-family: 'Cairo', 'Segoe UI', Tahoma, sans-serif;
    direction: rtl;
    text-align: right;
    line-height: 1.75;
}

.cover {
    background: linear-gradient(135deg, #047857 0%, #10b981 100%);
    color: #ffffff;
    padding: 40px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 10px 25px -5px rgba(16, 185, 129, 0.3);
}

.cover h1 {
    font-size: 28px;
    font-weight: 800;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
}

.cover .subtitle {
    font-size: 16px;
    opacity: 0.9;
    margin: 0 0 15px 0;
}

.cover .meta {
    display: flex;
    gap: 15px;
    font-size: 12px;
    opacity: 0.8;
}

.section {
    margin-bottom: 30px;
    page-break-inside: avoid;
}

h2 {
    font-size: 19px;
    font-weight: 700;
    color: #065f46;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}

body.ar h2 {
    color: #065f46;
}

h3 {
    font-size: 15px;
    font-weight: 600;
    color: #334155;
    margin-top: 18px;
    margin-bottom: 8px;
}

p {
    margin: 0 0 10px 0;
}

ul, ol {
    margin: 0 0 12px 0;
    padding-left: 22px;
}

body.ar ul, body.ar ol {
    padding-left: 0;
    padding-right: 22px;
}

li {
    margin-bottom: 4px;
}

.callout {
    background: #f8fafc;
    border-left: 4px solid #10b981;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin: 15px 0;
    font-size: 13px;
}

body.ar .callout {
    border-left: none;
    border-right: 4px solid #10b981;
    border-radius: 8px 0 0 8px;
}

.callout.warning {
    border-color: #f59e0b;
    background: #fffbeb;
}

.callout.tip {
    border-color: #059669;
    background: #ecfdf5;
}

.callout-title {
    font-weight: 700;
    margin-bottom: 4px;
    color: #065f46;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-size: 12.5px;
}

th, td {
    border: 1px solid #cbd5e1;
    padding: 8px 12px;
    text-align: left;
}

body.ar th, body.ar td {
    text-align: right;
}

th {
    background-color: #f1f5f9;
    font-weight: 700;
    color: #1e293b;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

.badge {
    display: inline-block;
    padding: 2px 8px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
    background: #d1fae5;
    color: #065f46;
}

.page-break {
    page-break-after: always;
}
"""

html_ecom_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>E-Commerce - Comprehensive Midterm Summary</title>
<style>{css_shared}</style>
</head>
<body>

<div class="cover">
    <h1>E-Commerce: Business, Technology, Society</h1>
    <div class="subtitle">Complete Midterm Study Guide & Comprehensive Knowledge Reference</div>
    <div class="meta">
        <span>Covering: Lecture 1, Chapter 2, Chapter 4, Chapter 5</span>
        <span>•</span>
        <span>Models, Infrastructure, SDLC, Security & Payment Systems</span>
    </div>
</div>

<div class="section">
    <h2>1. Introduction to Electronic Commerce & Fundamentals (Lecture 1)</h2>
    <p>Electronic Commerce (EC) represents digitally enabled commercial transactions between and among organizations and individuals. It transforms traditional business through telecommunications and the Internet.</p>

    <h3>1.1 Diverse Perspectives of E-Commerce</h3>
    <table>
        <tr>
            <th>Perspective</th>
            <th>Core Definition & Scope</th>
        </tr>
        <tr>
            <td><strong>Commercial (Trading)</strong></td>
            <td>Provides the capability of buying, selling, and exchanging products, services, and information over computer networks.</td>
        </tr>
        <tr>
            <td><strong>Business Process</strong></td>
            <td>Doing business electronically by completing workflows over networks, substituting digital information for physical processes.</td>
        </tr>
        <tr>
            <td><strong>Service</strong></td>
            <td>A tool that addresses the desire of firms, consumers, and management to cut service costs while improving the quality of goods and increasing delivery speed.</td>
        </tr>
        <tr>
            <td><strong>Collaborative & Learning</strong></td>
            <td>Enables online collaborative work, inter-organizational learning, information sharing, and global team coordination.</td>
        </tr>
    </table>

    <h3>1.2 Major Classifications by Market Relationship</h3>
    <ul>
        <li><strong>B2C (Business-to-Consumer):</strong> Online businesses selling merchandise or services directly to individual consumers (e.g. Amazon, Walmart.com). Highly visible to the public.</li>
        <li><strong>B2B (Business-to-Business):</strong> Businesses selling to other businesses (e.g. Grainger, Boeing parts procurement). <strong>Accounts for the vast majority of overall e-commerce dollar volume</strong>.</li>
        <li><strong>C2C (Consumer-to-Consumer):</strong> Consumers selling directly to other consumers, facilitated by a platform (e.g. eBay auctions, Craigslist, Etsy).</li>
        <li><strong>C2B (Consumer-to-Business):</strong> Consumers setting prices or requirements and businesses competing to satisfy them (e.g. Priceline's "Name Your Own Price", reverse auctions).</li>
        <li><strong>Intra-business EC (B2E - Business-to-Employee):</strong> Internal corporate portal activities, training, benefits selection, and employee self-service on private intranets.</li>
        <li><strong>Non-business EC:</strong> Religious, academic, non-profit institutions, and social agencies using the Internet to reduce costs and accept contributions.</li>
        <li><strong>B2G & G2C:</strong> Business-to-Government (public e-procurement) and Government-to-Citizen (online tax filing, renewing driver's licenses).</li>
    </ul>

    <h3>1.3 Pure vs. Partial E-Commerce (The 3 Dimensions)</h3>
    <p>EC is classified along 3 dimensions: <strong>(1) The Product/Service</strong>, <strong>(2) The Business Process</strong>, and <strong>(3) The Delivery Agent/Intermediary</strong>.</p>
    <ul>
        <li><strong>Traditional Brick-and-Mortar:</strong> All 3 dimensions are physical (physical store, cash payment, physical product).</li>
        <li><strong>Partial E-Commerce:</strong> At least one dimension is digital while others are physical. Example: buying a physical paperback book online on Amazon and having FedEx deliver it.</li>
        <li><strong>Pure E-Commerce:</strong> All 3 dimensions are entirely digital. Example: buying and downloading an ebook, software license, or streaming music directly online.</li>
    </ul>

    <h3>1.4 Benefits and Limitations of E-Commerce</h3>
    <table>
        <tr>
            <th>Dimension</th>
            <th>Key Benefits</th>
            <th>Limitations & Barriers</th>
        </tr>
        <tr>
            <td><strong>For Organizations</strong></td>
            <td>Global market reach, significant cost reductions, 24/7 continuous operations, rapid time to market, mass customization, and supply chain disintermediation.</td>
            <td><strong>Technical:</strong> Bandwidth constraints, software integration with legacy ERP systems, evolving security standards.</td>
        </tr>
        <tr>
            <td><strong>For Consumers</strong></td>
            <td>Unmatched convenience, massive product selection, instantaneous price comparison, customer reviews, and immediate delivery of digital goods.</td>
            <td><strong>Non-Technical:</strong> Lack of trust, privacy and security fears, inability to physically inspect items before purchase, resistance to change.</td>
        </tr>
        <tr>
            <td><strong>For Society</strong></td>
            <td>Enables telecommuting (reducing traffic congestion and pollution), delivers education/healthcare to remote rural communities.</td>
            <td>Digital divide, potential loss of local community retail jobs.</td>
        </tr>
    </table>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. E-Commerce Business Models & Concepts (Chapter 2)</h2>
    <div class="callout tip">
        <div class="callout-title">Definition of a Business Model</div>
        A <strong>Business Model</strong> is a set of planned activities designed to result in a profit in a marketplace. A business plan documents this model, and an e-commerce business model leverages Internet unique qualities.
    </div>

    <h3>2.1 The 8 Key Elements of a Business Model</h3>
    <table>
        <tr>
            <th>#</th>
            <th>Element</th>
            <th>Key Question Addressed</th>
            <th>Core Concept & Examples</th>
        </tr>
        <tr>
            <td>1</td>
            <td><strong>Value Proposition</strong></td>
            <td>Why should the customer buy from you?</td>
            <td>Defines how a product satisfies customer needs (convenience, lower price, personalization).</td>
        </tr>
        <tr>
            <td>2</td>
            <td><strong>Revenue Model</strong></td>
            <td>How will you earn money and generate profits?</td>
            <td>Advertising, Subscription, Transaction Fee, Sales, Affiliate models.</td>
        </tr>
        <tr>
            <td>3</td>
            <td><strong>Market Opportunity</strong></td>
            <td>What marketspace do you intend to serve, and what is its size?</td>
            <td>Realistic financial potential in the designated target niche.</td>
        </tr>
        <tr>
            <td>4</td>
            <td><strong>Competitive Environment</strong></td>
            <td>Who else occupies your intended marketspace?</td>
            <td>Direct competitors (similar products) and indirect competitors (substitute products).</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>Competitive Advantage</strong></td>
            <td>What special advantages does your firm possess?</td>
            <td>First-mover advantages, brand prestige, lower cost structures, patents, network effects.</td>
        </tr>
        <tr>
            <td>6</td>
            <td><strong>Market Strategy</strong></td>
            <td>How do you plan to promote your products to attract customers?</td>
            <td>Pricing, promotion channels, social media campaigns, SEO, distribution.</td>
        </tr>
        <tr>
            <td>7</td>
            <td><strong>Organizational Development</strong></td>
            <td>What types of organizational structures are necessary?</td>
            <td>Department divisions, reporting hierarchies, and functional workflow allocation.</td>
        </tr>
        <tr>
            <td>8</td>
            <td><strong>Management Team</strong></td>
            <td>What experience and background are important for leaders?</td>
            <td>Crucial for venture capital; demonstrates operational competence and execution ability.</td>
        </tr>
    </table>

    <h3>2.2 Major B2C Business Models</h3>
    <ul>
        <li><strong>Portal:</strong> Offers search tools and integrated content packages. <em>Horizontal Portals</em> (Yahoo, MSN) cover diverse topics. <em>Vertical Portals / Vortals</em> (Sailnet, WebMD) focus on niche industries.</li>
        <li><strong>E-tailer:</strong> Online retail store. Includes <em>Virtual Merchants</em> (pure-play like Amazon/Wayfair), <em>Clicks-and-Mortar</em> (multi-channel like Walmart, Best Buy), <em>Catalog Merchants</em> (L.L. Bean), and <em>Manufacturer-Direct</em> (Dell, Apple).</li>
        <li><strong>Content Provider:</strong> Distributes digital content (news, music, video). Monetizes via subscriptions (Netflix), micropayments, syndication, and advertising (WSJ, CNN).</li>
        <li><strong>Transaction Broker:</strong> Processes online transactions (Expedia, E*Trade). Value proposition is saving consumers time and money through instant execution.</li>
        <li><strong>Market Creator:</strong> Uses Internet technology to create digital platforms where buyers and sellers meet, negotiate, and transact (eBay, Uber, Airbnb).</li>
        <li><strong>Service Provider:</strong> Sells online services (Google Maps, Carbonite cloud backups, Dropbox).</li>
        <li><strong>Community Provider:</strong> Creates digital environments where people with similar interests congregate, share content, and communicate (Facebook, LinkedIn, iVillage).</li>
    </ul>

    <h3>2.3 Major B2B Business Models</h3>
    <ul>
        <li><strong>E-distributor:</strong> Supplies indirect MRO goods (maintenance, repair, and operations) directly to thousands of business buyers (e.g. W.W. Grainger).</li>
        <li><strong>E-procurement:</strong> Digital markets creating and selling access to digital procurement software (e.g. Ariba).</li>
        <li><strong>Exchanges (Net Marketplaces):</strong> Independently owned digital marketplaces connecting thousands of commercial suppliers and buyers for spot purchasing.</li>
        <li><strong>Industry Consortia:</strong> Industry-owned vertical markets owned by a small group of dominant purchasing enterprises.</li>
        <li><strong>Private Industrial Networks (PTX):</strong> Digital networks coordinating supply chain communications and collaborative design between a dominant firm (e.g. Walmart) and its key tier-1 suppliers.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>3. Building an E-Commerce Presence: Websites, Mobile Sites, and Apps (Chapter 4)</h2>
    <p>Developing an e-commerce presence requires synthesizing business objectives, technical infrastructure, software engineering, and mobile responsiveness.</p>

    <h3>3.1 The Systems Development Life Cycle (SDLC) - 5 Steps</h3>
    <table>
        <tr>
            <th>Step</th>
            <th>Phase Name</th>
            <th>Primary Activities & Deliverables</th>
        </tr>
        <tr>
            <td>1</td>
            <td><strong>Systems Analysis / Planning</strong></td>
            <td>Identify <strong>Business Objectives</strong> (what the site should do), <strong>System Functionalities</strong> (features needed), and <strong>Information Requirements</strong> (data elements required).</td>
        </tr>
        <tr>
            <td>2</td>
            <td><strong>Systems Design</strong></td>
            <td><strong>Logical Design:</strong> Data flow diagrams (DFD), entity-relationship models, processing logic.<br><strong>Physical Design:</strong> Hardware servers, software platforms, database engines, and telecommunications specs.</td>
        </tr>
        <tr>
            <td>3</td>
            <td><strong>Building the System</strong></td>
            <td>Decide between <em>In-house</em> build vs. <em>Outsourcing</em> development; choose hosting architecture (Self-hosting, Co-location, or Cloud/Managed Hosting).</td>
        </tr>
        <tr>
            <td>4</td>
            <td><strong>Testing</strong></td>
            <td><strong>Unit Testing:</strong> Testing individual program modules.<br><strong>System Testing:</strong> Testing the entire integrated multi-tier system under load.<br><strong>Acceptance Testing:</strong> Verifying system satisfies client business requirements.</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>Implementation & Maintenance</strong></td>
            <td>24/7/365 site monitoring, continuous security patching, benchmarking, database reorganization, and ongoing feature updates. <em>Dominates long-term lifetime costs</em>.</td>
        </tr>
    </table>

    <h3>3.2 Multi-Tier Architecture & Performance Optimization</h3>
    <ul>
        <li><strong>Multi-Tier Hierarchy:</strong>
            <ul>
                <li><strong>Tier 1 (Client):</strong> Browser or mobile app rendering HTML/CSS/JS.</li>
                <li><strong>Tier 2 (Web Server):</strong> Serves static assets, handles SSL/TLS termination, routes dynamic queries (e.g. Apache, NGINX).</li>
                <li><strong>Tier 3 (Application Server):</strong> Processes core business logic, shopping carts, taxes, and inventory workflows.</li>
                <li><strong>Tier 4 (Database Server):</strong> Manages relational/ACID data persistence, indexes, and transactions.</li>
            </ul>
        </li>
        <li><strong>Optimization Strategies:</strong> Caching in memory (Redis, Memcached), Content Delivery Networks (CDNs like Cloudflare), database connection pooling, image compression, and minimizing HTTP round-trip requests.</li>
    </ul>

    <h3>3.3 Mobile Presence: Responsive Web Design vs. Native Apps</h3>
    <table>
        <tr>
            <th>Approach</th>
            <th>Technology & Architecture</th>
            <th>Pros & Cons</th>
        </tr>
        <tr>
            <td><strong>Responsive Web Design (RWD)</strong></td>
            <td>Fluid grid layouts, flexible CSS media queries. Single codebase for all devices.</td>
            <td><strong>Pros:</strong> Cost-effective, universal reach, single maintenance URL.<br><strong>Cons:</strong> Limited access to native phone hardware, requires persistent connection.</td>
        </tr>
        <tr>
            <td><strong>Native Mobile App</strong></td>
            <td>Compiled platform code (Swift for iOS, Kotlin for Android).</td>
            <td><strong>Pros:</strong> Peak performance, full hardware integration (GPS, camera, push notifications, biometrics), offline capabilities.<br><strong>Cons:</strong> High development cost, requires app store approval and dual codebases.</td>
        </tr>
    </table>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>4. E-Commerce Security and Payment Systems (Chapter 5)</h2>

    <h3>4.1 The 6 Dimensions of E-Commerce Security</h3>
    <table>
        <tr>
            <th>Security Dimension</th>
            <th>Customer's Perspective</th>
            <th>Merchant's Perspective</th>
        </tr>
        <tr>
            <td><strong>Integrity</strong></td>
            <td>Has the information I transmitted or received been altered?</td>
            <td>Has data on the site or in the database been modified by unauthorized parties?</td>
        </tr>
        <tr>
            <td><strong>Non-repudiation</strong></td>
            <td>Can a merchant deny having received my payment?</td>
            <td>Can a customer order goods and falsely deny having placed the order?</td>
        </tr>
        <tr>
            <td><strong>Authenticity</strong></td>
            <td>Am I dealing with the real merchant and authentic website?</td>
            <td>What is the real identity of the customer making this purchase?</td>
        </tr>
        <tr>
            <td><strong>Confidentiality</strong></td>
            <td>Can unauthorized third parties view my messages or credit card details?</td>
            <td>Are corporate proprietary trade secrets and consumer data protected from snooping?</td>
        </tr>
        <tr>
            <td><strong>Privacy</strong></td>
            <td>Can I control the use and distribution of my personal profile data?</td>
            <td>Is personal information collected responsibly and compliant with privacy laws?</td>
        </tr>
        <tr>
            <td><strong>Availability</strong></td>
            <td>Can I access the e-commerce website whenever I need to shop?</td>
            <td>Is the server infrastructure resilient against crashes, outages, and DoS attacks?</td>
        </tr>
    </table>

    <h3>4.2 Major Security Threats</h3>
    <ul>
        <li><strong>Malware:</strong> Viruses (require host file execution), Worms (self-replicating autonomous programs), Trojan Horses (disguised malicious programs), Ransomware (extortion via data encryption).</li>
        <li><strong>Botnets:</strong> Networks of compromised zombie computers used to launch massive Distributed Denial of Service (DDoS) attacks.</li>
        <li><strong>Phishing & Spoofing:</strong> Deceptive emails and counterfeit clone websites designed to steal credentials. Pharming redirects domain traffic directly.</li>
        <li><strong>Hacking:</strong> White hats (ethical security researchers), Black hats (malicious criminals), Grey hats (unauthorized researchers without criminal intent).</li>
        <li><strong>Sniffing & Man-in-the-Middle (MitM):</strong> Eavesdropping on unencrypted network traffic or intercepting communication streams.</li>
    </ul>

    <h3>4.3 Technology Solutions: Cryptography & PKI</h3>
    <table>
        <tr>
            <th>Technology</th>
            <th>Mechanism</th>
            <th>Primary Application</th>
        </tr>
        <tr>
            <td><strong>Symmetric Encryption</strong></td>
            <td>Single shared secret key used for both encryption and decryption (AES, DES). Fast.</td>
            <td>Bulk payload data encryption. <em>Key distribution is the major challenge.</em></td>
        </tr>
        <tr>
            <td><strong>Asymmetric Encryption (Public Key)</strong></td>
            <td>Two mathematically linked keys: Public Key (shared freely for encryption) and Private Key (secret, for decryption).</td>
            <td>Secure key exchange, digital signatures (RSA, ECC). Solves key distribution.</td>
        </tr>
        <tr>
            <td><strong>Digital Signature</strong></td>
            <td>Message digest hashed and encrypted with the sender's Private Key.</td>
            <td>Guarantees <strong>Integrity</strong> and <strong>Non-repudiation</strong>. Verified using sender's public key.</td>
        </tr>
        <tr>
            <td><strong>Digital Certificate & CA</strong></td>
            <td>Digital document issued by a trusted Certificate Authority (CA) binding a public key to an entity's verified identity.</td>
            <td>Guarantees <strong>Authenticity</strong>, enabling HTTPS/SSL/TLS communication.</td>
        </tr>
        <tr>
            <td><strong>SSL/TLS & HTTPS</strong></td>
            <td>Combines asymmetric handshake for session key exchange and symmetric encryption for data stream.</td>
            <td>Secures client-server communication channels over the open Web.</td>
        </tr>
    </table>

    <h3>4.4 Online Payment Systems & Protocols</h3>
    <ul>
        <li><strong>Credit Card Transaction Flow:</strong> Consumer -> Merchant Gateway -> Acquiring Bank -> Card Brand Network (Visa/MC) -> Issuing Bank (authorizes fund transfer).</li>
        <li><strong>Digital Wallets (Apple Pay, PayPal, Google Pay):</strong> Store payment details securely. Modern wallets use <strong>Tokenization</strong>: replacing actual 16-digit card numbers with dynamic, one-time encrypted tokens.</li>
        <li><strong>3D Secure (Verified by Visa, Mastercard Identity Check):</strong> Adds multi-factor authentication (OTP/biometrics) during checkout, shifting chargeback fraud liability to the card issuer.</li>
        <li><strong>PCI-DSS Compliance:</strong> Mandatory security standard governing all organizations handling cardholder data to protect against breaches.</li>
    </ul>
</div>

</body>
</html>"""

html_ecom_ar = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>التجارة الإلكترونية (E-Commerce) - ملخص الميدتيرم الشامل</title>
<style>{css_shared}</style>
</head>
<body class="ar">

<div class="cover">
    <h1>التجارة الإلكترونية (E-Commerce: Business, Technology, Society)</h1>
    <div class="subtitle">الملخص الدراسي الشامل والموسوعة المرجعية لامتحان الميدتيرم</div>
    <div class="meta">
        <span>تغطية: المحاضرة 1، الفصل 2، الفصل 4، الفصل 5</span>
        <span>•</span>
        <span>النماذج التجارية، دورة حياة النظام، البنية التحتية، الأمان والمدفوعات</span>
    </div>
</div>

<div class="section">
    <h2>1. مقدمة في التجارة الإلكترونية والمفاهيم الأساسية (المحاضرة 1)</h2>
    <p>تُعرف التجارة الإلكترونية بأنها المعاملات التجارية المدعومة رقمياً بين المنظمات والأفراد عبر شبكات الحاسوب والإنترنت. تمثل تحولاً جذرياً في أداء الأعمال واستبدال الخطوات الورقية بالمعلومات الرقمية.</p>

    <h3>1.1 منظورات التجارة الإلكترونية المتعددة</h3>
    <table>
        <tr>
            <th>المنظور</th>
            <th>التعريف والنطاق الأكاديمي</th>
        </tr>
        <tr>
            <td><strong>المنظور التجاري (Trading)</strong></td>
            <td>إتاحة القدرة على بيع وشراء وتبادل المنتجات والخدمات والمعلومات عبر شبكات الاتصال والإنترنت.</td>
        </tr>
        <tr>
            <td><strong>منظور إجراءات العمل (Business Process)</strong></td>
            <td>ممارسة الأعمال إلكترونياً وأتمتة مسارات العمل وتدفق البيانات كبديل للمسارات والوثائق الورقية المادية.</td>
        </tr>
        <tr>
            <td><strong>منظور الخدمة (Service)</strong></td>
            <td>أداة استراتيجية لخفض تكاليف تقديم الخدمات مع تحسين جودة المنتجات وسرعة التوصيل للعملاء.</td>
        </tr>
        <tr>
            <td><strong>المنظور التعاوني والتعليمي</strong></td>
            <td>تمكين التعاون الرقمي بين المؤسسات والتعلم المشترك وتنسيق فرق العمل العالمية.</td>
        </tr>
    </table>

    <h3>1.2 تصنيفات التجارة الإلكترونية حسب أطراف السوق</h3>
    <ul>
        <li><strong>B2C (بين الشركات والمستهلك):</strong> بيع التجزئة المباشر من الشركات إلى الأفراد (مثل أمازون و وول مارت). وهو الأكثر شهرة وظهوراً للمستهلكين.</li>
        <li><strong>B2B (بين الشركات والشركات):</strong> بيع وتوريد الشركات لشركات أخرى. <strong>يمثل الحجم الأكبر على الإطلاق من حيث القيمة المالية والأثر الاقتصادي</strong>.</li>
        <li><strong>C2C (بين المستهلكين):</strong> بيع المستهلكين لبعضهم البعض عبر منصات وسيطة (مثل مزادات eBay والإعلانات المبوبة).</li>
        <li><strong>C2B (من المستهلك للشركات):</strong> قيام المستهلكين بتحديد السعر أو المواصفات، وتتنافس الشركات لتلبية طلباتهم (مثل نظام Priceline "حدد سعرك بنفسك").</li>
        <li><strong>Intra-business EC (التجارة الداخلية B2E):</strong> الأنشطة الإلكترونية داخل المؤسسة الواحدة عبر شبكة الإنترانت (تدريب الموظفين، إدارة المزايا، والخدمات الذاتية).</li>
        <li><strong>Non-business EC:</strong> استخدام المؤسسات غير الربحية والدينية والجامعات للإنترنت لجمع التبرعات وخفض التكاليف.</li>
        <li><strong>B2G و G2C:</strong> التعاملات الحكومية كالمناقصات والتوريدات الحكومية (B2G) وخدمات المواطنين الإلكترونية كدفع الضرائب واستخراج الرخص (G2C).</li>
    </ul>

    <h3>1.3 التجارة البحتة مقابل التجارة الجزئية (الأبعاد الثلاثة)</h3>
    <p>تُصنف التجارة الإلكترونية وفقاً لـ 3 أبعاد رئيسية: <strong>(1) المنتج/الخدمة</strong>، <strong>(2) عملية التداول</strong>، و <strong>(3) وكيل التوصيل/الوسيط</strong>.</p>
    <ul>
        <li><strong>التجارة التقليدية المادية:</strong> الأبعاد الثلاثة مادية بالكامل (متجر مادي، نقود ورقية، منتج ملموس).</li>
        <li><strong>التجارة الجزئية (Partial EC):</strong> بعد واحد على الأقل رقمي والأبعاد الأخرى مادية (مثال: طلب كتاب ورقي من أمازون وتوصيله عبر شركة شحن مادية).</li>
        <li><strong>التجارة البحتة (Pure EC):</strong> كافة الأبعاد الثلاثة رقمية 100% (مثال: شراء وتحميل كتاب إلكتروني، برمجيات، أو الاستماع للموسيقى عبر الإنترنت).</li>
    </ul>

    <h3>1.4 فوائد وعوائق التجارة الإلكترونية</h3>
    <table>
        <tr>
            <th>الطرف المستفيد</th>
            <th>الفوائد والمكاسب</th>
            <th>العوائق والمحددات</th>
        </tr>
        <tr>
            <td><strong>المؤسسات والشركات</strong></td>
            <td>الوصول للأسواق العالمية، خفض النفقات التشغيلية، العمل على مدار الساعة 24/7، وسرعة النزول بالمنتجات للسوق والتخصيص الشامل (Mass Customization).</td>
            <td><strong>عوائق تقنية:</strong> قيود سرعة الشبكات، صعوبة التكامل مع الأنظمة القديمة (Legacy Systems)، وسرعة تغير المعايير الأمنية.</td>
        </tr>
        <tr>
            <td><strong>المستهلكون</strong></td>
            <td>الراحة وسهولة الشراء من المنزل، خيارات لا حصر لها، المقارنة السريعة للأسعار، وقراءة تقييمات المشترين الآخرين.</td>
            <td><strong>عوائق غير تقنية:</strong> ضعف الثقة بالمتاجر المجهولة، الخوف على الخصوصية والبيانات المالية، والمقاومة الثقافية للتسوق عن بعد.</td>
        </tr>
        <tr>
            <td><strong>المجتمع</strong></td>
            <td>العمل عن بُعد وتقليل الزحام المروري والتلوث، وإيصال خدمات التعليم والصحة للمناطق الريفية النائية.</td>
            <td>الفجوة الرقمية (Digital Divide) وفقدان بعض وظائف التجزئة التقليدية.</td>
        </tr>
    </table>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. نماذج أعمال التجارة الإلكترونية وعناصرها الرئيسية (الفصل 2)</h2>
    <div class="callout tip">
        <div class="callout-title">تعريف نموذج الأعمال (Business Model)</div>
        هو مجموعة الأنشطة والخطط الهادفة لتحقيق الأرباح والمكاسب المالية داخل السوق المستهدف عبر استغلال قدرات الإنترنت الرقمية.
    </div>

    <h3>2.1 العناصر الثمانية الرئيسية لأي نموذج عمل ناجح</h3>
    <table>
        <tr>
            <th>#</th>
            <th>العنصر الاستراتيجي</th>
            <th>السؤال الجوهري الذي يجيب عليه</th>
            <th>المعنى والتطبيقات</th>
        </tr>
        <tr>
            <td>1</td>
            <td><strong>عرض القيمة (Value Proposition)</strong></td>
            <td>لماذا يجب على العميل الشراء منك أنت تحديداً؟</td>
            <td>كيف يلبي المنتج حاجة العميل بتميز (راحة، سعر أقل، تخصيص فريد).</td>
        </tr>
        <tr>
            <td>2</td>
            <td><strong>نموذج الإيرادات (Revenue Model)</strong></td>
            <td>كيف ستكسب الشركة الأموال والأرباح؟</td>
            <td>الإعلانات، الاشتراكات، رسوم المعاملات، المبيعات المباشرة، والتسويق بالعمولة.</td>
        </tr>
        <tr>
            <td>3</td>
            <td><strong>فرصة السوق (Market Opportunity)</strong></td>
            <td>ما هو السوق المستهدف وما حجمه المالي الواقعي؟</td>
            <td>حجم السوق الرقمي المتاح للشركة للمنافسة فيه.</td>
        </tr>
        <tr>
            <td>4</td>
            <td><strong>البيئة التنافسية (Competitive Environment)</strong></td>
            <td>من ينافسك في نفس السوق المستهدف؟</td>
            <td>المنافسون المباشرون (نفس المنتج) وغير المباشرين (منتجات بديلة).</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>الميزة التنافسية (Competitive Advantage)</strong></td>
            <td>ما الميزات الفريدة التي تمتلكها ولا يمتلكها غيرك؟</td>
            <td>ميزة السبق الأول (First-Mover)، انخفاض التكاليف، براءات الاختراع، وشهرة العلامة.</td>
        </tr>
        <tr>
            <td>6</td>
            <td><strong>استراتيجية السوق (Market Strategy)</strong></td>
            <td>كيف ستروج لمنتجاتك لجذب الجمهور والعملاء؟</td>
            <td>خطة المزيج التسويقي، حملات التواصل، تحسين محركات البحث، والانتشار.</td>
        </tr>
        <tr>
            <td>7</td>
            <td><strong>التطوير التنظيمي (Organizational Development)</strong></td>
            <td>كيف ستنظم الشركة العمل والإدارات لتنفيذ الخطة؟</td>
            <td>الهيكل الوظيفي، فرق العمل، خطوط الإدارة، ومسارات تدفق المهام.</td>
        </tr>
        <tr>
            <td>8</td>
            <td><strong>فريق الإدارة (Management Team)</strong></td>
            <td>ما هي خبرات وكفاءات قادة الشركة ومديريها؟</td>
            <td>العنصر الأكثر طلباً من المستثمرين؛ يثبت القدرة التنفيذية والخبرة السوقية.</td>
        </tr>
    </table>

    <h3>2.2 أبرز نماذج B2C</h3>
    <ul>
        <li><strong>البوابات (Portals):</strong> تقدم محركات بحث ومحتوى مجمع. تنقسم إلى <em>بوابات أفقية</em> عامة (Yahoo, MSN) و <em>بوابات رأسية متخصصة (Vortals)</em> تركز على قطاع محدد (مثل Sailnet أو WebMD).</li>
        <li><strong>تجار التجزئة الإلكترونيون (E-tailers):</strong> متاجر رقمية بحتة (Virtual Merchants مثل أمازون)، أو متاجر مدمجة مع فروع مادية (Clicks-and-Mortar مثل وول مارت)، أو متاجر مصنعين مباشرة (Dell).</li>
        <li><strong>مزودو المحتوى (Content Providers):</strong> توزيع المحتوى الرقمي (أخبار، موسيقى، فيديو) والربح عبر الاشتراكات، الدفع عند المشاهدة، أو الإعلانات (Netflix, WSJ).</li>
        <li><strong>وسطاء المعاملات (Transaction Brokers):</strong> تسهيل الصفقات وحجز السفر والتداول بأسلوب سريع وموفر للمال (Expedia, E*Trade).</li>
        <li><strong>صانعو الأسواق (Market Creators):</strong> بناء منصة تجمع البائعين والمشترين وتتقاضى نسبة على كل معاملة دون امتلاك السلع (eBay, Uber, Airbnb).</li>
    </ul>

    <h3>2.3 أبرز نماذج B2B</h3>
    <ul>
        <li><strong>الموزع الإلكتروني (E-distributor):</strong> تقديم كتالوج موحد لبيع منتجات الصيانة والإصلاح (MRO) لآلاف الشركات المشترية (مثل Grainger).</li>
        <li><strong>المشتريات الإلكترونية (E-procurement):</strong> بيع اشتراكات الوصول لمنصات أتمتة سلاسل التوريد الرقمية (مثل Ariba).</li>
        <li><strong>البورصات المستقلة (Exchanges):</strong> أسواق عامة تجمع آلاف الموردين والمشترين للشراء الفوري.</li>
        <li><strong>اتحادات الصناعة (Industry Consortia):</strong> أسواق قطاعية رأسية مملوكة لمجموعة من الشركات العملاقة في مجالها للتحكم في مشترياتها.</li>
        <li><strong>شبكات الصناعة الخاصة (Private Industrial Networks):</strong> شبكات رقمية مغلقة تربط شركة عملاقة (مثل Walmart) بمورديها الاستراتيجيين لتنسيق المخزون وتصميم المنتجات.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>3. بناء الحضور الإلكتروني: المواقع وتطبيقات الموبايل (الفصل 4)</h2>

    <h3>3.1 دورة حياة تطوير الأنظمة (SDLC) - المراحل الخمس</h3>
    <table>
        <tr>
            <th>المرحلة</th>
            <th>الاسم والهدف</th>
            <th>المخرجات والأنشطة الأساسية</th>
        </tr>
        <tr>
            <td>1</td>
            <td><strong>تخطيط وتحليل النظام</strong></td>
            <td>تحديد أهداف العمل (Business Objectives)، وظائف النظام البرمجية (System Functionalities)، ومتطلبات المعلومات (Information Requirements).</td>
        </tr>
        <tr>
            <td>2</td>
            <td><strong>تصميم النظام</strong></td>
            <td><strong>التصميم المنطقي:</strong> مخططات تدفق البيانات والعلاقات.<br><strong>التصميم المادي:</strong> مواصفات الخوادم، نظم التشغيل، وقواعد البيانات.</td>
        </tr>
        <tr>
            <td>3</td>
            <td><strong>بناء النظام والاستضافة</strong></td>
            <td>اتخاذ قرار البرمجة الداخلية أم الاستعانة بشركات خارجية (In-house vs. Outsource)؛ واختيار الاستضافة (ذاتية، مشتركة، Co-location، أو سحابية).</td>
        </tr>
        <tr>
            <td>4</td>
            <td><strong>الاختبار والتحقق</strong></td>
            <td><strong>اختبار الوحدات (Unit Testing):</strong> فحص كل كود برمجي منفصلاً.<br><strong>اختبار النظام:</strong> فحص النظام المجمع تحت الضغط.<br><strong>اختبار القبول (Acceptance Testing):</strong> اختبار رضا أصحاب الأعمال والعملاء.</td>
        </tr>
        <tr>
            <td>5</td>
            <td><strong>التشغيل والصيانة المستمرة</strong></td>
            <td>المراقبة 24/7، التحديثات الأمنية، وتطوير الميزات باستمرار. <em>تستحوذ الصيانة على الحصة الأكبر من تكاليف دورة حياة الموقع</em>.</td>
        </tr>
    </table>

    <h3>3.2 المعمارية متعددة الطبقات وتحسين الأداء</h3>
    <ul>
        <li><strong>المعمارية متعددة الطبقات (Multi-Tier):</strong>
            <ul>
                <li><strong>طبقة العميل (Client Tier):</strong> المتصفح أو تطبيق الموبايل لعرض الواجهات للمستخدم.</li>
                <li><strong>طبقة خادم الويب (Web Server):</strong> استقبال طلبات HTTP/HTTPS، تشفير SSL، وتقديم الملفات الثابتة.</li>
                <li><strong>طبقة خادم التطبيقات (Application Server):</strong> معالجة منطق العمل، عربة التسوق، حساب الضرائب، وإدارة المخزون.</li>
                <li><strong>طبقة خادم قواعد البيانات (Database Server):</strong> حفظ البيانات الدائمة وإجراء المعاملات المالية الموثوقة.</li>
            </ul>
        </li>
        <li><strong>استراتيجيات السرعة والتحسين:</strong> التخزين المؤقت في الذاكرة (Caching)، شبكات توزيع المحتوى (CDN)، وتجميع اتصالات قواعد البيانات (Connection Pooling).</li>
    </ul>

    <h3>3.3 استراتيجيات التواجد عبر الموبايل</h3>
    <table>
        <tr>
            <th>الاستراتيجية</th>
            <th>التقنية المعمارية</th>
            <th>المزايا والعيوب</th>
        </tr>
        <tr>
            <td><strong>التصميم المستجيب (Responsive Web Design - RWD)</strong></td>
            <td>تنسيقات CSS متغيرة وأطر مرنة تضبط مقاس الصفحة تلقائياً حسب الشاشة.</td>
            <td><strong>المزايا:</strong> تكلفة تطوير موحدة، رابط واحد للموقع، وتحديث فوري.<br><strong>العيوب:</strong> وصول محدود لحساسات الهاتف، وتعتمد على الاتصال الدائم بالإنترنت.</td>
        </tr>
        <tr>
            <td><strong>تطبيقات الموبايل الأصلية (Native Mobile Apps)</strong></td>
            <td>أكواد مخصصة لكل منصة (Swift للآيفون، Kotlin للأندرويد).</td>
            <td><strong>المزايا:</strong> سرعة فائقة، استغلال كامل لعتاد الهاتف (الكاميرا، GPS، الإشعارات، البصمة)، والعمل أوفلاين.<br><strong>العيوب:</strong> تكلفة عالية جداً، وموافقة متاجر التطبيقات.</td>
        </tr>
    </table>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>4. أمان التجارة الإلكترونية وأنظمة المدفوعات (الفصل 5)</h2>

    <h3>4.1 الأبعاد الستة لأمان التجارة الإلكترونية</h3>
    <table>
        <tr>
            <th>البعد الأمني</th>
            <th>منظور العميل</th>
            <th>منظور التاجر</th>
        </tr>
        <tr>
            <td><strong>التكامل وسلامة البيانات (Integrity)</strong></td>
            <td>هل تم تعديل بيانات طلبي أو الدفع أثناء الإرسال؟</td>
            <td>هل تم التلاعب بالبيانات أو الأسعار في موقعي وقاعدتي؟</td>
        </tr>
        <tr>
            <td><strong>عدم الإنكار (Non-repudiation)</strong></td>
            <td>هل يمكن للتاجر إنكار استلام الدفعة المالية؟</td>
            <td>هل يمكن للعميل إنكار قيامه بالطلب بعد إتمامه؟</td>
        </tr>
        <tr>
            <td><strong>الأصالة والتحقق (Authenticity)</strong></td>
            <td>هل الموقع الذي أتعامل معه هو المتجر الحقيقي وليس مزيفاً؟</td>
            <td>ما هي الهوية الحقيقية للمشتري الذي يقوم بالدفع الآن؟</td>
        </tr>
        <tr>
            <td><strong>السرية (Confidentiality)</strong></td>
            <td>هل يمكن لطرف ثالث مجهول قراءة رقم بطاقتي الائتمانية؟</td>
            <td>هل أسرار الشركة وبيانات العملاء محصنة ضد التجسس؟</td>
        </tr>
        <tr>
            <td><strong>الخصوصية (Privacy)</strong></td>
            <td>هل أمتلك السيطرة على بياناتي الشخصية واستخداماتها؟</td>
            <td>هل يتم جمع البيانات واستخدامها بمسؤولية وفقاً للقوانين؟</td>
        </tr>
        <tr>
            <td><strong>الإتاحة والتوافر (Availability)</strong></td>
            <td>هل الموقع يعمل ومتاح كلما رغبت بالتسوق؟</td>
            <td>هل بنيتي التحتية تصمد أمام الانهيارات وهجمات الحرمان من الخدمة؟</td>
        </tr>
    </table>

    <h3>4.2 التهديدات الأمنية الشائعة</h3>
    <ul>
        <li><strong>البرمجيات الخبيثة (Malware):</strong> الفيروسات (تحتاج ملفاً مضيفاً)، الديدان (برامج مستقلة تتكاثر ذاتياً عبر الشبكة)، أحصنة طروادة (برامج خبيثة متنكرة بزي برامج مفيدة)، وبرمجيات الفدية (تشفير البيانات وطلب فدية لفكها).</li>
        <li><strong>هجمات حجب الخدمة الموزعة (DDoS):</strong> استغلال شبكات أجهزة مخترقة (Botnets) لإغراق الخادم بطلبات وهمية وشل قدرته على خدمة العملاء الحقيقيين.</li>
        <li><strong>التصيد الاحتيالي (Phishing) وانتحال الشخصية:</strong> رسائل ومواقع مقلدة لخداع الضحايا لسرقة كلمات المرور والبطاقات.</li>
        <li><strong>القرصنة (Hacking):</strong> القبعات البيضاء (باحثون أمنيون أخلاقيون)، القبعات السوداء (مجرمون ومخربون)، والقبعات الرمادية (وسط بينهما).</li>
    </ul>

    <h3>4.3 الحلول التكنولوجية: التشفير والبنية التحتية للمفاتيح العامة (PKI)</h3>
    <table>
        <tr>
            <th>التقنية</th>
            <th>الآلية التقنية</th>
            <th>الوظيفة والتطبيق الرئيسي</th>
        </tr>
        <tr>
            <td><strong>التشفير المتماثل (Symmetric)</strong></td>
            <td>استخدام نفس المفتاح السري الوحيد للتشفير وفك التشفير (AES, DES). سريع جداً.</td>
            <td>تشفير البيانات الضخمة. <em>المشكلة الكبرى هي كيفية نقل المفتاح بأمان</em>.</td>
        </tr>
        <tr>
            <td><strong>التشفير غير المتماثل (Asymmetric)</strong></td>
            <td>مفتاحان رياضيان: مفتاح عام (Public Key) معلن للجميع للتشفير، ومفتاح خاص (Private Key) سري للمستلم فقط للفك.</td>
            <td>تبادل المفاتيح والتوقيع الرقمي (RSA). حل مشكلة توزيع المفاتيح نهائياً.</td>
        </tr>
        <tr>
            <td><strong>التوقيع الرقمي (Digital Signature)</strong></td>
            <td>تشفير بصمة الرسالة المجتزأة (Hash) بالمفتاح الخاص للراسل.</td>
            <td>يضمن <strong>سلامة البيانات (Integrity)</strong> و <strong>عدم الإنكار (Non-repudiation)</strong>.</td>
        </tr>
        <tr>
            <td><strong>الشهادات الرقمية (Certificates)</strong></td>
            <td>وثيقة رقمية تصدرها جهات توثيق معتمدة (CAs) لربط المفتاح العام بهوية صاحبه الحقيقية.</td>
            <td>تضمن <strong>الأصالة (Authenticity)</strong> وتفعيل بروتوكولات الأمان المشفرة HTTPS.</td>
        </tr>
        <tr>
            <td><strong>بروتوكول SSL/TLS</strong></td>
            <td>دمج التشفير غير المتماثل في المصافحة الأولية، ثم التشفير المتماثل لنقل البيانات المشفرة.</td>
            <td>حماية قنوات الاتصال بين المتصفح والخادم وتحويل الرابط إلى HTTPS.</td>
        </tr>
    </table>

    <h3>4.4 أنظمة المدفوعات الإلكترونية</h3>
    <ul>
        <li><strong>دورة دفع البطاقات:</strong> المشتري -> بوابة الدفع (Payment Gateway) -> بنك التاجر المحصل (Acquiring Bank) -> شبكة البطاقة (Visa/Mastercard) -> بنك العميل المصدر (Issuing Bank).</li>
        <li><strong>المحافظ الرقمية والترميز (Tokenization):</strong> استبدال رقم البطاقة الحقيقي برمز تشفيري مؤقت لا قيمة له في حال اختراق قاعدة بيانات التاجر.</li>
        <li><strong>بروتوكول 3D Secure:</strong> التحقق بخطوتين (OTP/بصمة) أثناء الشراء ونقل مسؤولية الاحتيال من التاجر إلى البنك المصدر.</li>
        <li><strong>معيار PCI-DSS:</strong> المعيار الأمني الدولي الإلزامي لحماية وتخزين بيانات حاملي البطاقات الائتمانية.</li>
    </ul>
</div>

</body>
</html>"""

with open('summaries/ECommerce_Summary_EN.html', 'w', encoding='utf-8') as f:
    f.write(html_ecom_en)
with open('summaries/ECommerce_Summary_AR.html', 'w', encoding='utf-8') as f:
    f.write(html_ecom_ar)

print("Saved HTML summaries for E-Commerce.")

# Compile to PDF using Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
for lang, fn_html, fn_pdf in [
    ('EN', 'summaries/ECommerce_Summary_EN.html', 'summaries/ECommerce_Summary_EN.pdf'),
    ('AR', 'summaries/ECommerce_Summary_AR.html', 'summaries/ECommerce_Summary_AR.pdf')
]:
    abs_html = os.path.abspath(fn_html)
    abs_pdf = os.path.abspath(fn_pdf)
    cmd = [
        chrome_path,
        '--headless=new',
        '--disable-gpu',
        '--no-pdf-header-footer',
        f'--print-to-pdf={abs_pdf}',
        f'file:///{abs_html.replace(os.sep, "/")}'
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    print(f"Compiled {fn_pdf} - Exists: {os.path.exists(abs_pdf)}, Size: {os.path.getsize(abs_pdf) if os.path.exists(abs_pdf) else 0}")
