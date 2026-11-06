import os
import subprocess
import shutil

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
    background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%);
    color: #ffffff;
    padding: 38px 40px;
    border-radius: 12px;
    margin-bottom: 25px;
    box-shadow: 0 10px 25px -5px rgba(2, 132, 199, 0.3);
}

.cover h1 {
    font-size: 26px;
    font-weight: 800;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
}

.cover .subtitle {
    font-size: 15px;
    opacity: 0.92;
    margin: 0 0 15px 0;
}

.cover .meta {
    display: flex;
    gap: 15px;
    font-size: 12px;
    opacity: 0.85;
    flex-wrap: wrap;
}

.section {
    margin-bottom: 25px;
    page-break-inside: avoid;
}

h2 {
    font-size: 18px;
    font-weight: 700;
    color: #0369a1;
    border-bottom: 2px solid #e0f2fe;
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
}

body.ar h2 {
    color: #0369a1;
    border-bottom-color: #e0f2fe;
}

h3 {
    font-size: 15px;
    font-weight: 700;
    color: #0f172a;
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
    background: #f0f9ff;
    border-left: 4px solid #0284c7;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin: 15px 0;
    font-size: 13px;
}

body.ar .callout {
    border-left: none;
    border-right: 4px solid #0284c7;
    border-radius: 8px 0 0 8px;
}

.callout.warning {
    border-color: #f59e0b;
    background: #fffbeb;
}

.callout.tip {
    border-color: #10b981;
    background: #ecfdf5;
}

.callout-title {
    font-weight: 700;
    margin-bottom: 4px;
    color: #0369a1;
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
    background-color: #f8fafc;
    font-weight: 700;
    color: #0f172a;
}

tr:nth-child(even) {
    background-color: #f0f9ff;
}

