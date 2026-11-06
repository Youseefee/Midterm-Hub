import os, subprocess
from summary_design_engine import get_css

# Business Analytics - Amber / Gold Theme (#b45309, #d97706, #f59e0b)
theme_color = "#b45309"
grad_start = "#92400e"
grad_end = "#d97706"

css_en = get_css(theme_color, grad_start, grad_end, is_arabic=False)
css_ar = get_css(theme_color, grad_start, grad_end, is_arabic=True)

html_ba_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Business Analytics (BA) - Executive Midterm Summary</title>
<style>{css_en}</style>
</head>
<body>

<div class="hero-banner">
    <h1>Business Analytics & Data Lifecycle</h1>
    <div class="subtitle">Executive Midterm Study Guide & Comprehensive Knowledge Architecture</div>
    <div class="hero-badges">
        <span class="hero-badge">Course: Business Analytics</span>
        <span class="hero-badge">Instructor: Dr. Rehab Mahmoud</span>
        <span class="hero-badge">Faculty of Computers & AI</span>
        <span class="hero-badge">Fayoum University</span>
        <span class="hero-badge">Scope: Module 1, Chapter 2, Chapter 3</span>
    </div>
</div>

<div class="section-block">
    <h2><span class="sec-pill">01</span> Introduction to Data Analytics (Module 1)</h2>
    <p>Data Analytics has become the core competitive differentiator for modern enterprises. Organizations no longer compete merely on capital or physical assets; they compete on their ability to convert raw operational data into actionable strategic insights.</p>

    <div class="callout tip">
        <div class="callout-title">📌 Core Definition: Data vs. Data Analytics</div>
        <strong>Data:</strong> Raw facts, observations, measurements, or records (e.g. sales transactions, web clicks, sensor readings). Data has zero intrinsic value until it is organized.<br>
        <strong>Data Analytics:</strong> A systematic process of examining datasets to discover patterns, trends, correlations, and actionable insights to support better questions, decisions, and outcomes.
    </div>

    <h3>1.1 The Value Transformation Chain: From Data to Decision</h3>
    <table>
        <tr>
            <th>Stage</th>
            <th>Nature & State</th>
            <th>Real-World Example</th>
        </tr>
        <tr>
            <td><strong>1. DATA</strong></td>
            <td>Raw, unorganized facts and records.</td>
            <td>10,000 recorded customer retail transactions.</td>
        </tr>
        <tr>
            <td><strong>2. INFORMATION</strong></td>
            <td>Organized, structured, and cleaned data.</td>
            <td>Monthly sales summarized by age group and region.</td>
        </tr>
        <tr>
            <td><strong>3. INSIGHT</strong></td>
            <td>Meaning, patterns, and underlying relationships discovered.</td>
            <td>Customers aged 25-34 in Region A generate 45% of total revenue.</td>
        </tr>
        <tr>
            <td><strong>4. DECISION</strong></td>
            <td>Actionable business strategy executed.</td>
            <td>Reallocate 60% of digital marketing budget to targeted mobile ads for Region A young adults.</td>
        </tr>
    </table>

    <h3>1.2 Data Analysis vs. Data Analytics: Key Distinctions</h3>
    <table>
        <tr>
            <th>Attribute</th>
            <th>Data Analysis</th>
            <th>Data Analytics</th>
        </tr>
        <tr>
            <td><strong>Primary Focus</strong></td>
            <td>Examining historical data to answer specific past questions.</td>
            <td>Broader discipline covering data pipelines, statistics, modeling, prediction, and strategic action.</td>
        </tr>
        <tr>
            <td><strong>Guiding Questions</strong></td>
            <td>"What happened?" and "Why did it happen?"</td>
            <td>"What happened? Why? What may happen next? What action should we take?"</td>
        </tr>
        <tr>
            <td><strong>Organizational Scope</strong></td>
            <td>A specific analytical activity or task.</td>
            <td>An entire capability, methodology, architecture, and professional field.</td>
        </tr>
    </table>

    <h3>1.3 The Four Major Types of Analytics (High-Yield Exam Focus)</h3>
    <table>
        <tr>
            <th>Type</th>
            <th>Guiding Question</th>
            <th>Core Characteristics & Outputs</th>
            <th>Business Scenario Example</th>
        </tr>
        <tr>
            <td><strong>1. Descriptive</strong></td>
            <td><em>"What happened?"</em></td>
            <td>Summarizes historical and current data. KPI metrics, reporting dashboards, sales trends, averages.</td>
            <td>Monthly revenue decreased by 12% in the footwear category.</td>
        </tr>
        <tr>
            <td><strong>2. Diagnostic</strong></td>
            <td><em>"Why did it happen?"</em></td>
            <td>Investigates root causes and relationships. Uses drill-down, segmentation, cohort comparison, and correlation.</td>
            <td>The 12% drop was isolated to supplier shipping delays that caused stockouts in Store #4.</td>
        </tr>
        <tr>
            <td><strong>3. Predictive</strong></td>
            <td><em>"What may happen?"</em></td>
            <td>Uses historical patterns, regression, and machine learning to forecast future probabilities. <em>Probabilistic, not guaranteed.</em></td>
            <td>If current churn rates persist, the subscription base will decline by 8% next quarter.</td>
        </tr>
        <tr>
            <td><strong>4. Prescriptive</strong></td>
            <td><em>"What should we do?"</em></td>
            <td>Evaluates potential choices using optimization, simulation, and decision rules to recommend the best course of action.</td>
            <td>Offer an automated 15% renewal discount to high-churn-risk subscribers with > 2 support calls.</td>
        </tr>
    </table>

    <div class="callout trap">
        <div class="callout-title">⚠️ Exam Trap: Business Questions vs. Analytical Questions</div>
        Business problems are phrased in commercial terms (e.g. <em>"Why are profits falling?"</em>). An analyst must never search for answers until this is decomposed into quantifiable <strong>Analytical Questions</strong>: <em>Which products experienced margin compression? Did freight costs increase? What was the price elasticity?</em> Good analytics starts with clear questions, not with software tools!
    </div>

    <h3>1.4 Analytics Career Paths & Ecosystem Tools</h3>
    <ul>
        <li><strong>Data Analyst:</strong> Queries databases via SQL, manipulates data in Excel, builds reporting dashboards, communicates operational trends.</li>
        <li><strong>BI Analyst:</strong> Focuses on corporate Business Intelligence, semantic layers, dimensional modeling, and interactive dashboards (Power BI / Tableau).</li>
        <li><strong>Product Analyst:</strong> Analyzes digital user experience, funnel conversion, user engagement, and A/B testing experiment telemetry.</li>
        <li><strong>Data Scientist:</strong> Applies advanced mathematical statistics, machine learning algorithms, deep predictive modeling, and custom Python/R scripts.</li>
        <li><strong>Core Competency Matrix:</strong> Technical (Excel, SQL, Python), Analytical (critical thinking, pattern recognition), Business Acumen (understanding KPIs and profit drivers), Data Literacy (critiquing data bias and quality limitations), and Communication.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section-block">
    <h2><span class="sec-pill">02</span> Decision Models & 6-Step Problem Solving (Chapter 2)</h2>

    <h3>2.1 What is a Model? The Three Forms of Models</h3>
    <p>A <strong>Model</strong> is an abstraction or representation of a real-world system, idea, or object. It strips away irrelevant real-world noise to focus on critical relationships.</p>
    <table>
        <tr>
            <th>Form</th>
            <th>Description & Medium</th>
            <th>Example</th>
        </tr>
        <tr>
            <td><strong>1. Written / Verbal</strong></td>
            <td>Expressed in natural language prose or spoken sentences.</td>
            <td>"Sales volume increases with advertising expenditure, but at a decreasing rate."</td>
        </tr>
        <tr>
            <td><strong>2. Visual / Graphical</strong></td>
            <td>Visual charts, flowcharts, plots, and network diagrams.</td>
            <td>A scatter plot curve plotting Advertising on X and Sales on Y.</td>
        </tr>
        <tr>
            <td><strong>3. Mathematical</strong></td>
            <td>Formal equations, variables, and mathematical relationships.</td>
            <td>$S = 20,000 &times; (1 - e^(-0.05 * A)) - 50 &times; P$</td>
        </tr>
    </table>

    <h3>2.2 Decision Model Architecture: Inputs to Outputs</h3>
    <p>A Decision Model processes three classes of inputs to calculate performance outputs:</p>
    <ul>
        <li><strong>Data:</strong> Known, constant numerical facts (e.g. historical sales tax rates, current inventory count).</li>
        <li><strong>Uncontrollable Variables:</strong> External economic and environmental factors dictated by the market or nature that management cannot directly control (e.g. inflation, competitor pricing, weather).</li>
        <li><strong>Decision Variables:</strong> Controllable variables that management can directly choose and manipulate (e.g. product retail price, production quantity, marketing budget).</li>
        <li><strong>Outputs:</strong> Performance metrics and consequences calculated by the model (e.g. Total Revenue, Net Profit, Return on Investment).</li>
    </ul>

    <h3>2.3 Descriptive Decision Models: Total Cost & Break-Even Analysis</h3>
    <div class="card">
        <div class="callout-title">📐 The Break-Even Decision Model</div>
        <p>In cost accounting, Total Cost is composed of Fixed Overhead Costs ($F$) and Variable Unit Costs ($V$):</p>
        <p style="font-family: Consolas; font-size: 13px; font-weight: 700; color: #b45309;">Total Cost: TC = F + V &times; Q</p>
        <p>Total Revenue ($TR$) generated by selling quantity $Q$ at unit price $P$ is:</p>
        <p style="font-family: Consolas; font-size: 13px; font-weight: 700; color: #b45309;">Total Revenue: TR = P &times; Q</p>
        <p>The <strong>Break-Even Point ($Q_{{BE}}$)</strong> occurs where Total Revenue equals Total Cost ($TR = TC$), resulting in zero profit and zero loss:</p>
        <div class="code-box">
