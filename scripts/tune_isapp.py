# scripts/tune_isapp.py
# Targeted distractor and option length tuning for IS Applications question bank.
# Ensures that options are roughly the same length and correct is longest in < 20% of questions.

import sys
sys.path.insert(0, 'scripts')
import isapp_part1
import isapp_part2
import isapp_part3
import isapp_part4

p1 = isapp_part1.part1_questions
p2 = isapp_part2.part2_questions
p3 = isapp_part3.part3_questions
p4 = isapp_part4.part4_questions

# --- PART 1 TUNING ---
# Q3: correct len=106
p1[3]["distractors"][0] = "To replace every human employee with fully automated algorithmic decision agents across all administrative departments"
# Q9: correct len=103
p1[9]["distractors"][0] = "It is programmed exclusively using social media application programming interfaces and external web discussion boards"
# Q18: correct len=121
p1[18]["distractors"][0] = "A database administrator creates a nightly encrypted backup of raw customer credit card transactions onto offline magnetic storage tape"
# Q20: correct len=106
p1[20]["distractors"][0] = "Actionable Knowledge, because the sensor utilizes specialized industrial wireless radio frequencies to transmit its reading"
# Q23: correct len=117
p1[23]["distractors"][0] = "By multiplying 42 units by the $19.99 price and deleting the associated product color and size attributes from all database tables"
# Q27: correct len=80
p1[27]["distractors"][0] = "A multi-core enterprise server blade mounted securely inside a climate-controlled corporate data center equipment rack"
# Q28: correct len=22 -> expand all options to roughly 30-36 chars
p1[28]["correct"] = "Formal Operating Procedures and Workflows"
p1[28]["distractors"][0] = "Physical Computer Hardware Infrastructure"
p1[28]["distractors"][1] = "Structured Database Raw Data Records"
p1[28]["distractors"][2] = "Core Application Software Logic Code"
# Q30: correct len=109
p1[30]["distractors"][0] = "They physically transmit high-voltage electrical current across server motherboards to prevent catastrophic system crashes"
# Q33: correct len=15 -> balance option lengths
p1[33]["correct"] = "Business Systems Analyst"
p1[33]["distractors"][0] = "Hardware Assembly Technician"
p1[33]["distractors"][1] = "Frontline Retail Cashier Clerk"
p1[33]["distractors"][2] = "Data Center Facilities Technician"
# Q37: correct len=77
p1[37]["distractors"][0] = "The booking servers and SAN storage arrays mounted inside the airline's enterprise data center facility"
# Q39: correct len=133
p1[39]["distractors"][0] = "A server (Hardware) automatically creates new commercial products (Data) without human interaction (People) or operating systems (Software)"
# Q41: correct len=113
p1[41]["distractors"][0] = "To permanently delete customer transaction records once monthly financial reports are completed and verified by internal auditing teams"
# Q44: correct len=88
p1[44]["distractors"][0] = "The numeric final course exam score entered by a professor into the official online faculty grading web portal"
# Q46: correct len=94
p1[46]["distractors"][0] = "An unrecoverable system malfunction caused by database schema constraint violations across multiple distributed servers"
# Q47: correct len=107
p1[47]["distractors"][0] = "Erasing redundant database tables to free up physical magnetic disk space across all primary and secondary corporate data centers"
# Q49: correct len=143
p1[49]["distractors"][0] = "Disseminate invoice receipt -> Store audit record -> Retrieve transaction record -> Process electronic payment -> Capture customer order details"