.badge {
    display: inline-block;
    padding: 2px 8px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
    background: #e0f2fe;
    color: #0369a1;
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

# ==========================================
# ENGLISH SUMMARY HTML
# ==========================================
html_isapp_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Information Systems Applications (IS App) - Comprehensive Midterm Guide</title>
<style>
{css_shared}
</style>
</head>
<body>

<div class="cover">
    <h1>Information Systems Applications (IS App)</h1>
    <div class="subtitle">Comprehensive Midterm Academic Study Guide & Systematic Reference</div>
    <div class="meta">
        <span>📖 Scope: Chapter 1 (IS Foundations) & Chapter 2 (IS in Organizations)</span>
        <span>🎯 Target: Midterm Exam High-Performance Review</span>
        <span>⏱️ Format: Definitions, Frameworks, Architectural Flows & Comparative Tables</span>
    </div>
</div>

<div class="section">
    <h2>1. Chapter 1: Introduction to Information Systems</h2>

    <h3>1.1 What is an Information System (IS)?</h3>
    <p>An <strong>Information System (IS)</strong> is defined as a formal, socio-technical set of interrelated components designed to:</p>
    <ul>
        <li><strong>Collect (Capture):</strong> Gather raw data from internal operational sources and the external environment.</li>
        <li><strong>Process:</strong> Transform raw data into meaningful, actionable information through calculation, sorting, and classification.</li>
        <li><strong>Store:</strong> Persist data and structural models securely for future recall.</li>
        <li><strong>Distribute (Disseminate):</strong> Deliver tailored outputs and analytical insights to decision-makers and stakeholders.</li>
    </ul>
    <p><strong>Primary Organizational Purposes Supported by IS:</strong></p>
    <ul>
        <li><strong>Decision-Making:</strong> Furnishes accurate, timely facts to reduce risk and uncertainty.</li>
        <li><strong>Coordination:</strong> Synchronizes tasks and workflows across disparate functional departments.</li>
        <li><strong>Control & Monitoring:</strong> Benchmarks actual performance against planned organizational goals.</li>
        <li><strong>Analysis & Visualization:</strong> Unveils trends, operational bottlenecks, and strategic patterns.</li>
    </ul>

    <div class="callout tip">
        <div class="callout-title">Core Driver: Why Do Organizations Invest in Information Systems?</div>
        Organizations leverage IS to convert fragmented data into strategic assets, optimize operational productivity, drastically cut cycle times, minimize administrative overhead, and adapt rapidly to competitive shifts.
    </div>

    <h3>1.2 Data vs. Information: The Definitive Distinction</h3>
    <table>
        <tr>
            <th style="width: 25%;">Dimension</th>
            <th style="width: 37%;">Data (البيانات)</th>
            <th style="width: 38%;">Information (المعلومات)</th>
        </tr>
        <tr>
            <td><strong>Definition</strong></td>
            <td>Raw facts, unformatted figures, and uninterpreted symbols lacking context.</td>
            <td>Data that has been processed, structured, contextualized, and organized to convey meaning.</td>
        </tr>
        <tr>
            <td><strong>State</strong></td>
            <td>Unprocessed input.</td>
            <td>Processed, value-added output.</td>
        </tr>
        <tr>
            <td><strong>Decision Utility</strong></td>
            <td>Minimal to none on its own (cannot directly guide complex strategy).</td>
            <td>High utility (directly empowers managerial decisions).</td>
        </tr>
        <tr>
            <td><strong>Concrete Example</strong></td>
            <td><code>80, 75, 90, 65</code> (Four isolated exam scores)</td>
            <td><code>Class Average = 77.5%</code> (Passing rate = 100%)</td>
        </tr>
    </table>

    <div class="code-box">
Fundamental IS Equation: Data + Processing / Context = Information → Actionable Knowledge → Sound Decision
    </div>

    <h3>1.3 The Five Core Components of an Information System</h3>
    <p>An Information System is far more than mere hardware and software. It is a <em>socio-technical system</em> comprising five synergistic pillars:</p>
    <ol>
        <li><strong>Hardware:</strong> The physical tangible machinery (servers, desktop PCs, solid-state storage devices, routers, switches, barcode scanners, and IoT sensors).</li>
        <li><strong>Software:</strong> The algorithmic instructions and applications that control hardware (Operating Systems, DBMS like Oracle/SQL Server, Enterprise Resource Planning systems, mobile apps).</li>
        <li><strong>Data:</strong> The core raw material ingested and manipulated by the system (student matriculation IDs, product catalog codes, patient clinical histories, timestamped invoices).</li>
        <li><strong>People:</strong> The indispensable human element that operates, administers, and benefits from the system (end-users, database administrators, systems analysts, software engineers, and executive decision-makers).</li>
        <li><strong>Procedures / Processes:</strong> Formalized organizational policies, operating rules, and sequence workflows governing how technology and humans interact (e.g., University Registration: <em>Log In → Select Courses → Prerequisite Validation → Payment Verification → Official Enrollment</em>).</li>
    </ol>

    <div class="callout warning">
        <div class="callout-title">Critical Academic Principle</div>
        Technology without trained, motivated <strong>People</strong> and well-governed <strong>Procedures</strong> will inevitably fail. Enterprise IS failures stem far more often from flawed human workflows than from software coding bugs.
    </div>

    <h3>1.4 How an Information System Works: The Operational Loop</h3>
    <div class="code-box">
[INPUT: Data Capture] ───► [PROCESSING: Transformation / Calculation] ───► [OUTPUT: Information Dissemination]
                                         ▲                                             │
                                         │──────────── [FEEDBACK LOOP] ────────────────┘
    </div>
    <p><strong>The Five Universal IS Operations:</strong></p>
    <ul>
        <li><strong>1. Data Capture:</strong> Collecting or recording raw data at the point of origin (e.g., POS terminal, web form, RFID badge reader).</li>
        <li><strong>2. Data Processing:</strong> Applying logical, arithmetic, and filtering algorithms to restructure inputs.</li>
        <li><strong>3. Data Storage:</strong> Persisting records into structured relational or cloud storage for durability and referential integrity.</li>
        <li><strong>4. Data Retrieval:</strong> Querying, indexing, and pulling stored records on-demand (e.g., SQL SELECT queries).</li>
        <li><strong>5. Data Dissemination:</strong> Formatting and distributing reports, alerts, notifications, and visual charts to target users.</li>
        <li><strong>Feedback:</strong> Output evaluated against expectations; discrepancies route back into input/processing adjustments to ensure continuous quality control.</li>
    </ul>

    <h3>1.5 Clear Boundary Demarcation: Computer Science vs. IT vs. IS</h3>
    <table>
        <tr>
            <th style="width: 20%;">Field</th>
            <th style="width: 40%;">Primary Conceptual Focus</th>
            <th style="width: 40%;">Typical Scope & Artifacts</th>
        </tr>
        <tr>
            <td><strong>Computer Science (CS)</strong></td>
            <td>Theoretical foundations of computation, algorithms, compiler design, software engineering, and computational complexity.</td>
            <td>Designing efficient search algorithms, creating programming languages, developing core operating system kernels.</td>
        </tr>
        <tr>
            <td><strong>Information Technology (IT)</strong></td>
            <td>Implementing, configuring, securing, and maintaining technological infrastructure, networks, and communication hardware.</td>
            <td>Deploying local area networks (LANs), configuring firewalls, administering server racks, tech support troubleshooting.</td>
        </tr>
        <tr>
            <td><strong>Information Systems (IS)</strong></td>
            <td>Applying technology, people, data, and workflows within organizational and business contexts to solve real-world problems.</td>
            <td>Business process reengineering, ERP deployments, decision support, executive dashboards, competitive digital strategy.</td>
        </tr>
    </table>

    <h3>1.6 IS and Emerging Technologies</h3>
    <p>Modern Information Systems are increasingly augmented by frontier technologies:</p>
    <ul>
        <li><strong>Artificial Intelligence (AI) & Machine Learning (ML):</strong> Predictive maintenance, automated fraud detection, intelligent recommendation engines.</li>
        <li><strong>Cloud Computing:</strong> Elastic on-demand infrastructure (SaaS, PaaS, IaaS) providing high availability and global scalability without heavy on-premise capital expenditure.</li>
        <li><strong>Big Data Analytics:</strong> Processing high-volume, high-velocity, high-variety data streams to uncover micro-segment consumer behaviors.</li>
        <li><strong>Internet of Things (IoT):</strong> Connected smart meters, RFID tags, and telematics sensors broadcasting live real-world physical telemetry into transactional databases.</li>
        <li><strong>Blockchain:</strong> Cryptographically verified, distributed, tamper-proof ledgers for supply-chain provenance and financial cross-border settlements.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. Chapter 2: Information Systems in Organizations</h2>

    <h3>2.1 The Organization: Purpose and Core Resources</h3>
    <p>An <strong>Organization</strong> is a formal, structured social collective of individuals working in concert through coordinated activities to attain shared strategic objectives.</p>
    <p>Every enterprise mobilizes five fundamental resource categories:</p>
    <ol>
        <li><strong>Human Resources:</strong> Skilled employees, frontline workers, specialists, and managers.</li>
        <li><strong>Financial Resources:</strong> Investment capital, working cash reserves, lines of credit, and retained earnings.</li>
        <li><strong>Physical Resources:</strong> Commercial real estate, industrial machinery, manufacturing plants, vehicles, and raw inventory.</li>
        <li><strong>Information Resources:</strong> Structured customer databases, market research, patents, employee knowledge assets, and operational logs.</li>
        <li><strong>Technological Resources:</strong> Computer hardware, proprietary software licenses, cloud architectures, and telecommunication networks.</li>
    </ol>

    <h3>2.2 Traditional Functional Areas (Departmental Silos)</h3>
    <table>
        <tr>
            <th style="width: 25%;">Functional Department</th>
            <th style="width: 45%;">Core Organizational Responsibility</th>
            <th style="width: 30%;">Information System Support</th>
        </tr>
        <tr>
            <td><strong>Marketing & Sales</strong></td>
            <td>Promoting products, identifying consumer demand, pricing, advertising, and closing sales contracts.</td>
            <td>CRM systems, lead tracking, customer demographic profiling, web analytics.</td>
        </tr>
        <tr>
            <td><strong>Finance</strong></td>
            <td>Managing capital structure, long-term portfolio investments, loan facilities, and cash-flow liquidity.</td>
            <td>Financial modeling, investment forecasting, portfolio management systems.</td>
        </tr>
        <tr>
            <td><strong>Accounting</strong></td>
            <td>Recording historical financial transactions, billing, accounts payable/receivable, payroll, and statutory tax compliance.</td>
            <td>General ledger systems, accounts reconciliation, automated auditing modules.</td>
        </tr>
        <tr>
            <td><strong>Human Resources (HR)</strong></td>
            <td>Talent recruiting, onboarding, benefits compensation administration, performance appraisal, and regulatory labor compliance.</td>
            <td>HRIS (Human Resource Information Systems), automated payroll, employee self-service portals.</td>
        </tr>
        <tr>
            <td><strong>Production / Operations</strong></td>
            <td>Transforming raw components into finished physical goods or delivering operational service commitments.</td>
            <td>Supply Chain Management (SCM), Computer-Integrated Manufacturing (CIM), inventory replenishment.</td>
        </tr>
        <tr>
            <td><strong>Management</strong></td>
            <td>Setting overarching mission goals, planning resource allocations, and governing organizational execution.</td>
            <td>Executive dashboards, enterprise performance tracking, risk assessment suites.</td>
        </tr>
    </table>

    <h3>2.3 The Three Hierarchical Management Levels & Information Needs</h3>
    <table>
        <tr>
            <th>Characteristic</th>
            <th>Operational Management</th>
            <th>Middle Management</th>
            <th>Top / Executive Management</th>
        </tr>
        <tr>
            <td><strong>Key Personnel</strong></td>
            <td>Shift supervisors, team leads, frontline cashiers, clerks.</td>
            <td>Department heads, branch managers, plant directors.</td>
            <td>CEO, CFO, CIO, Board of Directors, University President.</td>
        </tr>
        <tr>
            <td><strong>Focus & Horizon</strong></td>
            <td>Day-to-day routine tasks; short-term (hours, days, weeks).</td>
            <td>Departmental tactics & control; medium-term (months, quarters).</td>
            <td>Enterprise vision & survival; long-term (1 to 5+ years).</td>
        </tr>
        <tr>
            <td><strong>Decision Nature</strong></td>
            <td><strong>Structured</strong> (Predefined rules, algorithmic, deterministic).</td>
            <td><strong>Semi-Structured</strong> (Combines standard procedures with human evaluation).</td>
            <td><strong>Unstructured</strong> (Novel, ambiguous, high uncertainty, strategic judgment).</td>
        </tr>
        <tr>
            <td><strong>Information Requirements</strong></td>
            <td>Highly <strong>detailed</strong>, current, real-time, strictly internal.</td>
            <td><strong>Summarized</strong>, periodic (monthly/quarterly), comparative (actual vs budget).</td>
            <td>Highly <strong>aggregated</strong>, macro-level KPIs, combined internal + external environment.</td>
        </tr>
        <tr>
            <td><strong>Dedicated System</strong></td>
            <td><strong>TPS</strong> (Transaction Processing Systems).</td>
            <td><strong>MIS</strong> (Management Info Systems) & <strong>DSS</strong>.</td>
            <td><strong>EIS / ESS</strong> (Executive Information/Support Systems).</td>
        </tr>
    </table>

    <h3>2.4 Taxonomy of Enterprise Information Systems</h3>
    <ul>
        <li><strong>1. Transaction Processing Systems (TPS):</strong>
            <ul>
                <li>The foundation of all organizational systems; records continuous daily operational events.</li>
                <li>Characteristics: High transaction throughput, rapid processing, strict atomicity/data integrity, routine structured outputs.</li>
                <li>Examples: Supermarket checkout scanner, ATM cash withdrawals, airline reservation bookings, hotel guest check-in.</li>
            </ul>
        </li>
        <li><strong>2. Management Information Systems (MIS):</strong>
            <ul>
                <li>Extracts data directly from underlying TPS to generate scheduled, structured reports for middle management.</li>
                <li>Characteristics: Historical and current internal orientation, summary reports, exception reports (highlighting deviations exceeding tolerances).</li>
                <li>Examples: Monthly sales variance report by store, department budget vs. actual expenditure, inventory scrap rate summaries.</li>
            </ul>
        </li>
        <li><strong>3. Decision Support Systems (DSS):</strong>
            <ul>
                <li>Interactive systems providing mathematical modeling, simulation, and data analysis to resolve semi-structured dilemmas.</li>
                <li>Characteristics: Highly flexible, user-driven, features <em>What-If Analysis</em>, sensitivity analysis, goal-seeking models.</li>
                <li>Examples: Simulating financial ROI of alternative warehouse locations, production scheduling under fluctuating raw material costs.</li>
            </ul>
        </li>
        <li><strong>4. Executive Information / Support Systems (EIS / ESS):</strong>
            <ul>
                <li>Designed for senior corporate executives with zero tolerance for complicated technical interfaces.</li>
                <li>Characteristics: Graphic-rich dashboards, macro economic monitoring, real-time corporate pulse, and <strong>Drill-Down capability</strong> (clicking high-level charts to reveal nested root-cause operational data).</li>
                <li>Examples: Enterprise KPI executive cockpit showing market share, quarterly net profit margin, and supply chain vulnerability indexes.</li>
            </ul>
        </li>
    </ul>

    <div class="callout tip">
        <div class="callout-title">System Interdependence Hierarchy</div>
        TPS acts as the vital data wellspring. Operational transactions in TPS feed into MIS and DSS databases. In turn, MIS and DSS aggregate insights that populate executive dashboards in EIS/ESS. They are synergistic complements, not isolated silos.
    </div>

    <h3>2.5 Business Processes and Cross-Functional Systems</h3>
    <p>A <strong>Business Process</strong> is a structured network of logically related activities performed in sequence to transform defined inputs into valued outputs that satisfy organizational goals or customer needs.</p>
    <p><strong>Three Primary Classes of Business Processes:</strong></p>
    <ul>
        <li><strong>Core (Primary) Processes:</strong> Directly touch the external customer and create core economic value (e.g., manufacturing automobiles, fulfilling online store orders, serving hospital patients).</li>
        <li><strong>Support Processes:</strong> Enable core activities behind the scenes (e.g., IT workstation maintenance, HR recruitment, vendor invoice accounting).</li>
        <li><strong>Management Processes:</strong> Govern, coordinate, and steer the enterprise (e.g., annual strategic budgeting, compliance audits, quality management).</li>
    </ul>

    <h4>The Power of Cross-Functional Information Systems:</h4>
    <p>Traditional organizations suffered from isolated <em>Departmental Silos</em> where Marketing, Finance, and Warehousing did not communicate. Modern Enterprise Systems (ERP) are <strong>Cross-Functional</strong>, integrating end-to-end business workflows seamlessly:</p>
    <div class="code-box">
Customer Order Placed (Sales)
       │
       ▼
Inventory Availability Verified (Warehouse / SCM)
       │
       ▼
Customer Credit Approved (Finance / Accounting)
       │
       ▼
Goods Packaged & Dispatched (Operations / Logistics)
       │
       ▼
Invoice Disseminated & Payment Settled (Accounting)
    </div>

    <h3>2.6 Achieving Competitive Advantage Through Information Systems</h3>
    <p>A <strong>Competitive Advantage</strong> represents a distinctive capability or structural edge enabling a firm to outperform industry rivals in profitability, customer acquisition, or market share.</p>
    <p>Information Systems create competitive advantages via:</p>
    <ul>
        <li><strong>Operational Cost Leadership:</strong> Automating repetitive labor, slashing clerical errors, and optimizing supply chain holding costs.</li>
        <li><strong>Product & Service Differentiation:</strong> Embedding digital capabilities (e.g., real-time parcel tracking, personalized smart recommendations).</li>
        <li><strong>Customer & Supplier Lock-In:</strong> Establishing seamless digital interfaces that raise switching costs for buyers and suppliers.</li>
        <li><strong>Organizational Agility:</strong> Real-time telemetric visibility enabling instantaneous pivots when consumer market demands fluctuate.</li>
    </ul>

    <h3>2.7 Practical Case Study: University Enterprise Analysis</h3>
    <table>
        <tr>
            <th>University Stakeholder</th>
            <th>Management Level</th>
            <th>Primary Information Needs & System Interaction</th>
        </tr>
        <tr>
            <td><strong>Registration Clerks</strong></td>
            <td>Operational</td>
            <td>Student prerequisite clearance, seat availability in classrooms, hold status checks (via TPS).</td>
        </tr>
        <tr>
            <td><strong>Academic Department Chair</strong></td>
            <td>Middle Management</td>
            <td>Semester enrollment trends, faculty teaching load balance, course failure rates (via MIS).</td>
        </tr>
        <tr>
            <td><strong>Finance Director</strong></td>
            <td>Middle Management</td>
            <td>Tuition fee collection status, departmental budget variances, scholarship expenditure tracking (via MIS/DSS).</td>
        </tr>
        <tr>
            <td><strong>University President</strong></td>
            <td>Top Management</td>
            <td>Multi-year student retention metrics, 5-year campus expansion budget feasibility, institutional ranking benchmarks (via EIS/ESS).</td>
        </tr>
    </table>
</div>

</body>
</html>
"""

# ==========================================
# ARABIC SUMMARY HTML
# ==========================================
html_isapp_ar = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>تطبيقات نظم المعلومات (IS App) - ملخص الميدتيرم الشامل</title>
<style>
{css_shared}
</style>
</head>
<body class="ar">

<div class="cover">
    <h1>تطبيقات نظم المعلومات (Information Systems Applications - IS App)</h1>
    <div class="subtitle">الملخص الأكاديمي الشامل والمرجع المنهجي المكثف لامتحان الميدتيرم</div>
    <div class="meta">
        <span>📖 النطاق: المحاضرة 1 (مقدمة في نظم المعلومات) & المحاضرة 2 (نظم المعلومات في المنظمات)</span>
        <span>🎯 الهدف: تغطية 100% من المفاهيم، المقارنات، والهياكل التنظيمية</span>
        <span>⚡ الأسلوب: صياغة منهجية مركزة، مقارنات جدولية، وأمثلة تطبيقية واقعية</span>
    </div>
</div>

<div class="section">
    <h2>1. الفصل الأول: مدخل إلى نظم المعلومات (Introduction to IS)</h2>

    <h3>1.1 ما هو نظام المعلومات (Information System)؟</h3>
    <p>يُعرَّف <strong>نظام المعلومات (IS)</strong> بأنه منظومة اجتماعية-تقنية متكاملة تتألف من مجموعة من العناصر المترابطة التي تعمل معاً في تناغم مستمر بهدف:</p>
    <ul>
        <li><strong>جمع البيانات (Collect / Capture):</strong> التقاط وحصر البيانات الأولية من مصادرها الداخلية وبيئتها الخارجية.</li>
        <li><strong>معالجة البيانات (Process):</strong> تحويل البيانات الخام عبر الحساب والتصنيف والترتيب إلى صيغ مفهومة.</li>
        <li><strong>تخزين البيانات (Store):</strong> حفظ البيانات والمعلومات والملفات في وسائط آمنة لضمان استرجاعها مستقبلاً.</li>
        <li><strong>توزيع ونشر المعلومات (Distribute / Disseminate):</strong> إيصال النتائج والمعلومات المجهزة إلى المستفيدين وصناع القرار بالوقت والشكل المناسبين.</li>
    </ul>
    <p><strong>الأنشطة التنظيمية الحيوية التي يدعمها نظام المعلومات:</strong></p>
    <ul>
        <li><strong>دعم اتخاذ القرار (Decision-making):</strong> توفير حقائق دقيقة وموثوقة تقلل من المخاطرة والغموض عند الاختيار بين البدائل.</li>
        <li><strong>التنسيق والربط (Coordination):</strong> مزامنة الأنشطة والتدفقات التشغيلية بين الأقسام المختلفة ومنع التضارب.</li>
        <li><strong>الرقابة والتحكم (Control):</strong> مقارنة الإنجاز الفعلي مع الخطط والمعايير المستهدفة لتحديد الانحرافات ومعالجتها.</li>
        <li><strong>التحليل واستشراف المستقبل (Analysis & Visualization):</strong> مساعدة المديرين في رؤية المشكلات المعقدة وتحديد الفرص المستقبلية.</li>
    </ul>

    <div class="callout tip">
        <div class="callout-title">لماذا تحتاج المنظمات الحديثة إلى نظم المعلومات؟</div>
        تحتاج المنظمات إلى نظم المعلومات لجمع وتنظيم البيانات المتدفقة، تحويلها إلى معلومات ذات قيمة، تعزيز الكفاءة والإنتاجية، تحسين التواصل الإداري، تسريع إنجاز الخدمات للعملاء، وتخفيض التكاليف التشغيلية الإجمالية.
    </div>

    <h3>1.2 الفرق الجوهري بين البيانات والمعلومات (Data vs. Information)</h3>
    <table>
        <tr>
            <th style="width: 25%;">وجه المقارنة</th>
            <th style="width: 37%;">البيانات (Data)</th>
            <th style="width: 38%;">المعلومات (Information)</th>
        </tr>
        <tr>
            <td><strong>المفهوم والتعريف</strong></td>
            <td>حقائق وأرقام أولية خام لم تتم معالجتها أو تفسيرها وتفتقر إلى المعنى والسياق.</td>
            <td>بيانات جرت معالجتها ووضعها في سياق تنظيمي محدد يمنحها معنى وقيمة عملية واضحة.</td>
        </tr>
        <tr>
            <td><strong>الحالة في النظام</strong></td>
            <td>المدخلات الأساسية (Inputs).</td>
            <td>المخرجات النهائية ذات القيمة (Outputs).</td>
        </tr>
        <tr>
            <td><strong>القيمة لاتخاذ القرار</strong></td>
            <td>شبه منعدمة بمفردها (لا يمكن لمدير بناء خطة استراتيجية على رقم مجرد).</td>
            <td>عالية جداً (تمثل الأساس المباشر لصناعة القرارات الرشيدة).</td>
        </tr>
        <tr>
            <td><strong>مثال توضيحي واقعي</strong></td>
            <td>الأرقام المجردة: <code>80، 75، 90، 65</code> (درجات طلاب منفصلة).</td>
            <td><code>متوسط درجات الدفعة = 77.5%</code> (نسبة النجاح العامة = 100%).</td>
        </tr>
    </table>

    <div class="code-box">
المعادلة الذهبية لنظم المعلومات: بيانات أولية (Data) + معالجة وسياق (Processing) = معلومات قابلة للتطبيق (Information)
    </div>

    <h3>1.3 المكونات الخمسة الأساسية لنظام المعلومات</h3>
    <p>يخطئ الكثيرون بحصر نظام المعلومات في أجهزة الكمبيوتر فقط؛ فنظام المعلومات هو <em>منظومة متكاملة</em> تتألف من 5 مكونات لا غنى عن أحدها:</p>
    <ol>
        <li><strong>المكونات المادية (Hardware):</strong> الأجهزة والمعدات الملموسة في النظام (الخوادم المركزية Servers، الحواسيب الشخصية، وسائط التخزين، محولات وموجهات الشبكة، أجهزة المسح وقراءة الباركود، وأجهزة الاستشعار Sensors).</li>
        <li><strong>البرمجيات (Software):</strong> التعليمات والأكواد البرمجية والتطبيقات التي تدير العتاد وتعالج البيانات (نظم التشغيل كـ Windows و Linux، أنظمة إدارة قواعد البيانات DBMS كـ Oracle و SQL Server، وتطبيقات تخطيط الموارد ERP وتطبيقات الهواتف والويب).</li>
        <li><strong>البيانات (Data):</strong> المادة الخام التي يعالجها النظام ويحفظها كأصل معرفي (مثل: أرقام الطلاب الجامعية، الأسماء، الدرجات الأكاديمية، سجلات المرضى، الفواتير، وبيانات العملاء).</li>
        <li><strong>العنصر البشري (People):</strong> الأفراد الذين يديرون النظام ويستفيدون منه، وهم الركيزة الأهم (المستخدمون النهائيون End Users، محللو النظم Systems Analysts، مديرو قواعد البيانات DBAs، المطورون، ومسؤولو تقنية المعلومات والمديرون التنفيذيون).</li>
        <li><strong>الإجراءات والعمليات (Procedures & Processes):</strong> القواعد والسياسات وسلاسل الخطوات المنظمة التي تحدد كيفية تنفيذ الأنشطة داخل النظام والربط بين العنصر البشري والتقنية (مثال دورة التسجيل الجامعي: <em>تسجيل الدخول ← اختيار المقررات ← التحقق الآلي من المتطلبات ← اعتماد الدفع ← تأكيد التسجيل</em>).</li>
    </ol>

    <div class="callout warning">
        <div class="callout-title">قاعدة أكاديمية بالغة الأهمية</div>
        التقنية المتطورة والبرمجيات الغالية بمفردها لا تضمن النجاح؛ فإذا افتقرت المؤسسة إلى <strong>كوادر بشرية مؤهلة (People)</strong> و<strong>إجراءات عمل محكمة (Procedures)</strong>، فإن نظام المعلومات مصيره الفشل المحتوم.
    </div>

    <h3>1.4 كيف يعمل نظام المعلومات؟ والعمليات الخمس الرئيسية</h3>
    <div class="code-box">
[المدخلات: التقاط البيانات] ───► [المعالجة: التحويل والحساب] ───► [المخرجات: نشر المعلومات]
                                      ▲                                        │
                                      │────────── [التغذية الراجعة / Feedback] ─┘
    </div>
    <p><strong>العمليات التشغيلية الخمس التي يقوم بها نظام المعلومات:</strong></p>
    <ul>
        <li><strong>1. التقاط البيانات (Data Capture):</strong> جمع البيانات وتسجيلها لحظة حدوثها من مصادرها (أجهزة نقاط البيع، الاستمارات الإلكترونية، القارئات الذكية).</li>
        <li><strong>2. معالجة البيانات (Data Processing):</strong> إجراء العمليات الحسابية والمنطقية وتصنيف وفرز البيانات الخام لتحويلها لمخرجات مفيدة.</li>
        <li><strong>3. تخزين البيانات (Data Storage):</strong> حفظ السجلات بأمان في قواعد بيانات مركزية أو سحابية لضمان سلامتها واسترجاعها المستقبلي.</li>
        <li><strong>4. استرجاع البيانات (Data Retrieval):</strong> البحث والوصول السريع للسجلات المخزنة عند الحاجة (عبر استعلامات قواعد البيانات).</li>
        <li><strong>5. نشر وتوزيع المعلومات (Data Dissemination):</strong> إيصال التقارير واللوحات الإحصائية والتنبيهات للمستفيدين وصناع القرار.</li>
        <li><strong>التغذية الراجعة (Feedback):</strong> إعادة توجيه جزء من المخرجات لتقييم المدخلات ومراحل المعالجة وتصحيح أي أخطاء أو انحرافات أولاً بأول.</li>
    </ul>

    <h3>1.5 المقارنة الفاصلة: علوم الحاسب مقابل تكنولوجيا المعلومات مقابل نظم المعلومات</h3>
    <table>
        <tr>
            <th style="width: 20%;">التخصص</th>
            <th style="width: 40%;">محور الاهتمام والتركيز</th>
            <th style="width: 40%;">النطاق والمخرجات النمطية</th>
        </tr>
        <tr>
            <td><strong>علوم الحاسب<br>(Computer Science - CS)</strong></td>
            <td>الأسس النظرية للحوسبة، تصميم الخوارزميات، هياكل البيانات، هندسة البرمجيات المعقدة، والأنظمة الحسابية.</td>
            <td>ابتكار خوارزميات جديدة، بناء مترجمات اللغات (Compilers)، تطوير محركات نظم التشغيل والذكاء الاصطناعي العميق.</td>
        </tr>
        <tr>
            <td><strong>تكنولوجيا المعلومات<br>(Information Technology - IT)</strong></td>
            <td>التركيز التطبيقي على تثبيت، تهيئة، تأمين، صيانة، وإدارة البنية التحتية التكنولوجية والشبكات.</td>
            <td>بناء وإدارة الشبكات (LAN/WAN)، تثبيت الخوادم، تكوين الجدران النارية، تقديم الدعم الفني وحل مشاكل العتاد.</td>
        </tr>
        <tr>
            <td><strong>نظم المعلومات<br>(Information Systems - IS)</strong></td>
            <td>المواءمة الاستراتيجية بين التكنولوجيا والأعمال؛ استغلال التقنية والبيانات والإجراءات البشرية لتحقيق أهداف المؤسسات.</td>
            <td>تطبيق أنظمة تخطيط الموارد (ERP)، تطوير نظم دعم القرار (DSS)، إعادة هندسة العمليات، وصناعة الميزة التنافسية.</td>
        </tr>
    </table>

    <h3>1.6 نظم المعلومات والتقنيات الناشئة الحديثة</h3>
    <p>لم تعد نظم المعلومات مجرد برامج محاسبية تقليدية، بل أصبحت مدمجة بأحدث التقنيات الثورية:</p>
    <ul>
        <li><strong>الذكاء الاصطناعي وتعلم الآلة (AI & ML):</strong> تمكين الأنظمة من التنبؤ الذكي، اكتشاف محاولات الاحتيال آلياً، وتقديم التوصيات المخصصة للعملاء.</li>
        <li><strong>الحوسبة السحابية (Cloud Computing):</strong> توفير بنية تحتية وبرمجيات مرنة عبر الإنترنت قابلة للتوسع الفوري مع تخفيض تكاليف الخوادم المحلية.</li>
        <li><strong>تحليلات البيانات الضخمة (Big Data Analytics):</strong> تحليل ملايين السجلات غير المنظمة لحظياً لاكتشاف أنماط وسلوكيات السوق الخفية.</li>
        <li><strong>إنترنت الأشياء (IoT):</strong> ربط الأجهزة والمعدات الفيزيائية والحساسات بالنظام لجمع البيانات اللحظية مباشرة دون تدخل بشري.</li>
        <li><strong>سلاسل الكتل (Blockchain):</strong> توفير سجلات مشفرة وموزعة غير قابلة للتلاعب لضمان الشفافية في سلاسل الإمداد والخدمات المالية.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. الفصل الثاني: نظم المعلومات في المنظمات (IS in Organizations)</h2>

    <h3>2.1 مفهوم المنظمة ومواردها الاستراتيجية الخمسة</h3>
    <p><strong>المنظمة (Organization):</strong> كيان وهيكل اجتماعي منظم يضم مجموعة من الأفراد يعملون بتنسيق وتكامل مشترك لتحقيق أهداف وغايات محددة (مثل: الجامعات، البنوك، المستشفيات، والمصانع).</p>
    <p>تعتمد أي منظمة على حشد واستثمار 5 موارد رئيسية:</p>
    <ol>
        <li><strong>الموارد البشرية (Human Resources):</strong> رأس المال البشري من موظفين وفنيين ومديرين وكفاءات متخصصة.</li>
        <li><strong>الموارد المالية (Financial Resources):</strong> رؤوس الأموال، السيولة النقدية، الميزانيات التشغيلية، والاعتمادات الاستثمارية.</li>
        <li><strong>الموارد المادية (Physical Resources):</strong> الأصول الملموسة كالمباني، والمصانع، والآلات والمعدات، ومخزون المواد الخام.</li>
        <li><strong>الموارد المعلوماتية والمعرفية (Information Resources):</strong> قواعد البيانات، الدراسات السوقية، براءات الاختراع، والخبرات التراكمية للمؤسسة.</li>
        <li><strong>الموارد التكنولوجية (Technological Resources):</strong> الحواسيب، شبكات الاتصال، البرمجيات المتخصصة، والأنظمة السحابية.</li>
    </ol>

    <h3>2.2 المجالات الوظيفية التقليدية في المنظمات ودور نظم المعلومات فيها</h3>
    <table>
        <tr>
            <th style="width: 25%;">المجال الوظيفي</th>
            <th style="width: 45%;">المسؤولية التنظيمية الأساسية</th>
            <th style="width: 30%;">دور نظام المعلومات الداعم</th>
        </tr>
        <tr>
            <td><strong>التسويق والمبيعات<br>(Marketing & Sales)</strong></td>
            <td>الترويج للمنتجات والخدمات، بحوث السوق، تسعير السلع، إدارة العلاقات مع العملاء، وتحقيق المبيعات.</td>
            <td>نظم إدارة علاقات العملاء (CRM)، تتبع الحملات الإعلانية، وتحليل تفضيلات المستهلكين.</td>
        </tr>
        <tr>
            <td><strong>المحاسبة<br>(Accounting)</strong></td>
            <td>تسجيل وتوثيق المعاملات المالية التاريخية، إدارة الدفاتر المحاسبية، إصدار الفواتير، ومتابعة الالتزامات الضريبية.</td>
            <td>أنظمة الأستاذ العام (General Ledger)، برامج الفوترة الإلكترونية، وإعداد القوائم المالية الرسمية.</td>
        </tr>
        <tr>
            <td><strong>التمويل<br>(Finance)</strong></td>
            <td>التخطيط المالي المستقبلي، إدارة الاستثمارات النقدية، تقييم الجدوى الاقتصادية، وتدبير القروض وإدارة السيولة.</td>
            <td>نماذج التحليل المالي، أنظمة إدارة المحافظ الاستثمارية، والتنبؤ بالتدفقات النقدية.</td>
        </tr>
        <tr>
            <td><strong>الموارد البشرية<br>(Human Resources - HR)</strong></td>
            <td>استقطاب وتوظيف الكفاءات، تنظيم برامج التدريب والتطوير، تقييم الأداء، وحساب الرواتب والبدلات والمكافآت.</td>
            <td>نظم معلومات الموارد البشرية (HRIS)، بوابات الخدمة الذاتية للموظفين، وأنظمة الحضور والانصراف.</td>
        </tr>
        <tr>
            <td><strong>الإنتاج والعمليات<br>(Production & Operations)</strong></td>
            <td>تحويل المواد الخام لمنتجات نهائية، جدولة خطوط الإنتاج، إدارة المخازن اللوجستية، وضمان معايير الجودة.</td>
            <td>نظم إدارة سلاسل الإمداد (SCM)، تخطيط متطلبات المواد (MRP)، والتحكم الآلي في خطوط التصنيع.</td>
        </tr>
        <tr>
            <td><strong>الإدارة<br>(Management)</strong></td>
            <td>التخطيط الاستراتيجي، قيادة المنظمة وتوجيه الموارد، التنسيق بين الإدارات، ومراقبة مؤشرات الأداء العام.</td>
            <td>لوحات التحكم التنفيذية (Dashboards)، ونظم المتابعة وتقييم المخاطر المؤسسية.</td>
        </tr>
    </table>

    <h3>2.3 المستويات الإدارية الثلاثة واحتياجاتها من المعلومات</h3>
    <table>
        <tr>
            <th>وجه المقارنة</th>
            <th>الإدارة التشغيلية (Operational)</th>
            <th>الإدارة الوسطى (Middle Management)</th>
            <th>الإدارة العليا (Top Management)</th>
        </tr>
        <tr>
            <td><strong>المسؤولون والوظائف</strong></td>
            <td>مشرفو الورديات، موظفو الاستقبال، المحاسبون، أمناء المخازن.</td>
            <td>مديرو الإدارات والأقسام، مديرو الفروع والمصانع.</td>
            <td>الرئيس التنفيذي (CEO)، مجلس الإدارة، رئيس الجامعة.</td>
        </tr>
        <tr>
            <td><strong>نطاق الاهتمام والمدى الزمني</strong></td>
            <td>المهام الروتينية اليومية؛ قصير الأجل (لحظي، يومي، أسبوعي).</td>
            <td>الخطط التكتيكية والرقابة؛ متوسط الأجل (شهري، ربع سنوي).</td>
            <td>الرؤية والاستراتيجية العامة؛ طويل الأجل (1 إلى 5+ سنوات).</td>
        </tr>
        <tr>
            <td><strong>طبيعة القرارات</strong></td>
            <td><strong>مهيكلة (Structured):</strong> قرارات روتينية مكررة محكومة بقواعد ولوائح ثابتة محددة مسبقاً.</td>
            <td><strong>شبه مهيكلة (Semi-Structured):</strong> قرارات تجمع بين القواعد النظامية والتقدير الإداري الشخصي.</td>
            <td><strong>غير مهيكلة (Unstructured):</strong> قرارات استراتيجية معقدة وغير مسبوقة تتسم بالغموض وارتفاع المخاطرة.</td>
        </tr>
        <tr>
            <td><strong>طبيعة المعلومات المطلوبة</strong></td>
            <td>معلومات <strong>تفصيلية ودقيقة جداً</strong>، لحظية، وتتعلق بالعمل الداخلي الروتيني.</td>
            <td>معلومات <strong>ملخصة ودورية</strong> (تقارير شهرية ومقارنات بين الأداء الفعلي والميزانية).</td>
            <td>معلومات <strong>ملخصة للغاية وشاملة</strong>، تجمع بين المؤشرات الداخلية ومسح البيئة والأسواق الخارجية.</td>
        </tr>
        <tr>
            <td><strong>النظام الداعم الرئيسي</strong></td>
            <td><strong>TPS</strong> (نظم معالجة المعاملات).</td>
            <td><strong>MIS</strong> (نظم المعلومات الإدارية) و <strong>DSS</strong>.</td>
            <td><strong>EIS / ESS</strong> (نظم دعم الإدارة التنفيذية).</td>
        </tr>
    </table>

    <h3>2.4 خريطة نظم المعلومات وفق المستويات الإدارية</h3>
    <ul>
        <li><strong>1. نظم معالجة المعاملات (Transaction Processing Systems - TPS):</strong>
            <ul>
                <li>تخدم <strong>المستوى التشغيلي</strong>، وتعد القاعدة الأساسية لجميع نظم المؤسسة بتسجيل المعاملات اليومية الروتينية.</li>
                <li>تتميز بالسرعة الفائقة، حجم العمليات الضخم، الدقة العالية، والحفاظ التام على سلامة البيانات.</li>
                <li>أمثلة: أجهزة تسجيل الخروج في السوبرماركت (POS)، نظام سحب الأموال من الصراف الآلي (ATM)، حجز تذاكر الطيران، وتسجيل غياب الطلاب اليومي.</li>
            </ul>
        </li>
        <li><strong>2. نظم المعلومات الإدارية (Management Information Systems - MIS):</strong>
            <ul>
                <li>تخدم <strong>الإدارة الوسطى</strong>، حيث تسحب البيانات من نظام TPS لإنتاج تقارير دورية قياسية للمتابعة التكتيكية.</li>
                <li>تركز على التقارير الموجزة والتقارير الاستثنائية (Exception Reports) التي تبرز الانحرافات عن المعايير المستهدفة.</li>
                <li>أمثلة: تقرير مبيعات الفروع الشهري مقارنة بالمستهدف، تقرير مقارنة تكاليف القسم الفعلي مع الميزانية التقديرية.</li>
            </ul>
        </li>
        <li><strong>3. نظم دعم القرار (Decision Support Systems - DSS):</strong>
            <ul>
                <li>تخدم <strong>الإدارة وصناع القرار</strong> في حل المشكلات شبه المهيكلة والمعقدة.</li>
                <li>تعتمد على النماذج الرياضية والإحصائية والمحاكاة لتقديم تحليلات معمقة وسيناريوهات افتراضية (مثل: <em>تحليل ماذا-لو What-If Analysis</em>).</li>
                <li>أمثلة: تقييم الأثر المالي لرفع أسعار المنتجات بنسبة 5%، تحديد الموقع الأمثل لافتتاح مصنع جديد في ضوء تكاليف الشحن.</li>
            </ul>
        </li>
        <li><strong>4. نظم دعم الإدارة التنفيذية (Executive Information / Support Systems - EIS / ESS):</strong>
            <ul>
                <li>تخدم <strong>الإدارة العليا (التنفيذيين)</strong> وتزودهم برؤية بانورامية شاملة للمؤسسة والبيئة المحيطة.</li>
                <li>تتميز بواجهات بيانية ولوحات تحكم تفاعلية متطورة (Dashboards) مع خاصية التعمق والتحليل الدقيق <strong>(Drill-Down Capability)</strong> لنزول المدير بنقرة واحدة من المؤشر الإجمالي لمصدر الخلل بالتفصيل.</li>
                <li>أمثلة: لوحة التحكم الرقمية لرئيس الجامعة التي تعرض إجمالي نسب الاحتفاظ بالطلاب، والوضع المالي العام، ومعدلات الاعتماد الأكاديمي.</li>
            </ul>
        </li>
    </ul>

    <div class="callout tip">
        <div class="callout-title">التكامل والتكاملية بين النظم</div>
        لا تعمل نظم المعلومات في معزل عن بعضها؛ فنظام TPS هو الشريان الذي يغذي قواعد بيانات MIS و DSS، وهما بدورهما يمدان نظام الإدارة العليا EIS بالمعلومات المركزة. النظم تتكامل لخدمة أهداف المنظمة ككل.
    </div>

    <h3>2.5 العمليات التجارية والنظم العابرة للوظائف (Cross-Functional Systems)</h3>
    <p><strong>العملية التجارية (Business Process):</strong> سلسلة من الأنشطة والمهام المترابطة منطقياً التي تبدأ بمدخلات وتمر بمراحل متتابعة لتنتج مخرجات محددة تقدم قيمة مضافة للعميل أو المنظمة.</p>
    <p><strong>الأنواع الثلاثة للعمليات التجارية:</strong></p>
    <ul>
        <li><strong>العمليات الأساسية (Core Processes):</strong> الأنشطة المحورية التي ترتبط مباشرة بإنتاج وتقديم القيمة للعميل الخارجي (مثل: تصنيع السلع، تلبية وتسليم طلبات الشراء، تقديم الاستشارات الطبية).</li>
        <li><strong>العمليات الداعمة (Support Processes):</strong> الأنشطة المساندة التي تمكّن العمليات الأساسية من الاستمرار دون أن يراها العميل مباشرة (مثل: الدعم الفني، التوظيف، المشتريات والمحاسبة).</li>
        <li><strong>العمليات الإدارية (Management Processes):</strong> الأنشطة الخاصة بالتخطيط والرقابة والحوكمة الإستراتيجية (مثل: التخطيط الاستراتيجي السنوي، تدقيق الجودة والامتثال القانوني).</li>
    </ul>

    <h4>أهمية النظم العابرة للوظائف وكسر "الجزر المنعزلة" (Information Silos):</h4>
    <p>في الهياكل القديمة، كانت كل إدارة تعمل بمفردها كجزيرة منعزلة؛ فالمبيعات لا تعلم رصيد المخزن، والمخزن لا يعلم موقف العميل المالي. جاءت <strong>النظم العابرة للوظائف (كأنظمة ERP)</strong> لتربط الأقسام معاً في مسار موحد:</p>
    <div class="code-box">
استلام طلب العميل (المبيعات)
       │
       ▼
التحقق التلقائي من المخزون (المستودعات)
       │
       ▼
التحقق من الرصيد والائتمان المالي (المالية والحسابات)
       │
       ▼
تجهيز السلع وشحنها للعميل (العمليات والشحن)
       │
       ▼
إصدار الفاتورة وتأكيد الدفع (المحاسبة)
    </div>

    <h3>2.6 تحقيق الميزة التنافسية عبر نظم المعلومات (Competitive Advantage)</h3>
    <p><strong>الميزة التنافسية:</strong> هي التفوق والامتياز الذي تمتلكه المنظمة ويمكنها من التفوق على منافسيها في السوق وتحقيق أرباح أو حصة سوقية أعلى أو تقديم قيمة لا يستطيع المنافسون مجاراتها.</p>
    <p><strong>كيف تُمكِّن نظم المعلومات المنظمات من تحقيق الميزة التنافسية؟</strong></p>
    <ul>
        <li><strong>قيادة التكلفة (Cost Leadership):</strong> أتمتة العمليات اليومية وتقليل الأخطاء البشرية، مما يخفض تكاليف الإنتاج والتشغيل مقارنة بالمنافسين.</li>
        <li><strong>تمييز المنتجات والخدمات (Differentiation):</strong> ابتكار خدمات رقمية نوعية تفوق توقعات العملاء (مثل: التتبع الفوري للشحنات، التوصيات الذكية).</li>
        <li><strong>سرعة الاستجابة لمتطلبات العملاء:</strong> تقليص زمن الاستجابة والشكاوى وتقديم دعم فوري على مدار الساعة.</li>
        <li><strong>دعم الابتكار والمرونة المؤسسية:</strong> توفير رؤى فورية تمكّن المنظمة من التكيف السريع مع تقلبات السوق والتوسع في مجالات جديدة.</li>
    </ul>

    <h3>2.7 دراسة الحالة التطبيقية: منظومة الجامعة الأكاديمية والإدارية</h3>
    <table>
        <tr>
            <th>الطرف المستفيد في الجامعة</th>
            <th>المستوى الإداري</th>
            <th>الاحتياجات المعلوماتية ونوع النظام الداعم</th>
        </tr>
        <tr>
            <td><strong>موظف شؤون الطلاب</strong></td>
            <td>تشغيلي (Operational)</td>
            <td>التحقق من اجتياز الطالب للمتطلبات السابقة، توافر المقاعد بالشعبة، وتسجيل المواد لحظياً (عبر TPS).</td>
        </tr>
        <tr>
            <td><strong>رئيس القسم الأكاديمي</strong></td>
            <td>إدارة وسطى (Middle)</td>
            <td>تقرير بعدد الطلاب المسجلين بالقسم، مقارنة نسب النجاح والرسوب، وتوزيع العبء التدريسي لأعضاء هيئة التدريس (عبر MIS).</td>
        </tr>
        <tr>
            <td><strong>المدير المالي بالجامعة</strong></td>
            <td>إدارة وسطى (Middle)</td>
            <td>تقرير المصروفات مقابل ميزانية الكليات، ومتابعة تحصيل الرسوم الدراسية وأوجه الصرف المعملية (عبر MIS/DSS).</td>
        </tr>
        <tr>
            <td><strong>رئيس الجامعة (University President)</strong></td>
            <td>إدارة عليا (Top Management)</td>
            <td>معدلات استبقاء الطلاب متعددة السنوات، مؤشرات التصنيف والاعتماد الأكاديمي الدولي، ودراسة الجدوى المالية لافتتاح كليات جديدة (عبر EIS/ESS).</td>
        </tr>
    </table>
</div>

</body>
</html>
"""

# Write HTML files
os.makedirs("summaries", exist_ok=True)
with open("summaries/ISApp_Summary_EN.html", "w", encoding="utf-8") as f:
    f.write(html_isapp_en)
with open("summaries/ISApp_Summary_AR.html", "w", encoding="utf-8") as f:
    f.write(html_isapp_ar)

print("Saved HTML summaries for IS App successfully!")

# Compile to PDF using Chrome Headless
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
for lang, fn_html, fn_pdf in [
    ('EN', 'summaries/ISApp_Summary_EN.html', 'summaries/ISApp_Summary_EN.pdf'),
    ('AR', 'summaries/ISApp_Summary_AR.html', 'summaries/ISApp_Summary_AR.pdf')
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
    size = os.path.getsize(abs_pdf) if os.path.exists(abs_pdf) else 0
    print(f"Compiled {fn_pdf} - Exists: {os.path.exists(abs_pdf)}, Size: {size} bytes")

# Copy to web/downloads
os.makedirs("web/downloads", exist_ok=True)
if os.path.exists("summaries/ISApp_Summary_EN.pdf"):
    shutil.copy("summaries/ISApp_Summary_EN.pdf", "web/downloads/ISApp_Summary_EN.pdf")
if os.path.exists("summaries/ISApp_Summary_AR.pdf"):
    shutil.copy("summaries/ISApp_Summary_AR.pdf", "web/downloads/ISApp_Summary_AR.pdf")

print("Copied PDFs to web/downloads successfully!")