P * Q = F + V * Q
Q * (P - V) = F
Q_BE = F / (P - V)

Where:
  (P - V) = Unit Contribution Margin (amount per unit contributing to covering fixed costs)
        </div>
        <p><strong>Worked Example:</strong> If $F = \$120,000$, Unit Variable Cost $V = \$30$, and Selling Price $P = \$70$:<br>
        Unit Contribution Margin = $\$70 - \$30 = \$40$.<br>
        Break-Even Quantity $Q_{{BE}} = \frac{{\$120,000}}{{\$40}} = 3,000\text{{ units}}$.</p>
    </div>

    <h3>2.4 Demand Prediction Models: Linear vs. Non-Linear</h3>
    <ul>
        <li><strong>Linear Demand Model:</strong> $D = a - b &times; P$<br>
        Assumes a constant absolute change in demand for every dollar change in price ($b$ is the slope).</li>
        <li><strong>Non-Linear Demand Model:</strong> $D = a &times; P^{{-b}}$<br>
        In this power formulation, the exponent $-b$ directly represents the <strong>constant Price Elasticity of Demand</strong> ($\% \Delta D / \% \Delta P$).</li>
    </ul>

    <h3>2.5 Prescriptive Decision Models: Deterministic vs. Stochastic</h3>
    <table>
        <tr>
            <th>Model Type</th>
            <th>Nature of Inputs</th>
            <th>Primary Methodologies</th>
        </tr>
        <tr>
            <td><strong>Deterministic Model</strong></td>
            <td>All inputs, parameters, and constraints are known with <strong>absolute certainty</strong>.</td>
            <td>Linear Programming (LP), Integer Programming, Break-Even Models.</td>
        </tr>
        <tr>
            <td><strong>Stochastic (Probabilistic) Model</strong></td>
            <td>One or more inputs involve <strong>randomness, risk, or probability distributions</strong>.</td>
            <td>Monte Carlo Simulation, Decision Trees, Queuing Theory, Forecasting models.</td>
        </tr>
    </table>

    <h3>2.6 The 6-Step Problem Solving & Decision Making Framework</h3>
    <ol>
        <li><strong>1. Recognizing the Problem:</strong> Management senses that a gap exists between current actual performance and desired goals (e.g. sales are dropping, defects are rising).</li>
        <li><strong>2. Defining the Problem:</strong> The most difficult step! Disentangling root causes from mere symptoms, clarifying organizational constraints, identifying decision makers, and agreeing on objectives.</li>
        <li><strong>3. Structuring the Problem:</strong> Formulating the formal model; identifying decision variables, uncontrollable inputs, constraints, boundary assumptions, and mathematical relationships.</li>
        <li><strong>4. Analyzing the Problem:</strong> Solving the model; executing optimization algorithms, computing formulas, running simulations, and generating candidate solutions.</li>
        <li><strong>5. Interpreting Results & Sensitivity Analysis:</strong> Understanding what the numerical outputs mean in business terms; running "what-if" sensitivity checks to test model robustness under parameter changes.</li>
        <li><strong>6. Implementing the Solution:</strong> Executing the selected decision in live operations; managing human organizational change, monitoring feedback, and establishing operational controls.</li>
    </ol>
