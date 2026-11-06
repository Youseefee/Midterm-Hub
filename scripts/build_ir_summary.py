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
    background: linear-gradient(135deg, #4338ca 0%, #6366f1 100%);
    color: #ffffff;
    padding: 40px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.3);
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
    color: #3730a3;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}

body.ar h2 {
    color: #3730a3;
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
    border-left: 4px solid #6366f1;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin: 15px 0;
    font-size: 13px;
}

body.ar .callout {
    border-left: none;
    border-right: 4px solid #6366f1;
    border-radius: 8px 0 0 8px;
}

.callout.warning {
    border-color: #f59e0b;
    background: #fffbeb;
}

.callout.tip {
    border-color: #4f46e5;
    background: #eef2ff;
}

.callout-title {
    font-weight: 700;
    margin-bottom: 4px;
    color: #312e81;
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
    background: #e0e7ff;
    color: #3730a3;
}

.code-box {
    background: #0f172a;
    color: #f8fafc;
    padding: 12px 16px;
    border-radius: 6px;
    font-family: 'Consolas', monospace;
    font-size: 12px;
    direction: ltr;
    text-align: left;
    margin: 12px 0;
    overflow-x: auto;
}

.page-break {
    page-break-after: always;
}
"""

html_ir_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Information Storage and Retrieval (IR) - Comprehensive Midterm Summary</title>
<style>{css_shared}</style>
</head>
<body>

<div class="cover">
    <h1>Information Storage and Retrieval (IR)</h1>
    <div class="subtitle">Complete Midterm Study Guide & Comprehensive Knowledge Reference</div>
    <div class="meta">
        <span>Covering: Chapter 1, Lecture 2, Lecture 3, Lecture 5</span>
        <span>•</span>
        <span>Boolean Model, Inverted Index, Skip Pointers, Normalization & Stemming</span>
    </div>
</div>

<div class="section">
    <h2>1. Introduction to Information Retrieval & Inverted Indexes (Chapter 1)</h2>
    <div class="callout tip">
        <div class="callout-title">Formal Definition of Information Retrieval (IR)</div>
        <strong>Information Retrieval (IR)</strong> is finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers).
    </div>

    <h3>1.1 Information Need vs. Query</h3>
    <ul>
        <li><strong>Information Need:</strong> The semantic topic or desire for knowledge in the user's mind (e.g. "I want to know if drinking coffee raises blood pressure").</li>
        <li><strong>Query:</strong> What the user actually types into the search engine to communicate that need (e.g. `coffee blood pressure`). Often ambiguous or incomplete.</li>
    </ul>

    <h3>1.2 Information Retrieval vs. Traditional Databases</h3>
    <table>
        <tr>
            <th>Dimension</th>
            <th>Traditional Database (RDBMS)</th>
            <th>Information Retrieval (IR)</th>
        </tr>
        <tr>
            <td><strong>Data Structure</strong></td>
            <td>Structured relational tables with well-defined schemas.</td>
            <td>Unstructured or semi-structured free-form text.</td>
        </tr>
        <tr>
            <td><strong>Semantics & Matching</strong></td>
            <td>Clear, deterministic semantics; exact boolean matching.</td>
            <td>Ambiguous natural language; relevance ranking and probabilistic scoring.</td>
        </tr>
        <tr>
            <td><strong>Query Language</strong></td>
            <td>Formal declarative SQL statements.</td>
            <td>Natural language keywords, boolean operators, or free-text queries.</td>
        </tr>
        <tr>
            <td><strong>Result Set</strong></td>
            <td>Exact set of rows matching the WHERE clause (unordered unless ORDER BY).</td>
            <td>Ranked list of documents ordered by estimated relevance.</td>
        </tr>
    </table>

    <h3>1.3 The Term-Document Incidence Matrix & Its Fatal Limitation</h3>
    <ul>
        <li><strong>Incidence Matrix:</strong> A 2D binary matrix where rows represent vocabulary terms ($V$) and columns represent documents ($N$). Cell $(t, d) = 1$ if term $t$ appears in document $d$, and $0$ otherwise.</li>
        <li><strong>The Sparsity Problem:</strong> In a collection of $N = 1,000,000$ documents and $V = 500,000$ terms, the matrix contains $500,000 \times 1,000,000 = 500 billion$ cells! Over 99.9% of these cells are 0. Storing this dense matrix is completely impractical.</li>
    </ul>

    <h3>1.4 The Inverted Index: The Standard Data Structure</h3>
    <p>An <strong>Inverted Index</strong> stores only the non-zero entries (the occurrences), mapping each term to the documents where it appears.</p>
    <ul>
        <li><strong>Dictionary (Vocabulary):</strong> A sorted list of unique terms, typically held in RAM (using a B-Tree or Hash Table) for fast lookup. Includes the <em>Document Frequency ($df$)</em>.</li>
        <li><strong>Postings Lists:</strong> For each term, a contiguous variable-length array or linked list of Document IDs (DocIDs) where the term occurs, sorted in ascending DocID order.</li>
    </ul>

    <h3>1.5 Inverted Index Construction Pipeline</h3>
    <ol>
        <li><strong>Document Parsing:</strong> Extract raw character streams from formats (HTML, PDF, DOCX) and identify character encoding (UTF-8).</li>
        <li><strong>Tokenizer:</strong> Break character stream into a sequence of word tokens.</li>
        <li><strong>Linguistic Modules:</strong> Apply case folding, stop word handling, and stemming/lemmatization to produce canonical <em>terms</em>.</li>
        <li><strong>Indexer:</strong> Extract (Term, DocID) pairs, sort alphabetically by term and secondarily by DocID, and aggregate identical terms into dictionary entries with attached postings lists.</li>
    </ol>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. Boolean Query Processing, Optimization & Phrase Queries (Lecture 2)</h2>

    <h3>2.1 The Postings Merge (Intersection) Algorithm</h3>
    <p>To evaluate a boolean AND query (e.g. `Brutus AND Caesar`), the search engine simultaneously traverses the sorted postings lists of both terms using two pointers ($p_1, p_2$).</p>
    
    <div class="code-box">
Algorithm INTERSECT(p1, p2):
    answer = []
    while p1 != NIL and p2 != NIL:
        if DocID(p1) == DocID(p2):
            answer.append(DocID(p1))
            p1 = p1.next
            p2 = p2.next
        else if DocID(p1) < DocID(p2):
            p1 = p1.next
        else:
            p2 = p2.next
    return answer
    </div>

    <div class="callout tip">
        <div class="callout-title">Time Complexity</div>
        Because both lists are strictly sorted in ascending order of DocID, each pointer traverses its list at most once. The time complexity is strictly linear: <strong>O(x + y)</strong>, where $x$ and $y$ are the lengths of the two postings lists.
    </div>

    <h3>2.2 Query Optimization for Boolean Queries</h3>
    <ul>
        <li><strong>Optimal AND Evaluation Order:</strong> Always process terms in order of <strong>increasing Document Frequency ($df$)</strong> (i.e. shortest postings lists first).</li>
        <li><strong>Concrete Example:</strong>
            <ul>
                <li>`Calpurnia` ($df = 4$)</li>
                <li>`Brutus` ($df = 20,000$)</li>
                <li>`Caesar` ($df = 40,000$)</li>
                <li>Evaluate as: `(Calpurnia AND Brutus) AND Caesar`. The intermediate result of the first intersection contains at most <strong>4 documents</strong>! Intersecting 4 DocIDs with Caesar's list requires negligible time.</li>
            </ul>
        </li>
    </ul>

    <h3>2.3 Phrase Queries: Biword vs. Positional Indexes</h3>
    <p>A standard inverted index only records document presence, not word order. It cannot distinguish `"Stanford University"` from a document containing "Stanford" on page 1 and "University" on page 50.</p>
    <table>
        <tr>
            <th>Index Approach</th>
            <th>How It Works</th>
            <th>Advantages & Disadvantages</th>
        </tr>
        <tr>
            <td><strong>Biword Index</strong></td>
            <td>Every adjacent pair of consecutive words is indexed as a discrete vocabulary term (e.g. "friends romans", "romans countrymen").</td>
            <td><strong>Pros:</strong> Fast lookup for 2-word phrases.<br><strong>Cons:</strong> Vocabulary explosion ($V^2$ potential pairs), false positives for longer phrases, cannot handle proximity queries.</td>
        </tr>
        <tr>
            <td><strong>Positional Index</strong></td>
            <td>For every term and document, stores the exact sequential word token position offsets: `term -> docID: <pos1, pos2, ...>`.</td>
            <td><strong>Pros:</strong> Solves arbitrary N-word phrase queries and proximity queries (`/k`). Standard industry solution.<br><strong>Cons:</strong> Postings lists expand 2-4x (occupying 35-50% of raw text volume).</td>
        </tr>
        <tr>
            <td><strong>Combination Scheme (Hybrid)</strong></td>
            <td>Biwords for highly frequent common phrases (e.g. "New York", "Michael Jackson"); positional index for arbitrary queries.</td>
            <td>Optimal balance between throughput and storage efficiency.</td>
        </tr>
    </table>

    <h3>2.4 Proximity Queries (`/k` Operator)</h3>
    <p>A proximity query like `employment /3 federal` requires that "employment" and "federal" occur within at most 3 words of each other ($|pos_1 - pos_2| \le 3$). The positional merge checks matching DocIDs and verifies position differences.</p>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>3. Faster Postings Merges & Skip Pointers (Lecture 3)</h2>

    <h3>3.1 Skip Pointers: Mechanics & Motivation</h3>
    <p>When intersecting two postings lists where one is very short and the other is very long (or both are long), linear scanning inspects many DocIDs that could never match. <strong>Skip Pointers</strong> augment postings lists with forward shortcut pointers to jump ahead.</p>

    <div class="callout tip">
        <div class="callout-title">The Skip Decision Rule</div>
        During merge of $p_1$ and $p_2$: If $p_1$ has a skip pointer and <strong>skip(p1) &le; DocID(p2)</strong>, take the jump directly to `skip(p1)`! If `skip(p1) > DocID(p2)`, do NOT take the skip (to avoid overshooting); advance $p_1$ by one step normally.
    </div>

    <h3>3.2 Placement of Skip Pointers: The Heuristic Rule of Thumb</h3>
    <ul>
        <li><strong>The Tradeoff:</strong> More frequent skips provide more jump opportunities but increase index storage size and pointer-checking overhead; fewer skips have low overhead but offer few chances to jump.</li>
        <li><strong>Heuristic Rule:</strong> For a postings list of length $P$, place skip pointers evenly spaced every <strong>&radic;P</strong> elements!</li>
        <li><strong>Example:</strong> If a postings list contains $P = 10,000$ elements, place skips every $\sqrt{10,000} = 100$ elements, resulting in roughly 100 evenly spaced skip pointers.</li>
        <li><strong>Dynamic Index Limitation:</strong> Skip pointers work best on static indexes. In dynamic collections with frequent inserts and deletes, skip intervals degrade, requiring costly pointer maintenance.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>4. The Term Vocabulary & Text Normalization (Lecture 5)</h2>

    <h3>4.1 Document Parsing & Tokenization Challenges</h3>
    <ul>
        <li><strong>Character Encodings:</strong> Detecting whether raw bytes are UTF-8, UTF-16, or ASCII is vital to avoid mojibake (corrupted characters).</li>
        <li><strong>Tokenization:</strong> The process of segmenting a stream of characters into discrete tokens (words).
            <ul>
                <li><em>Hyphens:</em> Compound words (`Hewlett-Packard`, `state-of-the-art`, `co-education`) challenge whether to index as one token or split.</li>
                <li><em>Apostrophes:</em> Contractions (`aren't`) vs. possessives (`children's`) vs. proper names (`O'Neill`).</li>
                <li><em>Numbers & Formats:</em> Dates, model numbers (`Boeing 747`, `iPhone 15`), and chemical formulas have high discriminatory value and must be preserved.</li>
                <li><em>Language Specifics:</em> Chinese/Japanese have no whitespace delimiters, requiring morphological segmenters or character N-grams. Arabic has clitics (prefixes like 'and' و, 'the' ال) attached directly to nouns.</li>
            </ul>
        </li>
    </ul>

    <h3>4.2 Stop Words: Traditional vs. Modern Paradigm</h3>
    <ul>
        <li><strong>Stop Words:</strong> Extremely common functional grammatical words (e.g. `the`, `a`, `is`, `of`, `to`, `at`) that appear in virtually all documents.</li>
        <li><strong>Traditional Approach:</strong> Filter out 30 to 150 (or up to 750) stop words from the index to save disk space.</li>
        <li><strong>Modern Search Engine Approach:</strong> Keep all or almost all stop words in the index. Reasons: (1) Storage compression has made index size manageable; (2) Users frequently search for exact phrases consisting heavily of stop words (e.g. `"To be or not to be"`, `"Let it be"`, `"The Who"`).</li>
    </ul>

    <h3>4.3 Normalization: Case Folding & Equivalence Classes</h3>
    <ul>
        <li><strong>Equivalence Classes:</strong> Mapping different surface tokens to a single canonical term (e.g. `U.S.A.` and `USA` &rarr; `usa`).</li>
        <li><strong>Case Folding:</strong> Lowercasing all characters. While standard, it risks conflating proper nouns with common words (`US` country vs. `us` pronoun; `Bush` president vs. `bush` plant; `CAT` scan vs. `cat` animal).</li>
        <li><strong>Soundex:</strong> Phonetic hashing algorithm based on consonant sounds, matching names with different spellings that sound identical (e.g. `Smith` and `Smyth`).</li>
    </ul>

    <h3>4.4 Stemming vs. Lemmatization (Crucial Exam Concept)</h3>
    <table>
        <tr>
            <th>Dimension</th>
            <th>Stemming (e.g. Porter Stemmer)</th>
            <th>Lemmatization</th>
        </tr>
        <tr>
            <td><strong>Methodology</strong></td>
            <td>Crude, fast, heuristic suffix chopping without grammar or vocabulary lookup.</td>
            <td>Full morphological analysis using vocabulary, grammar rules, and Part of Speech (POS) context.</td>
        </tr>
        <tr>
            <td><strong>Output</strong></td>
            <td>Often produces an artificial, non-word stem (e.g. `automate, automatic, automation` &rarr; `automat`).</td>
            <td>Always produces a true, grammatically valid base dictionary form called a <strong>lemma</strong>.</td>
        </tr>
        <tr>
            <td><strong>Context Sensitivity</strong></td>
            <td>Blind to grammatical context; treats every word identically.</td>
            <td>Context-aware: reduces `saw` to `see` if used as a verb, or leaves as `saw` if used as a noun. Reduces `better` to `good`.</td>
        </tr>
        <tr>
            <td><strong>Speed & Complexity</strong></td>
            <td>Very fast, low memory footprint, simple algorithmic rules.</td>
            <td>Computationally intensive, requires extensive lexical dictionaries and grammatical parsers.</td>
        </tr>
    </table>

    <h3>4.5 The Porter Stemmer (5 Phases) & Stemming Errors</h3>
    <ul>
        <li><strong>Porter's Algorithm (1980):</strong> The standard English stemmer consisting of 5 sequential phases of suffix stripping rules based on syllable measure $m$ (vowel-consonant sequences).</li>
        <li><strong>Over-stemming Error:</strong> Chopping too much, causing semantically distinct words to merge to the same stem (e.g. `universe` and `university` &rarr; `univers`; `police` and `policy` &rarr; `polic`). Hurts retrieval <em>precision</em>.</li>
        <li><strong>Under-stemming Error:</strong> Failing to merge forms that share the same conceptual root (e.g. `adhere` and `adhesion`). Hurts retrieval <em>recall</em>.</li>
        <li><strong>Heaps' Law:</strong> Vocabulary size $V$ grows sublinearly with collection size $N$ following $V = k N^\beta$ (where $\beta \approx 0.4 - 0.6$), showing vocabulary continues to expand indefinitely as new documents are indexed.</li>
    </ul>
</div>

</body>
</html>"""

