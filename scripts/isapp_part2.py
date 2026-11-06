# scripts/isapp_part2.py
# 50 Rigorous, Medium-Difficulty Questions for Lecture 1 (Part 2):
# CS vs IT vs IS, Major Types of IS Overview, Industry Applications & Emerging Tech, University Case Study

part2_questions = [
    # --- 2.1 Distinguishing Computer Science, IT, and IS (Q51 - Q60) ---
    {
        "topic": "CS vs. IT vs. IS",
        "question": "Which of the following best delineates the primary academic and professional focus of Computer Science (CS)?",
        "correct": "Theoretical computation foundations, mathematical algorithms, programming languages, and software development",
        "distractors": [
            "Configuring enterprise local area network cables, managing firewalls, and troubleshooting office PC hardware",
            "Integrating business processes, people, and technology to optimize strategic decision-making in corporations",
            "Managing corporate marketing campaigns and administering quarterly financial payroll compliance audits"
        ],
        "explanation": "Computer Science focuses on the mathematical and theoretical foundations of computation, algorithms, compiler design, and software engineering."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "A team of engineers is tasked with installing network switches, setting up firewalls, and configuring cloud storage servers for an office. This work falls primarily under:",
        "correct": "Information Technology (IT)",
        "distractors": [
            "Computer Science (CS)",
            "Information Systems (IS)",
            "Strategic Management"
        ],
        "explanation": "Information Technology (IT) centers on deploying, configuring, maintaining, and supporting hardware, networking infrastructure, and telecommunications."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "What is the defining distinction of Information Systems (IS) when compared to Computer Science and Information Technology?",
        "correct": "IS focuses on applying technology within organizations to solve business problems and support workflows",
        "distractors": [
            "IS focuses exclusively on designing silicon microprocessor architectures and circuit board physics",
            "IS concentrates purely on proving mathematical computational complexity theorems and formal logic",
            "IS is restricted to assembling consumer desktop computer hardware components in manufacturing plants"
        ],
        "explanation": "Information Systems bridges technology, people, data, and business processes to satisfy organizational needs and achieve business objectives."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "An enterprise plans a digital transformation to streamline customer order fulfillment across departments. Which professional is most directly prepared to lead the redesign of these organizational workflows?",
        "correct": "An Information Systems specialist, because they understand business processes alongside technological capabilities",
        "distractors": [
            "A Computer Science algorithmic theorist, because they analyze asymptotic Big-O runtime boundaries",
            "An IT hardware technician, because they specialize in crimping RJ-45 Ethernet cables and installing racks",
            "A hardware design engineer, because they focus on fabricating semiconductor silicon wafer substrates"
        ],
        "explanation": "IS professionals specialize in socio-technical systems, analyzing business workflows, information needs, and organizational processes to deploy effective digital solutions."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "Which of the following professional activities is an example of Computer Science rather than Information Systems?",
        "correct": "Developing a novel mathematical algorithm that reduces graph-traversal time complexity from O(n^2) to O(n log n)",
        "distractors": [
            "Analyzing how a hospital can streamline clinical workflows by deploying an integrated patient electronic chart",
            "Configuring an enterprise ERP system to share real-time sales data between marketing and production departments",
            "Conducting user interviews with bank branch managers to define reporting requirements for a new loan approval portal"
        ],
        "explanation": "Inventing mathematical algorithms and analyzing computational complexity is core Computer Science; analyzing and deploying organizational solutions belongs to IS."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "Which of the following scenarios best reflects the domain of Information Technology (IT)?",
        "correct": "Administering server operating systems, maintaining fiber-optic connectivity, and applying security patches",
        "distractors": [
            "Proving that a cryptographic hashing function is NP-complete using mathematical induction and proofs",
            "Redesigning a retail bank's mortgage application workflow to reduce loan approval cycle times by 40%",
            "Developing corporate strategic goals to achieve market differentiation through customer loyalty data"
        ],
        "explanation": "Administering operating systems, hardware, networks, and applying patches are core operational responsibilities of Information Technology (IT)."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "Why would an organization hire an Information Systems graduate instead of a pure Computer Science graduate for a Business Analyst role?",
        "correct": "The IS graduate possesses training in business functions, organizational strategy, and process modeling alongside technical skills",
        "distractors": [
            "The IS graduate requires zero salary compensation during their first five years of professional employment",
            "The CS graduate is legally prohibited from reading corporate balance sheets or attending departmental meetings",
            "The IS graduate specializes exclusively in physical computer motherboard assembly and hardware repair"
        ],
        "explanation": "IS graduates are trained at the intersection of business management and technology, making them uniquely equipped to analyze business processes and user needs."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "How do Computer Science, Information Technology, and Information Systems collaborate in launching an enterprise mobile banking app?",
        "correct": "CS developers code the underlying encryption algorithms; IT engineers secure the server hosting infrastructure; IS analysts design the user workflows and business logic",
        "distractors": [
            "CS engineers assemble the physical server cases; IT analysts code the encryption math; IS specialists manage the bank's stock portfolio",
            "IS analysts write compiler binaries; CS developers configure network cables; IT administrators handle customer loan underwriting",
            "CS theorists manage human resources; IT specialists audit accounting ledgers; IS developers manufacture touchscreen glass"
        ],
        "explanation": "CS contributes core algorithms and software architecture; IT provides and secures the operating and network infrastructure; IS aligns the system with business workflows and user needs."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "Which of the following is NOT typically a primary focus of an Information Systems (IS) curriculum or career?",
        "correct": "Designing microarchitecture logic gates and semiconductor fabrication etching processes",
        "distractors": [
            "Aligning enterprise information technology investments with competitive business strategy",
            "Designing relational database schemas to model complex enterprise transactional workflows",
            "Managing enterprise system implementations, organizational change, and user training programs"
        ],
        "explanation": "Microarchitecture and semiconductor fabrication belong to Computer Engineering and Applied Physics, whereas IS focuses on organizational technology use."
    },
    {
        "topic": "CS vs. IT vs. IS",
        "question": "Which statement correctly summarizes the primary difference in perspective between IT and IS?",
        "correct": "IT focuses on the technological infrastructure itself, while IS focuses on how that infrastructure serves organizational objectives",
        "distractors": [
            "IT focuses entirely on human social interactions, while IS focuses exclusively on computer microchip architecture",
            "IT is an academic branch of sociology, while IS is an industrial branch of mechanical robotics engineering",
            "IT deals exclusively with historical paper records, while IS deals exclusively with future artificial intelligence"
        ],
        "explanation": "IT provides the technological tools, network pipes, and hardware platforms; IS focuses on utilizing those tools to solve organizational problems and achieve business goals."
    },

    # --- 2.2 Major Types of IS Overview (Q61 - Q75) ---
    {
        "topic": "Major Types of IS",
        "question": "What is the primary role of a Transaction Processing System (TPS) in an enterprise?",
        "correct": "To capture, process, and record routine, day-to-day operational business transactions with high accuracy",
        "distractors": [
            "To simulate 10-year macroeconomic scenarios for board-of-director executive retreats",
            "To provide interactive mathematical modeling tools for senior financial investment managers",
            "To publish weekly marketing advertisements and public relations statements across social media"
        ],
        "explanation": "A TPS is the foundational operational system that records daily routine events—such as point-of-sale transactions, bank deposits, and order bookings."
    },
    {
        "topic": "Major Types of IS",
        "question": "Which of the following systems is designed primarily to provide scheduled summary reports and exception reports for middle management?",
        "correct": "Management Information Systems (MIS)",
        "distractors": [
            "Transaction Processing Systems (TPS)",
            "Executive Support Systems (ESS)",
            "Electronic Data Interchanges (EDI)"
        ],
        "explanation": "Management Information Systems (MIS) extract data from TPS to produce standardized, periodic reports that help middle managers monitor and control operations."
    },
    {
        "topic": "Major Types of IS",
        "question": "A financial analyst is evaluating three alternative factory expansion locations by testing various interest rates and construction cost models. Which system is being used?",
        "correct": "Decision Support System (DSS)",
        "distractors": [
            "Transaction Processing System (TPS)",
            "Customer Billing System (CBS)",
            "Barcode Scanning Terminal (BST)"
        ],
        "explanation": "Decision Support Systems (DSS) provide interactive mathematical models and What-If analysis to assist managers in evaluating alternatives and semi-structured dilemmas."
    },
    {
        "topic": "Major Types of IS",
        "question": "Which type of Information System specifically serves senior corporate executives by providing graphical dashboards and external market intelligence?",
        "correct": "Executive Information / Support System (EIS / ESS)",
        "distractors": [
            "Transaction Processing System (TPS)",
            "Factory Floor Data Collector (FDC)",
            "Point-of-Sale Terminal Scanner (POS)"
        ],
        "explanation": "EIS/ESS is tailored for top executives, featuring easy-to-read graphical dashboards, high-level KPIs, competitive intelligence, and drill-down capabilities."
    },
    {
        "topic": "Major Types of IS",
        "question": "How do Transaction Processing Systems (TPS) directly support Management Information Systems (MIS)?",
        "correct": "TPS captures and stores granular operational data, which serves as the primary data input for MIS summary reports",
        "distractors": [
            "TPS formulates five-year strategic market expansion goals that MIS middle managers execute daily",
            "TPS replaces the MIS database by archiving all historical enterprise records onto offline paper tape",
            "TPS operates independently of MIS and never shares transactional records across enterprise departments"
        ],
        "explanation": "TPS acts as the vital data wellspring for an enterprise; MIS queries the operational records generated by TPS to produce aggregated managerial reports."
    },
    {
        "topic": "Major Types of IS",
        "question": "An automated teller machine (ATM) allowing a customer to withdraw cash and instantly updating their checking account balance is a classic example of:",
        "correct": "A Transaction Processing System (TPS)",
        "distractors": [
            "A Decision Support System (DSS)",
            "An Executive Support System (ESS)",
            "A Strategic Management System (SMS)"
        ],
        "explanation": "An ATM is a classic operational TPS: it executes a structured, high-volume, real-time transaction requiring strict data consistency and atomicity."
    },
    {
        "topic": "Major Types of IS",
        "question": "A regional sales manager receives a report every Monday morning showing sales reps whose revenue fell 20% below target. This type of report is known as:",
        "correct": "An exception report generated by a Management Information System (MIS)",
        "distractors": [
            "A raw unstructured data dump produced by an uncalibrated point-of-sale scanner",
            "A long-term strategic forecast generated by an Executive Support System (ESS)",
            "A real-time network protocol analyzer trace produced by enterprise firewall software"
        ],
        "explanation": "Exception reports highlight conditions that deviate from predefined standards or thresholds (e.g., sales falling 20% below target), allowing middle managers to take action."
    },
    {
        "topic": "Major Types of IS",
        "question": "What is the primary purpose of 'What-If Analysis' in a Decision Support System (DSS)?",
        "correct": "To observe how changes in input variables (e.g., price or interest rates) impact calculated outcomes",
        "distractors": [
            "To identify and delete duplicate customer records from the core transactional relational database",
            "To capture raw optical barcode data from warehouse inventory pallets during physical receiving",
            "To prevent unauthorized end users from accessing the corporate internal local area network"
        ],
        "explanation": "What-If Analysis is an interactive DSS capability that allows decision-makers to test alternative scenarios and observe the mathematical consequences of changing parameters."
    },
    {
        "topic": "Major Types of IS",
        "question": "Which capability of an Executive Information System (EIS) allows a CEO to click a summarized regional revenue chart to inspect individual store sales?",
        "correct": "Drill-down capability",
        "distractors": [
            "Transaction logging",
            "Data encryption",
            "Batch compilation"
        ],
        "explanation": "Drill-down allows an executive to navigate from high-level summarized KPIs down into progressively more detailed underlying operational layers."
    },
    {
        "topic": "Major Types of IS",
        "question": "Which of the following is NOT a typical characteristic of a Transaction Processing System (TPS)?",
        "correct": "Extensive use of statistical simulation models and unstructured scenario forecasting",
        "distractors": [
            "High transaction throughput and rapid processing of daily operational activities",
            "Strict adherence to predefined business rules and highly structured transactional inputs",
            "Detailed operational outputs such as customer receipts, invoices, and shipping labels"
        ],
        "explanation": "Simulation models and unstructured scenario forecasting belong to DSS and EIS/ESS, not operational TPS."
    },
    {
        "topic": "Major Types of IS",
        "question": "What is the defining purpose of an Enterprise Information System (such as an ERP system)?",
        "correct": "To integrate core business processes across multiple functional areas into a single unified system",
        "distractors": [
            "To run isolated personal spreadsheet applications on individual employee desktop machines",
            "To restrict communication between sales and manufacturing to prevent corporate espionage",
            "To manage the physical cooling systems and diesel backup generators in enterprise data centers"
        ],
        "explanation": "Enterprise Information Systems (like ERP) break down departmental silos by connecting disparate business processes across marketing, finance, HR, and operations."
    },
    {
        "topic": "Major Types of IS",
        "question": "A hospital uses a specialized system that inputs patient symptoms, lab results, and medical history to recommend optimal antibiotic dosages. This system is best categorized as:",
        "correct": "A Decision Support System (DSS)",
        "distractors": [
            "A Point-of-Sale System (POS)",
            "A Transaction Processing System (TPS)",
            "An Executive Support System (ESS)"
        ],
        "explanation": "Systems that combine data and analytical models to assist professional decision-makers in evaluating alternatives are Decision Support Systems."
    },
    {
        "topic": "Major Types of IS",
        "question": "Which of the following best contrasts the time horizons of a TPS versus an EIS/ESS?",
        "correct": "TPS focuses on immediate, day-to-day transactions; EIS/ESS focuses on multi-year strategic trends",
        "distractors": [
            "TPS focuses on ten-year macroeconomic forecasts; EIS/ESS focuses on hourly checkout scanner logs",
            "TPS and EIS/ESS both focus exclusively on quarterly departmental budget variance reconciliation",
            "TPS operates without any time horizon, while EIS/ESS records transactions strictly in real-time nanoseconds"
        ],
        "explanation": "TPS operates in the present, handling hourly and daily operational events; EIS/ESS focuses on long-range strategic horizons spanning quarters and years."
    },
    {
        "topic": "Major Types of IS",
        "question": "Which type of system relies most heavily on external data sources such as competitor filings, industry benchmarks, and macroeconomic indicators?",
        "correct": "Executive Information / Support System (EIS / ESS)",
        "distractors": [
            "Transaction Processing System (TPS)",
            "Shop Floor Machine Controller (SMC)",
            "Automated Cash Register System (ACR)"
        ],
        "explanation": "Top executives using EIS/ESS require broad environmental scanning data—including macroeconomic trends, competitor actions, and regulatory news—alongside internal KPIs."
    },
    {
        "topic": "Major Types of IS",
        "question": "If an organization's TPS suffers a catastrophic failure and stops recording sales, how does this directly impact the rest of the enterprise systems hierarchy?",
        "correct": "MIS and DSS cannot generate accurate reports or models because their underlying data source is missing",
        "distractors": [
            "EIS/ESS automatically generates valid financial revenues through mathematical simulation formulas",
            "Departmental managers can still make perfect operational decisions because MIS operates without data",
            "The failure has zero impact because enterprise systems operate in complete analytical isolation"
        ],
        "explanation": "TPS is the foundational layer of organizational data. If it fails, upstream systems (MIS, DSS, EIS) are starved of accurate operational inputs."
    },

    # --- 2.3 Industry Applications & Emerging Technologies (Q76 - Q90) ---
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "In the banking industry, which Information System application enables financial institutions to detect fraudulent credit card transactions in real time?",
        "correct": "Machine learning algorithms that analyze transaction patterns against known baseline user behavior",
        "distractors": [
            "Batch printing of weekly paper account balance ledgers for manual postal mail distribution",
            "Physical microfilming of monthly paper customer deposit slips inside bank vault basements",
            "Manual phone calls placed by branch tellers to cardholders after every credit card swipe"
        ],
        "explanation": "Modern banks use AI and machine learning to analyze transaction attributes (location, amount, velocity) in milliseconds to detect and block fraud."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "What is the primary benefit of deploying Cloud Computing for enterprise Information Systems?",
        "correct": "Providing scalable, on-demand computing resources without the need for heavy initial on-premises hardware expenditure",
        "distractors": [
            "Eliminating the need for software programming by using physical atmospheric weather satellites",
            "Guaranteeing that enterprise data is permanently immune to unauthorized access without encryption",
            "Restricting system usage to employees who physically work inside the corporate headquarters"
        ],
        "explanation": "Cloud computing offers scalable, on-demand access to servers, storage, and applications (IaaS, PaaS, SaaS) with lower upfront capital expenditure."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "A modern hospital implements Electronic Health Record (EHR) systems. What is a primary clinical benefit delivered by this IS application?",
        "correct": "Ensuring instantaneous access to patient medical histories and reducing adverse medication conflicts",
        "distractors": [
            "Eliminating the need for licensed doctors and nurses by performing surgeries algorithmically",
            "Converting all surgical wards into automated semiconductor cleanrooms for chip fabrication",
            "Preventing clinical lab results from being shared between different hospital departments"
        ],
        "explanation": "EHR systems provide instant, secure access to comprehensive patient records, drastically cutting medical errors and dangerous drug-drug interactions."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "Which emerging technology integrates physical connected sensors to monitor warehouse temperatures and vehicle fleet locations in real time?",
        "correct": "Internet of Things (IoT)",
        "distractors": [
            "Compiler Optimization",
            "Desktop Publishing",
            "Relational Calculus"
        ],
        "explanation": "The Internet of Things (IoT) connects physical devices—sensors, RFID tags, vehicles—to digital networks to stream telemetry data directly into enterprise IS."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "How does Big Data Analytics provide strategic value to modern e-commerce retailers?",
        "correct": "By processing high-volume, high-velocity customer browsing streams to generate real-time personalized recommendations",
        "distractors": [
            "By physically delivering packages to consumer doorsteps using telepathic transmission protocols",
            "By replacing all digital web shopping carts with printed mail-order product catalogs",
            "By deleting historical customer order data every 24 hours to minimize disk storage requirements"
        ],
        "explanation": "Big Data Analytics enables retailers to analyze vast, rapid streams of clickstream and purchasing data to personalize recommendations and optimize dynamic pricing."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "What is the key technological capability that Blockchain introduces to supply chain Information Systems?",
        "correct": "A decentralized, cryptographically secure, and tamper-evident ledger for recording provenance and transactions",
        "distractors": [
            "A high-speed laser printer capable of generating millions of physical paper shipping manifests",
            "A physical conveyor belt mechanism used to sort heavy shipping containers in container ports",
            "An algorithm that allows any unauthorized third party to rewrite past historical accounting ledgers"
        ],
        "explanation": "Blockchain creates an immutable, shared distributed ledger, ensuring transparent and tamper-resistant tracking of goods and financial transactions across supply chains."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "Which of the following is NOT an emerging technology commonly integrated into modern enterprise Information Systems?",
        "correct": "Vacuum tube vacuum-state logic circuits for local memory storage",
        "distractors": [
            "Artificial Intelligence and Machine Learning for predictive forecasting",
            "Cloud Computing for elastic resource provisioning and SaaS delivery",
            "Internet of Things (IoT) sensors for continuous telemetry data capture"
        ],
        "explanation": "Vacuum tubes were first-generation 1950s computing hardware, obsolete for decades. AI, Cloud, and IoT are contemporary emerging technologies."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "How do government agencies utilize Information Systems to improve public service delivery?",
        "correct": "By offering digital citizen portals for license renewals, tax filings, and social service applications",
        "distractors": [
            "By requiring all citizens to physically visit regional agency offices for every routine transaction",
            "By keeping citizen demographic records exclusively in locked paper filing cabinets without indexing",
            "By eliminating computer networks across government agencies to avoid software update costs"
        ],
        "explanation": "E-government portals streamline public services, enabling citizens to renew licenses, file taxes, and access social benefits online with greater speed and lower overhead."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "In manufacturing, Computer-Integrated Manufacturing (CIM) and production IS primarily aim to:",
        "correct": "Coordinate product design, factory floor machinery, and raw material replenishment seamlessly",
        "distractors": [
            "Replace human industrial managers with speculative foreign currency investment bots",
            "Eliminate all quality control standards to accelerate daily factory production quotas",
            "Isolate assembly line machines from inventory data to prevent network congestion"
        ],
        "explanation": "CIM coordinates design, production scheduling, shop floor machinery, and material requirements planning into an integrated, efficient manufacturing workflow."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "What does 'SaaS' (Software as a Service) mean in the context of cloud-based enterprise Information Systems?",
        "correct": "Applications hosted centrally by a cloud vendor and accessed by clients over the internet via a web browser",
        "distractors": [
            "Custom-built computer motherboards sold to retail consumers for home computer assembly",
            "A legal contract requiring corporate employees to write their own operating system software",
            "An enterprise software package that functions only when completely disconnected from the internet"
        ],
        "explanation": "SaaS is a cloud model where the software application is hosted in the cloud and licensed on a subscription basis, accessed via web browsers without local installation."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "A global shipping company attaches GPS and temperature sensors to refrigerated cargo containers. If a container's temperature rises above safe levels, an alert is instantly sent to the ship engineer. This is an application of:",
        "correct": "Internet of Things (IoT) combined with real-time operational monitoring",
        "distractors": [
            "Batch transaction processing executed once at the end of each maritime voyage",
            "Computer Science theoretical algorithm design without physical hardware deployment",
            "Offline desktop spreadsheet calculation performed manually by harbor customs officers"
        ],
        "explanation": "IoT sensors stream real-time environmental data (GPS, temperature) to operational systems, enabling automated alerts and rapid preventive intervention."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "Why is Artificial Intelligence (AI) increasingly embedded inside modern Customer Relationship Management (CRM) systems?",
        "correct": "To predict customer churn, score sales leads, and provide automated conversational customer support",
        "distractors": [
            "To permanently delete customer contact records whenever client satisfaction drops below 50%",
            "To replace company executives by automatically issuing public corporate dividend distributions",
            "To ensure that marketing emails are sent only via traditional physical postal paper mail"
        ],
        "explanation": "AI inside CRM systems analyzes customer behaviors to forecast churn, rank leads by likelihood to convert, and power intelligent customer chatbots."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "What fundamental business benefit do enterprise Information Systems deliver regarding operational costs?",
        "correct": "They decrease operational costs by streamlining redundant workflows and eliminating paper-based manual tasks",
        "distractors": [
            "They permanently eliminate 100% of all future corporate capital and labor expenditures",
            "They double the number of clerical employees required to process each daily customer invoice",
            "They require organizations to purchase new physical server hardware every single calendar month"
        ],
        "explanation": "IS reduces operational costs by automating routine processes, eliminating clerical errors, lowering paper consumption, and accelerating transaction cycle times."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "In education, what is the primary role of a Student Information System (SIS)?",
        "correct": "To manage matriculation records, course registrations, academic transcripts, and tuition billing",
        "distractors": [
            "To physically clean university lecture halls and schedule maintenance for campus bus engines",
            "To design the architectural floorplans and oversee construction of new athletic stadiums",
            "To replace human professors by automating all university research publications algorithmically"
        ],
        "explanation": "An SIS manages the core operational data of an educational institution: admissions, class registration, student records, grades, transcripts, and billing."
    },
    {
        "topic": "IS Applications & Emerging Tech",
        "question": "Which characteristic best describes 'Big Data' in enterprise analytics?",
        "correct": "Data sets characterized by high volume, high velocity, and diverse variety that exceed traditional database tools",
        "distractors": [
            "Any single spreadsheet file that contains more than one hundred rows of numerical student grades",
            "A collection of paper documents stored in cardboard filing boxes inside a corporate archive warehouse",
            "Data that can only be processed on standalone mechanical calculators manufactured before 1970"
        ],
        "explanation": "Big Data is universally defined by the 3Vs: Volume (massive scale), Velocity (real-time generation speed), and Variety (structured, semi-structured, and unstructured data)."
    },

    # --- 2.4 Lec 1 Real-Life Case Study: University Information System (Q91 - Q100) ---
    {
        "topic": "University IS Case Study",
        "question": "In the University Information System case study from Lecture 1, which of the following is categorized as an 'Input'?",
        "correct": "Student personal details, selected course registrations, and submitted semester exam scores",
        "distractors": [
            "An official certified academic transcript presented to an employer after graduation",
            "The calculation of a student's cumulative Grade Point Average by the processing engine",
            "The final decision made by an academic dean to dismiss a student for poor scholarship"
        ],
        "explanation": "Inputs are the raw data entering the system: student demographic details, selected courses, and raw exam scores entered by instructors."
    },
    {
        "topic": "University IS Case Study",
        "question": "In the same university case study, which activity constitutes 'Processing'?",
        "correct": "Validating course prerequisites, verifying enrollment limits, and computing semester GPAs",
        "distractors": [
            "A student typing their matriculation identification password into the web login portal",
            "A printed physical diploma certificate awarded to a graduating senior at commencement",
            "A high-speed laser printer running out of toner paper inside the university registrar office"
        ],
        "explanation": "Processing involves the computational and logical transformation of inputs: checking prerequisites, enforcing seat caps, and calculating GPAs."
    },
    {
        "topic": "University IS Case Study",
        "question": "Which of the following constitutes an 'Output' in the University Information System?",
        "correct": "An official semester grade report, updated transcript, and registration confirmation notice",
        "distractors": [
            "The course syllabus drafted in a word processor by a professor prior to the semester",
            "The optical answer sheet filled out by a student using a graphite pencil during an exam",
            "The network switch connecting the engineering campus laboratory to the campus fiber loop"
        ],
        "explanation": "Outputs are the meaningful information products generated and disseminated by the system: transcripts, grade reports, and registration confirmations."
    },
    {
        "topic": "University IS Case Study",
        "question": "Who are identified as the primary 'Users' of a comprehensive University Information System?",
        "correct": "Students, instructors/professors, academic advisors, and administrative staff",
        "distractors": [
            "External consumer appliance manufacturers who purchase student browsing history",
            "Offshore computer motherboard fabricators who supply memory chips to campus labs",
            "Automated web crawler bots that scrape publicly listed campus telephone extensions"
        ],
        "explanation": "The core user groups of a university IS are internal academic stakeholders: students, faculty/instructors, academic advisors, and administrative staff."
    },
    {
        "topic": "University IS Case Study",
        "question": "A student attempts to register for 'Advanced Database Systems' but the system immediately blocks enrollment because 'Database Fundamentals' has not been completed. What is the system doing?",
        "correct": "Enforcing procedural business rules and prerequisite validation logic during data processing",
        "distractors": [
            "Experiencing a fatal hardware memory crash caused by excessive network bandwidth demand",
            "Violating academic regulations by refusing a paying customer's registration request",
            "Executing an uncalibrated executive support simulation regarding future campus tuition costs"
        ],
        "explanation": "The system applies predefined business rules (prerequisites) to validate transactions during processing, preserving academic policy."
    },
    {
        "topic": "University IS Case Study",
        "question": "When a professor submits course grades and the system recalculates class statistics and student GPAs, what role does the professor play in the IS operational model?",
        "correct": "A primary data input source capturing operational academic performance facts",
        "distractors": [
            "A hardware central processing unit executing binary floating-point calculations",
            "An external telecommunications carrier providing inter-campus fiber-optic connectivity",
            "A storage device physically archiving relational database blocks onto magnetic tapes"
        ],
        "explanation": "The instructor serves as the frontline human actor entering raw operational data (exam grades) into the system's input interface."
    },
    {
        "topic": "University IS Case Study",
        "question": "In a University Information System, which of the following best represents a 'Feedback' loop?",
        "correct": "An automated alert sent to an academic advisor when a student's GPA drops below 2.0, triggering an intervention",
        "distractors": [
            "A student logging out of the university web portal after checking their scheduled final exam dates",
            "A database backup job writing an exact copy of course catalog tables to an offsite cloud bucket",
            "A computer lab technician wiping keyboard surfaces with disinfectant spray between class sessions"
        ],
        "explanation": "Evaluating academic performance output against a standard (GPA < 2.0) and alerting an advisor to adjust the student's study plan is a textbook feedback loop."
    },
    {
        "topic": "University IS Case Study",
        "question": "How does the University Information System support administrative 'Control'?",
        "correct": "By verifying classroom seat capacity limits to prevent overcrowding and ensure safety compliance",
        "distractors": [
            "By physically dictating the lecture delivery pace and spoken vocabulary of classroom professors",
            "By permanently locking classroom doors whenever attendance falls below ninety-five percent",
            "By replacing human academic department chairs with automated curriculum revision algorithms"
        ],
        "explanation": "Controlling enrollment against room capacity constraints enforces organizational rules, safety standards, and resource allocations."
    },
    {
        "topic": "University IS Case Study",
        "question": "Which of the following represents an 'Organizational Procedure' within the University Information System?",
        "correct": "The sequence requiring students to log in, select courses, validate prerequisites, and settle tuition fees before enrollment",
        "distractors": [
            "The physical Cisco Wi-Fi router mounted to the ceiling of the campus library study hall",
            "The MySQL relational database software hosting student demographic and matriculation records",
            "The numeric grade '88' assigned to a student's midterm paper in Business Communication"
        ],
        "explanation": "The required, stepwise workflow (Login -> Select Courses -> Prerequisite Validation -> Fee Payment -> Confirmed Enrollment) is an organizational Procedure."
    },
    {
        "topic": "University IS Case Study",
        "question": "If a university's registration system allows 200 students to enroll in a 50-seat classroom, what system component most likely failed?",
        "correct": "The Software and Procedures components failed to validate seat constraints and enforce capacity limits",
        "distractors": [
            "The Physical Hardware component failed because computer monitors cannot render numbers above 50",
            "The Data component was corrupted because student identification numbers cannot contain digits",
            "The University President failed to personally inspect each student's enrollment ticket at the classroom door"
        ],
        "explanation": "Overbooking indicates that the software rules or business procedures governing class capacity validation were missing, incorrectly programmed, or bypassed."
    }
]
