# scripts/isapp_part3.py
# 50 Rigorous, Medium-Difficulty Questions for Lecture 2 (Part 1):
# Organizations & 5 Resources, 6 Functional Areas, 3 Management Levels & Information Needs, Decision Types

part3_questions = [
    # --- 3.1 Organizations & Five Organizational Resources (Q101 - Q110) ---
    {
        "topic": "Organizations & 5 Resources",
        "question": "What is the formal definition of an 'Organization' in the context of enterprise management?",
        "correct": "A structured group of people working collaboratively with shared resources to achieve common goals",
        "distractors": [
            "A collection of computer hardware devices linked together via high-speed fiber-optic network switches",
            "A random assemblage of individuals operating independently without formal communication or leadership",
            "A legal document filed with government agencies that specifies corporate tax liability formulas"
        ],
        "explanation": "An organization is a structured social collective of people working together toward shared strategic objectives using coordinated resources."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "Which of the following lists the FIVE primary resource categories mobilized by modern organizations?",
        "correct": "Human, Financial, Physical, Information, and Technological resources",
        "distractors": [
            "Marketing, Accounting, Sales, Advertising, and Public Relations resources",
            "Hardware, Software, Firmware, Middleware, and Freeware resources",
            "Desktops, Laptops, Tablets, Smartphones, and Server blade resources"
        ],
        "explanation": "Modern organizations mobilize five core resources: Human (people), Financial (capital), Physical (facilities/machinery), Information (data/knowledge), and Technological (hardware/software/networks)."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "A multinational firm holds 50 patents, a customer contact database, and specialized chemical formulas. These assets belong to which resource category?",
        "correct": "Information Resources",
        "distractors": [
            "Physical Resources",
            "Financial Resources",
            "Technological Resources"
        ],
        "explanation": "Patents, proprietary trade formulas, customer records, and accumulated organizational knowledge constitute Information Resources."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "What distinguishes an organization's 'Technological Resources' from its 'Physical Resources'?",
        "correct": "Technological resources consist of hardware, software, and networks; Physical resources encompass real estate, buildings, and industrial machinery",
        "distractors": [
            "Technological resources include cash reserves; Physical resources include employee patents and trade formulas",
            "Technological resources exist only on paper ledgers; Physical resources exist exclusively in cloud databases",
            "Technological resources represent employee talent; Physical resources represent corporate investment bonds"
        ],
        "explanation": "Technological resources comprise IT infrastructure (hardware, software, networks); Physical resources include tangible enterprise facilities, buildings, and fabrication equipment."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "Cash reserves, bank credit facilities, and venture capital investments are classified as which type of organizational resource?",
        "correct": "Financial Resources",
        "distractors": [
            "Information Resources",
            "Physical Resources",
            "Technological Resources"
        ],
        "explanation": "Money, working capital reserves, bank loans, and equity investments represent an organization's Financial Resources."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "Why is 'Information' now recognized as an organizational resource on par with capital and human talent?",
        "correct": "Accurate, actionable information is essential for effective decision-making, operational coordination, and competitive strategy",
        "distractors": [
            "Information has completely eliminated the need for human employees and physical manufacturing equipment",
            "Government tax laws allow organizations to convert stored database bytes directly into physical gold bullion",
            "Information permanently prevents competitors from offering products at lower consumer prices"
        ],
        "explanation": "Information is a vital strategic resource because poor or missing information leads to flawed decisions, wasted capital, and lost competitiveness."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "Which of the following is considered part of an organization's 'Human Resources'?",
        "correct": "Frontline assembly workers, research scientists, department managers, and executive officers",
        "distractors": [
            "Automated relational database backup scripts scheduled to run at midnight",
            "The corporate headquarters building and adjacent industrial logistics warehouse",
            "A proprietary customer relationship management software license purchased from a vendor"
        ],
        "explanation": "Human Resources encompasses all organizational personnel—from entry-level employees and specialists to middle managers and executive leadership."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "A university campus features lecture halls, research laboratories, library books, and campus shuttle buses. These are examples of:",
        "correct": "Physical Resources",
        "distractors": [
            "Financial Resources",
            "Technological Resources",
            "Information Resources"
        ],
        "explanation": "Real estate, campus buildings, laboratory furniture, library volumes, and shuttle vehicles are tangible Physical Resources."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "How do Information Systems fundamentally interact with an organization's resources?",
        "correct": "They capture data about all resources to help managers allocate, monitor, and utilize them effectively",
        "distractors": [
            "They physically manufacture industrial machinery and deposit printed paper banknotes into bank vaults",
            "They eliminate financial resources by converting all enterprise assets into open-source software scripts",
            "They replace physical buildings with virtual computer screens so employees no longer exist"
        ],
        "explanation": "IS acts as the central tracking and management system that monitors and optimizes the allocation of human, financial, physical, and technological resources."
    },
    {
        "topic": "Organizations & 5 Resources",
        "question": "Which of the following is NOT a characteristic of a formal organization?",
        "correct": "Operating without defined objectives, established roles, or coordinated workflows",
        "distractors": [
            "Having a structured hierarchy of authority and defined functional responsibilities",
            "Mobilizing resources such as people, money, and technology to attain shared objectives",
            "Utilizing operational processes and procedures to deliver products, services, or public value"
        ],
        "explanation": "Formal organizations always have defined objectives, structured roles, and coordinated workflows; operating randomly without goals contradicts the definition."
    },

    # --- 3.2 Organizational Functional Areas (Q111 - Q125) ---
    {
        "topic": "Organizational Functional Areas",
        "question": "Which functional area in an enterprise is primarily responsible for identifying customer demand, promoting products, and closing sales?",
        "correct": "Marketing and Sales",
        "distractors": [
            "Accounting and Auditing",
            "Human Resources Management",
            "Production and Operations"
        ],
        "explanation": "Marketing & Sales is tasked with market research, advertising, promoting goods/services, customer relationship management, and sales transactions."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "What is the primary operational distinction between 'Accounting' and 'Finance' functional areas?",
        "correct": "Accounting records historical financial transactions and ensures regulatory compliance; Finance manages capital, liquidity, and investment planning",
        "distractors": [
            "Accounting recruits new engineering staff; Finance manufactures physical inventory components in factories",
            "Accounting focuses exclusively on future long-term investments; Finance records historical receipts from retail registers",
            "Accounting operates without software systems; Finance uses only physical paper cash registers and handwritten ledgers"
        ],
        "explanation": "Accounting is historically oriented (recording past transactions, general ledgers, tax compliance); Finance is forward-looking (capital structure, cash flow, investments)."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "An enterprise Human Resources (HR) department relies on an HR Information System (HRIS). Which of the following is a core task supported by this system?",
        "correct": "Tracking employee recruiting pipelines, benefits compensation, performance evaluations, and labor compliance",
        "distractors": [
            "Calculating optimal freight shipping routes for ocean-going container cargo vessels",
            "Managing physical automated lathe machines inside industrial metal fabrication factories",
            "Executing real-time algorithmic trades across global high-frequency stock exchanges"
        ],
        "explanation": "HRIS manages human capital workflows: job applications, employee onboarding, benefits administration, performance reviews, and training records."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "Which functional area is directly responsible for converting raw materials into finished physical goods or executing core service commitments?",
        "correct": "Production / Operations",
        "distractors": [
            "Marketing",
            "Accounting",
            "Finance"
        ],
        "explanation": "Production/Operations oversees the actual transformation of raw inputs into finished goods and the direct delivery of operational services."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "The Management functional area is primarily tasked with:",
        "correct": "Setting organizational goals, planning resource allocation, and controlling departmental activities",
        "distractors": [
            "Operating cash registers and issuing paper change to retail consumers at checkout lanes",
            "Physically repairing damaged electrical wiring and assembling desktop computer frames",
            "Entering daily attendance records into spreadsheet software for entry-level factory workers"
        ],
        "explanation": "Management is responsible for executive planning, setting corporate vision, organizing resources, and exercising governance and control."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "A retail bank needs to record customer deposits, balance daily teller drawers, and prepare quarterly tax filings. Which department is responsible for these activities?",
        "correct": "Accounting",
        "distractors": [
            "Marketing",
            "Production",
            "Human Resources"
        ],
        "explanation": "Balancing ledgers, recording transactional deposits, and filing statutory tax returns are standard functions of the Accounting department."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "Which Information System would the Marketing department most heavily rely on to manage customer leads, track interactions, and analyze campaign performance?",
        "correct": "Customer Relationship Management (CRM) system",
        "distractors": [
            "Computer-Integrated Manufacturing (CIM) system",
            "Automated General Ledger Accounting system",
            "Shop Floor Material Requirements Planning system"
        ],
        "explanation": "CRM systems are dedicated tools that empower marketing and sales teams to manage prospective leads, track client histories, and evaluate campaign ROI."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "A corporate treasurer is deciding whether to issue commercial bonds or negotiate a bank credit facility to fund a $50 million plant expansion. This decision belongs to:",
        "correct": "Finance",
        "distractors": [
            "Human Resources",
            "Marketing",
            "Accounting"
        ],
        "explanation": "Long-term capital financing, debt issuance, and liquidity management are core responsibilities of the Finance department."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "Which functional department is primarily concerned with inventory turnover rates, bill of materials (BOM), and factory machine scheduling?",
        "correct": "Production / Operations",
        "distractors": [
            "Human Resources",
            "Corporate Finance",
            "Legal Affairs"
        ],
        "explanation": "Production/Operations manages manufacturing schedules, material bills, inventory replenishment, and shop floor throughput."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "Why does a traditional 'siloed' functional structure often create operational inefficiencies in an enterprise?",
        "correct": "Each department maintains isolated databases, resulting in duplicate data, communication delays, and conflicting goals",
        "distractors": [
            "Employees are forced to share the same physical desktop computer across multiple departments",
            "Corporate software vendors refuse to sell software to companies with more than three departments",
            "Accounting and Finance are legally barred from using electronic calculations under commercial law"
        ],
        "explanation": "Departmental silos isolate information in incompatible departmental systems, leading to data inconsistencies, blind spots, and coordination friction."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "When the Human Resources department integrates with the Accounting department, what operational process is directly automated?",
        "correct": "Payroll processing, where employee work hours and wage rates automatically calculate salary payments and tax deductions",
        "distractors": [
            "Marketing advertising campaigns across television networks and digital social channels",
            "Physical maintenance of manufacturing conveyor belts and cooling ventilation fans",
            "Long-term forecasting of international consumer demand for newly developed electronics"
        ],
        "explanation": "Integrating HR (employee hours/wages) and Accounting (general ledger/bank disbursement) automates payroll calculation and tax compliance."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "Which functional area would use web analytics tools to measure click-through rates, customer acquisition costs, and conversion funnels?",
        "correct": "Marketing",
        "distractors": [
            "Accounting",
            "Production",
            "Human Resources"
        ],
        "explanation": "Measuring advertising reach, conversion funnels, and customer acquisition costs is a primary analytics responsibility of the Marketing department."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "A manufacturing supervisor notices that a key stamping machine will run out of steel sheets in two hours. Which functional information system must alert the procurement team?",
        "correct": "Production / Operations Information System (e.g., SCM or MRP module)",
        "distractors": [
            "Human Resources Information System (HRIS)",
            "Marketing Campaign Automation Portal",
            "Executive Compensation Tracking System"
        ],
        "explanation": "Material requirements planning (MRP) and supply chain systems track inventory consumption on factory floors and trigger replenishment alerts."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "Which of the following is an example of an Accounting Information System (AIS) deliverable?",
        "correct": "An audited balance sheet, income statement, and accounts receivable aging schedule",
        "distractors": [
            "A prospective customer profile compiled from social media demographic surveys",
            "A technical blueprint outlining the microchip routing architecture for a smartphone",
            "A 3D graphic animation created for an upcoming television advertising broadcast"
        ],
        "explanation": "Balance sheets, income statements, and accounts receivable aging reports are standard, mandatory deliverables produced by an Accounting Information System."
    },
    {
        "topic": "Organizational Functional Areas",
        "question": "In an organization, which functional area is responsible for employee onboarding, administering health benefits, and managing labor union agreements?",
        "correct": "Human Resources",
        "distractors": [
            "Finance",
            "Operations",
            "Marketing"
        ],
        "explanation": "Human Resources manages the employee lifecycle: recruiting, onboarding, benefits, performance reviews, and labor relations."
    },

    # --- 3.3 Management Levels & Information Needs (Q126 - Q140) ---
    {
        "topic": "Management Levels & Info Needs",
        "question": "What are the three traditional hierarchical levels of management found within an organization?",
        "correct": "Operational Level, Middle Management Level, and Top Management Level",
        "distractors": [
            "Clerical Level, Technical Level, and Outsourced Contractor Level",
            "Hardware Level, Software Level, and Telecommunications Level",
            "Domestic Level, Regional Level, and Multinational Level"
        ],
        "explanation": "Management hierarchy is structured into three primary tiers: Operational Management, Middle Management, and Top (Executive) Management."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "Which of the following describes the primary responsibility and time horizon of Operational Management?",
        "correct": "Directing daily routine activities with a short-term focus spanning hours, days, or weeks",
        "distractors": [
            "Formulating 5-year corporate expansion strategies and negotiating international joint ventures",
            "Allocating quarterly departmental budgets and evaluating mid-level branch manager productivity",
            "Restructuring corporate capital debt ratios and issuing common stock shares to investors"
        ],
        "explanation": "Operational managers (supervisors, shift leads) oversee day-to-day routine tasks on a short-term time horizon (daily/weekly)."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "What type of information is required by Operational Management to perform their duties effectively?",
        "correct": "Highly detailed, current, real-time, and internally focused transactional records",
        "distractors": [
            "Broadly aggregated macroeconomic indicators and five-year competitor projections",
            "Highly summarized quarterly financial variance charts without individual transaction lines",
            "Abstract industry whitepapers discussing geopolitical trade agreements"
        ],
        "explanation": "Operational managers require detailed, real-time internal data—such as specific order lines, employee shift logs, and current inventory levels."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "A branch manager reviews a report comparing this month's actual sales against budgeted targets across four retail stores. This manager belongs to which level?",
        "correct": "Middle Management Level",
        "distractors": [
            "Operational Management Level",
            "Top Management Level",
            "Board of Directors Level"
        ],
        "explanation": "Reviewing departmental performance against tactical monthly budgets is the hallmark responsibility of Middle Management."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "What type of information is most suitable for Middle Management?",
        "correct": "Summarized, periodic information that compares actual performance against established departmental plans",
        "distractors": [
            "Granular, continuous streams of every customer barcode scan happening at every cashier lane",
            "Exclusively external news feeds regarding international monetary currency fluctuations",
            "Raw unindexed hexadecimal database memory logs captured during network packet routing"
        ],
        "explanation": "Middle management needs summarized, periodic reports (monthly/quarterly) and comparative variance analysis to control departmental progress."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "The Chief Executive Officer (CEO) and Board of Directors are deciding whether to enter the European retail market over the next five years. They represent:",
        "correct": "Top Management Level",
        "distractors": [
            "Middle Management Level",
            "Operational Management Level",
            "Supervisory Staff Level"
        ],
        "explanation": "The CEO and Board of Directors constitute Top (Executive) Management, responsible for overall corporate vision and long-term strategic decisions."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "What characterizes the information requirements of Top Management?",
        "correct": "Highly aggregated, macro-level KPIs combining internal summary data with external competitive and economic intelligence",
        "distractors": [
            "Minute-by-minute transactional receipts from individual supermarket register lanes",
            "Standard operating procedure checklists for cleaning industrial shop floor machinery",
            "Unprocessed time-clock punch timestamps for temporary warehouse forklift drivers"
        ],
        "explanation": "Top executives need highly aggregated, macro-level insights combining internal enterprise health metrics with external market/economic trends."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "Which of the following roles is an example of Operational Management in a manufacturing company?",
        "correct": "A factory shift supervisor who assigns daily assembly line tasks and tracks hourly unit production",
        "distractors": [
            "The Chief Financial Officer who prepares annual corporate SEC financial disclosures",
            "A regional plant director who oversees capital equipment budgets across four factories",
            "The Vice President of Global Supply Chain who negotiates five-year shipping contracts"
        ],
        "explanation": "A shift supervisor managing daily assignments and tracking hourly output is an operational-level manager."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "How does the time horizon of decision-making change as one moves up from Operational to Top Management?",
        "correct": "It expands from short-term daily/weekly execution to long-term multi-year strategic vision",
        "distractors": [
            "It shrinks from five-year strategic roadmaps down to millisecond high-frequency transaction windows",
            "It remains completely identical across all three tiers, focusing solely on monthly accounting ledgers",
            "It transitions from external industry benchmarking to internal shop floor machine troubleshooting"
        ],
        "explanation": "Time horizons expand upward: operational management focuses on days/weeks, middle management on months/quarters, and top management on years (3-5+ years)."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "Why would providing raw operational transactional logs to a corporate CEO be considered bad IS design?",
        "correct": "It causes information overload; executives need concise, aggregated summaries and trends to make strategic decisions",
        "distractors": [
            "Enterprise databases refuse to display raw transactions on monitors used by senior executives",
            "Corporate bylaws make it illegal for corporate officers to view individual customer transaction names",
            "Operational logs are automatically deleted by the server immediately after receipt generation"
        ],
        "explanation": "Flooding executives with thousands of daily operational transactions creates information overload, distracting from strategic decision-making."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "Which management level is responsible for translating the broad strategic goals established by executives into actionable departmental plans?",
        "correct": "Middle Management Level",
        "distractors": [
            "Operational Management Level",
            "External Consultant Level",
            "Frontline Cashier Level"
        ],
        "explanation": "Middle management bridges the gap: they take broad strategic directives from top management and translate them into concrete departmental objectives."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "A warehouse clerk needs to check whether a specific replacement part (SKU #4819) is physically available on Shelf 4B. This inquiry represents:",
        "correct": "An operational-level information need requiring real-time granular data",
        "distractors": [
            "A strategic-level information need requiring multi-year economic forecasting",
            "A middle-management tactical inquiry requiring quarterly variance analysis",
            "An unstructured executive decision requiring interactive mathematical modeling"
        ],
        "explanation": "Finding an item on a shelf is a routine, real-time, highly granular operational task handled at the operational level."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "Which of the following reports would most likely be delivered exclusively to Top Management?",
        "correct": "A corporate executive dashboard showing five-year market share projections and global revenue by division",
        "distractors": [
            "A daily list of employee time-card clock-in timestamps for a single retail branch store",
            "An hourly machine temperature log for the stamping press in Manufacturing Unit 2",
            "A receipt reprint for a customer who purchased office stationery supplies this morning"
        ],
        "explanation": "Five-year market share trends and corporate revenue dashboards are high-level strategic artifacts designed for executive decision-makers."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "Which management level relies most heavily on internal operational data rather than external market data?",
        "correct": "Operational Management",
        "distractors": [
            "Top Management",
            "Board of Directors",
            "Strategic Planning Committee"
        ],
        "explanation": "Operational management is inward-looking: their job is to run internal processes smoothly using internal operational metrics."
    },
    {
        "topic": "Management Levels & Info Needs",
        "question": "What is the primary danger when an Information System provides only summarized reports to operational managers?",
        "correct": "They cannot resolve immediate operational problems because they lack granular details about specific transactions",
        "distractors": [
            "The organization will instantly become vulnerable to international copyright infringement lawsuits",
            "Middle managers will be forced to resign because their departmental authority is superseded",
            "The physical servers will experience overheating due to reduced database query processing"
        ],
        "explanation": "Operational personnel need specific details (which customer, which part, which transaction). Summaries prevent them from executing daily tasks."
    },

    # --- 3.4 Decision Types & Management Alignment (Q141 - Q150) ---
    {
        "topic": "Decision Types & Alignment",
        "question": "Which type of decision involves established procedures, clear decision rules, and deterministic criteria with little to no ambiguity?",
        "correct": "Structured Decision",
        "distractors": [
            "Unstructured Decision",
            "Semi-Structured Decision",
            "Intuitive Heuristic Decision"
        ],
        "explanation": "Structured decisions are routine, repetitive, and follow definite procedures and formulas, leaving no ambiguity about how they should be handled."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "A supermarket cash register automatically calculates sales tax and applies a standard 10% senior citizen discount on Tuesdays. What type of decision is this?",
        "correct": "A Structured Decision, executed at the operational level",
        "distractors": [
            "An Unstructured Decision, executed at the top executive level",
            "A Semi-Structured Decision, executed by corporate legal counsel",
            "A Strategic Policy Decision, executed by the board of directors"
        ],
        "explanation": "Applying sales tax and a defined promotional discount follows exact mathematical and calendar rules—a structured operational decision."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "What is the defining characteristic of an 'Unstructured Decision'?",
        "correct": "It involves novel, complex, and non-routine situations where no predefined procedure or deterministic solution exists",
        "distractors": [
            "It is executed exclusively by automated relational database scripts without human awareness",
            "It requires the user to follow a rigid three-step checklist printed on paper forms",
            "It applies only to daily employee attendance and hourly payroll tax withholdings"
        ],
        "explanation": "Unstructured decisions are non-routine, novel, and ambiguous, requiring human judgment, evaluation, and executive insight rather than standard formulas."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "Which of the following is an example of an Unstructured Decision made by Top Management?",
        "correct": "Deciding whether to acquire a struggling competitor and enter a completely new foreign market",
        "distractors": [
            "Reordering 100 boxes of printer paper when warehouse inventory hits the safety reorder threshold",
            "Approving an employee's requested dental leave according to standard company benefits policy",
            "Calculating the monthly overtime wages owed to factory assembly technicians"
        ],
        "explanation": "Acquiring a competitor and expanding into foreign markets is a novel, high-stakes, strategic decision with no fixed algorithm—an unstructured decision."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "How does a 'Semi-Structured Decision' differ from both structured and unstructured decisions?",
        "correct": "It combines standardized algorithmic procedures with subjective human managerial judgment",
        "distractors": [
            "It is handled entirely by hardware sensors without any software programming or human intervention",
            "It has zero importance to organizational profitability and is delegated exclusively to interns",
            "It is executed once every hundred years and requires unanimous shareholder consensus"
        ],
        "explanation": "Semi-structured decisions have some routine, structured elements (e.g. credit score formulas), but require human judgment for the final call."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "A bank loan officer uses an automated credit scoring model to screen an applicant, but then reviews the applicant's character and business plan before approving the loan. This is:",
        "correct": "A Semi-Structured Decision, characteristic of Middle Management",
        "distractors": [
            "A purely Structured Decision, characteristic of frontline ATM hardware",
            "A completely Unstructured Decision, characteristic of corporate boardroom retreats",
            "A non-managerial clerical activity without any business significance"
        ],
        "explanation": "Blending credit scoring algorithms (structured) with subjective evaluation of character and business plans (unstructured) constitutes a semi-structured decision."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "Which management level makes the highest proportion of Structured Decisions?",
        "correct": "Operational Management Level",
        "distractors": [
            "Middle Management Level",
            "Top Executive Management Level",
            "Board of Directors Level"
        ],
        "explanation": "Operational management deals with day-to-day routine tasks governed by explicit rules, making their decisions predominantly structured."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "Which type of Information System is best suited to support Semi-Structured Decisions by providing simulation and What-If analysis?",
        "correct": "Decision Support System (DSS)",
        "distractors": [
            "Transaction Processing System (TPS)",
            "Point-of-Sale Register (POS)",
            "Optical Character Recognition (OCR)"
        ],
        "explanation": "Decision Support Systems (DSS) are purpose-built to assist managers with semi-structured decisions by offering modeling, simulation, and data analysis."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "An algorithm reorders office supplies whenever inventory falls below 20 units. If an office manager wants to override the rule because the office is moving next week, what is happening?",
        "correct": "A routine structured rule is modified by human managerial judgment due to changing contextual conditions",
        "distractors": [
            "A hardware failure has corrupted the relational database inventory table",
            "The office manager is committing corporate fraud by refusing to order paper",
            "The system is executing an automated top-management strategic acquisition"
        ],
        "explanation": "Real-world context (office relocation) requires human judgment to override a routine structured rule, converting the task into a semi-structured decision."
    },
    {
        "topic": "Decision Types & Alignment",
        "question": "Which row in the table correctly pairs Management Level, Decision Nature, and Primary Information System?",
        "correct": "Top Management -> Unstructured Decisions -> Executive Support Systems (ESS)",
        "distractors": [
            "Operational Management -> Unstructured Decisions -> Management Information Systems (MIS)",
            "Middle Management -> Structured Decisions -> Transaction Processing Systems (TPS)",
            "Top Management -> Highly Structured Decisions -> Point-of-Sale Registers (POS)"
        ],
        "explanation": "Top Management tackles Unstructured Decisions and is supported by Executive Support Systems (ESS). Operational uses TPS for structured; Middle uses MIS/DSS for semi-structured."
    }
]