# --- PART 2 TUNING ---
# Q0 (overall Q51): correct len=112
p2[0]["distractors"][0] = "Configuring enterprise local area network cables, managing corporate firewalls, and troubleshooting office PC operating hardware"
# Q1 (overall Q52): balance option lengths
p2[1]["correct"] = "Information Technology Infrastructure (IT)"
p2[1]["distractors"][0] = "Computer Science Computational Theory (CS)"
p2[1]["distractors"][1] = "Organizational Information Systems (IS)"
p2[1]["distractors"][2] = "Strategic Corporate Management Policy"
# Q2: correct len=103
p2[2]["distractors"][0] = "IS focuses exclusively on designing silicon microprocessor architectures, cache memories, and circuit board physics"
# Q3: correct len=119
p2[3]["distractors"][0] = "A Computer Science algorithmic theorist, because they analyze asymptotic Big-O runtime boundaries and computational complexity"
# Q5: correct len=99
p2[5]["distractors"][0] = "Proving that a cryptographic hashing function is computationally NP-complete using mathematical induction and formal logic proofs"
# Q6: correct len=133
p2[6]["distractors"][0] = "The CS graduate is legally prohibited by industry certification bodies from reading corporate balance sheets or attending departmental meetings"
# Q7: correct len=168
p2[7]["distractors"][0] = "CS engineers assemble the physical server cases; IT analysts code the encryption math; IS specialists manage the bank's long-term stock portfolio"
# Q9: correct len=123
p2[9]["distractors"][0] = "IT focuses entirely on human social interactions, while IS focuses exclusively on computer microchip architecture and silicon semiconductors"
# Q10: correct len=107
p2[10]["distractors"][0] = "To simulate 10-year macroeconomic scenarios for board-of-director executive retreats and multi-billion-dollar acquisition reviews"
# Q13 (overall Q64): balance option lengths
p2[13]["correct"] = "Executive Information / Support Systems (EIS / ESS)"
p2[13]["distractors"][0] = "Transaction Processing Systems for Frontline Clerks (TPS)"
p2[13]["distractors"][1] = "Factory Floor Automated Data Collector Appliances (FDC)"
p2[13]["distractors"][2] = "Electronic Data Interchange Transmission Gateways (EDI)"
# Q14: correct len=116
p2[14]["distractors"][0] = "TPS formulates five-year strategic market expansion goals that MIS middle managers execute daily across regional branch offices"
# Q15: correct len=40
p2[15]["distractors"][0] = "An Interactive Decision Support System (DSS)"
# Q17: correct len=88
p2[17]["distractors"][0] = "To identify and delete duplicate customer records from the core transactional relational database management repository"
# Q18 (overall Q69): balance option lengths
p2[18]["correct"] = "Interactive drill-down navigation capability"
p2[18]["distractors"][0] = "Automated transactional logging protocol"
p2[18]["distractors"][1] = "Asymmetric data encryption indexing mechanism"
p2[18]["distractors"][2] = "High-speed batch compiler script execution"
# Q20: correct len=102
p2[20]["distractors"][0] = "To run isolated personal spreadsheet applications on individual employee desktop machines without network integration"
# Q23: balance option lengths
p2[23]["correct"] = "Executive Information / Support System (EIS / ESS)"
p2[23]["distractors"][0] = "Transaction Processing System with Local Storage (TPS)"
p2[23]["distractors"][1] = "Factory Floor Shop Floor Machine Controller (SFMC)"
p2[23]["distractors"][2] = "Automated Cash Register Terminal Scanning Unit (ACR)"
# Q24: correct len=99
p2[24]["distractors"][0] = "EIS/ESS automatically generates valid financial revenues through mathematical simulation formulas and predictive heuristics"
# Q25: correct len=98
p2[25]["distractors"][0] = "Batch printing of weekly paper account balance ledgers for manual postal mail distribution to account holders"
# Q26: correct len=120
p2[26]["distractors"][0] = "Eliminating the need for software programming by using physical atmospheric weather satellites and cosmic wave telemetry detectors"
# Q27: correct len=107
p2[27]["distractors"][0] = "Eliminating the need for licensed doctors and nurses by performing complex surgical operations algorithmically without staff"
# Q28 (overall Q79): balance option lengths
p2[28]["correct"] = "Internet of Things (IoT) Sensor Telemetry"
p2[28]["distractors"][0] = "Compiler Optimization Microarchitecture"
p2[28]["distractors"][1] = "Desktop Publishing Typography Software"
p2[28]["distractors"][2] = "Relational Relational Database Calculus"
# Q29: correct len=118
p2[29]["distractors"][0] = "By physically delivering packages to consumer doorsteps using telepathic transmission protocols and automated flying drones"
# Q30: correct len=113
p2[30]["distractors"][0] = "A high-speed laser printing apparatus capable of generating millions of physical paper shipping manifests and warehouse receipts"
# Q32: correct len=100
p2[32]["distractors"][0] = "By requiring all citizens to physically visit regional agency offices in person for every routine administrative transaction"
# Q33: correct len=96
p2[33]["distractors"][0] = "Replace human industrial managers with speculative foreign currency investment bots operating across global markets"
# Q34: correct len=111
p2[34]["distractors"][0] = "Custom-built computer motherboards sold to retail consumers for home computer assembly and hobbyist electronics projects"
# Q36: correct len=98
p2[36]["distractors"][0] = "To permanently delete customer contact records whenever client satisfaction metrics drop below predetermined enterprise thresholds"
# Q37: correct len=109
p2[37]["distractors"][0] = "They permanently eliminate one hundred percent of all future corporate operational capital and personnel labor expenditures"
# Q38: correct len=94
p2[38]["distractors"][0] = "To physically clean university lecture halls and schedule maintenance for campus bus engines and mechanical equipment"
# Q39: correct len=118
p2[39]["distractors"][0] = "Any single spreadsheet file that contains more than one hundred thousand rows of numerical student grades and class exam results"
# Q40: correct len=89
p2[40]["distractors"][0] = "An official certified academic transcript presented to an employer after formal degree graduation ceremonies"
# Q42: correct len=93
p2[42]["distractors"][0] = "The detailed course syllabus drafted in a word processor by a professor prior to the start of the academic semester"
# Q46: correct len=117
p2[46]["distractors"][0] = "A student logging out of the university web portal after checking their scheduled final exam dates and course room assignments"
# Q47: correct len=97
p2[47]["distractors"][0] = "By physically dictating the lecture delivery pace and spoken vocabulary of classroom professors during course hours"
# Q48: correct len=122
p2[48]["distractors"][0] = "The physical Cisco high-density Wi-Fi router mounted to the ceiling of the central campus library quiet study hall facility"


