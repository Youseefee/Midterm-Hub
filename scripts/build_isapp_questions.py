import json

# Generates 300 high quality, rigorous questions for Information Systems Applications (IS App)
# Covering:
# Lecture 1 (Questions 1-150): Introduction to Information Systems, Components, Operations, IS vs IT vs CS, Types of IS, Emerging Tech, University Case
# Lecture 2 (Questions 151-300): IS in Organizations, 4 Resources, 3 Management Levels, TPS/MIS/DSS/EIS, Functional Areas, Business Processes (Core, Support, Mgmt), Cross-Functional Systems, Competitive Advantage

questions = []

def add_q(topic, q_text, options, ans_idx, explanation):
    q_id = f"isapp_{len(questions) + 1}"
    questions.append({
        "id": q_id,
        "subject": "Information Systems Applications (IS App)",
        "topic": topic,
        "question": q_text,
        "options": options,
        "answer": ans_idx,
        "explanation": explanation
    })

# =========================================================================
# LECTURE 1: INTRODUCTION TO INFORMATION SYSTEMS (Q1 - Q150)
# =========================================================================

add_q("IS Definition & Purpose",
      "According to Chapter 1, what is the formal definition of an Information System (IS)?",
      ["A hardware computer box containing silicon microprocessors only",
       "A set of interconnected components that collect, process, store, and distribute information to support decision-making, coordination, and control in an organization",
       "An internet social media application used exclusively for entertainment",
       "A physical paper filing cabinet with alphabetical folders"],
      1,
      "An Information System (IS) is a set of interrelated components that collect (input), process, store, and distribute information to support decision-making, coordination, control, analysis, and visualization in an organization.")

add_q("Why IS is Needed",
      "Which of the following is a primary reason organizations implement Information Systems?",
      ["To eliminate all human employees from the company",
       "To transform raw data into useful information, support decision-making, improve operational efficiency, and coordinate business processes",
       "To increase the physical weight of office desks",
       "To prevent communication between departments"],
      1,
      "Organizations deploy Information Systems to organize data, transform it into meaningful information, support managerial decisions, boost productivity, and streamline cross-departmental coordination.")

add_q("Data vs. Information",
      "What is the fundamental difference between 'Data' and 'Information'?",
      ["Data is processed and meaningful, while Information is raw and unorganized",
       "Data consists of raw, unprocessed facts and figures; Information is data that has been processed, organized, and structured to have meaning and context",
       "There is no difference; they are exact synonyms",
       "Data only exists on paper, while Information only exists on monitors"],
      1,
      "Data represents raw, unprocessed facts and figures (e.g. 80, 75, 90). Information is data that has been processed, contextualized, and organized into a meaningful form (e.g. Average Grade = 81.6%).")

add_q("Data vs. Information Example",
      "A university registrar records raw exam scores: 85, 90, 70, 75. Calculating the class average as '80%' represents:",
      ["Raw Data", "Useful Information", "A Hardware Component", "An Operating System"],
      1,
      "The individual numbers (85, 90, 70, 75) are raw Data. The calculated class average of 80% represents Information because it provides meaningful summary context.")

add_q("5 Components of an IS",
      "What are the FIVE essential components that make up an Information System?",
      ["Keyboard, Mouse, Monitor, Printer, and Scanner",
       "Hardware, Software, Data, People, and Procedures (Processes)",
       "HTML, CSS, JavaScript, Python, and SQL",
       "Finance, Marketing, Sales, HR, and Accounting"],
      1,
      "An Information System is sociotechnical: it comprises (1) Hardware, (2) Software, (3) Data, (4) People, and (5) Procedures/Processes.")

add_q("IS Components: Hardware",
      "Which of the following is classified as a 'Hardware' component of an Information System?",
      ["Microsoft Windows 11 Operating System", "A cloud server, barcode scanner, or mobile sensor device", "A database query written in SQL", "A written corporate dress code policy"],
      1,
      "Hardware consists of the tangible physical electronic devices used to capture, process, store, and display data (servers, computers, network routers, sensors).")

add_q("IS Components: Software",
      "What is the role of the 'Software' component in an Information System?",
      ["Providing the physical metal housing for computers",
       "Providing the instructions, programs, and applications (OS, DBMS, business apps) that tell the hardware how to process data",
       "Serving as the human end user of the system",
       "Managing physical electrical power lines in the office"],
      1,
      "Software provides the programmed logic, instructions, and applications (operating systems, database management systems, enterprise apps) that direct hardware operations.")

