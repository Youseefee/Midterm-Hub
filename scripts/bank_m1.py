# scripts/bank_m1.py
# 66 Rigorous, Medium-Difficulty Questions for Module 1: Introduction to Data Analytics

BANK_M1 = [
    # --- 1.1 The Value Transformation Chain: Data -> Information -> Insight -> Decision ---
    {
        "topic": "Data Definition & Value Chain",
        "question": "In the analytics value transformation chain, which characteristic formally distinguishes raw data from information?",
        "correct": "Raw data consists of unorganized records that lack contextual meaning until structured",
        "distractors": [
            "Raw data consists of qualitative user survey feedback that has already been aggregated",
            "Raw data is structured into multidimensional OLAP cubes for executive sales reporting",
            "Raw data represents actionable strategic recommendations derived from regression models"
        ],
        "explanation": "Data represents raw facts, observations, and records without context. It only transforms into information once organized, structured, and cleaned."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "A retail chain records 100,000 raw barcode scans every hour. At what point does this collection become 'Information'?",
        "correct": "When transaction logs are aggregated to show product sales by store location and department",
        "distractors": [
            "When individual barcode timestamps are archived into cold tape storage without indexing",
            "When the corporate marketing director decides to launch a nationwide discount campaign",
            "As soon as the laser scanner successfully registers the numerical product code at checkout"
        ],
        "explanation": "Information represents data that has been organized, categorized, and structured to provide context, such as sales aggregated by department."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "What is the correct sequential order of stages in the analytics value transformation chain?",
        "correct": "Data -> Information -> Insight -> Decision",
        "distractors": [
            "Information -> Data -> Decision -> Insight",
            "Data -> Insight -> Information -> Decision",
            "Insight -> Data -> Information -> Decision"
        ],
        "explanation": "The value transformation chain progresses systematically from raw Data to structured Information, to actionable Insight, and finally to Decision execution."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "An e-commerce company notices that users aged 18-24 abandon carts 40% more often when shipping fees exceed $5. In the value transformation chain, this finding represents:",
        "correct": "An Insight, because it reveals an underlying behavioral pattern and relationship",
        "distractors": [
            "Raw Data, because it involves numerical measurements collected from web server access logs",
            "Information, because it merely categorizes raw transaction amounts by user age brackets",
            "A Decision, because it represents an implemented operational policy change by management"
        ],
        "explanation": "An Insight goes beyond summary information by uncovering meaningful patterns, correlations, and causal relationships within data."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Following a detailed customer behavior study, an airline reduces excess baggage fees on underperforming routes to boost bookings. In the value transformation chain, this action is classified as:",
        "correct": "A Decision, representing the execution of an actionable business strategy",
        "distractors": [
            "An Insight, representing statistical discovery of customer price sensitivity curves",
            "Information, representing the historical report of average passenger ticket prices",
            "Raw Data, representing the collected flight manifests and baggage weight measurements"
        ],
        "explanation": "The final stage of the value transformation chain is Decision, where analytical insights are converted into concrete business actions and policies."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Why does raw operational data inherently possess zero intrinsic business value on its own?",
        "correct": "Without contextual structuring and interpretation, it cannot inform managerial action",
        "distractors": [
            "Raw data is stored in relational schemas that prevent statistical querying by analysts",
            "Data warehouse architectures automatically purge unindexed records after twenty-four hours",
            "Operational transaction files are restricted to administrative system logging protocols"
        ],
        "explanation": "Raw facts and measurements lack context and meaning. Value is only unlocked when data is transformed into information, insights, and actionable decisions."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Which of the following scenarios best illustrates the organizational breakdown known as being 'data rich but insight poor'?",
        "correct": "A firm stores terabytes of sensor logs but lacks analytical workflows to explain failure patterns",
        "distractors": [
            "A startup possesses validated predictive models but cannot secure adequate cloud compute credits",
            "An enterprise executive board refuses to invest in modern distributed storage data lakes",
            "A research laboratory analyzes benchmark data using non-relational document database engines"
        ],
        "explanation": "'Data rich but insight poor' occurs when organizations accumulate vast quantities of raw data without having the tools or processes to extract meaningful patterns."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Which of the following is NOT an example of raw data in a hospital management setting?",
        "correct": "A quarterly report highlighting that readmission rates rose 14% due to medication errors",
        "distractors": [
            "Unprocessed systolic and diastolic blood pressure readings stored in ICU monitor caches",
            "Individual patient admission timestamp records captured by the reception desk check-in software",
            "Raw digital sensor readings emitted by infusion pumps during patient intravenous therapies"
        ],
        "explanation": "A quarterly report identifying a 14% readmission rise due to medication errors combines context and causation, making it Information/Insight, not raw data."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "In the transition from Information to Insight, what primary analytical shift occurs?",
        "correct": "Analysts move from summarizing historical metrics to identifying causal drivers and relationships",
        "distractors": [
            "Analysts transition from utilizing relational databases to writing manual ledger spreadsheets",
            "Analysts discard historical records and focus exclusively on speculative qualitative intuition",
            "Analysts convert proprietary numerical tables into unformatted text files for storage efficiency"
        ],
        "explanation": "Transitioning from Information to Insight requires synthesizing organized metrics to explain why patterns occur and identifying underlying relationships."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "A telecommunications provider aggregates weekly dropped call figures across 500 cellular towers into a regional performance report. This structured summary represents:",
        "correct": "Information, because raw network telemetry has been organized and categorized",
        "distractors": [
            "Raw Data, because the numbers reflect automated electronic signals from cell equipment",
            "An Insight, because tower data automatically reveals the exact electronic hardware defect",
            "A Decision, because the weekly compilation forces engineers to purchase new cell towers"
        ],
        "explanation": "Organizing and summarizing raw telemetry logs into weekly dropped-call counts by tower provides structured Information."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Which factor is most responsible for preventing actionable insights from translating into successful business decisions?",
        "correct": "Organizational inertia, lack of executive sponsorship, or resistance to process change",
        "distractors": [
            "Database management systems lacking multi-threaded CPU processor hardware cores",
            "Relational database tables having strictly enforced primary and foreign key constraints",
            "Software developers choosing Python rather than proprietary spreadsheet macros for data pipelines"
        ],
        "explanation": "Insights fail to become decisions primarily due to organizational barriers, cultural resistance, and lack of alignment between analysts and leaders."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Consider a supermarket transaction database. Which of the following elements represents 'Information' rather than 'Data'?",
        "correct": "A monthly summary table displaying total dairy sales revenue by branch store",
        "distractors": [
            "The numeric value '12.99' stored in a raw point-of-sale receipt line item record",
            "A timestamp '2026-11-04 14:22:05' recorded on a single store checkout register terminal",
            "A barcode sequence '079400012345' scanned during an individual customer grocery purchase"
        ],
        "explanation": "A monthly summary table of dairy revenue structures and aggregates raw transaction figures, elevating it to Information."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "What primary operational danger arises when an enterprise makes strategic corporate decisions directly from raw data without extracting insight?",
        "correct": "Decisions may be distorted by uncleaned outliers, statistical noise, or missing context",
        "distractors": [
            "The organization will automatically violate industry software licensing copyright agreements",
            "Relational database management servers will immediately experience irreversible disk write failures",
            "Competitors will be granted automatic administrative access to internal company communications"
        ],
        "explanation": "Raw data contains noise, missing fields, and unadjusted anomalies; acting without intermediate structuring and insight leads to flawed, reactionary decisions."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "A commercial bank calculates that customers holding both a checking account and an auto loan exhibit an 80% lower attrition rate. This finding represents:",
        "correct": "An Insight, revealing a cross-product relationship affecting customer retention",
        "distractors": [
            "Raw Data, because it is based on customer account balances and loan identifiers",
            "A Decision, because it mandates loan officers to offer checking accounts to borrowers",
            "Operational Information, because it is merely a raw tally of total loan accounts"
        ],
        "explanation": "Uncovering that holding multi-product relationships drastically reduces attrition is an Insight that reveals underlying customer retention dynamics."
    },
    {
        "topic": "Data Definition & Value Chain",
        "question": "Which of the following statements regarding the analytics value transformation chain is FALSE?",
        "correct": "Reaching the Insight stage guarantees that an organization will achieve profitable decisions",
        "distractors": [
            "Raw data must be filtered, normalized, and contextualized to yield useful information",
            "A single dataset can yield multiple distinct insights depending on the analytical queries posed",
            "Decision execution requires cross-functional alignment and resource allocation in the business"
        ],
        "explanation": "Deriving insight does not guarantee profitability; poor execution, flawed strategy, or timing issues can still derail business decisions."
    },

    # --- 1.2 Data Analysis vs. Data Analytics ---
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "How do Data Analysis and Data Analytics primarily differ in terms of their guiding temporal focus?",
        "correct": "Data Analysis focuses on past performance, whereas Data Analytics extends into predictive and prescriptive actions",
        "distractors": [
            "Data Analysis predicts future outcomes, whereas Data Analytics focuses strictly on auditing past tax records",
            "Data Analysis examines real-time sensor streams, whereas Data Analytics ignores historical datasets entirely",
            "Data Analysis is applied only to non-profit organizations, whereas Data Analytics is exclusive to finance"
        ],
        "explanation": "Data Analysis typically answers 'What happened and why?', while Data Analytics covers the broader spectrum including 'What will happen and what should we do?'"
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "In terms of organizational scope, how is Data Analytics distinguished from Data Analysis?",
        "correct": "Data Analytics encompasses an entire enterprise capability, architecture, and toolset, not just a task",
        "distractors": [
            "Data Analytics is restricted to single-user desktop spreadsheets for ad-hoc quarterly calculations",
            "Data Analysis requires multi-node cloud clusters, whereas Data Analytics uses paper survey cards",
            "Data Analytics is an entry-level job title, whereas Data Analysis is a board-level corporate officer"
        ],
        "explanation": "Data Analysis refers to specific investigative activities on datasets, while Data Analytics is a holistic discipline, infrastructure, and organizational capability."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Which guiding question is characteristic of traditional Data Analysis rather than advanced Data Analytics?",
        "correct": "'What specific operational events caused our sales volume to drop last quarter?'",
        "distractors": [
            "'What is the optimal discount rate to maximize next month's gross profit margin?'",
            "'Which customer cohorts have a 70% or greater probability of churning next year?'",
            "'How should supply chain inventory routes be dynamically reconfigured tomorrow?'"
        ],
        "explanation": "Questions focusing strictly on retrospective diagnosis ('What happened?' and 'Why?') are the hallmark of traditional Data Analysis."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "An analytics manager explains that their team does not just perform retrospective reporting, but builds end-to-end data pipelines and automated optimization models. This demonstrates:",
        "correct": "The comprehensive, forward-looking scope of Data Analytics as an organizational discipline",
        "distractors": [
            "A failure to understand the fundamental purpose of basic relational database normalization",
            "That the company is engaging in high-frequency algorithmic speculation without oversight",
            "A violation of standard data hygiene practices by mixing past and future metrics together"
        ],
        "explanation": "Data Analytics spans data architecture, statistical modeling, machine learning, and decision optimization across the entire enterprise lifecycle."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Which of the following activities is best classified as an instance of Data Analysis rather than Data Analytics?",
        "correct": "Filtering last month's customer support tickets in a spreadsheet to categorize common complaints",
        "distractors": [
            "Designing an automated real-time fraud detection pipeline using gradient boosted decision trees",
            "Developing an enterprise-wide data governance policy and predictive customer lifetime value architecture",
            "Constructing a mixed-integer linear program to optimize delivery fleet routes across five distribution hubs"
        ],
        "explanation": "Categorizing past support tickets is a retrospective, specific investigative task characteristic of Data Analysis."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Why does modern enterprise strategy view Data Analytics as a core competitive differentiator rather than a routine back-office task?",
        "correct": "It enables proactive optimization and automated decision making rather than mere retrospective audits",
        "distractors": [
            "Data Analytics allows corporations to replace all human executive managers with static spreadsheets",
            "Cloud computing providers offer Data Analytics tools completely free of charge to all businesses",
            "Government regulatory agencies require every registered company to file weekly predictive models"
        ],
        "explanation": "Modern organizations compete on their ability to anticipate market shifts and optimize decisions using analytics, moving beyond passive record-keeping."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Which of the following best describes the relationship between Data Analysis and Data Analytics?",
        "correct": "Data Analysis is a vital component and historical foundation within the broader discipline of Data Analytics",
        "distractors": [
            "Data Analysis and Data Analytics are mutually exclusive methodologies that cannot coexist in a firm",
            "Data Analysis has been completely deprecated and banned from modern business computing systems",
            "Data Analytics is strictly qualitative, whereas Data Analysis relies exclusively on calculus"
        ],
        "explanation": "Data Analysis (inspecting and understanding historical data) is an essential sub-component of the broader, forward-looking Data Analytics framework."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "When an analyst moves from answering 'Why did website traffic decline in July?' to 'How will website traffic trend in December?', they are transitioning:",
        "correct": "From retrospective diagnostic analysis to forward-looking predictive analytics",
        "distractors": [
            "From prescriptive decision optimization to raw unconditioned data collection",
            "From advanced algorithmic data science to entry-level database administration",
            "From structured business intelligence to unstructured subjective speculation"
        ],
        "explanation": "Shifting from historical root-cause evaluation to future estimation marks the transition from diagnostic analysis to predictive analytics."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Which organizational component is essential to a mature Data Analytics capability but often unnecessary for simple ad-hoc Data Analysis?",
        "correct": "End-to-end data infrastructure, automated pipelines, and continuous model governance",
        "distractors": [
            "A spreadsheet program capable of summing tabular numeric columns and creating bar charts",
            "A single desktop computer connected to an office local area network file server",
            "A team member who has completed an introductory course in accounting principles"
        ],
        "explanation": "Enterprise Data Analytics requires durable architectures, ingestion pipelines, machine learning environments, and governance frameworks."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Which of the following statements accurately reflects the toolset differences between Data Analysis and Data Analytics?",
        "correct": "Analysis often relies on Excel and basic SQL; analytics leverages distributed clusters, Python, R, and ML frameworks",
        "distractors": [
            "Analysis requires multi-node Spark clusters; analytics is strictly performed with manual ledger calculations",
            "Analysis uses deep learning neural networks; analytics is limited to simple two-variable scatter plots",
            "Analysis cannot use relational databases; analytics is prohibited from connecting to cloud platforms"
        ],
        "explanation": "Traditional analysis typically uses desktop spreadsheets and query tools, while full analytics utilizes advanced programming, machine learning, and big data engines."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "If a manufacturing plant uses sensors to trigger automatic machine recalibration before overheating occurs, this operational capability is an example of:",
        "correct": "Prescriptive analytics embedded within an automated operational decision workflow",
        "distractors": [
            "Basic data analysis summarizing last week's equipment maintenance expenses",
            "Descriptive reporting providing monthly scrap waste tallies to plant supervisors",
            "Diagnostic analysis explaining why a motor bearing melted three weeks ago"
        ],
        "explanation": "Automated real-time action based on predictive triggers embodies prescriptive analytics embedded in operations."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "Why is it fundamentally inaccurate to equate Business Analytics solely with software applications like Excel, Power BI, or Tableau?",
        "correct": "Analytics is a rigorous problem-solving methodology; software packages are merely execution tools",
        "distractors": [
            "Business analytics software applications are incapable of storing floating-point decimal figures",
            "Enterprise executives are legally required to perform all strategic modeling using handwritten proofs",
            "Commercial software tools only store data and cannot execute any mathematical operations"
        ],
        "explanation": "Analytics is fundamentally about framing questions, applying scientific reasoning, and interpreting models; software tools are just vehicles for execution."
    },
    {
        "topic": "Data Analysis vs Data Analytics",
        "question": "An executive demands: 'Stop telling me what went wrong in our logistics division and start showing me how to prevent it!' The executive is requesting a transition:",
        "correct": "From descriptive/diagnostic analysis to predictive and prescriptive analytics",
        "distractors": [
            "From advanced predictive modeling to basic manual ledger bookkeeping",
            "From quantitative decision science to purely subjective executive intuition",
            "From strategic enterprise analytics to low-level database schema design"
        ],
        "explanation": "Moving from backward-looking explanations to forward prevention requires predictive modeling and prescriptive optimization."
    },

    # --- 1.3 The Four Major Types of Analytics ---
    {
        "topic": "The Four Types of Analytics",
        "question": "Which type of analytics is primarily concerned with answering the guiding question: 'What happened?'",
        "correct": "Descriptive Analytics, which summarizes past performance metrics and operational records",
        "distractors": [
            "Diagnostic Analytics, which determines the root causes behind sudden KPI variances",
            "Predictive Analytics, which models future likelihoods based on historical patterns",
            "Prescriptive Analytics, which identifies the mathematically optimal decision course"
        ],
        "explanation": "Descriptive Analytics focuses strictly on historical and current facts, answering 'What happened?' through summaries, reports, and dashboards."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A quarterly sales dashboard showing regional revenue, units sold, and average customer transaction size is an example of:",
        "correct": "Descriptive Analytics, providing a consolidated historical view of operational performance",
        "distractors": [
            "Diagnostic Analytics, evaluating why specific product lines failed to meet sales targets",
            "Predictive Analytics, generating probabilistic demand forecasts for next year's budget",
            "Prescriptive Analytics, recommending specific price increases to maximize profit"
        ],
        "explanation": "Standard KPI dashboards and summaries that depict historical performance belong to Descriptive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which core analytical question defines Diagnostic Analytics?",
        "correct": "'Why did it happen?', focusing on root causes, correlations, and performance variances",
        "distractors": [
            "'What happened?', focusing on historical transaction aggregation and status tracking",
            "'What will happen?', focusing on statistical forecasts and probabilistic trends",
            "'What is the best course of action?', focusing on mathematical optimization rules"
        ],
        "explanation": "Diagnostic Analytics searches for underlying reasons and causal relationships, answering 'Why did it happen?'"
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "An e-commerce retailer notices a 15% drop in mobile sales. The analyst performs drill-down analysis by browser version and discovers that an updated checkout button fails to render on Safari. This investigation exemplifies:",
        "correct": "Diagnostic Analytics, because it isolates the specific root cause of an operational failure",
        "distractors": [
            "Descriptive Analytics, because it merely records the total dollar amount of lost purchases",
            "Predictive Analytics, because it forecasts how many users will buy new phones next month",
            "Prescriptive Analytics, because it automatically reconfigures Safari web server certificates"
        ],
        "explanation": "Drilling down to identify the exact cause behind a metric anomaly is the hallmark of Diagnostic Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following analytical techniques is most commonly associated with Diagnostic Analytics?",
        "correct": "Drill-down slicing, cohort segmentation, and variance root-cause analysis",
        "distractors": [
            "Mixed-integer linear programming and multi-objective Pareto frontier solvers",
            "Simple historical tabulation of total annual electricity expenditure invoices",
            "Randomized Monte Carlo simulation of global geopolitical currency fluctuations"
        ],
        "explanation": "Diagnostic analytics relies on drill-down, cohort comparison, segmentation, and anomaly detection to uncover root causes."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "What is the primary guiding question addressed by Predictive Analytics?",
        "correct": "'What may happen in the future?', assessing probabilities based on historical trends",
        "distractors": [
            "'What happened in our retail stores over the previous three operating quarters?'",
            "'Why did our enterprise network servers crash during the holiday promotional rush?'",
            "'What exact schedule of employee shifts minimizes overall overtime payroll costs?'"
        ],
        "explanation": "Predictive Analytics assesses historical patterns and statistical models to forecast future likelihoods: 'What may happen?'"
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Why is it vital to understand that Predictive Analytics provides probabilistic estimates rather than deterministic guarantees?",
        "correct": "Future outcomes are subject to uncertainty, external shifts, and random variability",
        "distractors": [
            "Machine learning algorithms are mathematically incapable of calculating decimal values",
            "Enterprise cloud database servers introduce artificial noise into regression calculations",
            "Predictive algorithms are legally barred from calculating single point-estimate projections"
        ],
        "explanation": "Predictive models estimate likelihoods based on historical distributions; unexpected real-world changes and uncertainty mean outcomes are never guaranteed."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A credit card company calculates a credit risk score for each loan applicant using a logistic regression model. This is an application of:",
        "correct": "Predictive Analytics, estimating the applicant's future probability of default",
        "distractors": [
            "Descriptive Analytics, providing a historical tally of all loans issued since 2010",
            "Diagnostic Analytics, explaining why a specific branch manager approved past bad loans",
            "Prescriptive Analytics, legally forcing the applicant to accept a predetermined interest rate"
        ],
        "explanation": "Scoring credit risk estimates the future probability of repayment or default, which is Predictive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which guiding question defines Prescriptive Analytics?",
        "correct": "'What should we do?', evaluating alternatives to recommend or automate optimal decisions",
        "distractors": [
            "'What happened?', compiling historical transaction data into monthly financial statements",
            "'Why did it happen?', conducting retrospective audits of past supplier shipping delays",
            "'What could happen?', generating multi-scenario forecasts of macroeconomic inflation"
        ],
        "explanation": "Prescriptive Analytics focuses on decision optimization, advising decision makers on 'What should we do?'"
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "An airline uses an algorithm that continuously adjusts seat prices across flight routes to maximize total flight revenue subject to seat capacity. This is an example of:",
        "correct": "Prescriptive Analytics, utilizing mathematical optimization to identify the best action",
        "distractors": [
            "Descriptive Analytics, reporting how many passengers flew on yesterday's morning flights",
            "Diagnostic Analytics, investigating why flight 402 experienced a two-hour gate delay",
            "Predictive Analytics, merely predicting the total number of travelers flying next summer"
        ],
        "explanation": "Dynamic pricing algorithms evaluate trade-offs and select price points to optimize an objective (revenue), which is Prescriptive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following methods is a cornerstone of Prescriptive Analytics rather than Predictive Analytics?",
        "correct": "Linear programming optimization, constraint satisfaction, and decision rule simulation",
        "distractors": [
            "Time-series autoregressive integrated moving average (ARIMA) forecasting",
            "Logistic regression modeling to estimate binary customer churn probabilities",
            "Unsupervised k-means clustering to segment existing retail loyalty shoppers"
        ],
        "explanation": "Optimization modeling (such as linear programming) and simulation evaluate potential choices to prescribe the best course of action."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Rank the four types of analytics in order of increasing analytical complexity and business value added:",
        "correct": "Descriptive -> Diagnostic -> Predictive -> Prescriptive",
        "distractors": [
            "Predictive -> Descriptive -> Prescriptive -> Diagnostic",
            "Descriptive -> Predictive -> Diagnostic -> Prescriptive",
            "Prescriptive -> Predictive -> Diagnostic -> Descriptive"
        ],
        "explanation": "The standard maturity framework ascends from Descriptive (hindsight) to Diagnostic (insight), Predictive (foresight), and Prescriptive (optimization)."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A hotel chain analyzes reviews and discovers that negative ratings spiked in July due to air conditioning breakdowns in Tower B. This finding belongs to:",
        "correct": "Diagnostic Analytics, identifying the underlying cause of customer dissatisfaction",
        "distractors": [
            "Descriptive Analytics, counting the total number of guest reservations in July",
            "Predictive Analytics, forecasting the total electricity usage of Tower B in December",
            "Prescriptive Analytics, automatically purchasing brand-new HVAC units for all hotels"
        ],
        "explanation": "Identifying that air conditioning failures caused negative review spikes answers 'Why did it happen?', which is Diagnostic Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A ride-sharing platform dynamically dispatches idle drivers to zones where passenger demand is predicted to surge within 15 minutes. This system combines:",
        "correct": "Predictive Analytics (demand surge estimation) with Prescriptive Analytics (optimal driver dispatching)",
        "distractors": [
            "Descriptive Analytics (driver log archiving) with Diagnostic Analytics (investigating fare disputes)",
            "Diagnostic Analytics (root cause of traffic) with Descriptive Analytics (aggregating total mileage)",
            "Manual data entry (paper logs) with retrospective historical financial auditing (tax calculation)"
        ],
        "explanation": "Forecasting surge areas uses predictive analytics, while the automated dispatch optimization represents prescriptive analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following is a major limitation of relying exclusively on Descriptive Analytics?",
        "correct": "It describes historical outcomes but cannot explain root causes or forecast future performance",
        "distractors": [
            "It requires high-performance parallel computing clusters to process tabular datasets",
            "It produces summary tables that violate standard corporate accounting auditing procedures",
            "It automatically executes unverified algorithmic changes to live customer production records"
        ],
        "explanation": "Descriptive analytics shows what occurred in the past, but leaves decision makers blind to why it occurred or what will happen next."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A hospital analyst builds a model forecasting patient bed occupancy for the upcoming influenza season. Which type of analytics is being employed?",
        "correct": "Predictive Analytics, assessing future patient volume based on seasonal patterns",
        "distractors": [
            "Descriptive Analytics, calculating the total number of hospital beds in the facility",
            "Diagnostic Analytics, identifying which strain of influenza infected patient #104",
            "Prescriptive Analytics, permanently revoking nursing staff vacation permissions"
        ],
        "explanation": "Forecasting future bed demand based on seasonal epidemiological trends is Predictive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A supply chain manager uses an algorithm that determines the exact inventory reorder quantities that minimize holding costs while maintaining a 99% service level. This is:",
        "correct": "Prescriptive Analytics, optimizing inventory levels subject to service constraints",
        "distractors": [
            "Descriptive Analytics, tallying the current stock on hand in the regional warehouse",
            "Diagnostic Analytics, finding out why a specific forklift broke down last Tuesday",
            "Predictive Analytics, calculating the probability of a hurricane hitting the factory"
        ],
        "explanation": "Optimizing a mathematical objective (minimizing holding cost) subject to constraints (service level) is Prescriptive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following scenarios represents Diagnostic Analytics?",
        "correct": "Analyzing customer exit surveys to explain why churn increased following a price hike",
        "distractors": [
            "Publishing the annual audited profit and loss statement on the company investor portal",
            "Projecting next quarter's revenue based on macroeconomic consumer confidence trends",
            "Using integer programming to assign call center staff to shifts at minimum labor cost"
        ],
        "explanation": "Analyzing exit surveys to uncover the root cause behind churn is Diagnostic Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following scenarios represents Descriptive Analytics?",
        "correct": "Generating an end-of-month summary report of total store sales and customer foot traffic",
        "distractors": [
            "Simulating the impact of a 5% price reduction on competitor market share response",
            "Building an artificial neural network to identify fraudulent credit card charges in real time",
            "Using automated solvers to determine the optimal delivery route for forty couriers"
        ],
        "explanation": "Generating monthly summary reports of sales and traffic is classic Descriptive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Why is Prescriptive Analytics considered the most complex and actionable tier in the analytics hierarchy?",
        "correct": "It requires integrating predictive models, business constraints, and mathematical optimization algorithms",
        "distractors": [
            "It cannot be processed using electronic computers and must be calculated using manual pencil proofs",
            "It requires data scientists to hold active government regulatory clearances before training models",
            "It depends on collecting complete, exhaustive datasets spanning every global competitor in the sector"
        ],
        "explanation": "Prescriptive analytics combines predictions, constraints, objective functions, and optimization to guide or automate decisions, making it the most complex."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A retail bank notices that debit card fraud surged on Saturday. Analysts isolate the fraud to transactions processed at gas pumps in District 4. This isolation represents:",
        "correct": "Diagnostic Analytics, pinpointing the geographical and terminal source of the anomaly",
        "distractors": [
            "Predictive Analytics, predicting which gas station will open next year in District 4",
            "Prescriptive Analytics, permanently closing all bank branches across the entire state",
            "Descriptive Analytics, calculating the bank's annual return on equity for shareholders"
        ],
        "explanation": "Pinpointing where and why the fraud surge occurred is Diagnostic Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "An algorithm flags a mortgage applicant as having an 82% likelihood of prepayment within 36 months. This output represents:",
        "correct": "A Predictive Analytics output, providing a probabilistic assessment of customer behavior",
        "distractors": [
            "A Prescriptive Analytics output, legally prohibiting the borrower from refinancing",
            "A Descriptive Analytics output, reporting the exact interest rate on the loan note",
            "A Diagnostic Analytics output, explaining why the borrower lost their previous job"
        ],
        "explanation": "Estimating the future probability of mortgage prepayment is Predictive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "When an analyst utilizes simulation models to evaluate how different advertising budget allocations affect market share under competitor counter-attacks, they are performing:",
        "correct": "Prescriptive Analytics, testing decision policies to identify the superior strategic choice",
        "distractors": [
            "Descriptive Analytics, merely cataloging past media invoices paid to television networks",
            "Diagnostic Analytics, identifying which graphic designer created an ineffective print flyer",
            "Unconditioned raw data capture, storing digital audio files from focus group sessions"
        ],
        "explanation": "Simulating decision alternatives and competitive responses to choose the best strategy is Prescriptive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following is NOT a typical output of Descriptive Analytics?",
        "correct": "An automated recommendation on the exact price discount that maximizes customer renewals",
        "distractors": [
            "A monthly sales summary table broken down by geographical sales territory",
            "A bar chart comparing quarterly operating expenses against annual corporate budgets",
            "A metric card displaying the average customer wait time in minutes at call centers"
        ],
        "explanation": "Recommending an optimal price discount to maximize renewals is Prescriptive Analytics, not Descriptive."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "A fleet management system predicts that truck tire blowouts increase significantly when road temperatures exceed 40°C. It therefore instructs drivers to take mandatory cooling stops. This workflow demonstrates:",
        "correct": "Predictive insights directly powering an operational prescriptive policy",
        "distractors": [
            "A regression model failing to satisfy minimum statistical degrees of freedom",
            "Pure descriptive reporting with zero impact on real-world vehicle operations",
            "An unconditioned data pipeline causing network hardware failures across the fleet"
        ],
        "explanation": "Predicting tire failure risk under heat (predictive) combined with mandatory stops (prescriptive policy) illustrates analytics driving action."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "What primary risk occurs when an organization implements Prescriptive Analytics without thoroughly validating the underlying Predictive models?",
        "correct": "The optimization engine may prescribe highly confident actions based on fundamentally flawed forecasts",
        "distractors": [
            "The corporate database management system will immediately lose its primary key constraints",
            "Enterprise data analysts will be stripped of their academic university degrees and credentials",
            "Distributed cloud servers will experience complete electrical hardware burnout across data centers"
        ],
        "explanation": "Prescriptive optimization depends on accurate predictive inputs; optimizing decisions on false predictions yields disastrously bad decisions."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "An analyst conducts a cohort retention analysis across twelve customer onboarding groups to determine which onboarding step reduces early churn. This work is:",
        "correct": "Diagnostic Analytics, investigating the factors driving retention differences among cohorts",
        "distractors": [
            "Descriptive Analytics, stating the total number of registered user accounts in the database",
            "Predictive Analytics, building a deep reinforcement learning agent to write website copy",
            "Prescriptive Analytics, shutting down all marketing channels that yield non-English users"
        ],
        "explanation": "Cohort analysis investigating factors that drive retention differences is Diagnostic Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which question best illustrates Predictive Analytics in a retail banking context?",
        "correct": "'Which personal loan customers are most likely to miss their next payment installment?'",
        "distractors": [
            "'How many checking accounts were opened at our downtown branch during September?'",
            "'Why did our mobile banking app crash during the morning payroll direct deposit window?'",
            "'What is the optimal branch staffing schedule that minimizes teller idle labor hours?'"
        ],
        "explanation": "Predicting which customers will miss their next installment assesses future likelihoods (Predictive)."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which question best illustrates Prescriptive Analytics in an e-commerce context?",
        "correct": "'What personalized coupon amount should be offered to maximize margin without losing the sale?'",
        "distractors": [
            "'How many visitors clicked on our seasonal holiday promotional banner last week?'",
            "'Why did cart abandonment rates increase by 8% following the payment gateway update?'",
            "'What will our total gross merchandise value be during next year's Black Friday event?'"
        ],
        "explanation": "Determining the specific coupon amount to maximize margin subject to conversion is Prescriptive Analytics."
    },
    {
        "topic": "The Four Types of Analytics",
        "question": "Which of the following statements about the four types of analytics is accurate?",
        "correct": "Each stage builds upon the data foundations, insights, and outputs established in preceding tiers",
        "distractors": [
            "Organizations should bypass descriptive analytics entirely and implement prescriptive models first",
            "Predictive models are only capable of processing qualitative textual interview transcripts",
            "Diagnostic analytics cannot be performed unless a company has already hired fifty data scientists"
        ],
        "explanation": "Mature analytics capabilities build sequentially: solid descriptive reporting feeds diagnostic discovery, which enables predictive modeling and prescriptive optimization."
    },

    # --- 1.4 Business Questions vs. Analytical Questions, Roles & Skills ---
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "What is the primary difference between a Business Question and an Analytical Question?",
        "correct": "Business questions are phrased in commercial terms; analytical questions decompose them into quantifiable, testable inquiries",
        "distractors": [
            "Business questions evaluate database server memory; analytical questions focus on software copyright legal filings",
            "Business questions are answered using Python scripts; analytical questions are solved exclusively with desktop calculators",
            "Business questions are posed only by external tax auditors; analytical questions are asked by administrative receptionists"
        ],
        "explanation": "Business questions reflect strategic concerns ('Why are profits down?'), while analytical questions translate them into measurable hypotheses and variables."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "A CEO asks: 'Why are our profit margins shrinking?' Which of the following represents an appropriate decomposition into an Analytical Question?",
        "correct": "'How have unit production costs and product price discounting changed across each product line over the past four quarters?'",
        "distractors": [
            "'Why do regional retail consumers express dissatisfaction with our corporate brand aesthetic on digital discussion forums?'",
            "'Should executive management terminate thirty percent of operational staff to reduce fixed administrative payroll expenses?'",
            "'Can the enterprise migrate its primary email communication servers to an offshore cloud hosting infrastructure provider?'"
        ],
        "explanation": "Decomposing the business problem into specific metrics (unit production costs, price discounting by product line) creates testable analytical questions."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "What common trap occurs when an inexperienced analyst receives a vague business question from management?",
        "correct": "Jumping directly into software tools to query data before clearly framing and defining the analytical questions",
        "distractors": [
            "Demanding that all enterprise team members complete advanced academic graduate degrees in theoretical statistics",
            "Dropping all foreign key constraints from the relational data warehouse to speed up tabular analytical joins",
            "Refusing to utilize electronic computers and insisting on running all company financial ledgers by hand"
        ],
        "explanation": "The primary trap is diving into tools and coding without properly decomposing the business problem into well-defined analytical questions."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "Which analytics role is primarily responsible for designing semantic layers, building interactive executive dashboards (Power BI/Tableau), and tracking corporate KPIs?",
        "correct": "Business Intelligence (BI) Analyst, focusing on dimensional data modeling and reporting dashboards",
        "distractors": [
            "Data Engineer, focusing on tuning distributed data extraction scripts and managing data pipelines",
            "Database Administrator (DBA), focusing on server storage allocations and database security patching",
            "Product Analyst, focusing exclusively on digital user interface clickstream event telemetry"
        ],
        "explanation": "BI Analysts specialize in dimensional modeling, semantic layers, enterprise KPIs, and interactive reporting dashboards."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "Which role primarily applies advanced mathematical statistics, machine learning algorithms, and predictive modeling using Python or R?",
        "correct": "Data Scientist, focusing on complex predictive models, statistical inference, and algorithm development",
        "distractors": [
            "Business User, focusing on daily operational tasks, workflow execution, and domain consulting",
            "Project Sponsor, focusing on high-level executive financing, stakeholder management, and project ROI",
            "Data Analyst, focusing primarily on descriptive reporting, basic SQL queries, and spreadsheet summaries"
        ],
        "explanation": "Data Scientists specialize in advanced statistics, feature engineering, machine learning algorithms, and custom predictive modeling."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "In the core competency matrix for analytics professionals, what does 'Data Literacy' specifically denote?",
        "correct": "The ability to critically read, interpret, communicate with data, and evaluate its quality and limitations",
        "distractors": [
            "The typing speed at which a programmer can manually write SQL queries into a terminal window",
            "The ability to memorize the binary ASCII representations of alphanumeric database character sets",
            "Holding an active government legal certification to audit commercial corporate balance sheets"
        ],
        "explanation": "Data Literacy is the ability to read, work with, analyze, and argue with data, including understanding data provenance, quality, and limitations."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "Which role primarily focuses on digital product funnels, feature adoption, user onboarding drop-off, and A/B testing experiment telemetry?",
        "correct": "Product Analyst, evaluating user experience journeys and digital engagement metrics",
        "distractors": [
            "Database Administrator (DBA), managing physical server rack cooling and backup tape archives",
            "Data Engineer, tuning distributed MapReduce batch scripts for enterprise data warehouses",
            "Project Sponsor, providing high-level executive financing and quarterly investor briefings"
        ],
        "explanation": "Product Analysts specialize in understanding digital user interactions, feature adoption funnels, and experimental A/B testing data."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "A retail marketing director asks: 'How can we increase customer loyalty?' Which analytical decomposition provides the most actionable investigation?",
        "correct": "'What are the retention rates and repeat purchase frequencies of loyalty members compared to non-members across customer segments?'",
        "distractors": [
            "'Why do customers choose competitors who have brighter store lighting and friendlier cashier staff members?'",
            "'Should we completely eliminate all cash registers and force customers to use mobile self-checkout kiosks?'",
            "'Can our software engineers redesign our website to look identical to our largest competitor's mobile application?'"
        ],
        "explanation": "Translating a broad loyalty goal into measurable metrics (retention rates, repeat purchase frequency across member segments) forms a rigorous analytical question."
    },
    {
        "topic": "Translating Questions & Analytics Roles",
        "question": "Which core competency pillar ensures that an analytics professional can contextualize findings within corporate profit drivers and industry KPIs?",
        "correct": "Business Acumen, enabling analysts to align technical discoveries with commercial strategic priorities",
        "distractors": [
            "Data Literacy, which focuses exclusively on understanding relational foreign key constraint rules",
            "Technical Expertise, ensuring that developers write Python scripts with optimal cyclomatic complexity",
            "Communication Skills, limited strictly to formatting visual typography and color palettes on slide decks"
        ],
        "explanation": "Business Acumen is the domain knowledge and commercial understanding required to connect data insights to corporate strategy, profit drivers, and operational KPIs."
    }
]