# --- PART 3 TUNING ---
# Q3 (overall Q104): correct len=145
p3[3]["distractors"][0] = "Technological resources include liquid corporate cash reserves; Physical resources include employee patents, secret formulas, and proprietary trade blueprints"
# Q5: correct len=124
p3[5]["distractors"][0] = "Information has completely eliminated the need for human personnel and physical manufacturing machinery across modern industrial corporations"
# Q6: correct len=96
p3[6]["distractors"][0] = "Automated relational database backup scripts scheduled to execute at midnight across distributed multi-region server clusters"
# Q11: correct len=138
p3[11]["distractors"][0] = "Accounting recruits new specialized engineering staff; Finance manufactures physical inventory components in automated fabrication factories"
# Q12: correct len=115
p3[12]["distractors"][0] = "Calculating optimal freight shipping routes for ocean-going container cargo vessels across trans-pacific maritime shipping lanes"
# Q13 (overall Q114): balance option lengths
p3[13]["correct"] = "Production and Operations Management"
p3[13]["distractors"][0] = "Accounting and Financial Recordkeeping"
p3[13]["distractors"][1] = "Marketing and Public Customer Relations"
p3[13]["distractors"][2] = "Human Resources and Employee Benefits"
# Q14: correct len=94
p3[14]["distractors"][0] = "Operating electronic cash registers and issuing paper change to retail consumers at checkout lanes throughout the day"
# Q17 (overall Q118): balance option lengths
p3[17]["correct"] = "Corporate Finance and Treasury"
p3[17]["distractors"][0] = "Human Resources Management Tier"
p3[17]["distractors"][1] = "Consumer Marketing and Branding"
p3[17]["distractors"][2] = "Accounting and Tax Compliance"
# Q18 (overall Q119): balance option lengths
p3[18]["correct"] = "Production and Operations Management"
p3[18]["distractors"][0] = "Human Resources and Staff Development"
p3[18]["distractors"][1] = "Corporate Finance and Capital Budgeting"
p3[18]["distractors"][2] = "Legal Affairs and Regulatory Compliance"
# Q19: correct len=119
p3[19]["distractors"][0] = "Employees are forced to share the same physical desktop computer workstation across multiple separate corporate departments"
# Q20: correct len=127
p3[20]["distractors"][0] = "Marketing advertising campaigns broadcast across television networks, radio stations, and digital social media communication channels"
# Q22: correct len=68
p3[22]["distractors"][0] = "Human Resources Information System with Applicant Tracking (HRIS)"
p3[22]["distractors"][1] = "Executive Compensation and Benefits Governance Portal (ECBGP)"
# Q24 (overall Q125): balance option lengths
p3[24]["correct"] = "Human Resources and Talent Management"
p3[24]["distractors"][0] = "Corporate Treasury and Investment Finance"
p3[24]["distractors"][1] = "Operations and Production Scheduling"
p3[24]["distractors"][2] = "Marketing and Consumer Market Research"
# Q25: correct len=68
p3[25]["distractors"][0] = "Clerical Administrative Tier, Technical Tier, and Outsourced Contracting Tier"
# Q29: correct len=115
p3[29]["distractors"][0] = "Granular, continuous streams of every customer barcode scan happening at every cashier lane throughout the retail branch store"
# Q31: correct len=127
p3[31]["distractors"][0] = "Minute-by-minute transactional receipts from individual supermarket register lanes across all regional metropolitan locations"
# Q32: correct len=99
p3[32]["distractors"][0] = "The Chief Financial Officer who prepares annual corporate SEC financial disclosures and shareholder reports"
# Q34: correct len=120
p3[34]["distractors"][0] = "Enterprise relational databases refuse to display raw transactions on monitors used by senior corporate executive officers"
# Q37: correct len=108
p3[37]["distractors"][0] = "A daily list of employee time-card clock-in timestamps for a single retail branch store across all cashiers and clerks"
# Q39: correct len=115
p3[39]["distractors"][0] = "The organization will instantly become vulnerable to international copyright infringement lawsuits and regulatory fines"
# Q42: correct len=123
p3[42]["distractors"][0] = "It is executed exclusively by automated relational database scripts without human administrative awareness or supervision"
# Q48: correct len=119
p3[48]["distractors"][0] = "A severe hardware memory controller failure has corrupted the relational database product inventory table in primary storage"