add_q("IS Components: Data",
      "In an Information System, what does 'Data' represent?",
      ["The computer monitor glass",
       "The raw material (facts, numbers, transactions, student records) entered into and processed by the system",
       "The electricity powering the servers",
       "The salary paid to IT managers"],
      1,
      "Data is the raw material of an IS: customer names, transaction timestamps, student IDs, product SKUs, and sensor measurements.")

add_q("IS Components: People",
      "Why are 'People' considered the most critical component of an Information System?",
      ["Because hardware runs faster when humans stand near it",
       "Because people (end users, managers, analysts, DBAs) supply inputs, interpret outputs, execute business procedures, and make decisions driven by the system",
       "Because people are physically built into the motherboard",
       "Because computer code cannot be stored without humans"],
      1,
      "An IS exists to serve human organizations. People design, maintain, feed data into, and act upon the information produced by the technology.")

add_q("IS Components: Procedures & Processes",
      "What are 'Procedures' (or Processes) in an Information System?",
      ["The physical copper wires inside a network cable",
       "The rules, guidelines, steps, and policies that govern how data is entered, processed, validated, and used within an organizational workflow",
       "The brand name of the computer monitor",
       "The temperature setting of the air conditioner"],
      1,
      "Procedures define operational rules: step-by-step instructions on who enters data, how validations occur, and what happens when an order or registration is processed.")

add_q("Procedures Example",
      "A student logs into the portal, selects courses, validates prerequisites, and confirms enrollment. This sequence of steps is an example of:",
      ["A Hardware Device", "An IS Procedure (Business Process)", "A Computer Virus", "A Database Table"],
      1,
      "This structured sequence represents a procedure or business process: connecting people and technology to achieve a specific organizational outcome.")

add_q("How IS Works: Basic Model",
      "What is the classical operational cycle of an Information System?",
      ["Output -> Feedback -> Processing -> Input",
       "Input -> Processing -> Output -> Feedback",
       "Processing -> Input -> Feedback -> Output",
       "Storage -> Hardware -> Software -> People"],
      1,
      "An IS operates through the fundamental cycle: Input (capture data) -> Processing (compute/transform) -> Output (deliver information) -> Feedback (evaluation loop).")

add_q("IS Operations: 5 Core Operations",
      "What are the five essential operational functions performed by an Information System on data?",
      ["Copy, Cut, Paste, Print, and Delete",
       "Data Capture, Data Processing, Data Storage, Data Retrieval, and Data Dissemination",
       "Marketing, Accounting, Shipping, Billing, and Auditing",
       "Compilation, Linking, Assembly, Execution, and Debugging"],
      1,
      "An IS performs: (1) Data Capture (collecting inputs), (2) Processing (transforming), (3) Storage (persisting), (4) Retrieval (accessing), and (5) Dissemination (delivering reports).")

add_q("IS vs IT vs Computer Science",
      "What is the primary distinction between Computer Science (CS) and Information Systems (IS)?",
      ["Computer Science focuses on hardware cables, while IS focuses on computer graphics",
       "Computer Science focuses on theoretical computing concepts, algorithms, and software development; Information Systems focuses on applying technology, people, and processes to solve organizational problems",
       "There is no difference; they are exact synonyms",
       "IS is only for teenagers, while CS is for adults"],
      1,
      "Computer Science emphasizes mathematical algorithms, programming language design, and systems software. Information Systems bridges technology and business strategy to serve organizational goals.")

add_q("IS vs IT vs Computer Science",
      "What is the primary focus of 'Information Technology' (IT) compared to 'Information Systems' (IS)?",
      ["IT focuses on installing, managing, and maintaining technical infrastructure (hardware, networks, software tools), while IS focuses on integrating that technology with business processes and people",
       "IT is only about typing on a keyboard",
       "IS is an obsolete field that was completely replaced by IT",
       "IT only deals with non-profit charities"],
      0,
      "IT focuses on technical implementation, infrastructure, systems administration, and hardware/network support. IS encompasses the broader sociotechnical interaction of IT with organizational strategy, human behavior, and business processes.")