</div>

<div class="page-break"></div>

<div class="section-block">
    <h2><span class="sec-pill">03</span> Data Analytics Lifecycle & Project Governance (Chapter 3)</h2>
    <p>Data science and analytics projects frequently fail not because of algorithm flaws, but because of poor project governance, lack of stakeholder alignment, or failure to frame problems rigorously. The <strong>Data Analytics Lifecycle</strong> provides a battle-tested, scientific 6-phase framework.</p>

    <h3>3.1 The 7 Key Roles in an Analytics Project Team</h3>
    <table>
        <tr>
            <th>Role</th>
            <th>Primary Mission</th>
            <th>Key Deliverables & Responsibilities</th>
        </tr>
        <tr>
            <td><strong>1. Project Sponsor</strong></td>
            <td>Executive ownership & funding.</td>
            <td>Champions the project, provides budget, defines business vision, signs off on business value and ROI.</td>
        </tr>
        <tr>
            <td><strong>2. Business User</strong></td>
            <td>Domain validation & end-use.</td>
            <td>Provides business domain knowledge, validates operational constraints, and utilizes deliverables in day-to-day work.</td>
        </tr>
        <tr>
            <td><strong>3. Project Manager</strong></td>
            <td>Tracking & milestone governance.</td>
            <td>Ensures project milestones are delivered on time, within budget, and tracks dependencies.</td>
        </tr>
        <tr>
            <td><strong>4. BI Analyst</strong></td>
            <td>Data & reporting context.</td>
            <td>Brings deep knowledge of existing reports, historical data warehouses, metric definitions, and legacy KPIs.</td>
        </tr>
        <tr>
            <td><strong>5. Database Admin (DBA)</strong></td>
            <td>Environment & security provisioning.</td>
            <td>Provisions database instances, grants secure permissions, optimizes heavy analytical extraction, protects production systems.</td>
        </tr>
        <tr>
            <td><strong>6. Data Engineer</strong></td>
            <td>Pipeline & data preparation.</td>
            <td>Builds data extraction pipelines (ETL/ELT), cleans raw data feeds, integrates data into the Analytic Sandbox.</td>
        </tr>
        <tr>
            <td><strong>7. Data Scientist</strong></td>
            <td>Advanced modeling & algorithmic design.</td>
            <td>Formulates mathematical models, engineers features, trains predictive algorithms, tests statistical validity.</td>
        </tr>
    </table>

    <h3>3.2 The 6 Phases of the Data Analytics Lifecycle in Depth</h3>
    
    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">Phase 1: Discovery</h3>
        <ul>
            <li><strong>Objective:</strong> Learn the business domain, assess data availability, survey hardware/software resources, and define project scope.</li>
            <li><strong>Key Activities:</strong> Interview stakeholders, establish <em>Initial Hypotheses (IH)</em>, frame the business challenge into an analytical problem, and formulate the formal <strong>Analytic Plan</strong>.</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">Phase 2: Data Preparation</h3>
        <ul>
            <li><strong>Objective:</strong> Collect, clean, inspect, and condition data for modeling.</li>
            <li><strong>The Analytic Sandbox:</strong> Provisioning a dedicated, high-performance workspace where analysts can explore and transform massive datasets without impacting production databases.</li>
            <li><strong>Key Activities:</strong> Extract, Transform, Load (ETL/ELT), treat missing data and outliers, execute Exploratory Data Analysis (EDA), verify data consistency and text encodings.</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">Phase 3: Model Planning</h3>
        <ul>
            <li><strong>Objective:</strong> Determine the methods, techniques, and workflow to follow.</li>
            <li><strong>Key Activities:</strong> Feature selection (identifying key explanatory variables), evaluating data distributions, and choosing candidate modeling families (e.g. regression vs classification vs clustering).</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">Phase 4: Model Building</h3>
        <ul>
            <li><strong>Objective:</strong> Develop and execute mathematical and machine learning models.</li>
            <li><strong>Key Activities:</strong> Partition data into distinct <strong>Training, Testing, and Validation sets</strong> to prevent overfitting; run algorithms; tune hyperparameters; evaluate model precision/recall.</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">Phase 5: Communicate Results</h3>
        <ul>
            <li><strong>Objective:</strong> Determine whether the project succeeded or failed against initial hypotheses.</li>
            <li><strong>Key Activities:</strong> Quantify commercial ROI and business value, identify key patterns and surprises, and present findings tailored to specific stakeholder audiences.</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">Phase 6: Operationalize</h3>
        <ul>
            <li><strong>Objective:</strong> Deploy the validated model into live production workflows.</li>
            <li><strong>Key Activities:</strong> Run a <strong>Pilot Project</strong> in a controlled production segment, deliver production code and API scoring pipelines, establish monitoring for data drift, and create user documentation.</li>
        </ul>
    </div>

    <h3>3.3 The 4 Core Deliverables for Diverse Stakeholders</h3>
    <table>
        <tr>
            <th>Deliverable</th>
            <th>Primary Audience</th>
            <th>Content & Tone</th>
        </tr>
        <tr>
            <td><strong>1. Executive Presentation</strong></td>
            <td>Project Sponsor & Senior Leaders</td>
            <td>High-level strategic briefing: business impact, ROI, key insights, and actionable recommendations. Zero low-level math code.</td>
        </tr>
        <tr>
            <td><strong>2. Operational Deck</strong></td>
            <td>Business Users & Operational Analysts</td>
            <td>Workflow impact: how the model integrates into daily tasks, operational metrics, interface guidelines.</td>
        </tr>
        <tr>
            <td><strong>3. Technical Document</strong></td>
            <td>Data Scientists & Peer Researchers</td>
            <td>Exhaustive mathematical documentation: algorithm specifications, training curves, validation metrics, data transformations.</td>
        </tr>
        <tr>
            <td><strong>4. Production Code & Runbooks</strong></td>
            <td>Data Engineers & DevOps / IT Ops</td>
            <td>Clean, commented, version-controlled scripts, ETL pipelines, API documentation, and monitoring alerts.</td>
        </tr>
    </table>

    <div class="callout tip">
        <div class="callout-title">💡 Golden Exam Takeaway: Lifecycle Iteration</div>
        The Data Analytics Lifecycle is <strong>inherently iterative, not purely linear</strong>. If Phase 5 shows the model failed to validate the initial hypothesis or achieve satisfactory accuracy, the team loops back to Phase 2 (Data Preparation for better features) or Phase 3 (Model Planning for different algorithms).
    </div>