# --- PART 4 TUNING ---
# Q0 (overall Q151): balance option lengths
p4[0]["correct"] = "Transaction Processing System (TPS)"
p4[0]["distractors"][0] = "Executive Support System Suite (ESS)"
p4[0]["distractors"][1] = "Decision Support Modeling System (DSS)"
p4[0]["distractors"][2] = "Strategic Forecasting Simulator (SFS)"
# Q1: correct len=163
p4[1]["distractors"][0] = "MIS is designed exclusively for corporate chief executive officers; DSS is deployed strictly on operational point-of-sale cashier terminals in retail stores"
# Q4: correct len=138
p4[4]["distractors"][0] = "A supermarket cashier scans a customer's loyalty barcode card to apply a five-dollar grocery coupon and prints an itemized checkout receipt"
# Q5: correct len=128
p4[5]["distractors"][0] = "They are completely redundant software packages that compete for identical user queries on employee desktop personal computer workstations"
# Q7: correct len=117
p4[7]["distractors"][0] = "The specific brand and batch serial number of sterile disposable syringes ordered by Nurse Station 4 during morning clinical rounds"
# Q8: correct len=124
p4[8]["distractors"][0] = "What-If is performed by frontline retail cashiers; Goal-Seeking is executed exclusively by external database administration consultants"
# Q9: correct len=114
p4[9]["distractors"][0] = "Generating 5-year macroeconomic trend charts for the airline's executive board members during annual strategic retreats"
# Q11: correct len=135
p4[11]["distractors"][0] = "Executive computer display monitors lack the physical hardware graphics capability to render dense alphanumeric text and financial fonts"
# Q13: correct len=108
p4[13]["distractors"][0] = "To schedule standard weekly employee wage deductions for mandatory payroll processing and tax compliance filing"
# Q14: correct len=77
p4[14]["distractors"][0] = "A Transaction Processing System (TPS) issuing electronic boarding passes to passengers"
# Q15: correct len=126
p4[15]["distractors"][0] = "A hardware central processing unit executing machine assembly code instructions inside an enterprise mainframe computer server"
# Q16 (overall Q167): balance option lengths
p4[16]["correct"] = "Inputs (data/resources), Activities (tasks/workflows), and Outputs (results produced)"
p4[16]["distractors"][0] = "Monitors (visual devices), Keyboards (input hardware), and Printers (output machinery)"
p4[16]["distractors"][1] = "Corporate Liquid Cash (money), Common Stock (equity), and Long-Term Debt (liabilities)"
p4[16]["distractors"][2] = "Attorneys (legal counsel), Accountants (tax auditors), and External Management Advisors"
# Q17: correct len=108
p4[17]["distractors"][0] = "Recruiting new assembly line workers and conducting mandatory annual occupational health and safety seminars for factory staff"
# Q18: correct len=118
p4[18]["distractors"][0] = "To directly manufacture finished commercial consumer goods on factory assembly lines using automated robotic fabrication arms"
# Q19: correct len=111
p4[19]["distractors"][0] = "Scanning a customer's retail items at a cash register checkout lane to print a detailed itemized paper sales receipt"
# Q20: correct len=99
p4[20]["distractors"][0] = "Purchasing bulk paper towels and sterile latex examination gloves for hospital supply storage closets"
# Q21: correct len=120
p4[21]["distractors"][0] = "By increasing the number of physical paper approval signatures required for every routine departmental purchasing transaction"
# Q24: correct len=112
p4[24]["distractors"][0] = "Replacing all optical laser barcode scanners with traditional handwritten paper shipping registers in receiving warehouses"
# Q25: correct len=122
p4[25]["distractors"][0] = "An isolated personal computer used exclusively by one department with no network connection to any other organizational units"
# Q26: correct len=126
p4[26]["distractors"][0] = "Departmental silos force customer service representatives to rewrite enterprise operating systems in low-level assembly language"
# Q27 (overall Q178): balance option lengths
p4[27]["correct"] = "Enterprise Resource Planning Systems (ERP)"
p4[27]["distractors"][0] = "Standalone Desktop Electronic Spreadsheet"
p4[27]["distractors"][1] = "Single-User Local Personal Word Processor"
p4[27]["distractors"][2] = "Optical Disc Master Media Authoring Tool"
# Q28: correct len=143
p4[28]["distractors"][0] = "The sales representative prints the order on paper and physically walks it to the warehouse floor manager during the following calendar week"
# Q31: correct len=126
p4[31]["distractors"][0] = "Every employee is required to manually retype customer order data into five separate departmental spreadsheet files every single day"
# Q32: correct len=99
p4[32]["distractors"][0] = "The customer must visit five different corporate branch offices in person to submit notarized paper address change request forms"
# Q33: correct len=81
p4[33]["distractors"][0] = "Eliminating redundant data storage and resolving cross-departmental data inconsistencies across business units"
# Q35: correct len=115
p4[35]["distractors"][0] = "Sales shuts down factory machines to ensure the client order is handcrafted exclusively by senior corporate executive officers"
# Q36: correct len=106
p4[36]["distractors"][0] = "They prohibit employees in different departments from sending electronic mail messages to colleagues in other units"
# Q37: correct len=116
p4[37]["distractors"][0] = "Purchasing the largest physical computer monitors available in the consumer retail electronics market for all corporate offices"
# Q38: correct len=116
p4[38]["distractors"][0] = "By setting retail product prices to zero so that the enterprise operates at a complete financial loss across all product lines"
# Q39: correct len=82
p4[39]["distractors"][0] = "Operational Cost Leadership achieved by permanently dismissing all retail bank branch managers"
# Q40: correct len=122
p4[40]["distractors"][0] = "By legally confiscating customer credit cards whenever they browse a competing enterprise's commercial retail shopping website"
# Q42: correct len=106
p4[42]["distractors"][0] = "Formulating the university's comprehensive 10-year capital campus expansion master plan and financing strategy"
# Q44: correct len=100
p4[44]["distractors"][0] = "The specific textbook ISBN numbers assigned by an adjunct university lecturer for an introductory poetry seminar"
# Q45: correct len=123
p4[45]["distractors"][0] = "The daily attendance record of student laboratory technicians working in the campus biological chemistry research department"
# Q46 (overall Q197): balance option lengths
p4[46]["correct"] = "Transaction Processing System (TPS)"
p4[46]["distractors"][0] = "Executive Support System Suite (ESS)"
p4[46]["distractors"][1] = "Decision Support Modeling Suite (DSS)"
p4[46]["distractors"][2] = "Strategic Policy Simulation Tool (SPS)"
# Q47: correct len=118
p4[47]["distractors"][0] = "It permanently eliminates the need for university professors, instructors, academic advisors, and physical lecture classrooms"
# Q48: correct len=138
p4[48]["distractors"][0] = "It forces all university professors to teach the exact same academic course syllabus and administer identical exams on the exact same calendar day"
# Q49: correct len=142
p4[49]["distractors"][0] = "By continually purchasing the most expensive cutting-edge hardware available regardless of actual strategic business requirements or operational ROI"

print("All tuning applied successfully!")