html_ir_ar = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>استرجاع وتخزين المعلومات (IR) - ملخص الميدتيرم الشامل</title>
<style>{css_shared}</style>
</head>
<body class="ar">

<div class="cover">
    <h1>استرجاع وتخزين المعلومات (Information Storage and Retrieval - IR)</h1>
    <div class="subtitle">الملخص الدراسي الشامل والموسوعة المرجعية لامتحان الميدتيرم</div>
    <div class="meta">
        <span>تغطية: الفصل 1، المحاضرة 2، المحاضرة 3، المحاضرة 5</span>
        <span>•</span>
        <span>النموذج البولياني، الفهرس المعكوس، مؤشرات القفز، التوحيد المعياري والتجذير</span>
    </div>
</div>

<div class="section">
    <h2>1. مقدمة في استرجاع المعلومات والفهرس المعكوس (الفصل 1)</h2>
    <div class="callout tip">
        <div class="callout-title">التعريف الأكاديمي المعتمد لاسترجاع المعلومات (IR)</div>
        هو عملية العثور على مواد (غالباً وثائق) ذات طبيعة غير مهيكلة (غالباً نصوص مكتوبة) تلبي حاجة معلوماتية لدى المستخدم من بين مجموعات تخزينية ضخمة مخزنة على الحواسيب.
    </div>

    <h3>1.1 الفرق بين الحاجة المعلوماتية والاستعلام (Need vs. Query)</h3>
    <ul>
        <li><strong>الحاجة المعلوماتية (Information Need):</strong> الموضوع أو الرغبة المعرفية الكامنة في عقل المستخدم (مثال: "أريد معرفة هل شرب القهوة يرفع ضغط الدم").</li>
        <li><strong>الاستعلام (Query):</strong> الكلمات الفعلية التي يكتبها المستخدم في مربع البحث للتعبير عن تلك الحاجة (مثال: `coffee blood pressure`). وغالباً ما تكون غير دقيقة أو مبهمة.</li>
    </ul>

    <h3>1.2 استرجاع المعلومات مقابل قواعد البيانات التقليدية</h3>
    <table>
        <tr>
            <th>وجه المقارنة</th>
            <th>قواعد البيانات العلائقية (RDBMS)</th>
            <th>أنظمة استرجاع المعلومات (IR)</th>
        </tr>
        <tr>
            <td><strong>طبيعة البيانات</strong></td>
            <td>بيانات مهيكلة في جداول وحقول محددة وصارمة.</td>
            <td>نصوص حرة غير مهيكلة أو شبه مهيكلة.</td>
        </tr>
        <tr>
            <td><strong>المطابقة والدلالة</strong></td>
            <td>دلالات واضحة ومطابقة منطقية صارمة (Exact Match).</td>
            <td>لغة طبيعية غامضة ومطابقة تقريبية تعتمد على الترتيب والصلة (Relevance Ranking).</td>
        </tr>
        <tr>
            <td><strong>لغة الاستعلام</strong></td>
            <td>لغة تصريحية دقيقة (SQL).</td>
            <td>كلمات مفتاحية، معاملات بوليانية، أو نصوص حرة.</td>
        </tr>
        <tr>
            <td><strong>النتائج المسترجعة</strong></td>
            <td>مجموعة غير مرتبة تطابق شرط WHERE تماماً.</td>
            <td>قائمة وثائق مرتبة تنازلياً حسب درجة الأهمية والملاءمة للبحث.</td>
        </tr>
    </table>

    <h3>1.3 مصفوفة وقوع الكلمات (Term-Document Matrix) ومأزق التناثر</h3>
    <ul>
        <li><strong>المصفوفة الثنائية:</strong> جدول يمثل صفوفه الكلمات ($V$) وأعمدته الوثائق ($N$)؛ وتوضع القيمة 1 إذا وردت الكلمة في الوثيقة و 0 إذا لم ترد.</li>
        <li><strong>مأزق التناثر (Sparsity Problem):</strong> إذا كان لدينا 1,000,000 وثيقة و 500,000 كلمة، فإن حجم المصفوفة هو 500 مليار خانة! أكثر من 99.9% منها أصفار. تخزين هذه المصفوفة كثيفة البيانات في الذاكرة مستحيل تماماً وهدر هائل للموارد.</li>
    </ul>

    <h3>1.4 الفهرس المعكوس (Inverted Index): الهيكل المعياري</h3>
    <p>يقوم الفهرس المعكوس بحفظ الخانات غير الصفرية فقط، بحيث يربط كل كلمة بقائمة أرقام الوثائق التي ظهرت فيها.</p>
    <ul>
        <li><strong>القاموس (Dictionary / Vocabulary):</strong> قائمة تحوي كافة الكلمات الفريدة مرتبة أبجدياً مع تردد الوثائق ($df$). يوضع غالباً في الذاكرة العشوائية (RAM) باستخدام B-Tree أو Hash Table.</li>
        <li><strong>قوائم النشر (Postings Lists):</strong> لكل كلمة في القاموس، قائمة متغيرة الطول بأرقام الوثائق (DocIDs) التي وردت فيها تلك الكلمة، وتكون مرتبة <strong>تصاعدياً دائماً</strong>.</li>
    </ul>

    <h3>1.5 مراحل بناء الفهرس المعكوس</h3>
    <ol>
        <li><strong>تحليل الوثائق (Parsing):</strong> استخراج سلاسل الحروف وتحديد الترميز (UTF-8) من الملفات المختلفة (PDF, HTML, Word).</li>
        <li><strong>التقطيع اللغوي (Tokenization):</strong> تقسيم تدفق الحروف إلى وحدات نصية وكلمات منفصلة (Tokens).</li>
        <li><strong>المعالجة اللغوية (Linguistic Processing):</strong> توحيد حالة الحروف، معالجة كلمات التوقف، والتجذير لتحويل الكلمات إلى مفردات معيارية (Terms).</li>
        <li><strong>الفهرسة والترتيب:</strong> استخراج أزواج (الكلمة، رقم الوثيقة)، ترتيبها أبجدياً حسب الكلمة ثم تصاعدياً حسب رقم الوثيقة، وتجميعها في قوائم النشر.</li>
    </ol>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. معالجة الاستعلامات البوليانية، التحسين واستعلامات العبارات (المحاضرة 2)</h2>

    <h3>2.1 خوارزمية دمج وتقاطع قوائم النشر (Postings Merge)</h3>
    <p>لتقييم استعلام بولياني يحتوي على AND (مثل `Brutus AND Caesar`)، يتم المرور المتزامن على قائمتي النشر المرتبتين باستخدام مؤشرين ($p_1, p_2$).</p>

    <div class="code-box">