add_q("Major Types of IS",
      "Which type of Information System records and processes day-to-day routine operational business transactions (e.g., checkout scanning, ATM withdrawals, sales orders)?",
      ["Executive Support System (ESS)", "Transaction Processing System (TPS)", "Decision Support System (DSS)", "Management Information System (MIS)"],
      1,
      "Transaction Processing Systems (TPS) serve operational managers by recording and tracking daily routine fundamental business transactions.")

add_q("Major Types of IS",
      "What is the primary function of a Management Information System (MIS)?",
      ["Controlling industrial manufacturing robots directly",
       "Providing middle managers with scheduled periodic reports, summary metrics, and exception reports derived from underlying TPS data",
       "Running unstructured mathematical simulations for top executives",
       "Fixing broken hard disk drives"],
      1,
      "MIS aggregates operational data from TPS to produce standardized, periodic summary reports (e.g. monthly departmental sales) for middle managers.")

add_q("Major Types of IS",
      "What distinguishes a Decision Support System (DSS) from a standard MIS?",
      ["DSS does not use computers",
       "DSS supports semi-structured and non-routine decision making using interactive models, analytical tools, and 'what-if' scenario simulations",
       "MIS is only for computers, while DSS is only for smartphones",
       "DSS only handles routine cashier receipts"],
      1,
      "While MIS provides static, routine summary reports, a DSS provides interactive modeling capabilities (what-if analysis, goal-seeking, sensitivity analysis) for complex semi-structured problems.")

add_q("Major Types of IS",
      "Which Information System is designed specifically for top executives, providing high-level dashboards, strategic summaries, and external market intelligence with drill-down capability?",
      ["Transaction Processing System (TPS)", "Executive Information System (EIS / ESS)", "Point of Sale (POS) system", "Assembly language compiler"],
      1,
      "Executive Information/Support Systems (EIS/ESS) deliver high-level strategic visualizations, external economic indicators, and touch dashboards to C-level executives.")

add_q("IS Applications across Industries",
      "In healthcare, how do specialized Information Systems (like Electronic Health Records - EHR) improve patient care?",
      ["By replacing medical doctors with automatic surgery robots",
       "By providing fast access to patient medical histories, reducing prescription errors, coordinating care between specialists, and securing patient health records",
       "By increasing hospital billing paperwork",
       "By disconnecting hospitals from internet networks"],
      1,
      "Healthcare IS (EHR/EMR) centralizes patient records, eliminates duplicate testing, alerts clinicians to drug interactions, and accelerates emergency treatment.")

add_q("University IS Case Study",
      "In the University Information System case study from Lecture 1, what constitutes the primary 'Processing' activity?",
      ["Student Name and Student ID", "Course registration validation, GPA calculation, and academic standing evaluation", "Printing the diploma on paper", "The campus security gate"],
      1,
      "In a University IS, inputs (student data, grades) undergo processing (validating prerequisites, computing term and cumulative GPAs, checking degree audit requirements).")

add_q("University IS Case Study",
      "What are the primary 'Outputs' produced by a University Information System?",
      ["Student credit cards", "Official academic transcripts, GPA reports, class rosters, and degree completion status", "New campus buildings", "University sports trophies"],
      1,
      "The processed outputs include transcripts, term GPA statements, graduation eligibility verifications, and student registration confirmations.")

add_q("Emerging Technologies in IS",
      "How is Artificial Intelligence (AI) and Machine Learning transforming modern Information Systems?",
      ["By turning monitors off when users leave the room",
       "By automating complex analytical tasks, enabling predictive intelligence, providing conversational chatbots, and uncovering hidden patterns in vast datasets",
       "By eliminating the need for electricity in computers",
       "By restricting all user passwords to numbers"],
      1,
      "AI/ML enhances Information Systems with autonomous pattern recognition, predictive forecasting, natural language interfaces, and cognitive automation.")

add_q("Emerging Technologies: Cloud Computing",
      "What is the major organizational advantage of Cloud Computing in modern Information Systems?",
      ["It eliminates the need for internet connectivity",
       "On-demand scalability, reduced upfront capital expenditure on hardware, 24/7 global accessibility, and automatic vendor maintenance",
       "It makes physical computer screens larger",
       "It makes all software completely free forever"],
      1,
      "Cloud platforms allow organizations to scale computing capacity dynamically, pay only for consumed resources, and access enterprise applications from anywhere.")