</div>

</body>
</html>"""

html_ba_ar = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>تحليلات الأعمال (Business Analytics) - ملخص الميدتيرم التنفيذي</title>
<style>{css_ar}</style>
</head>
<body class="ar">

<div class="hero-banner">
    <h1>تحليلات الأعمال ودورة حياة البيانات (Business Analytics)</h1>
    <div class="subtitle">الملخص الدراسي الشامل والموسوعة المرجعية التنفيذية لامتحان الميدتيرم</div>
    <div class="hero-badges">
        <span class="hero-badge">المادة: تحليلات الأعمال (بيزنس)</span>
        <span class="hero-badge">أستاذ المادة: د. رحاب محمود</span>
        <span class="hero-badge">كلية الحاسبات والذكاء الاصطناعي</span>
        <span class="hero-badge">جامعة الفيوم</span>
        <span class="hero-badge">نطاق المنهج: Module 1, Chapter 2, Chapter 3</span>
    </div>
</div>

<div class="section-block">
    <h2><span class="sec-pill">01</span> مقدمة في تحليلات البيانات (Module 1)</h2>
    <p>أصبحت تحليلات البيانات (Data Analytics) هي المحرك الأساسي للميزة التنافسية في كبرى الشركات المعاصرة؛ فالشركات لم تعد تتنافس فقط بحجم رؤوس الأموال، بل بقدرتها على تحويل كميات البيانات التشغيلية الأولية إلى قرارات استراتيجية مدروسة.</p>

    <div class="callout tip">
        <div class="callout-title">📌 التعريف الجوهري: البيانات مقابل تحليلات البيانات</div>
        <strong>البيانات (Data):</strong> حقائق خام، مشاهدات، قياسات، أو سجلات منفردة مجردة من السياق (مثل: فواتير المبيعات، نقرات الموقع، قراءات الحساسات). لا قيمة لها بمفردها حتى يتم تنظيمها.<br>
        <strong>تحليلات البيانات (Data Analytics):</strong> عملية منهجية منظمة لفحص وتحليل مجموعات البيانات لاكتشاف الأنماط والاتجاهات والعلاقات واستخراج رؤى قابلة للتطبيق العملي تدعم اتخاذ قرارات أفضل.
    </div>

    <h3>1.1 مسار التحول التصاعدي: من البيانات إلى القرار الاستراتيجي</h3>
    <table>
        <tr>
            <th>المرحلة</th>
            <th>الحالة والطبيعة</th>
            <th>مثال واقعي تطبيقي</th>
        </tr>
        <tr>
            <td><strong>1. البيانات (DATA)</strong></td>
            <td>حقائق وسجلات خام غير منظمة.</td>
            <td>10,000 عملية بيع مسجلة في المتجر.</td>
        </tr>
        <tr>
            <td><strong>2. المعلومات (INFORMATION)</strong></td>
            <td>بيانات تم تنظيمها وترتيبها في جداول.</td>
            <td>إجمالي مبيعات الشهر مقسمة حسب الفئات العمرية والمناطق.</td>
        </tr>
        <tr>
            <td><strong>3. الرؤية والرؤى (INSIGHT)</strong></td>
            <td>معنى ونمط علاقة مستكشف في البيانات.</td>
            <td>اكتشاف أن العملاء بين 25 و 34 سنة في المنطقة (أ) يحققون 45% من أرباح المتجر.</td>
        </tr>
        <tr>
            <td><strong>4. القرار (DECISION)</strong></td>
            <td>إجراء عملي استراتيجي يُنفذ على أرض الواقع.</td>
            <td>تخصيص 60% من ميزانية الإعلانات لحملات موجهة لشباب المنطقة (أ).</td>
        </tr>
    </table>

    <h3>1.2 الفرق بين تحليل البيانات وتحليلات البيانات (Analysis vs. Analytics)</h3>
    <table>
        <tr>
            <th>وجه المقارنة</th>
            <th>تحليل البيانات (Data Analysis)</th>
            <th>تحليلات البيانات (Data Analytics)</th>
        </tr>
        <tr>
            <td><strong>التركيز الأساسي</strong></td>
            <td>فحص البيانات السابقة للإجابة عن أسئلة محددة حدثت بالفعل.</td>
            <td>تخصص ومظلة أوسع تشمل جمع البيانات، الإحصاء، التنبؤ، ودعم اتخاذ القرار.</td>
        </tr>
        <tr>
            <td><strong>الأسئلة النموذجية</strong></td>
            <td>"ماذا حدث؟" و "لماذا حدث ذلك؟"</td>
            <td>"ماذا حدث؟ لماذا حدث؟ ماذا قد يحدث مستقبلاً؟ وما هو الإجراء الأفضل؟"</td>
        </tr>
        <tr>
            <td><strong>النطاق المؤسسي</strong></td>
            <td>مهمة أو نشاط تحليلي محدد.</td>
            <td>مجال وقدرة مؤسسية شاملة ومنظومة عمل متكاملة.</td>
        </tr>
    </table>

    <h3>1.3 الأنواع الأربعة للتحليلات (تركيز امتحاني عالي الأهمية)</h3>
    <table>
        <tr>
            <th>النوع</th>
            <th>السؤال الجوهري</th>
            <th>الخصائص والأساليب المتبعة</th>
            <th>مثال من واقع الأعمال</th>
        </tr>
        <tr>
            <td><strong>1. الوصفية (Descriptive)</strong></td>
            <td><em>"ماذا حدث؟"</em></td>
            <td>تلخيص البيانات التاريخية والحالية عبر التقارير ولوحات مؤشرات الأداء (KPIs) والمتوسطات.</td>
            <td>انخفاض إيرادات المبيعات الشهر الماضي بنسبة 12%.</td>
        </tr>
        <tr>
            <td><strong>2. التشخيصية (Diagnostic)</strong></td>
            <td><em>"لماذا حدث ذلك؟"</em></td>
            <td>التحري عن الأسباب الجذرية والعلاقات؛ باستخدام التعمق (Drill-down)، التقسيم لشرائح، والارتباط.</td>
            <td>الانخفاض تركز في المنطقة (أ) نتيجة تأخر وصول شحنات المورد الرئيسي للمتجر.</td>
        </tr>
        <tr>
            <td><strong>3. التنبؤية (Predictive)</strong></td>
            <td><em>"ماذا قد يحدث مستقبلاً؟"</em></td>
            <td>استخدام البيانات التاريخية ونماذج الإحصاء والتعلم الآلي لتقدير الاحتمالات القادمة (<em>احتمالية وليست مضمونة</em>).</td>
            <td>توقع استمرار انخفاض المبيعات بنسبة 8% في الشهر القادم إذا لم يتغير المورد.</td>
        </tr>
        <tr>
            <td><strong>4. التوجيهية (Prescriptive)</strong></td>
            <td><em>"ماذا يجب أن نفعل؟"</em></td>
            <td>تقييم الخيارات المتاحة عبر خوارزميات الاستمثال (Optimization) والمحاكاة لتقديم أفضل قرار عملي.</td>
            <td>تقديم عروض ترويجية فورية في المنطقة (أ) مع التعاقد المؤقت مع مورد بديل.</td>
        </tr>
    </table>

    <div class="callout trap">
        <div class="callout-title">⚠️ فخ امتحاني: سؤال الأعمال مقابل السؤال التحليلي</div>
        تطرح الإدارة المشاكل بصيغة تجارية عامة (مثل: <em>"لماذا تنخفض مبيعاتنا؟"</em>). لا يبدأ المحلل بالبحث عن إجابات حتى يفكك هذا السؤال إلى <strong>أسئلة تحليلية قابلة للقياس الرياضي</strong>: <em>أي المنتجات انخفضت مبيعاتها؟ في أي المناطق والشهور؟ وما الفئات العمرية المتأثرة؟</em> التحليل الناجح يبدأ بسؤال واضح، وليس بأداة برمجية!
    </div>

    <h3>1.4 المسارات المهنية والأدوار الوظيفية</h3>
    <ul>
        <li><strong>محلل البيانات (Data Analyst):</strong> استعلام قواعد البيانات بـ SQL، معالجة الجداول في Excel، وبناء التقارير ومؤشرات الأداء.</li>
        <li><strong>محلل ذكاء الأعمال (BI Analyst):</strong> بناء اللوحات التفاعلية (Power BI)، نمذجة البيانات المؤسسية، ومتابعة مؤشرات النمو.</li>
        <li><strong>محلل المنتجات (Product Analyst):</strong> تتبع سلوك المستخدمين داخل التطبيقات والمواقع، ومتابعة قمع الشراء (Funnel) وتجارب A/B.</li>
        <li><strong>عالم البيانات (Data Scientist):</strong> تطبيق الإحصاء المتقدم وخوارزميات تعلم الآلة المعقدة، والبرمجة الاحترافية بـ Python و R.</li>
        <li><strong>المهارات الأساسية:</strong> التقنية (SQL, Excel, Python)، التحليلية (التفكير النقدي واكتشاف الأنماط)، الفهم التجاري (Business Acumen)، الثقافة البيانية (Data Literacy)، والتواصل الفعال.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section-block">
    <h2><span class="sec-pill">02</span> نماذج اتخاذ القرار وحل المشكلات (Chapter 2)</h2>

    <h3>2.1 ما هو النموذج؟ الأشكال الثلاثة للنماذج</h3>
    <p><strong>النموذج (Model):</strong> هو تمثيل أو تجريد لنظام حقيقي أو فكرة أو شيء واقعي، يهدف إلى إبراز العلاقات الجوهرية واستبعاد التفاصيل غير المهمة لتسهيل دراستها.</p>
    <table>
        <tr>
            <th>شكل النموذج</th>
            <th>الوسط وطريقة التعبير</th>
            <th>مثال توضيحي</th>
        </tr>
        <tr>
            <td><strong>1. وصفي / لفظي (Written/Verbal)</strong></td>
            <td>كلمات وجمل باللغة الطبيعية تعبر عن العلاقة.</td>
            <td>"تزداد مبيعات المنتج بزيادة الإنفاق الإعلاني، ولكن بمعدل متناقص تدريجياً."</td>
        </tr>
        <tr>
            <td><strong>2. مرئي / بياني (Visual/Graphical)</strong></td>
            <td>رسومات بيانية، منحنيات، ومخططات تدفق.</td>
            <td>رسم منحنى يمثل الإنفاق الإعلاني على المحور السيني وحجم المبيعات على الصادي.</td>
        </tr>
        <tr>
            <td><strong>3. رياضي (Mathematical)</strong></td>
            <td>معادلات وعلاقات رياضية محددة برموز وحسابات.</td>
            <td>$S = a - b &times; P + c &times; A$</td>
        </tr>
    </table>

    <h3>2.2 معمارية نماذج القرار: من المدخلات إلى المخرجات</h3>
    <p>يتعامل نموذج القرار مع ثلاثة أنواع من المدخلات لحساب مخرجات الأداء:</p>
    <ul>
        <li><strong>البيانات (Data):</strong> حقائق وثوابت عددية معلومة (مثل: تكلفة استئجار المصنع الثابتة، معدل ضريبة المبيعات).</li>
        <li><strong>المتغيرات غير القابلة للتحكم (Uncontrollable Variables):</strong> عوامل بيئية واقتصادية تفرضها قوى السوق أو الطبيعة ولا تملك الإدارة سلطة التحكم فيها (مثل: التضخم، أسعار المنافسين، درجات الحرارة).</li>
        <li><strong>متغيرات القرار (Decision Variables):</strong> متغيرات تخضع مباشرة لسيطرة الإدارة وتختار قيمتها بإرادتها (مثل: سعر بيع المنتج، الكمية المنتجة، ميزانية الإعلانات).</li>
        <li><strong>المخرجات (Outputs):</strong> مقاييس الأداء المحسوبة الناتجة عن النموذج (مثل: إجمالي الأرباح، العائد على الاستثمار، الإيرادات).</li>
    </ul>

    <h3>2.3 النماذج الوصفية: التكلفة الإجمالية ونقطة التعادل</h3>
    <div class="card">
        <div class="callout-title">📐 نموذج نقطة التعادل (Break-Even Model)</div>
        <p>تتألف التكلفة الإجمالية في محاسبة التكاليف من التكاليف الثابتة ($F$) والتكاليف المتغيرة للوحدة ($V$):</p>
        <p style="font-family: Consolas; font-size: 13px; font-weight: 700; color: #b45309;">التكلفة الإجمالية: TC = F + V &times; Q</p>
        <p>بينما يُحسب الإيراد الإجمالي ($TR$) بضرب سعر بيع الوحدة ($P$) في الكمية المباعة ($Q$):</p>
        <p style="font-family: Consolas; font-size: 13px; font-weight: 700; color: #b45309;">الإيراد الإجمالي: TR = P &times; Q</p>
        <p><strong>نقطة التعادل ($Q_{{BE}}$):</strong> هي حجم المبيعات الذي يتساوى عنده الإيراد الكلي مع التكلفة الكلية ($TR = TC$)، وتكون الأرباح عنده صفراً (لا ربح ولا خسارة):</p>
        <div class="code-box">
P * Q = F + V * Q
Q * (P - V) = F
Q_BE = F / (P - V)

حيث:
  (P - V) = هامش المساهمة للوحدة (Unit Contribution Margin)
        </div>
        <p><strong>مثال رقمي:</strong> إذا كانت التكاليف الثابتة $F = 100,000\$، وتكلفة الوحدة المتغيرة $V = 20\$، وسعر البيع $P = 60\$:<br>
        هامش المساهمة للوحدة = $60 - 20 = 40\$$.<br>
        كمية التعادل $Q_{{BE}} = \frac{{100,000}}{{40}} = 2,500\text{{ وحدة}}$.</p>
    </div>

    <h3>2.4 نماذج التنبؤ بالطلب: الخطية وغير الخطية</h3>
    <ul>
        <li><strong>نموذج الطلب الخطي:</strong> $D = a - b &times; P$<br>
        يفترض انخفاضاً ثابتاً ومطلقا في كمية الطلب مقابل كل دولار زيادة في السعر ($b$ يمثل ميل المنحنى).</li>
        <li><strong>نموذج الطلب غير الخطي:</strong> $D = a &times; P^{{-b}}$<br>
        في هذه الدالة الأسية، يمثل الأس $-b$ مباشرة <strong>مرونة الطلب السعرية الثابتة (Price Elasticity)</strong>.</li>
    </ul>

    <h3>2.5 نماذج القرار التوجيهية: الحتمية مقابل الاحتمالية</h3>
    <table>
        <tr>
            <th>نوع النموذج</th>
            <th>طبيعة المدخلات</th>
            <th>أبرز الأساليب والأمثلة</th>
        </tr>
        <tr>
            <td><strong>النموذج الحتمي (Deterministic)</strong></td>
            <td>كافة المدخلات والمعاملات والقيود معروفة بـ <strong>يقين تام وبدون شك</strong>.</td>
            <td>البرمجة الخطية (Linear Programming)، نماذج التعادل الحسابية.</td>
        </tr>
        <tr>
            <td><strong>النموذج العشوائي / الاحتمالي (Stochastic)</strong></td>
            <td>واحد أو أكثر من المدخلات يخضع لـ <strong>المخاطرة أو الاحتمالات وتوزيعات عدم اليقين</strong>.</td>
            <td>محاكاة مونت كارلو (Monte Carlo Simulation)، أشجار القرار، ونماذج التنبؤ بالمخاطر.</td>
        </tr>
    </table>

    <h3>2.6 المراحل الست لحل المشكلات واتخاذ القرار</h3>
    <ol>
        <li><strong>1. إدراك المشكلة (Recognizing):</strong> شعور الإدارة بوجود فجوة ملحوظة بين الأداء الفعلي الحالي والهدف المنشود (مثل ملاحظة انخفاض المبيعات أو زيادة شكاوى العملاء).</li>
        <li><strong>2. تعريف المشكلة (Defining):</strong> أصعب المراحل وأكثرها حساسية! الفصل بين الأعراض السطحية والأسباب الجذرية، وتوضيح أهداف العمل والقيود الحاكمة.</li>
        <li><strong>3. هيكلة المشكلة (Structuring):</strong> تحويل المشكلة لنموذج رسمي؛ تحديد متغيرات القرار، المتغيرات الخارجية، القيود، والافتراضات.</li>
        <li><strong>4. تحليل المشكلة (Analyzing):</strong> حل النموذج وتطبيق الخوارزميات والمعادلات الرياضية للوصول للحلول الممكنة.</li>
        <li><strong>5. تفسير النتائج وتحليل الحساسية (Interpreting):</strong> ترجمة المخرجات الحسابية إلى قرارات تجارية واقعية؛ وإجراء تحليل "ماذا لو" (Sensitivity Analysis) لفحص متانة الحل عند تغير المدخلات.</li>
        <li><strong>6. تطبيق وتنفيذ الحل (Implementing):</strong> وضع القرار موضع التطبيق الميداني في العمليات؛ وتدريب الموظفين وإدارة التغيير ومتابعة التغذية الراجعة.</li>
    </ol>
</div>

<div class="page-break"></div>

<div class="section-block">
    <h2><span class="sec-pill">03</span> دورة حياة تحليلات البيانات وحوكمة المشاريع (Chapter 3)</h2>
    <p>تفشل الكثير من مشاريع علوم وتحليلات البيانات ليس بسبب خطأ في الخوارزمية، بل لغياب منهجية العمل وضعف التنسيق مع أصحاب المصلحة. توفر <strong>دورة حياة تحليلات البيانات (Data Analytics Lifecycle)</strong> إطاراً علمياً من 6 مراحل لضمان النجاح.</p>

    <h3>3.1 الأدوار السبعة الرئيسية في فريق مشروع التحليلات</h3>
    <table>
        <tr>
            <th>الدور الوظيفي</th>
            <th>المسؤولية الجوهرية</th>
            <th>المهام والمخرجات الرئيسية</th>
        </tr>
        <tr>
            <td><strong>1. راعي المشروع (Project Sponsor)</strong></td>
            <td>المالك التنفيذي وموفر التمويل.</td>
            <td>يحدد الرؤية التجارية، يوفر الميزانية والدعم السياسي، ويقيم العائد الاستثماري (ROI).</td>
        </tr>
        <tr>
            <td><strong>2. مستخدم الأعمال (Business User)</strong></td>
            <td>خبير المجال والمستفيد النهائي.</td>
            <td>يقدم الخبرة الميدانية، يوضح مسارات العمل، ويستخدم المخرجات في اتخاذ القرارات اليومية.</td>
        </tr>
        <tr>
            <td><strong>3. مدير المشروع (Project Manager)</strong></td>
            <td>التتبع وحوكمة الجداول الزمنية.</td>
            <td>يضمن تسليم مراحل المشروع في مواعيدها وضمن الميزانية ويدير العقبات.</td>
        </tr>
        <tr>
            <td><strong>4. محلل ذكاء الأعمال (BI Analyst)</strong></td>
            <td>فهم سياق التقارير المؤسسية.</td>
            <td>يمتلك دراية عميقة بمستودعات البيانات القديمة، قواعد احتساب مؤشرات الأداء، والتقارير التاريخية.</td>
        </tr>
        <tr>
            <td><strong>5. مسؤول قواعد البيانات (DBA)</strong></td>
            <td>تهيئة البيئة وحماية الصلاحيات.</td>
            <td>يهيئ خوادم قواعد البيانات، يمنح الصلاحيات بأمان، ويحمي قواعد بيانات الإنتاج من التوقف.</td>
        </tr>
        <tr>
            <td><strong>6. مهندس البيانات (Data Engineer)</strong></td>
            <td>بناء خطوط الأنابيب ومعالجة البيانات.</td>
            <td>يبني خطوط استخلاص ونقل البيانات (ETL/ELT)، ينظف البيانات، ويجهز بيئة صندوق الرمل التحليلي.</td>
        </tr>
        <tr>
            <td><strong>7. عالم البيانات (Data Scientist)</strong></td>
            <td>النمذجة الرياضية وبناء الخوارزميات.</td>
            <td>يصمم النماذج الإحصائية والتعلم الآلي، يهندس الخصائص، ويختبر دقة النتائج الرياضية.</td>
        </tr>
    </table>

    <h3>3.2 المراحل الست لدورة حياة التحليلات بالتفصيل</h3>
    
    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">المرحلة 1: الاستكشاف (Discovery)</h3>
        <ul>
            <li><strong>الهدف:</strong> استيعاب بيئة الأعمال، فحص البيانات المتاحة، وتقييم الموارد والعتاد البشري والتقني.</li>
            <li><strong>الأنشطة:</strong> إجراء المقابلات، صياغة <em>الفرضيات المبدئية (Initial Hypotheses)</em>، وتأطير المشكلة التجارية في تحدٍ تحليلي وصياغة خطة التحليل (Analytic Plan).</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">المرحلة 2: تجهيز البيانات (Data Preparation)</h3>
        <ul>
            <li><strong>الهدف:</strong> جمع وتنظيف وفحص وتكييف البيانات لتصبح جاهزة للنمذجة.</li>
            <li><strong>صندوق الرمل التحليلي (Analytic Sandbox):</strong> بيئة عمل منعزلة وعالية الكفاءة تتيح لفريق التحليلات استكشاف وتعديل كميات البيانات الضخمة دون المساس بأنظمة الإنتاج التشغيلية للشركة.</li>
            <li><strong>الأنشطة:</strong> عمليات ETL/ELT، معالجة القيم المفقودة والمتطرفة، والتحليل الاستكشافي للبيانات (EDA).</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">المرحلة 3: تخطيط النموذج (Model Planning)</h3>
        <ul>
            <li><strong>الهدف:</strong> تحديد المنهجيات والتقنيات ومسار التدريب للنماذج.</li>
            <li><strong>الأنشطة:</strong> اختيار الخصائص (Feature Selection)، فحص التوزيعات الإحصائية، واختيار عائلة الخوارزميات المناسبة (انحدار، تصنيف، تجميع).</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">المرحلة 4: بناء وتدريب النموذج (Model Building)</h3>
        <ul>
            <li><strong>الهدف:</strong> تطوير وتنفيذ خوارزميات التعلم الآلي الرياضية.</li>
            <li><strong>الأنشطة:</strong> تقسيم البيانات إلى مجموعات <strong>تدريب واختبار (Train / Test split)</strong> لمنع فرط التخصيص (Overfitting)؛ وضبط معايير النموذج بدقة.</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">المرحلة 5: إيصال النتائج (Communicate Results)</h3>
        <ul>
            <li><strong>الهدف:</strong> تحديد هل نجح المشروع أم فشل مقارنة بالفرضيات المبدئية المحددة في البداية.</li>
            <li><strong>الأنشطة:</strong> احتساب القيمة التجارية والعائد المالي (ROI)، وتلخيص النتائج بأسلوب يلائم كل طرف من أصحاب المصلحة.</li>
        </ul>
    </div>

    <div class="card">
        <h3 style="color: #b45309; margin-top: 0;">المرحلة 6: التشغيل الميداني (Operationalize)</h3>
        <ul>
            <li><strong>الهدف:</strong> نشر النموذج المعتمد داخل بيئة العمل الحية بالشركة.</li>
            <li><strong>الأنشطة:</strong> تشغيل <strong>مشروع تجريبي استرشادي (Pilot Project)</strong> في قطاع محدود لاختبار الاستقرار، تسليم الأكواد وخطوط النقل، ومراقبة تغير سلوك البيانات مع الوقت (Drift).</li>
        </ul>
    </div>

    <h3>3.3 المخرجات الأربعة لتلبية احتياجات أصحاب المصلحة</h3>
    <table>
        <tr>
            <th>المخرج النهائي</th>
            <th>الجمهور المستهدف</th>
            <th>طبيعة المحتوى والأسلوب</th>
        </tr>
        <tr>
            <td><strong>1. العرض التنفيذي</strong></td>
            <td>راعي المشروع وكبار القادة</td>
            <td>تركيز كامل على الأثر المالي والاستراتيجي وتوصيات العمل، وخالٍ تماماً من تفاصيل الأكواد المعقدة.</td>
        </tr>
        <tr>
            <td><strong>2. العرض التشغيلي</strong></td>
            <td>مستخدمو الأعمال والمحللون</td>
            <td>كيفية دمج مخرجات النموذج في المهام اليومية ومؤشرات الأداء التشغيلية.</td>
        </tr>
        <tr>
            <td><strong>3. التقرير الفني الشامل</strong></td>
            <td>علماء البيانات والباحثون النظراء</td>
            <td>توثيق رياضي كامل: المعادلات، منحنيات التدريب، معايير الدقة، وكافة الافتراضات.</td>
        </tr>
        <tr>
            <td><strong>4. الأكواد والوثائق التقنية</strong></td>
            <td>مهندسو البيانات ومسؤولو DevOps</td>
            <td>أكواد برمجية معلقة وموثقة، خطوط نقل البيانات، واجهات API، ونظام تنبيهات مراقبة الأداء.</td>
        </tr>
    </table>

    <div class="callout tip">
        <div class="callout-title">💡 وصية امتحانية ذهبية: التكرار في دورة الحياة (Iteration)</div>
        دورة حياة تحليلات البيانات <strong>تكرارية وليست خطية جامدة</strong>. إذا أثبتت المرحلة 5 أن النموذج لم يحقق الدقة المطلوبة أو فشل في إثبات الفرضية، يعود الفريق فوراً للمرحلة 2 (لإعادة تنظيف البيانات وهندسة خصائص جديدة) أو المرحلة 3 (لاختيار خوارزميات بديلة).
    </div>
</div>

</body>
</html>"""

os.makedirs('summaries', exist_ok=True)
with open('summaries/Business_Summary_EN.html', 'w', encoding='utf-8') as f:
    f.write(html_ba_en)
with open('summaries/Business_Summary_AR.html', 'w', encoding='utf-8') as f:
    f.write(html_ba_ar)

print("Saved HTML summaries for Business Analytics.")

# Compile Business PDFs
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
for lang, fn_html, fn_pdf in [
    ('EN', 'summaries/Business_Summary_EN.html', 'summaries/Business_Summary_EN.pdf'),
    ('AR', 'summaries/Business_Summary_AR.html', 'summaries/Business_Summary_AR.pdf')
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