Algorithm INTERSECT(p1, p2):
    answer = []
    while p1 != NIL and p2 != NIL:
        if DocID(p1) == DocID(p2):
            answer.append(DocID(p1))
            p1 = p1.next
            p2 = p2.next
        else if DocID(p1) < DocID(p2):
            p1 = p1.next
        else:
            p2 = p2.next
    return answer
    </div>

    <div class="callout tip">
        <div class="callout-title">التعقيد الزمني (Time Complexity)</div>
        نظراً لأن القائمتين مرتبتان تصاعدياً مسبقاً، فإن كل مؤشر يمر على القائمة مرة واحدة خطياً. التعقيد الزمني هو <strong>O(x + y)</strong> خطي تماماً، حيث x و y هما طولا القائمتين.
    </div>

    <h3>2.2 تحسين ترتيب تنفيذ الاستعلامات البوليانية</h3>
    <ul>
        <li><strong>قاعدة الترتيب الأمثل:</strong> في استعلامات AND المتعددة، يتم ترتيب الكلمات دائماً وفقاً لـ <strong>التردد التصاعدي للوثائق (Increasing df)</strong>؛ أي البدء بأقصر قوائم النشر طولاً.</li>
        <li><strong>مثال امتحاني شهير:</strong>
            <ul>
                <li>`Calpurnia` ($df = 4$)</li>
                <li>`Brutus` ($df = 20,000$)</li>
                <li>`Caesar` ($df = 40,000$)</li>
                <li>الترتيب الأمثل للتنفيذ هو: `(Calpurnia AND Brutus) AND Caesar`. لأن التقاطع الأول ينتج قائمة لا تزيد عن <strong>4 وثائق فقط</strong>! وتقاطع 4 وثائق مع قائمة Caesar يستغرق زمناً يقارب الصفر.</li>
            </ul>
        </li>
    </ul>

    <h3>2.3 استعلامات العبارات المركبة: فهرس الزوجين مقابل الفهرس الموضعي</h3>
    <table>
        <tr>
            <th>نوع الفهرس</th>
            <th>طريقة العمل</th>
            <th>المزايا والعيوب</th>
        </tr>
        <tr>
            <td><strong>فهرس الكلمتين (Biword Index)</strong></td>
            <td>فهرسة كل كلمتين متجاورتين كمفردة مستقلة في القاموس (مثل "friends romans", "romans countrymen").</td>
            <td><strong>المزايا:</strong> سرعة فائقة للعبارات المكونة من كلمتين.<br><strong>العيوب:</strong> انفجار هائل في حجم القاموس ($V^2$)، احتمالية ظهور نتائج خاطئة للعبارات الطويلة، وعجزه عن استعلامات التقارب.</td>
        </tr>
        <tr>
            <td><strong>الفهرس الموضعي (Positional Index)</strong></td>
            <td>حفظ أرقام مواقع الكلمات بدقة داخل كل وثيقة: `term -> docID: <pos1, pos2, ...>`.</td>
            <td><strong>المزايا:</strong> يحل استعلامات العبارات مهما كان طولها واستعلامات التقارب (`/k`). وهو الحل المعياري المتبع عالمياً.<br><strong>العيوب:</strong> تضخم قوائم النشر من 2 إلى 4 أضعاف (35-50% من حجم النص الأصلي).</td>
        </tr>
        <tr>
            <td><strong>المخطط الهجين (Combination Scheme)</strong></td>
            <td>فهرسة العبارات شديدة التكرار كزوجين (مثل "New York")، واستخدام الفهرس الموضعي للعبارات النادرة.</td>
            <td>أفضل توازن ممكن بين سرعة التنفيذ وسعة التخزين.</td>
        </tr>
    </table>

    <h3>2.4 استعلامات التقارب (Proximity Queries: `/k`)</h3>
    <p>استعلام مثل `employment /3 federal` يبحث عن الوثائق التي تظهر فيها الكلمتان بفاصل لا يتجاوز 3 كلمات بأي ترتيب ($|pos_1 - pos_2| \le 3$). يقوم الفهرس الموضعي بفحص تطابق رقم الوثيقة ثم مقارنة الفارق بين المواقع.</p>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>3. تسريع دمج القوائم ومؤشرات القفز (المحاضرة 3)</h2>

    <h3>3.1 آلية مؤشرات القفز (Skip Pointers) وأهميتها</h3>
    <p>عند تقاطع قائمتين طويلتين، يؤدي الفحص المتسلسل خطوة بخطوة إلى هدر فحص آلاف الوثائق التي لن تتطابق. تقوم <strong>مؤشرات القفز</strong> بإنشاء مسارات اختصار للأمام لتخطي أجزاء كبيرة من القائمة دفعة واحدة.</p>

    <div class="callout tip">
        <div class="callout-title">قاعدة اتخاذ قرار القفز</div>
        أثناء مقارنة المؤشرين $p_1$ و $p_2$: إذا كان لدى $p_1$ مؤشر قفز وكان <strong>skip(p1) &le; DocID(p2)</strong>، يتم القفز مباشرة إلى `skip(p1)`! أما إذا كان `skip(p1) > DocID(p2)`، فلا نقفز (لتجنب تجاوز وثيقة مطابقة محتملة) ونتقدم خطوة واحدة عادية.
    </div>

    <h3>3.2 موضع وضع مؤشرات القفز: القاعدة الذهبية</h3>
    <ul>
        <li><strong>المعادلة والمفاضلة:</strong> زيادة مؤشرات القفز تعطي فرصاً أكبر للقفز ولكنها تزيد مساحة التخزين وتكلفة الفحص؛ وقلة المؤشرات توفر التخزين ولكنها تفوت فرص التخطي السريع.</li>
        <li><strong>القاعدة القياسية (Heuristic):</strong> في قائمة نشر طولها $P$، يتم وضع مؤشرات قفز متباعدة بمسافات متساوية كل <strong>&radic;P</strong> عنصر!</li>
        <li><strong>مثال عملي:</strong> إذا كان طول القائمة $P = 10,000$ وثيقة، نضع مؤشر قفز كل $\sqrt{10,000} = 100$ عنصر، مما ينتج حوالي 100 مؤشر قفز.</li>
        <li><strong>محدودية الفهارس الديناميكية:</strong> تعمل مؤشرات القفز بكفاءة مثالية على الفهارس الثابتة (Static)؛ أما في الفهارس المتغيرة بكثرة، فإن عمليات الإضافة والحذف تفسد المسافات وتتطلب إعادة حساب مكلفة.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>4. مفردات القاموس والتوحيد المعياري للنصوص (المحاضرة 5)</h2>

    <h3>4.1 تحديات التقطيع النصي (Tokenization)</h3>
    <ul>
        <li><strong>ترميز المحارف (Character Encodings):</strong> التعرف الصحيح على ترميز الملفات (UTF-8, ASCII) لتجنب ظهور رموز غير مفهومة (Mojibake).</li>
        <li><strong>الشرطات الواصلة (Hyphens):</strong> الكلمات المركبة (مثل `Hewlett-Packard`, `state-of-the-art`) تفرض تحدياً: هل تُفهرس ككلمة واحدة أم تُفصل إلى كلمات مستقلة؟</li>
        <li><strong>الفاصلة العليا (Apostrophes):</strong> الاختصارات (`aren't`) وحالات الملكية (`children's`) والأسماء الأيرلندية (`O'Neill`).</li>
        <li><strong>الأرقام والصيغ:</strong> أرقام الطرازات (`Boeing 747`)، التواريخ، والصيغ الكيميائية تمتلك قدرة تمييزية فائقة ويجب الحفاظ عليها في الفهرس.</li>
        <li><strong>خصوصية اللغات:</strong> الصينية واليابانية لا تحتويان على مسافات بين الكلمات وتتطلبان تقطيعاً صرفياً أو N-grams؛ بينما تلتحق بلغة الضاد (العربية) سوابق لواصق مثل الواو وأداة التعريف "ال" في بداية الأسماء.</li>
    </ul>

    <h3>4.2 كلمات التوقف (Stop Words): التقليد القديم مقابل التوجه الحديث</h3>
    <ul>
        <li><strong>كلمات التوقف:</strong> كلمات وظيفية شديدة التكرار وقليلة الفائدة الدلالية في التمييز بين الوثائق (مثل: `the`, `a`, `in`, `of`, `to`, `من`, `في`, `على`).</li>
        <li><strong>المنهج التقليدي:</strong> حذف قائمة من 30 إلى 150 كلمة توقف لتوفير مساحة التخزين على القرص.</li>
        <li><strong>التوجه الحديث في محركات البحث الكبرى:</strong> الإبقاء على كافة كلمات التوقف في الفهرس، وذلك لسببين: (1) تقنيات الضغط الحديثة حلت مشكلة المساحة؛ (2) يحتاج المستخدمون للبحث عن عبارات دقيقة تتكون معظمها من كلمات توقف (مثل `"To be or not to be"`, `"Let it be"`).</li>
    </ul>

    <h3>4.3 توحيد النصوص: حالة الأحرف ومجموعات التكافؤ</h3>
    <ul>
        <li><strong>مجموعات التكافؤ (Equivalence Classes):</strong> دمج الأشكال المتعددة للكلمة الواحدة في رمز موحد (مثل تحويل `U.S.A.` و `USA` إلى مصطلح واحد).</li>
        <li><strong>توحيد حالة الأحرف (Case Folding):</strong> تحويل الحروف الإنجليزية جميعها إلى أحرف صغيرة (Lowercase). محاذيره: قد يخلط بين أسماء الأعلام والكلمات العادية (مثل `US` كدولة و `us` كضمير؛ و `Bush` كرئيس و `bush` كشجيرة).</li>
        <li><strong>خوارزمية ساوندكس (Soundex):</strong> خوارزمية صوتية تحول الكلمات إلى رموز وفقاً لنطقها الصوتي باللغة الإنجليزية لمطابقة الأسماء المتشابهة صوتياً رغم اختلاف كتابتها (مثل `Smith` و `Smyth`).</li>
    </ul>

    <h3>4.4 التجذير الصرفي مقابل التحليل المعجمي (Stemming vs. Lemmatization)</h3>
    <table>
        <tr>
            <th>وجه المقارنة</th>
            <th>التجذير الصرفي الخشن (Stemming)</th>
            <th>التحليل المعجمي الدقيق (Lemmatization)</th>
        </tr>
        <tr>
            <td><strong>المنهجية</strong></td>
            <td>قص تجريبي وسريع لنهايات الكلمات وزوائدها دون قواعد نحوية أو قواميس.</td>
            <td>تحليل صرفي ونحوي كامل بالاعتماد على معجم وقواعد وسياق موقع الكلمة (POS).</td>
        </tr>
        <tr>
            <td><strong>المخرج الناتج</strong></td>
            <td>غالباً ما ينتج جذراً غير حقيقي ولا يمثل كلمة في القاموس (مثل: `automate, automatic, automation` &rarr; `automat`).</td>
            <td>ينتج دائماً الكلمة المعجمية الأصلية الصحيحة نحوياً وتسمى <strong>Lemma</strong>.</td>
        </tr>
        <tr>
            <td><strong>حساسية السياق</strong></td>
            <td>أعمى للسياق النحوي ويعامل كل كلمة بنفس القاعدة الجامدة.</td>
            <td>يدرك السياق؛ فيحول `saw` إلى `see` إذا وردت كفعل، ويتركها `saw` (منشار) إذا كانت اسماً. ويحول `better` إلى `good`.</td>
        </tr>
        <tr>
            <td><strong>السرعة والتعقيد</strong></td>
            <td>فائق السرعة وخفيف جداً على الذاكرة ومناسب للأنظمة الضخمة.</td>
            <td>معقد حوسبياً ويستهلك معالجة وذاكرة أكبر لقراءة القواميس النحوية.</td>
        </tr>
    </table>

    <h3>4.5 خوارزمية بورتر (Porter Stemmer) وأخطاء التجذير</h3>
    <ul>
        <li><strong>خوارزمية بورتر (1980):</strong> الخوارزمية القياسية الأكثر انتشاراً لتجذير الإنجليزية، وتتألف من 5 مراحل متتالية من قواعد قص اللواحق استناداً لمقياس المقاطع الصوتية $m$.</li>
        <li><strong>خطأ الإفراط في التجذير (Over-stemming):</strong> قص أجزاء زائدة مما يؤدي لدمج كلمات مختلفة المعنى في جذر واحد خطأً (مثل دمج `universe` و `university` إلى `univers`؛ أو `policy` و `police` إلى `polic`)، مما يقلل من دقة البحث (Precision).</li>
        <li><strong>خطأ التقصير في التجذير (Under-stemming):</strong> الفشل في إرجاع الكلمات المرتبطة لنفس الجذر المشترك (مثل عدم دمج `adhere` و `adhesion`)، مما يضر بمعدل الاستدعاء (Recall).</li>
        <li><strong>قانون هيبس (Heaps' Law):</strong> حجم المفردات $V$ ينمو باستمرار مع نمو حجم الوثائق $N$ وفق قانون القوة $V = k N^\beta$ (حيث $\beta \approx 0.4 - 0.6$)، مما يؤكد أن مفردات القاموس لا تتوقف أبداً عن التوسع.</li>
    </ul>
</div>

</body>
</html>"""

with open('summaries/IR_Summary_EN.html', 'w', encoding='utf-8') as f:
    f.write(html_ir_en)
with open('summaries/IR_Summary_AR.html', 'w', encoding='utf-8') as f:
    f.write(html_ir_ar)

print("Saved HTML summaries for IR.")

# Compile to PDF using Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
for lang, fn_html, fn_pdf in [
    ('EN', 'summaries/IR_Summary_EN.html', 'summaries/IR_Summary_EN.pdf'),
    ('AR', 'summaries/IR_Summary_AR.html', 'summaries/IR_Summary_AR.pdf')
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