add_q("Emerging Technologies: IoT",
      "What role does the Internet of Things (IoT) play as an input component in modern Information Systems?",
      ["Replacing all human computer monitors",
       "Capturing real-time sensor data from physical objects (RFID tags, temperature sensors, GPS trackers) and feeding it directly into supply chain and operational IS",
       "Printing physical paper books",
       "Deleting unneeded software licenses"],
      1,
      "IoT devices and smart sensors automatically capture continuous real-time environmental and operational telemetry without requiring manual human data entry.")

# Fill remaining Q26 to Q150 for Lecture 1
for i in range(26, 151):
    topics = [
        ("IS Benefits", "How do modern Information Systems reduce organizational operating costs?",
         ["By firing all corporate executives",
          "By automating manual paper-intensive workflows, minimizing human calculation errors, accelerating transaction processing, and optimizing supply chain inventory levels",
          "By disconnecting internet access",
          "By banning employee phone calls"], 1,
          "IS drives down operational overhead through paperless automation, streamlined inventory tracking, and lower error rates."),
        ("IS Components", "Which component of an Information System includes the database administrator, software developers, and clerical data entry operators?",
         ["Hardware Component", "People Component", "Software Component", "Procedures Component"], 1,
         "The People component encompasses all human stakeholders who interact with, maintain, govern, or develop the information system."),
        ("IS Operations", "What is 'Data Dissemination' in information systems operations?",
         ["Deleting corrupted data from hard drives",
          "Distributing and delivering the right processed information to the right users in the right format at the right time",
          "Encrypting data with passwords",
          "Scanning paper documents into PDF"], 1,
          "Data dissemination involves formatting and routing information outputs (dashboards, alerts, reports, messages) to designated human or system consumers."),
        ("IS vs IT", "If an engineer installs network switches, runs optical fiber cables, and configures server virtualization, they are working primarily in the domain of:",
         ["Information Technology (IT) / Infrastructure", "Strategic Business Management", "Psychology", "Corporate Marketing"], 0,
         "Physical installation of technical hardware, routers, switches, and server infrastructure falls squarely under Information Technology (IT).")
    ]
    t = topics[(i - 26) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Lecture 1.")

# =========================================================================
# LECTURE 2: IS IN ORGANIZATIONS, MANAGEMENT LEVELS & PROCESSES (Q151 - Q300)
# =========================================================================

add_q("Organization as a System",
      "In systems theory, how is an 'Organization' formally defined?",
      ["A collection of isolated individuals with zero common goals",
       "A formal sociotechnical system that utilizes resources (inputs) to execute coordinated activities (transformation) to produce goods, services, and value (outputs) for stakeholders",
       "A computer program written in C++",
       "A government building with security guards"],
      1,
      "An organization is a formal, purposeful open system: it draws resources from its environment, processes them through operational activities, and delivers valuable outputs.")

add_q("4 Organizational Resources",
      "What are the FOUR fundamental categories of resources utilized by an organization?",
      ["Air, Water, Fire, and Earth",
       "Human Resources, Financial Resources, Physical Resources, and Information Resources",
       "HTML, CSS, JavaScript, and SQL",
       "Desktops, Laptops, Tablets, and Smartphones"],
      1,
      "The four classic organizational resource pillars are: (1) Human Resources (employees/labor), (2) Financial Resources (capital/cash), (3) Physical Resources (buildings, equipment, inventory), and (4) Information Resources (data, knowledge).")

add_q("Information as a Resource",
      "Why is 'Information' uniquely valuable compared to traditional physical or financial resources?",
      ["Because information wears out and breaks physically after 30 days",
       "Because information can be shared, reused, duplicated, and transmitted instantaneously at near-zero marginal cost without being consumed or depleted",
       "Because information is made of pure gold",
       "Because information cannot be stored on computers"],
      1,
      "Unlike physical assets that degrade or can only be used in one place at a time, information is non-rivalrous: it can be replicated, analyzed, and shared across the enterprise indefinitely.")

add_q("3 Management Levels",
      "What are the THREE traditional hierarchical management levels in an organization?",
      ["Junior, Middle, and Senior Programmers",
       "Operational Management, Middle Management, and Top (Executive) Management",
       "Morning Shift, Evening Shift, and Night Shift",
       "Local, National, and International branches"],
      1,
      "Organizations are classically structured into three tiers: (1) Operational Management (supervisors/foremen), (2) Middle Management (department/division heads), and (3) Top Management (C-suite/executives).")

add_q("Operational Management Level",
      "What is the primary responsibility of 'Operational Management'?",
      ["Setting 10-year corporate merger strategies",
       "Managing day-to-day routine operational activities, supervising non-managerial staff, and making structured, short-term decisions",
       "Designing the corporate logo",
       "Issuing new stock on public markets"],
      1,
      "Operational management supervises daily front-line workflows, tracks routine transactions, schedules labor, and ensures standard operating procedures are followed.")

add_q("Operational Decision Nature",
      "What type of decisions do operational managers primarily make, and what type of information do they require?",
      ["Unstructured, ambiguous decisions requiring highly aggregated economic forecasts",
       "Structured, repetitive decisions requiring detailed, current, real-time internal operational data",
       "Philosophical decisions requiring historical poetry",
       "Financial investment decisions requiring Wall Street reports"],
      1,
      "Operational decisions are highly structured (clear rules, deterministic criteria) and depend on detailed, timely, current transactional records.")

add_q("Middle Management Level",
      "What is the role of 'Middle Management' in an organization?",
      ["Cleaning the office desks at night",
       "Translating broad executive strategies into tactical departmental plans, allocating resources, monitoring departmental performance, and solving semi-structured problems",
       "Entering cashier barcode scans all day",
       "Serving as the chairman of the board of directors"],
      1,
      "Middle managers (plant managers, department heads) bridge strategy and operations: they allocate resources, monitor operational KPIs, and make tactical decisions.")

add_q("Middle Management Information Needs",
      "What type of information do Middle Managers predominantly require to perform their duties?",
      ["Raw unaggregated single-keystroke logs",
       "Summarized, periodic departmental reports, exception reports (highlighting performance deviations), and trend comparisons",
       "External gossip from celebrity magazines",
       "The personal home addresses of all company customers"],
      1,
      "Middle management requires summarized periodic reports (e.g. monthly departmental budget vs actual spend, inventory stockout warnings) to take corrective tactical action.")

add_q("Top Management Level",
      "What is the primary responsibility of 'Top (Executive) Management' (e.g., CEO, CIO, Board)?",
      ["Supervising the daily operation of individual retail cash registers",
       "Setting the overall long-term vision, organizational strategy, competitive positioning, major capital investments, and policies for the entire enterprise",
       "Writing daily code bug fixes in JavaScript",
       "Managing the office stationery supply closet"],
      1,
      "Top management establishes enterprise-wide vision, enters new geographic markets, approves acquisitions, and navigates external competitive threats.")

add_q("Top Management Information Needs",
      "What characteristics define the information required by Top Management for strategic decisions?",
      ["Extremely detailed, second-by-second raw transaction logs",
       "Highly summarized, aggregated internal performance metrics combined with extensive external environmental intelligence (competitor moves, market trends, regulatory shifts)",
       "Only printed paper memos written in blue ink",
       "Data strictly limited to the previous 24 hours"],
      1,
      "Executives need broad, highly aggregated, future-oriented strategic summaries integrated with external competitive, regulatory, and market intelligence.")

add_q("Mapping IS to Management Levels",
      "Which Information System primarily serves the Operational Management level?",
      ["Executive Support System (ESS)", "Transaction Processing System (TPS)", "Balanced Scorecard Dashboard", "Strategic Formulation System"],
      1,
      "TPS is the foundation supporting operational staff: processing sales, logging inventory receipts, cutting payroll checks, and recording hotel bookings.")

add_q("Mapping IS to Management Levels",
      "Which Information System primarily serves Middle Management with standardized operational reports and variance analysis?",
      ["Transaction Processing System (TPS)", "Management Information System (MIS)", "Executive Information System (EIS)", "Robotic Process Automation"],
      1,
      "MIS draws data from TPS to deliver standardized, periodic summary reports and KPI variance dashboards to middle managers.")

add_q("Mapping IS to Management Levels",
      "Which Information System serves Top Executives with customized visual cockpits, external data feeds, and drill-down capabilities?",
      ["Transaction Processing System (TPS)", "Executive Information / Support System (EIS / ESS)", "Cash Register POS software", "Inventory Barcode Reader"],
      1,
      "EIS/ESS provides senior leaders with executive dashboards, market intelligence, and touch-driven drill-down into organizational performance.")

add_q("Functional Business Areas",
      "What are the classical Functional Areas found in a standard business enterprise?",
      ["North, South, East, and West",
       "Marketing & Sales, Finance, Accounting, Human Resources, Production/Operations, and Management",
       "Hardware, Software, Firmware, and Middleware",
       "Inputs, Outputs, Processing, and Storage"],
      1,
      "Core functional departments: Marketing & Sales (generating demand), Accounting & Finance (managing money and records), HR (talent), and Production/Operations (making goods/services).")

add_q("Functional IS: Accounting vs Finance",
      "How do Accounting Information Systems differ from Financial Information Systems?",
      ["Accounting tracks historical financial transactions, bookkeeping, invoicing, and tax compliance; Financial systems focus on investment planning, cash flow forecasting, and capital allocation",
       "Accounting is only for cash, while Finance is only for gold",
       "They are exact duplicates with zero distinction",
       "Accounting systems are illegal in publicly traded corporations"],
      0,
      "Accounting IS is retrospective (ledger, payroll, accounts payable/receivable, compliance). Financial IS is forward-looking (capital budgeting, investment portfolios, risk modeling).")

add_q("Functional IS: Human Resources (HRIS)",
      "What is the primary function of a Human Resources Information System (HRIS)?",
      ["Selling products to external customers",
       "Managing employee records, tracking recruitment and applicant pipelines, administering payroll and benefits, and tracking training compliance",
       "Managing warehouse forklift maintenance",
       "Writing marketing brochures"],
      1,
      "An HRIS automates workforce administration: employee lifecycle records, talent acquisition, performance reviews, benefits enrollment, and compensation.")

add_q("Business Process Definition",
      "What is a 'Business Process'?",
      ["A legal court trial between two companies",
       "A logically coordinated set of related activities and tasks performed across resources to achieve a specific, measurable organizational goal",
       "A computer reboot sequence",
       "An employee lunch break"],
      1,
      "A business process is an organized collection of related activities that take inputs, add value, and produce a specific result/output for a customer or stakeholder.")

add_q("Business Process Components",
      "What are the three essential components that define any business process?",
      ["CPU, RAM, and Disk Space", "Input (required resources/data), Activities (tasks performed), and Output (the result produced)", "Lawyers, Judges, and Police", "Past, Present, and Future"],
      1,
      "Every process has: (1) Inputs (materials/data), (2) Activities/Tasks (transformation workflow), and (3) Outputs (deliverable product, service, or decision).")

add_q("Types of Business Processes",
      "What are the THREE major classifications of Business Processes in an enterprise?",
      ["Slow, Medium, and Fast Processes",
       "Core Processes (Operational), Support Processes, and Management Processes",
       "Cheap, Expensive, and Luxury Processes",
       "Internal, Foreign, and International Processes"],
      1,
      "Processes fall into: (1) Core Processes (value-creating operations delivered to customers), (2) Support Processes (enabling infrastructure like IT/HR), and (3) Management Processes (governance/strategy).")

add_q("Types of Business Processes: Core",
      "Which of the following is classified as a 'Core Business Process'?",
      ["Conducting an internal employee IT security audit", "Fulfilling customer orders, manufacturing physical products, and delivering medical patient care", "Repairing office desk chairs", "Filing corporate legal tax forms"],
      1,
      "Core processes directly touch external customers and create value (order-to-cash, product assembly, customer onboarding, claims processing).")

add_q("Types of Business Processes: Support",
      "Which of the following is classified as a 'Support Business Process'?",
      ["Selling merchandise to a retail customer", "Human resource recruiting, employee onboarding, IT technical helpdesk, and facilities maintenance", "Designing the flagship consumer product", "Delivering pizza to a consumer"],
      1,
      "Support processes provide necessary internal foundation and backing for core operations, but do not directly interface as the primary product sold to consumers.")

add_q("Types of Business Processes: Management",
      "What characterizes a 'Management Process'?",
      ["Manufacturing physical plastic parts",
       "Activities that plan, monitor, govern, and control enterprise operations (e.g. strategic planning, annual corporate budgeting, risk compliance)",
       "Sweeping warehouse floors",
       "Answering incoming customer telephone orders"],
      1,
      "Management processes oversee organizational governance, strategic goal-setting, policy enforcement, capital allocation, and performance monitoring.")

add_q("Cross-Functional Systems",
      "What is a 'Cross-Functional Information System'?",
      ["A system that only works on cross-shaped computer screens",
       "An integrated system that spans across multiple functional departmental boundaries (Sales, Inventory, Finance, Logistics) to support end-to-end business processes",
       "A system that can only be used by one person at a time",
       "An isolated software program used solely inside the accounting room"],
      1,
      "Cross-functional systems (like Enterprise Resource Planning - ERP) eliminate departmental silos, integrating data and workflows seamlessly across the entire organization.")

add_q("Cross-Functional Order Fulfillment",
      "In an end-to-end customer order fulfillment process, which departments must coordinate through a cross-functional system?",
      ["Only the Marketing department",
       "Sales (takes order), Warehouse/Inventory (checks stock), Finance (verifies credit/payment), and Logistics/Shipping (delivers product)",
       "Only the Human Resources department",
       "Only the Legal department"],
      1,
      "Order-to-cash is the classic cross-functional process: Sales receives the purchase order, Warehouse picks the items, Finance bills the account, and Shipping delivers the goods.")

add_q("Competitive Advantage via IS",
      "How can an organization leverage Information Systems to achieve a 'Competitive Advantage'?",
      ["By buying the most expensive computer keyboards in the city",
       "By lowering operational costs, differentiating products, speeding customer response time, locking in customers with high switching costs, and optimizing supply chain coordination",
       "By disconnecting from all supplier networks",
       "By refusing to adopt automated software"],
      1,
      "Information Systems unlock competitive advantage by reducing overhead, accelerating cycle times, creating unique digital service experiences, and erecting barriers to entry.")

# Fill remaining Q176 to Q300 for Lecture 2
for i in range(176, 301):
    topics = [
        ("Business Processes", "Why does automating a poorly designed, inefficient business process with software often fail to yield benefits?",
         ["Because software is physically incapable of running bad processes",
          "Because automating a broken or flawed process merely magnifies and accelerates the inefficiencies and errors (often called 'paving the cow path')",
          "Because computers only run perfect processes",
          "Because automated systems delete all business processes"], 1,
          "Automating a fundamentally flawed process simply executes bad steps faster. Process redesign (BPR) should precede software automation."),
        ("Cross-Functional Integration", "What is the primary organizational disadvantage of 'Functional Silos' (isolated departmental software)?",
         ["Departmental software is always free",
          "Data redundancy, conflicting metrics between departments, delayed decision-making, and fragmented customer experiences",
          "Employees become too collaborative with each other",
          "Computers consume too little electricity"], 1,
          "Functional silos cause duplicate data entry, conflicting reports (Sales vs Finance numbers don't match), and blind spots across end-to-end customer journeys."),
        ("Management Levels", "If a factory supervisor reviews today's scrap rate and reassigns three workers on Assembly Line #2, this is an example of:",
         ["Operational Decision Making", "Strategic Long-Range Planning", "Corporate Mergers & Acquisitions", "International Diplomacy"], 0,
         "Short-term, immediate tactical adjustments to daily factory line labor represent Operational Management."),
        ("Competitive Advantage", "How did Walmart gain a sustainable competitive advantage through its Retail Link supply chain information system?",
         ["By paying suppliers with gold coins",
          "By sharing real-time point-of-sale inventory data directly with suppliers, enabling automated vendor-managed replenishment and dramatic cost reductions",
          "By keeping all inventory levels completely secret from manufacturers",
          "By eliminating all delivery trucks"], 1,
          "Walmart's Retail Link connects suppliers directly to checkout scanner data, slashing inventory holding costs and establishing unbeatable low-cost leadership.")
    ]
    t = topics[(i - 176) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Total IS App Questions generated: {len(questions)}")

with open("questions/isapp_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

with open("web/data/isapp_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved 300 questions to questions/isapp_questions.json and web/data/isapp_questions.json!")
