// Midterm Hub - Interactive Engine & PWA Controller (Organized by Lectures in Sequential Order)

document.addEventListener('DOMContentLoaded', () => {
  // App State
  const state = {
    currentSubject: 'dba', // 'dba' | 'ecom' | 'ir' | 'ba' | 'isapp'
    currentView: 'quiz', // 'quiz' | 'summaries'
    currentMode: 'practice', // 'practice' | 'exam'
    currentIndex: 0,
    answers: {}, // { [qId]: selectedIndex }
    flagged: new Set(),
    summaryLang: 'ar', // 'ar' | 'en'
    searchQuery: '',
    lectureFilter: 'all', // 'all' | '1' | '2' | ...
    topicFilter: 'all',
    statusFilter: 'all', // 'all' | 'unanswered' | 'incorrect' | 'flagged'
    theme: localStorage.getItem('theme') || 'light'
  };

  // Init Theme
  document.documentElement.setAttribute('data-theme', state.theme);
  const themeToggle = document.getElementById('theme-toggle');
  if (themeToggle) {
    themeToggle.textContent = state.theme === 'dark' ? '☀️' : '🌙';
  }

  // Load Data
  const rawQuizData = window.QUIZ_DATA || { dba: [], ecom: [], ir: [], ba: [], isapp: [] };
  const rawSummariesData = window.SUMMARIES_DATA || {};

  // Guarantee every question has accurate lecture_num, lecture, lecture_short, lecture_title, lecture_q_num, lecture_q_total
  const ORDINALS = {
    1: 'المحاضرة الأولى (Lecture 1)',
    2: 'المحاضرة الثانية (Lecture 2)',
    3: 'المحاضرة الثالثة (Lecture 3)',
    4: 'المحاضرة الرابعة (Lecture 4)',
    5: 'المحاضرة الخامسة (Lecture 5)'
  };
  const SHORTS = {
    1: 'المحاضرة 1 (Lec 1)',
    2: 'المحاضرة 2 (Lec 2)',
    3: 'المحاضرة 3 (Lec 3)',
    4: 'المحاضرة 4 (Lec 4)',
    5: 'المحاضرة 5 (Lec 5)'
  };
  const SUBJECT_RANGES = {
    dba: [
      { max: 65, num: 1, title: 'المحاضرة الأولى (Lecture 1): Introduction to DBA & Management Discipline' },
      { max: 108, num: 2, title: 'المحاضرة الثانية (Lecture 2): Physical Database Design, Storage & Indexing' },
      { max: 135, num: 3, title: 'المحاضرة الثالثة (Lecture 3): Partitioning, Clustering & Denormalization' },
      { max: 167, num: 4, title: 'المحاضرة الرابعة (Lecture 4): Application Development, SQL, Middleware & ORM' },
      { max: 200, num: 5, title: 'المحاضرة الخامسة (Lecture 5): Transactions, ACID, Concurrency & Locking' }
    ],
    ecom: [
      { max: 50, num: 1, title: 'المحاضرة الأولى (Lecture 1): Introduction to E-Commerce, Classifications & Benefits' },
      { max: 100, num: 2, title: 'المحاضرة الثانية (Lecture 2 - Ch 2): E-Commerce Business Models & Revenue Concepts' },
      { max: 150, num: 3, title: 'المحاضرة الثالثة (Lecture 3 - Ch 4): Building an E-Commerce Site, SDLC & Architecture' },
      { max: 200, num: 4, title: 'المحاضرة الرابعة (Lecture 4 - Ch 5): Online Security, Encryption & Payment Systems' }
    ],
    ir: [
      { max: 46, num: 1, title: 'المحاضرة الأولى (Lecture 1 - Ch 1): IR Fundamentals, Incidence Matrix & Inverted Index' },
      { max: 111, num: 2, title: 'المحاضرة الثانية (Lecture 2): Boolean Query Processing, Optimization & Phrase Queries' },
      { max: 129, num: 3, title: 'المحاضرة الثالثة (Lecture 3): Skip Pointers & Faster Postings Merges' },
      { max: 200, num: 4, title: 'المحاضرة الرابعة (Lecture 4 - Lec 5): Document Parsing, Tokenization, Normalization & Stemming' }
    ],
    ba: [
      { max: 66, num: 1, title: 'المحاضرة الأولى (Lecture 1 - Module 1): Introduction to Data Analytics & Analytical Types' },
      { max: 133, num: 2, title: 'المحاضرة الثانية (Lecture 2 - Ch 2): Decision Models, Break-Even & Optimization' },
      { max: 200, num: 3, title: 'المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables' }
    ],
    isapp: [
      { max: 100, num: 1, title: 'المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components' },
      { max: 200, num: 2, title: 'المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy' }
    ]
  };

  Object.keys(SUBJECT_RANGES).forEach(subj => {
    const list = rawQuizData[subj] || [];
    const ranges = SUBJECT_RANGES[subj];
    const counts = {};
    list.forEach((q, i) => {
      const qNum1 = i + 1;
      const matched = ranges.find(r => qNum1 <= r.max) || ranges[ranges.length - 1];
      const lnum = q.lecture_num || matched.num;
      q.lecture_num = lnum;
      q.lecture = q.lecture || ORDINALS[lnum];
      q.lecture_short = q.lecture_short || SHORTS[lnum];
      q.lecture_title = q.lecture_title || matched.title;
      if (!q.subtopic) {
        q.subtopic = (q.topic || '').replace(/^المحاضرة\s*\d+\s*\(Lec\s*\d+\)\s*•\s*/, '');
      }
      counts[lnum] = (counts[lnum] || 0) + 1;
    });
    const running = {};
    list.forEach(q => {
      const lnum = q.lecture_num;
      running[lnum] = (running[lnum] || 0) + 1;
      q.lecture_q_num = running[lnum];
      q.lecture_q_total = counts[lnum];
    });
  });

  // DOM Elements
  const tabQuiz = document.getElementById('tab-quiz');
  const tabSummaries = document.getElementById('tab-summaries');
  const viewQuiz = document.getElementById('view-quiz');
  const viewSummaries = document.getElementById('view-summaries');

  const pillDba = document.getElementById('pill-dba');
  const pillEcom = document.getElementById('pill-ecom');
  const pillIr = document.getElementById('pill-ir');
  const pillBa = document.getElementById('pill-ba');
  const pillIsapp = document.getElementById('pill-isapp');

  const modePractice = document.getElementById('mode-practice');
  const modeExam = document.getElementById('mode-exam');

  const lectureBarWrapper = document.getElementById('lecture-bar-wrapper');
  const lecturePillsContainer = document.getElementById('lecture-pills');
  const lectureSelect = document.getElementById('lecture-select');

  const statAnswered = document.getElementById('stat-answered');
  const statCorrect = document.getElementById('stat-correct');
  const statWrong = document.getElementById('stat-wrong');

  const topicSelect = document.getElementById('topic-select');
  const statusSelect = document.getElementById('status-select');
  const searchInput = document.getElementById('search-input');

  const questionsGrid = document.getElementById('questions-grid');
  const gridCount = document.getElementById('grid-count');

  const questionCard = document.getElementById('question-card');
  const qProgressFill = document.getElementById('q-progress-fill');
  const qLectureBanner = document.getElementById('q-lecture-banner');
  const qLecturePill = document.getElementById('q-lecture-pill');
  const qLectureTitle = document.getElementById('q-lecture-title');
  const qLectureOrder = document.getElementById('q-lecture-order');
  const qNum = document.getElementById('q-num');
  const qLectureBadge = document.getElementById('q-lecture-badge');
  const qTopic = document.getElementById('q-topic');
  const qBody = document.getElementById('q-body');
  const optionsList = document.getElementById('options-list');
  const explanationBox = document.getElementById('explanation-box');
  const explanationText = document.getElementById('explanation-text');
  const btnFlag = document.getElementById('btn-flag');

  const btnPrev = document.getElementById('btn-prev');
  const btnNext = document.getElementById('btn-next');

  const summaryFrame = document.getElementById('summary-frame');
  const summaryLangAr = document.getElementById('summary-lang-ar');
  const summaryLangEn = document.getElementById('summary-lang-en');
  const btnDownloadAr = document.getElementById('btn-download-ar');
  const btnDownloadEn = document.getElementById('btn-download-en');

  // Mobile Drawer Elements
  const btnOpenSidebar = document.getElementById('btn-open-sidebar');
  const sidebarCloseBtn = document.getElementById('sidebar-close-btn');
  const sidebarBackdrop = document.getElementById('sidebar-backdrop');
  const quizSidebar = document.getElementById('quiz-sidebar');
  const mobileQCount = document.getElementById('mobile-q-count');
  const mobileStatCorrect = document.getElementById('mobile-stat-correct');
  const mobileStatWrong = document.getElementById('mobile-stat-wrong');

  // PWA & Installation Elements
  const btnInstall = document.getElementById('btn-install');
  const mobileInstallBanner = document.getElementById('mobile-install-banner');
  const btnBannerInstall = document.getElementById('btn-banner-install');
  const btnBannerClose = document.getElementById('btn-banner-close');
  const installModal = document.getElementById('install-modal');
  const modalClose = document.getElementById('modal-close');
  const modalBody = document.getElementById('modal-body');

  // Helpers
  function getCurrentQuestions() {
    return rawQuizData[state.currentSubject] || [];
  }

  function getLecturesMetadata() {
    const questions = getCurrentQuestions();
    const map = new Map();
    questions.forEach((q, idx) => {
      const lnum = String(q.lecture_num || 1);
      if (!map.has(lnum)) {
        map.set(lnum, {
          num: lnum,
          label: q.lecture || `المحاضرة ${lnum} (Lecture ${lnum})`,
          shortLabel: q.lecture_short || `المحاضرة ${lnum}`,
          title: q.lecture_title || q.lecture || `Lecture ${lnum}`,
          firstQ: idx + 1,
          lastQ: idx + 1,
          count: 0
        });
      }
      const entry = map.get(lnum);
      entry.lastQ = idx + 1;
      entry.count++;
    });
    return Array.from(map.values());
  }

  function getFilteredQuestions() {
    const list = getCurrentQuestions();
    return list.filter((q) => {
      // Lecture Filter
      if (state.lectureFilter !== 'all' && String(q.lecture_num) !== String(state.lectureFilter)) {
        return false;
      }
      // Topic Filter
      if (state.topicFilter !== 'all' && q.topic !== state.topicFilter && q.subtopic !== state.topicFilter) {
        return false;
      }
      // Status Filter
      const ans = state.answers[q.id];
      if (state.statusFilter === 'unanswered' && ans !== undefined) return false;
      if (state.statusFilter === 'incorrect' && (ans === undefined || ans === q.answer)) return false;
      if (state.statusFilter === 'flagged' && !state.flagged.has(q.id)) return false;
      // Search Filter
      if (state.searchQuery.trim()) {
        const query = state.searchQuery.toLowerCase();
        const inQ = q.question.toLowerCase().includes(query);
        const inOpt = q.options.some(opt => opt.toLowerCase().includes(query));
        const inLec = (q.lecture_title || '').toLowerCase().includes(query) || (q.topic || '').toLowerCase().includes(query);
        if (!inQ && !inOpt && !inLec) return false;
      }
      return true;
    });
  }

  // Populate Lectures Bar & Dropdown
  function populateLectures() {
    const lectures = getLecturesMetadata();
    const totalQs = getCurrentQuestions().length;

    // 1. Populate Sidebar Select
    if (lectureSelect) {
      lectureSelect.innerHTML = `<option value="all">كل المحاضرات بالترتيب (All Lectures • 1–${totalQs})</option>`;
      lectures.forEach(lec => {
        const opt = document.createElement('option');
        opt.value = lec.num;
        opt.textContent = `${lec.label} • (Q${lec.firstQ}–Q${lec.lastQ} | ${lec.count} سؤال)`;
        lectureSelect.appendChild(opt);
      });
      lectureSelect.value = state.lectureFilter;
    }

    // 2. Populate Top Lecture Pills Strip
    if (lecturePillsContainer) {
      lecturePillsContainer.innerHTML = '';

      const allBtn = document.createElement('button');
      allBtn.type = 'button';
      allBtn.className = `lecture-pill ${state.lectureFilter === 'all' ? 'active' : ''}`;
      allBtn.innerHTML = `
        <span>📚 كل المحاضرات بالترتيب</span>
        <span class="lec-range">Q1–Q${totalQs}</span>
      `;
      allBtn.addEventListener('click', () => {
        setLectureFilter('all');
      });
      lecturePillsContainer.appendChild(allBtn);

      lectures.forEach(lec => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = `lecture-pill ${String(state.lectureFilter) === String(lec.num) ? 'active' : ''}`;
        btn.innerHTML = `
          <span>${lec.label}</span>
          <span class="lec-range">Q${lec.firstQ}–Q${lec.lastQ} (${lec.count})</span>
        `;
        btn.addEventListener('click', () => {
          setLectureFilter(String(lec.num));
        });
        lecturePillsContainer.appendChild(btn);
      });
    }
  }

  function setLectureFilter(lecVal) {
    state.lectureFilter = lecVal;
    state.topicFilter = 'all';
    state.currentIndex = 0;
    if (lectureSelect) lectureSelect.value = lecVal;
    populateLectures();
    populateTopics();
    renderCurrentQuestion();
  }

  // Populate Sub-Topics
  function populateTopics() {
    const questions = getCurrentQuestions().filter(q =>
      state.lectureFilter === 'all' || String(q.lecture_num) === String(state.lectureFilter)
    );
    const topics = new Set(questions.map(q => q.topic));
    topicSelect.innerHTML = '<option value="all">All Sub-Topics (جميع الجزئيات بالترتيب)</option>';
    topics.forEach(t => {
      const opt = document.createElement('option');
      opt.value = t;
      opt.textContent = t;
      topicSelect.appendChild(opt);
    });
    topicSelect.value = state.topicFilter;
  }

  // Render Question
  function renderCurrentQuestion() {
    const filtered = getFilteredQuestions();
    if (filtered.length === 0) {
      qNum.textContent = "0/0";
      if (qLectureBadge) qLectureBadge.textContent = "—";
      qTopic.textContent = "No matches";
      if (qLecturePill) qLecturePill.textContent = "📚 لا توجد أسئلة مطابقة";
      if (qLectureTitle) qLectureTitle.textContent = "";
      if (qLectureOrder) qLectureOrder.textContent = "";
      qBody.textContent = "No questions match your current filter or search criteria.";
      optionsList.innerHTML = '';
      explanationBox.classList.remove('show');
      btnPrev.disabled = true;
      btnNext.disabled = true;
      if (qProgressFill) qProgressFill.style.width = '0%';
      if (mobileQCount) mobileQCount.textContent = '0';
      renderGrid();
      return;
    }

    if (state.currentIndex >= filtered.length) state.currentIndex = 0;
    if (state.currentIndex < 0) state.currentIndex = filtered.length - 1;

    const q = filtered[state.currentIndex];
    const totalCurrent = getCurrentQuestions();
    const rawIndex = totalCurrent.findIndex(item => item.id === q.id);

    // Lecture banner & metadata
    const lecLabel = q.lecture || `المحاضرة ${q.lecture_num || 1}`;
    const lecShort = q.lecture_short || `المحاضرة ${q.lecture_num || 1}`;
    const fullLecTitle = q.lecture_title || lecLabel;
    // Extract clean English part of lecture title after colon if present
    const cleanLecDesc = fullLecTitle.includes(':') ? fullLecTitle.split(':').slice(1).join(':').trim() : fullLecTitle;

    if (qLecturePill) qLecturePill.textContent = `📚 ${lecLabel}`;
    if (qLectureTitle) qLectureTitle.textContent = cleanLecDesc;
    if (qLectureOrder) {
      if (q.lecture_q_num && q.lecture_q_total) {
        qLectureOrder.textContent = `سؤال ${q.lecture_q_num} من ${q.lecture_q_total} في ${lecShort} • (الترتيب العام: ${rawIndex + 1} من ${totalCurrent.length})`;
      } else {
        qLectureOrder.textContent = `الترتيب العام: سؤال ${rawIndex + 1} من ${totalCurrent.length}`;
      }
    }

    qNum.textContent = `Q ${rawIndex + 1} of ${totalCurrent.length}`;
    if (qLectureBadge) qLectureBadge.textContent = `📌 ${lecShort}`;
    qTopic.textContent = q.subtopic || q.topic;
    qBody.textContent = q.question;

    // Update Progress Bar
    const progressPercent = filtered.length > 0 ? ((state.currentIndex + 1) / filtered.length) * 100 : 0;
    if (qProgressFill) qProgressFill.style.width = `${progressPercent}%`;
    if (mobileQCount) mobileQCount.textContent = `${lecShort} • Q${rawIndex + 1}/${totalCurrent.length}`;

    // Flag State
    if (state.flagged.has(q.id)) {
      btnFlag.classList.add('active');
      btnFlag.innerHTML = '🚩 Flagged';
    } else {
      btnFlag.classList.remove('active');
      btnFlag.innerHTML = '🏳️ Flag';
    }

    // Render Options
    optionsList.innerHTML = '';
    const letters = ['A', 'B', 'C', 'D'];
    const userAnswer = state.answers[q.id];

    q.options.forEach((optText, optIdx) => {
      const optDiv = document.createElement('div');
      optDiv.className = 'option-item';
      
      const letterSpan = document.createElement('span');
      letterSpan.className = 'option-letter';
      letterSpan.textContent = letters[optIdx];

      const textSpan = document.createElement('span');
      textSpan.textContent = optText;

      optDiv.appendChild(letterSpan);
      optDiv.appendChild(textSpan);

      // In practice mode or if answered
      if (userAnswer !== undefined) {
        if (optIdx === q.answer) {
          optDiv.classList.add('correct');
        } else if (optIdx === userAnswer) {
          optDiv.classList.add('wrong');
        }
      }

      optDiv.addEventListener('click', () => {
        handleOptionClick(q, optIdx);
      });

      optionsList.appendChild(optDiv);
    });

    // Explanation
    if (userAnswer !== undefined) {
      explanationText.textContent = q.explanation;
      explanationBox.classList.add('show');
    } else {
      explanationBox.classList.remove('show');
    }

    btnPrev.disabled = state.currentIndex === 0;
    btnNext.disabled = state.currentIndex === filtered.length - 1;

    renderGrid();
    updateStats();
  }

  function handleOptionClick(q, optIdx) {
    state.answers[q.id] = optIdx;
    renderCurrentQuestion();
  }

  // Render Grid (Grouped by Lecture with Dividers in Order)
  function renderGrid() {
    const all = getCurrentQuestions();
    const filtered = getFilteredQuestions();
    const currentQ = filtered[state.currentIndex];
    const lecturesMeta = getLecturesMetadata();

    gridCount.textContent = `(${filtered.length} / ${all.length})`;
    questionsGrid.innerHTML = '';

    let lastLecNum = null;

    filtered.forEach((q, idx) => {
      const qLecNum = String(q.lecture_num || 1);
      if (qLecNum !== lastLecNum) {
        lastLecNum = qLecNum;
        const lecInfo = lecturesMeta.find(l => String(l.num) === qLecNum);
        const divider = document.createElement('div');
        divider.className = 'grid-lecture-divider';
        if (lecInfo) {
          divider.innerHTML = `
            <span>📚 ${lecInfo.label}</span>
            <span class="grid-lec-range">Q${lecInfo.firstQ}–Q${lecInfo.lastQ}</span>
          `;
        } else {
          divider.textContent = `📚 المحاضرة ${qLecNum}`;
        }
        questionsGrid.appendChild(divider);
      }

      const btn = document.createElement('button');
      btn.className = 'q-btn';
      
      const trueNum = all.findIndex(item => item.id === q.id) + 1;
      btn.textContent = trueNum;
      btn.title = `${q.lecture || ''} - Q${trueNum}: ${q.subtopic || q.topic}`;

      if (currentQ && q.id === currentQ.id) {
        btn.classList.add('current');
      }

      const ans = state.answers[q.id];
      if (ans !== undefined) {
        if (ans === q.answer) {
          btn.classList.add('correct');
        } else {
          btn.classList.add('wrong');
        }
      }

      if (state.flagged.has(q.id)) {
        btn.classList.add('flagged');
      }

      btn.addEventListener('click', () => {
        state.currentIndex = idx;
        renderCurrentQuestion();
        closeSidebarDrawer(); // Auto close drawer on mobile upon selection
      });

      questionsGrid.appendChild(btn);
    });
  }

  // Update Statistics
  function updateStats() {
    const all = getCurrentQuestions();
    let answered = 0;
    let correct = 0;
    let wrong = 0;

    all.forEach(q => {
      const ans = state.answers[q.id];
      if (ans !== undefined) {
        answered++;
        if (ans === q.answer) correct++;
        else wrong++;
      }
    });

    statAnswered.textContent = `${answered}/${all.length}`;
    statCorrect.textContent = correct;
    statWrong.textContent = wrong;

    // Update Mobile Quick Stats
    if (mobileStatCorrect) mobileStatCorrect.textContent = `${correct} صح`;
    if (mobileStatWrong) mobileStatWrong.textContent = `${wrong} خطأ`;
  }

  // Switch Subject
  function switchSubject(newSubj) {
    state.currentSubject = newSubj;
    state.currentIndex = 0;
    state.lectureFilter = 'all';
    state.topicFilter = 'all';
    state.statusFilter = 'all';
    state.searchQuery = '';
    searchInput.value = '';
    statusSelect.value = 'all';

    [pillDba, pillEcom, pillIr, pillBa, pillIsapp].forEach(p => {
      if (p) p.classList.remove('active');
    });
    
    if (newSubj === 'dba' && pillDba) pillDba.classList.add('active');
    else if (newSubj === 'ecom' && pillEcom) pillEcom.classList.add('active');
    else if (newSubj === 'ir' && pillIr) pillIr.classList.add('active');
    else if (newSubj === 'ba' && pillBa) pillBa.classList.add('active');
    else if (newSubj === 'isapp' && pillIsapp) pillIsapp.classList.add('active');

    populateLectures();
    populateTopics();
    renderCurrentQuestion();
    renderSummary();
  }

  // Switch View (Quiz vs Summary)
  function switchView(newView) {
    state.currentView = newView;
    if (newView === 'quiz') {
      tabQuiz.classList.add('active');
      tabSummaries.classList.remove('active');
      viewQuiz.style.display = 'grid';
      viewSummaries.style.display = 'none';
      if (lectureBarWrapper) lectureBarWrapper.style.display = '';
      if (btnOpenSidebar) btnOpenSidebar.parentElement.style.display = '';
      renderCurrentQuestion();
    } else {
      tabQuiz.classList.remove('active');
      tabSummaries.classList.add('active');
      viewQuiz.style.display = 'none';
      viewSummaries.style.display = 'block';
      if (lectureBarWrapper) lectureBarWrapper.style.display = 'none';
      if (btnOpenSidebar) btnOpenSidebar.parentElement.style.display = 'none';
      renderSummary();
    }
  }

  // Render Summary
  function renderSummary() {
    const key = `${state.currentSubject}_${state.summaryLang}`;
    const htmlContent = rawSummariesData[key] || "<h3>Summary loading...</h3>";
    summaryFrame.srcdoc = htmlContent;

    const pdfNames = {
      dba_ar: 'downloads/DBA_Summary_AR.pdf',
      dba_en: 'downloads/DBA_Summary_EN.pdf',
      ecom_ar: 'downloads/ECommerce_Summary_AR.pdf',
      ecom_en: 'downloads/ECommerce_Summary_EN.pdf',
      ir_ar: 'downloads/IR_Summary_AR.pdf',
      ir_en: 'downloads/IR_Summary_EN.pdf',
      ba_ar: 'downloads/Business_Summary_AR.pdf',
      ba_en: 'downloads/Business_Summary_EN.pdf',
      isapp_ar: 'downloads/ISApp_Summary_AR.pdf',
      isapp_en: 'downloads/ISApp_Summary_EN.pdf'
    };

    btnDownloadAr.href = pdfNames[`${state.currentSubject}_ar`] || '#';
    btnDownloadEn.href = pdfNames[`${state.currentSubject}_en`] || '#';

    if (state.summaryLang === 'ar') {
      summaryLangAr.classList.add('active');
      summaryLangEn.classList.remove('active');
    } else {
      summaryLangAr.classList.remove('active');
      summaryLangEn.classList.add('active');
    }
  }

  // Mobile Drawer Controls
  function openSidebarDrawer() {
    if (quizSidebar) quizSidebar.classList.add('drawer-open');
    if (sidebarBackdrop) sidebarBackdrop.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeSidebarDrawer() {
    if (quizSidebar) quizSidebar.classList.remove('drawer-open');
    if (sidebarBackdrop) sidebarBackdrop.classList.remove('active');
    document.body.style.overflow = '';
  }

  if (btnOpenSidebar) btnOpenSidebar.addEventListener('click', openSidebarDrawer);
  if (sidebarCloseBtn) sidebarCloseBtn.addEventListener('click', closeSidebarDrawer);
  if (sidebarBackdrop) sidebarBackdrop.addEventListener('click', closeSidebarDrawer);

  // Touch Swipe on Question Card for Mobile
  if (questionCard) {
    let touchStartX = 0;
    let touchStartY = 0;

    questionCard.addEventListener('touchstart', (e) => {
      touchStartX = e.changedTouches[0].screenX;
      touchStartY = e.changedTouches[0].screenY;
    }, { passive: true });

    questionCard.addEventListener('touchend', (e) => {
      const touchEndX = e.changedTouches[0].screenX;
      const touchEndY = e.changedTouches[0].screenY;
      const diffX = touchEndX - touchStartX;
      const diffY = touchEndY - touchStartY;

      // Check if horizontal swipe was intentional and larger than vertical drag
      if (Math.abs(diffX) > 55 && Math.abs(diffY) < 65) {
        if (diffX < 0) {
          // Swipe Left -> Next
          if (!btnNext.disabled) {
            btnNext.click();
          }
        } else {
          // Swipe Right -> Prev
          if (!btnPrev.disabled) {
            btnPrev.click();
          }
        }
      }
    }, { passive: true });
  }

  // ==========================================
  // PWA & APP INSTALLATION ENGINE
  // ==========================================
  let deferredPrompt = null;

  const isIos = () => {
    const userAgent = window.navigator.userAgent.toLowerCase();
    return /iphone|ipad|ipod/.test(userAgent);
  };

  const isInAppBrowser = () => {
    const ua = window.navigator.userAgent || '';
    return /FBAN|FBAV|Instagram|WhatsApp|Telegram|Line|Snapchat|wv/i.test(ua);
  };

  const isStandalone = () => {
    return window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true;
  };

  if (isStandalone()) {
    document.body.classList.add('is-standalone');
  }

  // Register Service Worker & purge any broken legacy redirect caches
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('/sw.js', { scope: '/' })
        .then(reg => {
          reg.update().catch(() => {});
          console.log('Midterm ServiceWorker registered successfully:', reg.scope);
        })
        .catch(err => {
          console.warn('Midterm ServiceWorker registration failed:', err);
        });
    });
  }

  // Catch PWA Install Prompt Event
  window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;

    // Show mobile banner if user hasn't closed it in this session and not installed yet
    if (!sessionStorage.getItem('pwa_banner_dismissed') && !isStandalone()) {
      if (mobileInstallBanner) {
        mobileInstallBanner.style.display = 'block';
      }
    }
  });

  window.addEventListener('appinstalled', () => {
    deferredPrompt = null;
    document.body.classList.add('is-standalone');
    if (mobileInstallBanner) mobileInstallBanner.style.display = 'none';
    if (installModal) installModal.style.display = 'none';
  });

  async function triggerAppInstall() {
    if (deferredPrompt) {
      try {
        await deferredPrompt.prompt();
        const choice = await deferredPrompt.userChoice;
        if (choice && choice.outcome === 'accepted') {
          console.log('Midterm app installed by user');
        }
        deferredPrompt = null;
        if (mobileInstallBanner) mobileInstallBanner.style.display = 'none';
        return;
      } catch (err) {
        console.warn('Install prompt failed, falling back to manual instructions:', err);
        deferredPrompt = null;
      }
    }

    if (isIos()) {
      showIosInstallModal();
      return;
    }

    showGeneralInstallModal();
  }

  function showIosInstallModal() {
    if (!modalBody || !installModal) return;
    modalBody.innerHTML = `
      <div style="text-align: center; margin-bottom: 18px;">
        <div style="font-size: 38px; margin-bottom: 6px;">📱</div>
        <h3 style="font-size: 16px; font-weight: 800; color: var(--primary);">تثبيت تطبيق Midterm على آيفون (iOS)</h3>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 4px;">اتبع هذه الخطوات البسيطة لإضافة التطبيق لشاشتك الرئيسية:</p>
      </div>

      ${isInAppBrowser() ? `
      <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 10px 12px; margin-bottom: 14px; font-size: 12.5px; direction: rtl; text-align: right;">
        ⚠️ <strong>تنبيه هام:</strong> أنت تفتح الموقع الآن من داخل متصفح داخلي (مثل واتساب أو تليجرام). يرجى فتح الرابط في متصفح <strong>Safari</strong> أولاً ليتم التثبيت بدون خطأ.
      </div>
      ` : ''}

      <div class="modal-step">
        <div class="modal-step-num">1</div>
        <div class="modal-step-text">
          اضغط على زر <strong>المشاركة (Share) ⎋</strong> في الشريط السفلي لمتصفح Safari.
        </div>
      </div>

      <div class="modal-step">
        <div class="modal-step-num">2</div>
        <div class="modal-step-text">
          مرّر للأسفل في القائمة واضغط على <strong>"إضافة إلى الشاشة الرئيسية" ➕ (Add to Home Screen)</strong>.
        </div>
      </div>

      <div class="modal-step">
        <div class="modal-step-num">3</div>
        <div class="modal-step-text">
          اضغط <strong>"إضافة" (Add)</strong> في أعلى يمين الشاشة، وسيظهر تطبيق Midterm مباشرة كأيقونة تطبيق كامل على جهازك!
        </div>
      </div>

      <div style="margin-top: 20px; display: flex; gap: 8px;">
        <button id="modal-copy-btn" class="btn btn-outline" style="flex: 1;">📋 نسخ رابط الموقع</button>
        <button id="modal-ok-btn" class="btn btn-primary" style="flex: 1;">فهمت، شكراً 👍</button>
      </div>
    `;
    installModal.style.display = 'flex';
    const okBtn = document.getElementById('modal-ok-btn');
    if (okBtn) okBtn.onclick = () => installModal.style.display = 'none';
    const copyBtn = document.getElementById('modal-copy-btn');
    if (copyBtn) {
      copyBtn.onclick = () => {
        navigator.clipboard?.writeText(window.location.origin + '/');
        copyBtn.textContent = '✅ تم نسخ الرابط!';
      };
    }
  }

  function showGeneralInstallModal() {
    if (!modalBody || !installModal) return;
    modalBody.innerHTML = `
      <div style="text-align: center; margin-bottom: 18px;">
        <div style="font-size: 38px; margin-bottom: 6px;">📲</div>
        <h3 style="font-size: 16px; font-weight: 800; color: var(--primary);">تثبيت تطبيق Midterm على التليفون</h3>
        <p style="font-size: 12.5px; color: var(--text-muted); margin-top: 4px;">لتثبيت التطبيق بنجاح بدون أي خطأ، اتبع الخطوات التالية:</p>
      </div>

      ${isInAppBrowser() ? `
      <div style="background: rgba(239, 68, 68, 0.1); border: 1px solid rgba(239, 68, 68, 0.3); border-radius: 10px; padding: 10px 12px; margin-bottom: 14px; font-size: 12.5px; direction: rtl; text-align: right;">
        ⚠️ <strong>تنبيه هام:</strong> أنت تفتح الموقع من داخل تطبيق محادثة (مثل واتساب أو تليجرام أو فيسبوك). المتصفح الداخلي لا يدعم تثبيت التطبيقات!<br>
        اضغط على الثلاث نقاط <strong>(⋮)</strong> أعلى الشاشة واختر <strong>"الفتح في Chrome" (Open in Chrome)</strong> ثم اضغط تثبيت.
      </div>
      ` : ''}

      <div class="modal-step">
        <div class="modal-step-num">1</div>
        <div class="modal-step-text">
          افتح الموقع من متصفح <strong>Google Chrome</strong> أو <strong>Samsung Internet</strong> على هاتفك.
        </div>
      </div>

      <div class="modal-step">
        <div class="modal-step-num">2</div>
        <div class="modal-step-text">
          اضغط على قائمة الثلاث نقاط <strong>(⋮)</strong> أعلى المتصفح، ثم اختر <strong>"تثبيت التطبيق" (Install App)</strong> أو <strong>"إضافة إلى الشاشة الرئيسية" (Add to Home Screen)</strong>.
        </div>
      </div>

      <div style="margin-top: 20px; display: flex; gap: 8px;">
        <button id="modal-copy-btn" class="btn btn-outline" style="flex: 1;">📋 نسخ الرابط لـ Chrome</button>
        <button id="modal-ok-btn" class="btn btn-primary" style="flex: 1;">تم، حسناً 👍</button>
      </div>
    `;
    installModal.style.display = 'flex';
    const okBtn = document.getElementById('modal-ok-btn');
    if (okBtn) okBtn.onclick = () => installModal.style.display = 'none';
    const copyBtn = document.getElementById('modal-copy-btn');
    if (copyBtn) {
      copyBtn.onclick = () => {
        navigator.clipboard?.writeText(window.location.origin + '/');
        copyBtn.textContent = '✅ تم نسخ الرابط!';
      };
    }
  }

  if (btnInstall) btnInstall.addEventListener('click', triggerAppInstall);
  if (btnBannerInstall) btnBannerInstall.addEventListener('click', triggerAppInstall);

  if (btnBannerClose) {
    btnBannerClose.addEventListener('click', () => {
      if (mobileInstallBanner) mobileInstallBanner.style.display = 'none';
      sessionStorage.setItem('pwa_banner_dismissed', 'true');
    });
  }

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      if (installModal) installModal.style.display = 'none';
    });
  }

  if (installModal) {
    installModal.addEventListener('click', (e) => {
      if (e.target === installModal) installModal.style.display = 'none';
    });
  }

  // ==========================================
  // EVENT LISTENERS FOR QUIZ & UI
  // ==========================================
  if (pillDba) pillDba.addEventListener('click', () => switchSubject('dba'));
  if (pillEcom) pillEcom.addEventListener('click', () => switchSubject('ecom'));
  if (pillIr) pillIr.addEventListener('click', () => switchSubject('ir'));
  if (pillBa) pillBa.addEventListener('click', () => switchSubject('ba'));
  if (pillIsapp) pillIsapp.addEventListener('click', () => switchSubject('isapp'));

  tabQuiz.addEventListener('click', () => switchView('quiz'));
  tabSummaries.addEventListener('click', () => switchView('summaries'));

  modePractice.addEventListener('click', () => {
    state.currentMode = 'practice';
    modePractice.classList.add('active');
    modeExam.classList.remove('active');
    renderCurrentQuestion();
  });

  modeExam.addEventListener('click', () => {
    state.currentMode = 'exam';
    modeExam.classList.add('active');
    modePractice.classList.remove('active');
    renderCurrentQuestion();
  });

  btnPrev.addEventListener('click', () => {
    state.currentIndex--;
    renderCurrentQuestion();
  });

  btnNext.addEventListener('click', () => {
    state.currentIndex++;
    renderCurrentQuestion();
  });

  btnFlag.addEventListener('click', () => {
    const filtered = getFilteredQuestions();
    const q = filtered[state.currentIndex];
    if (!q) return;
    if (state.flagged.has(q.id)) {
      state.flagged.delete(q.id);
    } else {
      state.flagged.add(q.id);
    }
    renderCurrentQuestion();
  });

  if (lectureSelect) {
    lectureSelect.addEventListener('change', (e) => {
      setLectureFilter(e.target.value);
    });
  }

  topicSelect.addEventListener('change', (e) => {
    state.topicFilter = e.target.value;
    state.currentIndex = 0;
    renderCurrentQuestion();
  });

  statusSelect.addEventListener('change', (e) => {
    state.statusFilter = e.target.value;
    state.currentIndex = 0;
    renderCurrentQuestion();
  });

  searchInput.addEventListener('input', (e) => {
    state.searchQuery = e.target.value;
    state.currentIndex = 0;
    renderCurrentQuestion();
  });

  summaryLangAr.addEventListener('click', () => {
    state.summaryLang = 'ar';
    renderSummary();
  });

  summaryLangEn.addEventListener('click', () => {
    state.summaryLang = 'en';
    renderSummary();
  });

  themeToggle.addEventListener('click', () => {
    state.theme = state.theme === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', state.theme);
    localStorage.setItem('theme', state.theme);
    themeToggle.textContent = state.theme === 'dark' ? '☀️' : '🌙';
  });

  // Keyboard Shortcuts for Desktop
  document.addEventListener('keydown', (e) => {
    if (state.currentView !== 'quiz') return;
    if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;

    if (e.key === 'ArrowRight' || e.key === 'n') {
      if (!btnNext.disabled) {
        state.currentIndex++;
        renderCurrentQuestion();
      }
    } else if (e.key === 'ArrowLeft' || e.key === 'p') {
      if (!btnPrev.disabled) {
        state.currentIndex--;
        renderCurrentQuestion();
      }
    } else if (['1', '2', '3', '4'].includes(e.key)) {
      const idx = parseInt(e.key, 10) - 1;
      const filtered = getFilteredQuestions();
      const q = filtered[state.currentIndex];
      if (q && q.options[idx]) {
        handleOptionClick(q, idx);
      }
    }
  });

  // Initialize Data & Counts
  const totalQuestions = Object.values(rawQuizData).reduce((sum, arr) => sum + (arr ? arr.length : 0), 0);
  const totalBadge = document.getElementById('total-badge-count');
  if (totalBadge && totalQuestions > 0) {
    totalBadge.textContent = `${totalQuestions.toLocaleString()} Questions`;
  }

  // Update pills badges dynamically
  ['dba', 'ecom', 'ir', 'ba', 'isapp'].forEach(subj => {
    const pill = document.getElementById(`pill-${subj}`);
    if (pill) {
      const badge = pill.querySelector('.badge');
      if (badge && rawQuizData[subj]) {
        badge.textContent = `${rawQuizData[subj].length} Qs`;
      }
    }
  });

  populateLectures();
  populateTopics();
  renderCurrentQuestion();
});
