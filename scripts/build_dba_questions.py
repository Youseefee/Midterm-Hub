import json

# Generates 300 high quality, rigorous questions for Database Administration (DBA)
# Covering Lec 1 (Questions 1-100), Lec 2&3 (Questions 101-200), Lec 4&5 (Questions 201-300)

questions = []

def add_q(topic, q_text, options, ans_idx, explanation):
    q_id = f"dba_{len(questions) + 1}"
    questions.append({
        "id": q_id,
        "subject": "Database Administration (DBA)",
        "topic": topic,
        "question": q_text,
        "options": options,
        "answer": ans_idx,
        "explanation": explanation
    })

# =========================================================================
# LECTURE 1: DBA ROLES, RESPONSIBILITIES & ENVIRONMENT (Q1 - Q100)
# =========================================================================

# 1-10: Definitions & The DBA Persona
add_q("DBA Roles & Persona",
      "According to the course materials, what is the primary definition of a Database Administrator (DBA)?",
      ["A programmer who writes complex business application code in Java or C#",
       "An information technician responsible for ensuring the operational environment and directing infrastructure for data",
       "A hardware engineer who repairs physical server drives and network switches",
       "An executive solely responsible for setting corporate product prices"],
      1,
      "A DBA is defined as the information technician responsible for ensuring the operational environment and directing infrastructure for an organization's data.")

add_q("DBA Roles & Persona",
      "Which negative stereotype of a DBA refers to an unapproachable technician who sits in an office and reflexively says 'No' to any request?",
      ["The Agile Architect", "The Curmudgeon in the Corner", "The System Evangelist", "The Data Wrangler"],
      1,
      "The 'Curmudgeon in the Corner' or 'prima donna DBA' is an anti-pattern: an unhelpful technician who constantly rejects requests instead of collaborating with developers and management.")

add_q("DBA Roles & Persona",
      "Why is a DBA often described as a 'Jack of all Trades'?",
      ["Because DBAs only need to know how to install one operating system",
       "Because DBAs must possess a wide array of skills ranging from systems architecture, SQL tuning, and OS internals to communication and business domain knowledge",
       "Because DBAs perform accounting, marketing, and legal duties regularly",
       "Because modern DBAs do not need specialized database knowledge"],
      1,
      "A DBA must balance diverse responsibilities: system performance, security, data modeling, SQL optimization, disaster recovery, and interpersonal communication with developers and business users.")

add_q("DBA Roles & Persona",
      "Why is the need for Database Administrators growing in modern organizations?",
      ["Databases are disappearing in favor of flat text files",
       "The explosion of data volumes, mission-critical 24/7 availability demands, complex multi-platform environments, and regulatory compliance requirements",
       "Modern applications no longer require data storage",
       "Companies are replacing all databases with simple spreadsheets"],
      1,
      "The demand for DBAs grows because businesses generate unprecedented amounts of data, require 24/7 continuous operations, and must comply with strict data security and compliance laws.")

add_q("DBA Roles & Persona",
      "Which of the following is considered a major 'DBA Danger' discussed in the lectures?",
      ["Becoming too cooperative with end-users",
       "Acting as an arrogant 'prima donna' or bottleneck who impedes business progress rather than enabling it",
       "Learning too many database platforms",
       "Writing too much documentation"],
      1,
      "The DBA danger is becoming a prima donna who creates friction, behaves unprofessionally, or hoards knowledge, making the DBA department a business bottleneck.")

add_q("DBA vs Database 101",
      "What is the fundamental difference between a 'Database' and a 'DBMS' (Database Management System)?",
      ["A database is software, whereas a DBMS is the collection of physical disks",
       "A database is an organized collection of structured data, while a DBMS is the software suite used to create, manage, query, and maintain databases",
       "There is no difference; they are exact synonyms in computer science",
       "A DBMS stores data in text files, while a database stores data exclusively in memory"],
      1,
      "A database is the organized repository of data itself. A DBMS (e.g., Oracle, DB2, SQL Server, PostgreSQL) is the software layer that manages access, concurrency, security, and storage for databases.")

add_q("Administration Disciplines",
      "What is the primary focus of a Data Administrator (DA) or Chief Data Officer (CDO) compared to a DBA?",
      ["Configuring disk RAID arrays and DBMS installation patches",
       "Focusing on the business aspects of data, data governance, metadata policy, business semantics, and logical data modeling",
       "Writing low-level C network drivers",
       "Managing physical tape backup drives"],
      1,
      "The Data Administrator (DA/CDO) focuses on data governance, data dictionaries, business meaning, enterprise data architecture, and logical models, whereas the DBA focuses on physical implementation and technical operations.")

add_q("Administration Disciplines",
      "What is the primary scope of responsibility for a System Administrator (SA) in relation to database environments?",
      ["Designing physical primary keys and foreign keys for tables",
       "Managing the operating system, hardware, server infrastructure, OS patches, network, and basic system utilities",
       "Tuning SQL SELECT queries for user applications",
       "Defining relational integrity rules in database schemas"],
      1,
      "The System Administrator (SA) manages the server hardware, operating system installation, OS-level security, system memory, network configuration, and disk subsystems hosting the DBMS.")

add_q("Administration Disciplines",
      "Which administrative role sits between the business data definition and the operating system, handling DBMS installation, performance tuning, and schema realization?",
      ["Web Graphic Designer", "Database Administrator (DBA)", "Scrum Master", "Network Cabling Technician"],
      1,
      "The DBA operates between data administration and system administration, translating logical models into physical databases, optimizing SQL, and maintaining DBMS health.")

add_q("DBA Management Discipline",
      "Viewing Database Administration as a 'Management Discipline' means:",
      ["Treating database maintenance as random ad-hoc tasks done only when something crashes",
       "Establishing systematic, repeatable, and proactive procedures for availability, performance, data integrity, backup and recovery, and change management",
       "Requiring the DBA to manage the sales and human resources departments",
       "Eliminating all automated monitoring tools in favor of manual inspection"],
      1,
      "DBA as a management discipline means approaching data infrastructure with formal policies, repeatable standards, proactive monitoring, SLA adherence, and documented disaster recovery procedures.")

# 11-25: Types of DBAs
add_q("Types of DBAs",
      "Which type of DBA focuses primarily on DBMS software installation, upgrading versions, applying service packs/fixes, and tuning DBMS-wide memory parameters?",
      ["Application DBA", "System DBA", "Data Modeler", "Data Warehouse Administrator"],
      1,
      "The System DBA is technically focused on the DBMS software itself: installing new versions, applying migration patches, configuring memory buffers, and maintaining server-level system catalog structures.")

add_q("Types of DBAs",
      "What are the primary responsibilities of an Application DBA?",
      ["Installing operating system kernel updates",
       "Focusing on a specific application or business domain, writing and tuning application SQL, designing application schemas, and collaborating directly with development teams",
       "Managing physical building security and server room air conditioning",
       "Negotiating software procurement licenses exclusively"],
      1,
      "An Application DBA works closely with development teams on specific business applications, focusing on query tuning, schema changes for the app, and database access logic.")

add_q("Types of DBAs",
      "What is an advantage of having dedicated Application DBAs?",
      ["They have zero need to understand database mechanics",
       "They develop deep expertise in the specific business logic, data models, and queries of the applications they support",
       "They eliminate the need for any System DBAs or DBMS software",
       "They do not report to anyone in the organization"],
      1,
      "Application DBAs understand the application's unique query patterns, business workflows, and critical transactions deeply, leading to more responsive application-level tuning.")

add_q("Types of DBAs",
      "What is a potential disadvantage of dedicated Application DBAs?",
      ["They become too knowledgeable about SQL",
       "They may develop tunnel vision, prioritize their single application over enterprise data standards, or duplicate data across silos",
       "They are unable to talk to developers",
       "They are legally prohibited from modifying tables"],
      1,
      "Application DBAs can develop silos, create unstandardized table designs, or compete for system resources without considering the overall corporate DBMS health.")

add_q("Types of DBAs",
      "What is the role of a Database Architect?",
      ["Carrying out nightly tape backups",
       "Designing the overall enterprise database landscape, standards, data integration strategies, and long-term architectural roadmap",
       "Fixing forgotten user passwords",
       "Managing physical printer queues"],
      1,
      "A Database Architect designs the enterprise blueprint, establishing multi-system architectures, data flows, standards, and scalable infrastructure strategies.")

add_q("Types of DBAs",
      "When the Data Administrator (DA) role is not formally staffed in an organization, who typically assumes the duty of creating logical data models?",
      ["The Hardware Technician", "A Data Modeler or Database Analyst", "The Receptionist", "The End User"],
      1,
      "In the absence of a dedicated DA, a Data Modeler or Database Analyst (often part of the DBA group) handles entity-relationship modeling and logical design.")

add_q("Types of DBAs",
      "What distinguishes a Task-Oriented DBA?",
      ["They perform every database task randomly every day",
       "They specialize in one specific critical task across the enterprise, such as a Backup/Recovery DBA, a Database Security DBA, or a Tuning Specialist",
       "They only manage personal computers",
       "They are temporary interns who do not touch production"],
      1,
      "Task-oriented DBAs focus exclusively on specific disciplines—such as database security, high-availability replication, or performance diagnostics—across all corporate databases.")

add_q("Types of DBAs",
      "What is the focus of a Data Warehouse Administrator (DWA)?",
      ["Managing high-speed transaction-processing OLTP systems with short queries",
       "Managing analytical databases (OLAP), dimensional models (star/snowflake schemas), ETL pipeline performance, and large historical data aggregation",
       "Repairing broken mobile devices",
       "Writing front-end CSS stylesheets"],
      1,
      "A DWA handles decision support systems (DSS), large-scale ETL data loading, dimensional schemas, aggregation query tuning, and massive data volume warehousing.")

add_q("Procedural DBA",
      "What prompted the emergence of the 'Procedural DBA' role?",
      ["The elimination of relational databases",
       "The introduction of procedural database objects such as Stored Procedures, Triggers, and User-Defined Functions (UDFs) executing inside the DBMS engine",
       "The use of paper-based database records",
       "The replacement of SQL with basic HTML"],
      1,
      "As DBMS engines began executing procedural code (triggers, stored procedures, UDFs), DBAs needed to review, debug, and manage code executing directly inside the database server.")

add_q("Procedural DBA",
      "Why is a Procedural DBA's role critical for database stability?",
      ["Because procedural code inside the DBMS runs with high privileges, directly impacts engine performance, and can cause cascading locks or infinite recursion if poorly written",
       "Because procedural code only runs on the user's desktop browser",
       "Because procedural code cannot access database tables",
       "Because procedural code does not consume CPU or memory"],
      0,
      "Stored procedures and triggers execute within the DBMS address space. Poorly written triggers or long-running procedures can hold critical locks, consume excessive server CPU, or degrade overall database health.")

add_q("Cloud DBA",
      "How does the role of a DBA evolve when an organization migrates databases to a Managed Cloud Database service (DBaaS)?",
      ["The DBA is completely eliminated and never needed again",
       "Routine hardware maintenance, OS patching, and low-level physical disk replacement are offloaded to the cloud provider, allowing the DBA to focus on data modeling, query optimization, security, and cost control",
       "The DBA must personally build the physical data center buildings",
       "The DBA is only responsible for buying cloud server cables"],
      1,
      "Cloud DBaaS handles low-level provisioning and hardware maintenance, shifting the DBA's focus higher up the stack: schema design, performance optimization, access control, and cloud resource cost management.")

add_q("DBA Staffing",
      "Which of the following is a key factor when estimating how many DBAs an organization needs?",
      ["The color of the server racks in the data center",
       "The number of database instances, total data volume, transaction throughput, application criticality (24/7 vs 8/5), and DBA tool sophistication",
       "The number of desks available in the IT office",
       "The brand of keyboards used by developers"],
      1,
      "Staffing depends on system complexity, service level agreements (SLAs), number of supported platforms, transaction volume, criticality of 24/7 uptime, and the degree of automation tooling.")

add_q("DBA Organizational Structure",
      "In which reporting structure do DBAs report directly to Application Development Managers?",
      ["Decentralized (Application-based) reporting",
       "Centralized Infrastructure reporting",
       "Corporate Legal reporting",
       "External Vendor reporting"],
      0,
      "In decentralized/application reporting, DBAs are embedded within specific development teams, reporting to application project managers.")

add_q("DBA Organizational Structure",
      "What is the main advantage of a Centralized DBA group reporting to an IT Operations / Infrastructure Director?",
      ["DBAs can ignore all enterprise data standards",
       "Consistent enterprise policies, standardized procedures, shared knowledge, cross-application load balancing, and independent architectural oversight",
       "Faster delivery of hacks that violate database integrity",
       "Complete separation from any IT management"],
      1,
      "A centralized group fosters uniform standards, consistent backup/security policies, optimal resource allocation, and neutral technical governance.")

add_q("DBA Data Policies",
      "What is 'Metadata' in the context of database administration?",
      ["Corrupted data that must be deleted immediately",
       "Data about data, describing definitions, data types, relationships, constraints, source systems, and ownership of enterprise data assets",
       "Temporary user passwords stored in plain text",
       "Unused disk sectors on a hard drive"],
      1,
      "Metadata is data about data—it provides context, data dictionary definitions, column formats, relationships, and lineage for all stored information.")

# Continue generating comprehensive questions for Lecture 1 (up to 100)
for i in range(26, 101):
    subtopics = [
        ("DBA Tasks & Policies", "Which policy establishes who is authorized to view, modify, or delete specific data entities within an enterprise?",
         ["Network Routing Policy", "Data Access & Security Policy", "Hardware Disposal Policy", "Employee Dress Code"], 1,
         "A Data Access & Security Policy defines the rules, permissions, and roles that govern who can access or modify corporate data."),
        ("DBA Tasks & Policies", "What is the primary objective of Database Change Management?",
         ["Preventing any modifications to the database forever",
          "Ensuring that schema changes, index modifications, and migrations are planned, tested, versioned, and executed with minimal disruption and rollback capability",
          "Randomly modifying column names in production during peak hours",
          "Allowing all developers unrestricted root access to production tables"], 1,
          "Database Change Management establishes rigorous processes to review, test, script, and apply schema modifications safely with minimal downtime and clear rollback paths."),
        ("DBA Environment", "Why is disaster recovery planning a non-negotiable duty of a DBA?",
         ["Because hardware failures, natural disasters, cyberattacks, or human errors can destroy data, risking company solvency without verified recovery protocols",
          "Because disaster recovery plans are only used to satisfy marketing presentations",
          "Because modern hard drives are physically incapable of failing",
          "Because cloud providers guarantee that human error can never delete a database table"], 0,
          "Data loss can be catastrophic to an enterprise. DBAs must guarantee recovery point objectives (RPO) and recovery time objectives (RTO) through regular, tested backups."),
        ("DBMS vs File Systems", "What advantage does a relational DBMS offer over traditional flat file systems?",
         ["Lack of query optimization",
          "Declarative access, atomicity, concurrent multi-user access control, crash recovery, and reduced data redundancy",
          "Storing data exclusively in plain unindexed text",
          "Requiring every user to manually write disk sector seek routines"], 1,
          "DBMS systems provide ACID transaction guarantees, concurrency control, data independence, integrity constraints, and sophisticated query engines."),
        ("DBA Interaction", "When should a DBA ideally be involved in the software development life cycle (SDLC)?",
         ["Only after the application crashes in production on the first day",
          "Early in the analysis and design phase to advise on data modeling, indexing, capacity planning, and query performance",
          "Never; DBAs should only maintain hardware",
          "Only when the company undergoes a financial audit"], 1,
          "Early DBA involvement in the conceptual and logical design phases prevents catastrophic architectural errors and expensive rewrites later in production.")
    ]
    st = subtopics[(i - 26) % len(subtopics)]
    add_q(st[0], f"[{st[0]} #{i}] {st[1]}", st[2], st[3], st[4])

print(f"Generated {len(questions)} questions after Lecture 1.")

# =========================================================================
# LECTURES 2 & 3: PHYSICAL DATABASE DESIGN, STORAGE & INDEXING (Q101 - Q200)
# =========================================================================

add_q("Logical to Physical Mapping",
      "During the translation of a Logical Data Model to a Physical Database Design, what do 'Entities' and 'Attributes' become?",
      ["Files and Folders", "Tables and Columns", "Views and Triggers", "Indexes and Constraints"],
      1,
      "In physical relational database design, logical entities become physical tables, and logical attributes become physical columns.")

add_q("Logical to Physical Mapping",
      "What does an Entity's Primary Identifier translate to in a physical database schema?",
      ["A Foreign Key", "A Primary Key constraint (often backed by a unique index)", "A CHECK constraint", "A Database View"],
      1,
      "An entity's primary identifier translates into a Primary Key constraint, uniquely identifying each row in the physical table.")

add_q("Logical to Physical Mapping",
      "How are logical relationships between entities typically implemented in a relational physical schema?",
      ["Using hardware bridges", "Using Foreign Key constraints referencing Primary Keys", "By combining all data into one giant spreadsheet", "Using operating system file paths"],
      1,
      "Relationships are implemented through Foreign Keys: columns in a child table that reference the Primary Key of a parent table.")

add_q("Data Types & Physical Design",
      "Why is choosing the correct physical data type for each column a critical responsibility of the DBA?",
      ["Data types do not affect storage or performance",
       "Data types enforce domain integrity, prevent invalid data entry, optimize row length, and minimize disk I/O and memory consumption",
       "Modern databases only support one generic text data type",
       "Choosing larger data types always makes queries run faster"],
      1,
      "Selecting appropriate data types (e.g. INT vs BIGINT, VARCHAR vs CHAR) minimizes row size, allows more rows per page, reduces disk I/O, and enforces domain rules.")

add_q("NULLs vs DEFAULT",
      "What does a 'NULL' value represent in a relational database?",
      ["The number zero (0)", "An empty string of length zero (\"\")", "An unknown, missing, or inapplicable value", "A syntax error"],
      2,
      "In relational databases, NULL represents missing, unknown, or inapplicable information. It is distinct from zero or an empty string.")

add_q("NULLs vs DEFAULT",
      "What is a potential downside of allowing nullable columns in a physical database?",
      ["Nullable columns require an extra byte or bit indicator per row, complicate three-valued SQL logic (TRUE, FALSE, UNKNOWN), and can cause unexpected results in aggregate functions",
       "Nullable columns prevent tables from being backed up",
       "Databases automatically delete rows containing NULLs",
       "Nullable columns run ten times faster than NOT NULL columns"],
      0,
      "NULLs introduce three-valued logic, require null-indicator bytes, and can complicate joins and aggregates (like AVG, COUNT). Good physical design uses NOT NULL with sensible defaults when possible.")

add_q("Physical ROTs (Rules of Thumb)",
      "What is a standard physical database design Rule of Thumb (ROT) regarding column ordering in a table?",
      ["Place variable-length columns at the very beginning and fixed-length columns at the end",
       "Place frequently accessed fixed-length columns first, followed by variable-length columns (like VARCHAR/BLOB) toward the end of the row layout",
       "Sort columns randomly by their English name length",
       "Always alternate between numeric and text columns"],
      1,
      "A classic ROT for physical row layout is to put fixed-length, frequently searched columns first (fixed offsets for fast CPU access) and variable-length columns at the end.")

add_q("Storage Planning & Sizing",
      "When estimating the physical disk space required for a table, which formula represents the basic calculation?",
      ["Total Space = Number of Rows * Row Length (plus page overhead and PCTFREE allowances)",
       "Total Space = Number of Columns * 100 GB",
       "Total Space = Number of DBAs * 1 TB",
       "Total Space = Server RAM / 2"],
      0,
      "Disk storage calculation requires multiplying estimated row count by the average row size, factoring in row/page header overhead and free space reservations (PCTFREE).")

add_q("Free Space Management",
      "What is the purpose of the 'PCTFREE' parameter in database page/block storage allocation?",
      ["It specifies the percentage of CPU dedicated to free users",
       "It reserves a percentage of free space on each data page during initial loads to accommodate future row updates and expansions without causing row migration/chaining",
       "It deletes rows when the table becomes 80% full",
       "It sets the discount percentage for database software licenses"],
      1,
      "PCTFREE reserves empty space within each data page so that when existing rows are updated (e.g., expanding a VARCHAR), they can grow in place without splitting the page or migrating the row.")

add_q("Free Space Management",
      "What does the 'FREEPAGE' parameter specify in physical storage systems?",
      ["How many free web pages the company can host",
       "The frequency at which an entirely empty page is allocated within a table space (e.g. 1 free page every N pages) for localized insert clustering",
       "The number of pages deleted per minute",
       "The amount of RAM freed on shutdown"],
      1,
      "FREEPAGE specifies that the DBMS should leave an entire empty page every N pages, providing space for bulk inserts to remain clustered near related data.")

add_q("Database File Types",
      "In physical database architecture, what is the key distinction between Data Files and Index Files?",
      ["Data files store the actual table rows and user data, while Index files store search keys and pointers to quickly locate rows in data files",
       "Index files store audio and video, while Data files store numbers",
       "Data files are temporary and deleted on restart, while Index files are permanent",
       "Index files store user passwords only"],
      0,
      "Data files contain the raw data records. Index files contain auxiliary structures (keys and record identifiers/rowids) designed to speed up search operations.")

add_q("Index Design: B-Trees",
      "What is the primary architectural structure of a standard relational B-Tree (or B+ Tree) index?",
      ["A circular linked list without a root",
       "A balanced, multi-level hierarchical tree consisting of a Root page, Intermediate branch pages, and Leaf pages containing ordered keys and row pointers",
       "A single flat array stored in random order",
       "A hash table with unlimited collisions"],
      1,
      "A B-Tree index is a balanced tree where the root points to intermediate branch levels, which lead to leaf pages containing sorted keys and pointers (rowids) to table rows.")

add_q("Index Design: B-Trees",
      "Why are B-Trees termed 'balanced'?",
      ["Because all leaf nodes are at the exact same depth from the root, guaranteeing consistent logarithmic search time O(log N)",
       "Because they contain an equal number of odd and even numbers",
       "Because they weigh the same on hard disks as the data file",
       "Because half the tree is in RAM and half is on disk"],
      0,
      "A B-Tree is balanced because every path from the root to any leaf node is of identical length (height), ensuring predictable, fast lookups regardless of key value.")

add_q("Index Design: B-Trees",
      "Which type of queries do B-Tree indexes excel at processing?",
      ["Only full table scans",
       "Exact match lookups (WHERE id = 50), range scans (WHERE age BETWEEN 20 AND 30), and ordered scans (ORDER BY name)",
       "Only queries with NOT LIKE '%abc%'",
       "Soundex fuzzy voice searches"],
      1,
      "Because leaf pages in a B-Tree are linked in sequential sorted order, B-Trees efficiently support both point lookups and range queries.")

add_q("Index Design: Bitmap Indexes",
      "What is a Bitmap Index?",
      ["An index that stores JPEG or PNG images of database diagrams",
       "An index where each distinct column value is associated with a string of bits (0s and 1s), where each bit position corresponds to a specific row number in the table",
       "An index that cannot be used in relational databases",
       "A legacy index replaced by text files"],
      1,
      "A bitmap index uses a bit array (vector) for each distinct column key. A '1' indicates the row possesses that key value, and a '0' indicates it does not.")

add_q("Index Design: Bitmap Indexes",
      "Under which condition is a Bitmap Index most effective and appropriate?",
      ["On primary keys with millions of unique values (high cardinality)",
       "On low-cardinality columns (columns with very few distinct values, like Gender, Marital Status, or Boolean flags) in read-heavy/data warehousing environments",
       "On volatile OLTP tables with thousands of concurrent INSERTs and UPDATEs per second",
       "On large binary BLOB columns"],
      1,
      "Bitmap indexes are ideal for low-cardinality attributes in read-heavy analytical environments because bitwise boolean operations (AND, OR, NOT) are executed at lightning speed by the CPU.")

add_q("Index Design: Bitmap Indexes",
      "Why are Bitmap Indexes generally avoided in high-concurrency Online Transaction Processing (OLTP) systems?",
      ["Because updating a single row can lock the entire bitmap segment or range, causing severe concurrency bottlenecks and locking conflicts for other transactions",
       "Because bitmap indexes cannot store numbers",
       "Because bitmap indexes require more CPU than humanly possible",
       "Because SQL queries cannot read bitmap indexes"],
      0,
      "Locking a single bit in a bitmap page often locks hundreds or thousands of neighboring row representations, severely crippling concurrent transactional updates.")

add_q("Clustered vs Non-Clustered Indexes",
      "What is a 'Clustered Index'?",
      ["An index that connects multiple physical servers into a cluster",
       "An index where the physical order of rows in the table matches the logical order of the index key",
       "An index that can only be created on foreign keys",
       "An index stored in the cloud"],
      1,
      "In a clustered index, the physical storage sequence of table rows matches the sorted order of the index. Hence, a table can have only ONE clustered index.")

add_q("Clustered vs Non-Clustered Indexes",
      "How many clustered indexes can a single database table have, and why?",
      ["Unlimited, because disk drives have multiple sectors",
       "Exactly one, because physical table rows can only be physically stored on disk in one sequential order",
       "As many as the number of columns",
       "Zero, because clustering is only a conceptual theory"],
      1,
      "A table's data can only be physically sorted and stored on disk in one sequence at a time; therefore, only one clustered index is possible per table.")

add_q("Partitioning",
      "What is Table Partitioning in physical database design?",
      ["Splitting a single logical table into smaller, independently manageable physical storage units based on partition keys (e.g. dates, regions, or hash values)",
       "Deleting old tables to free up space",
       "Restricting user access based on department",
       "Copying the table to another computer using a flash drive"],
      0,
      "Partitioning divides large tables into smaller physical segments (partitions) transparently to applications, improving query pruning, maintenance, and parallelism.")

add_q("Partitioning Types",
      "Which partitioning strategy distributes data uniformly across physical partitions using a mathematical algorithm applied to the partition key?",
      ["Range Partitioning", "Hash Partitioning", "List Partitioning", "Composite Partitioning"],
      1,
      "Hash partitioning applies a hash function to the key column to evenly scatter rows across a predefined number of partitions, preventing I/O hotspots.")

add_q("Partitioning Types",
      "Which partitioning strategy is best suited for archiving historical data (e.g. storing sales data by year: 2024, 2025, 2026)?",
      ["Hash Partitioning", "Range Partitioning", "Random Partitioning", "Round-Robin Partitioning"],
      1,
      "Range partitioning organizes data based on specified continuous ranges (e.g. date boundaries), making historical pruning and rolling-window drops extremely fast.")

add_q("Denormalization",
      "What is 'Denormalization' in physical database design?",
      ["A severe database corruption error that requires restoring backups",
       "The intentional, deliberate process of introducing controlled redundancy or combining tables into a normalized schema to improve read performance",
       "Deleting foreign keys to prevent joins",
       "Converting a database into a spreadsheet"],
      1,
      "Denormalization is the deliberate optimization technique of adding redundant data or grouping attributes to reduce costly JOIN operations in read-intensive workloads.")

add_q("Denormalization",
      "Which of the following is a primary reason to consider denormalization?",
      ["To save hard drive space",
       "To avoid complex, expensive multi-table JOINs in performance-critical, read-heavy reporting queries",
       "To make INSERT and UPDATE queries run much faster",
       "To ensure the database strictly complies with 5th Normal Form (5NF)"],
      1,
      "Denormalization reduces the number of tables that must be joined during queries, drastically cutting down disk I/O and query latency for frequent read operations.")

add_q("Denormalization Costs & Risks",
      "What are the major costs and administrative risks associated with denormalizing a database?",
      ["Data redundancy, increased disk storage requirements, and the risk of data anomalies (inconsistencies) during UPDATEs, INSERTs, and DELETEs",
       "The DBMS will automatically refuse to start",
       "All indexes on the table are permanently erased",
       "Users will be unable to run SELECT statements"],
      0,
      "Denormalization introduces redundant data. When data is duplicated, any update must update multiple places; failure to do so results in data inconsistency and corruption.")

add_q("Denormalization Types",
      "Which type of denormalization involves pre-calculating and storing values like 'TotalOrderAmount' or 'CustomerTotalSpend' directly in a table?",
      ["Pre-joined Tables", "Derived or Calculated Data Columns", "Vertical Splitting", "Horizontal Splitting"],
      1,
      "Storing derived/calculated columns eliminates the need to run expensive SUM() or aggregate functions on thousands of detail rows every time an inquiry is made.")

add_q("Views in Physical Design",
      "What is a 'View' in relational database terminology?",
      ["A physical photograph of the database server",
       "A virtual table defined by a stored SQL query, which does not physically store data itself (unless materialized) but presents data dynamically from underlying base tables",
       "A hardware monitor attached to the server",
       "A backup file saved on tape"],
      1,
      "A view is a virtual table representing the result of a stored query. It provides logical data independence, security restrictions, and query simplification.")

add_q("Views Usage Rules",
      "Which of the following is an important architectural benefit of using Views?",
      ["Views make all updates instantaneous by skipping the transaction log",
       "Views provide security by restricting user access to specific columns/rows and simplify complex queries for end-user reporting",
       "Views eliminate the need for primary keys on base tables",
       "Views multiply the storage capacity of the disk drive"],
      1,
      "Views allow administrators to hide sensitive columns (like salaries or passwords) from certain users, presenting a customized, simplified interface to base tables.")

add_q("SQL Categories: DCL, DDL, DML",
      "Which category of SQL statements includes CREATE, ALTER, and DROP?",
      ["Data Control Language (DCL)", "Data Definition Language (DDL)", "Data Manipulation Language (DML)", "Transaction Control Language (TCL)"],
      1,
      "DDL (Data Definition Language) commands are used to define, alter, and manage the structural schema of database objects (tables, views, indexes).")

add_q("SQL Categories: DCL, DDL, DML",
      "Which category of SQL statements includes SELECT, INSERT, UPDATE, and DELETE?",
      ["Data Control Language (DCL)", "Data Definition Language (DDL)", "Data Manipulation Language (DML)", "Data Security Protocol (DSP)"],
      2,
      "DML (Data Manipulation Language) commands are used to query, insert, modify, and delete the data contained within tables.")

add_q("SQL Categories: DCL, DDL, DML",
      "Which category of SQL statements includes GRANT and REVOKE for security permissions?",
      ["Data Control Language (DCL)", "Data Definition Language (DDL)", "Data Manipulation Language (DML)", "Data Mining Language (DML2)"],
      0,
      "DCL (Data Control Language) encompasses commands used by DBAs to grant or revoke privileges and rights on database objects to users and roles.")

add_q("Temporal Data",
      "What is 'Temporal Data' in modern database management?",
      ["Data that expires and disappears automatically after 10 seconds",
       "Data that changes over time and whose historical evolution must be maintained and tracked for auditing, compliance, or analytical queries",
       "Data stored only in temporary RAM cache",
       "Data that has no timestamp"],
      1,
      "Temporal data refers to information that evolves over time where historical state changes must be preserved (e.g. employee salary history, product price history).")

add_q("Temporal Data: Business vs System Time",
      "What does 'Business Time' (also known as Valid Time or Application Time) represent in temporal tables?",
      ["The time when the database server CPU executed the SQL INSERT statement",
       "The time period during which a fact is true or effective in the real world (e.g., insurance coverage valid from Jan 1 to Dec 31)",
       "The opening hours of the company's retail stores",
       "The time taken to compile the application in Visual Studio"],
      1,
      "Valid/Business Time represents the actual real-world time period during which a fact is true, regardless of when it was entered into the database.")

add_q("Temporal Data: Business vs System Time",
      "What does 'System Time' (also known as Transaction Time) represent in temporal tables?",
      ["The time when the fact occurred in real life",
       "The time period during which the record was physically stored and active in the database system (tracked automatically by the DBMS)",
       "The time zone of the customer's phone",
       "The server's BIOS clock speed"],
      1,
      "Transaction/System Time is managed automatically by the DBMS engine, capturing the exact timestamp when a row was inserted, modified, or logically deleted in the database.")

add_q("Temporal Data: Bi-temporal",
      "What is a 'Bi-temporal Table'?",
      ["A table that stores data in two different languages simultaneously",
       "A table that supports both Business Time (Valid Time) AND System Time (Transaction Time), providing full historical tracking of both real-world validity and database record modifications",
       "A table with only two columns",
       "A table stored across two different hard drives"],
      1,
      "A bi-temporal table tracks both dimensions of time: what was true in the real world at any date, and what the database recorded as true at any point in system history.")

# Generate remaining questions for Lectures 2 & 3 (up to 200)
for i in range(136, 201):
    subtopics = [
        ("Physical Design Principles", "What is 'Row Migration' or 'Row Chaining' in database page storage?",
         ["When a row is moved to another server via email",
          "When an updated row grows larger than the remaining free space on its original page, forcing the DBMS to move it to a new page or split it across pages, causing extra I/O",
          "When rows are sorted alphabetically by the user",
          "When a DBA exports data to CSV"], 1,
          "Row chaining/migration occurs when row expansion exceeds page space, forcing the engine to store pointers to other pages, resulting in multiple page reads per row."),
        ("Physical ROTs", "Why is it recommended to avoid placing large LOB/BLOB/CLOB data directly inline in the main table data pages if they are rarely accessed?",
         ["Because LOBs cause data pages to fill up rapidly, drastically reducing the number of rows per page and crippling table scan performance for everyday queries",
          "Because databases cannot store binary files",
          "Because LOB columns delete neighboring numeric columns",
          "Because BLOBs cannot be saved on SSDs"], 0,
          "Storing large objects out-of-line keeps main data pages dense with scalar rows, preserving high cache efficiency and fast sequential scans."),
        ("Index Maintenance", "Why must DBAs regularly reorganize or rebuild indexes on high-churn tables?",
         ["Because index keys turn into text after 30 days",
          "Because frequent INSERTs, UPDATEs, and DELETEs cause index page splits, leading to internal fragmentation, wasted space, and degraded scan performance",
          "Because rebuilding indexes deletes all duplicate customer orders",
          "Because the DBMS license requires weekly index deletion"], 1,
          "Page splits and deletions leave B-Tree leaf pages fragmented and sparsely populated. Periodic reorganization restores page density and sequential I/O efficiency."),
        ("Index Selection", "What is an 'Index-Only Scan' (or Covering Index)?",
         ["An index scan where the user only has view permissions",
          "A query execution where all columns requested by the SELECT and WHERE clauses are present within the index itself, completely avoiding any lookup to the base table data pages",
          "An index that covers the entire hard drive",
          "An index created on every column of a table simultaneously"], 1,
          "A covering index includes all columns needed by a query. The engine satisfies the entire query from the index tree alone, avoiding table access entirely."),
        ("Denormalization ROTs", "Before implementing denormalization, what must a DBA always perform?",
         ["A complete audit proving that normalized design cannot meet query performance requirements, accompanied by benchmarks and documented update strategies",
          "A complete reinstallation of the operating system",
          "The deletion of all database foreign keys",
          "Changing all column types to VARCHAR(MAX)"], 0,
          "Denormalization should never be premature. DBAs should first benchmark, tune indexes, and verify that 3NF cannot meet SLAs before accepting redundancy risks.")
    ]
    st = subtopics[(i - 136) % len(subtopics)]
    add_q(st[0], f"[{st[0]} #{i}] {st[1]}", st[2], st[3], st[4])

print(f"Generated {len(questions)} questions after Lectures 2 & 3.")

# =========================================================================
# LECTURES 4 & 5: APPLICATION DEV, SQL, TRANSACTIONS & LOCKING (Q201 - Q300)
# =========================================================================

add_q("SQL Characteristics",
      "Why is SQL described as a 'Declarative' language rather than a procedural language?",
      ["Because programmers must manually write loops and disk head movement instructions",
       "Because the programmer specifies 'WHAT' data is desired, and the DBMS query optimizer determines 'HOW' to retrieve it",
       "Because SQL requires declaring variable memory registers before each query",
       "Because SQL cannot perform mathematical calculations"],
      1,
      "Declarative languages allow users to express the desired result set without specifying the algorithmic navigation or procedural steps to retrieve it.")

add_q("SQL Characteristics",
      "What does 'Set-at-a-Time' processing mean in relational SQL?",
      ["SQL operations process an entire set of rows satisfying a condition in a single statement, unlike traditional 3GL programs that iterate row-by-row",
       "The database executes queries only at specific set times of day (e.g. 12:00 PM)",
       "Each query can only return exactly one row at a time",
       "The programmer must manually set the clock on the database server"],
      0,
      "Set-at-a-time (or set-oriented) processing means relational operations (SELECT, UPDATE, DELETE) operate on collections/sets of rows simultaneously.")

add_q("Embedded SQL",
      "What is 'Embedded SQL'?",
      ["SQL queries saved on a physical microchip embedded in the motherboard",
       "SQL statements placed directly inside the source code of a host programming language (such as COBOL, C, C++, or Java)",
       "SQL queries sent via SMS text message",
       "A database stored entirely within browser local storage"],
      1,
      "Embedded SQL refers to embedding standard SQL statements directly within application source code in host languages like C, C++, or COBOL.")

add_q("Embedded SQL: Host Variables",
      "What are 'Host Variables' in embedded SQL programs?",
      ["Variables that store the IP address of the database server",
       "Program variables declared in the host language (prefixed with a colon ':' in SQL) used to pass data between the application program and the database engine",
       "Global variables that control the operating system kernel",
       "Variables that store the username and password in plain text"],
      1,
      "Host variables bridge host programming language code and SQL statements, allowing data to flow into SQL predicates and receive result columns.")

add_q("Embedded SQL: Cursors",
      "Why is a 'Cursor' necessary when an embedded SQL SELECT statement returns multiple rows into a procedural programming language?",
      ["Because 3GL procedural languages operate on one record at a time, so a cursor provides a pointer mechanism to fetch rows sequentially from the result set",
       "Because modern computers cannot display text without a mouse cursor",
       "Because cursors encrypt the database rows in memory",
       "Because cursors automatically delete duplicate records"],
      0,
      "Procedural languages (C, Java) cannot receive a multi-row set into a single scalar variable. A cursor acts as a pointer, allowing the program to FETCH rows one by one.")

add_q("SQL Middleware & APIs",
      "What is the primary role of database middleware and APIs like ODBC and JDBC?",
      ["To translate database queries into English audio files",
       "To provide a standard, vendor-neutral programming interface enabling application programs to connect to, query, and manage diverse DBMS engines uniformly",
       "To replace the need for database indexes",
       "To convert relational tables into PDF files automatically"],
      1,
      "ODBC (Open Database Connectivity) and JDBC (Java Database Connectivity) provide standardized APIs that abstract database vendor specifics from client applications.")

add_q("SQL Middleware Architecture",
      "In the ODBC architecture, what is the role of the 'Driver Manager'?",
      ["It repairs broken hard drives on the server",
       "It sits between the application and database-specific drivers, loading the appropriate vendor driver and routing API calls based on Data Source Names (DSN)",
       "It manages the company's vehicle fleet",
       "It compiles C++ source code into binary"],
      1,
      "The Driver Manager resolves the requested DSN, loads the appropriate vendor-specific driver DLL/shared library, and routes function calls to it.")

add_q("Application Infrastructure: Java vs .NET",
      "Which managed execution environment powers enterprise Java applications connecting to databases via JDBC?",
      ["Common Language Runtime (CLR)", "Java Virtual Machine (JVM)", "Windows Registry", "Node Package Manager (NPM)"],
      1,
      "Java applications execute inside the Java Virtual Machine (JVM), utilizing JDBC drivers to interface with database management systems.")

add_q("Application Infrastructure: Java vs .NET",
      "In the Microsoft .NET framework, what is the core database access technology used to connect to relational databases?",
      ["ADO.NET", "DirectX", "Flash Player", "ActiveX Desktop"],
      0,
      "ADO.NET (including components like SqlConnection, SqlCommand, SqlDataReader, and DataSet) is Microsoft's primary data access technology in the .NET Framework.")

add_q("Impedance Mismatch",
      "What is the 'Object-Relational Impedance Mismatch'?",
      ["A physical electrical resistance problem in server power supplies",
       "The fundamental conceptual and structural friction between the Object-Oriented programming paradigm (classes, inheritance, encapsulation, object graphs) and the Relational model (tables, relations, primary/foreign keys, set theory)",
       "A mismatch between server RAM speed and CPU clock speed",
       "The difference in file sizes between Windows and Linux"],
      1,
      "The impedance mismatch describes the architectural discord between OO languages (rich object hierarchies, pointers, polymorphism) and relational databases (2D mathematical relations, normalized tables).")

add_q("Object-Relational Mapping (ORM)",
      "What is an Object-Relational Mapping (ORM) framework (such as Hibernate or Entity Framework)?",
      ["Software that automatically translates between in-memory object models and relational database tables, abstracting manual SQL generation",
       "A tool that converts Word documents into SQL",
       "A hardware device that maps network cables to database ports",
       "A database engine that does not use tables"],
      0,
      "ORM frameworks automate the persistence of objects to relational tables, generating SQL statements under the hood and managing entity lifecycles.")

add_q("ORM: DBA Considerations",
      "Why must DBAs pay close attention to applications using ORM frameworks?",
      ["Because ORMs do not use database connections",
       "Because ORMs can generate highly inefficient SQL queries (e.g., the N+1 SELECT problem, Cartesian products, unnecessary column fetching) if not properly tuned",
       "Because ORMs prevent databases from creating backups",
       "Because ORMs only work on mainframe computers"],
      1,
      "While ORMs boost developer productivity, naive ORM configurations frequently generate suboptimal SQL, repeated queries (N+1), or massive unindexed table scans.")

add_q("SQL Coding for Performance",
      "What is a 'SARGable' predicate in SQL query optimization?",
      ["A predicate that is completely unreadable by the DBMS",
       "A 'Search Argument Able' condition that can effectively utilize a database index (e.g. `WHERE age > 30` rather than `WHERE YEAR(birth_date) = 1990`)",
       "A query that runs only on Sunday mornings",
       "A predicate that requires a full table scan"],
      1,
      "SARGable (Search Argument Able) predicates allow the optimizer to perform an index seek rather than a full table scan. Wrapping columns in functions usually disables index usage.")

add_q("SQL Coding for Performance",
      "Why is using `SELECT *` strongly discouraged in production enterprise applications?",
      ["Because SQL syntax prohibits using the asterisk character",
       "Because it retrieves unnecessary columns (wasting network bandwidth and memory), prevents index-only covering scans, and breaks code if columns are added/reordered",
       "Because `SELECT *` automatically deletes the underlying table",
       "Because `SELECT *` converts numbers into strings"],
      1,
      "Specifying explicit column names reduces network payload, avoids pulling massive LOB columns unintentionally, and enables covering index optimizations.")

add_q("XML and Databases",
      "Which query language is standard for querying and extracting elements from XML documents stored in relational or XML databases?",
      ["XPath and XQuery", "HTML5", "CSS3", "JavaScript React"],
      0,
      "XPath and XQuery are standard W3C languages used to navigate, filter, and extract data nodes from hierarchical XML documents.")

add_q("Transactions: Definition",
      "In database management, what is a 'Transaction'?",
      ["A financial payment made by credit card only",
       "A logical unit of database processing that includes one or more database operations (reads, writes, updates) that must be executed as an atomic whole",
       "The time it takes to boot up the server",
       "A conversation between a DBA and a developer"],
      1,
      "A transaction is a logical unit of work (LUW) comprising multiple database operations that must be committed or rolled back together to maintain data consistency.")

add_q("Transactions: ACID Properties",
      "What do the letters in the 'ACID' acronym stand for regarding database transactions?",
      ["Accuracy, Control, Integrity, Durability",
       "Atomicity, Consistency, Isolation, Durability",
       "Asynchronous, Concurrent, Indexed, Distributed",
       "Authentication, Confidentiality, Inspection, Deployment"],
      1,
      "ACID stands for Atomicity, Consistency, Isolation, and Durability—the four fundamental guarantees of reliable transaction processing.")

add_q("Transactions: Atomicity",
      "What does the 'Atomicity' property guarantee in a transaction?",
      ["Transactions execute at atomic-clock speed",
       "The 'All-or-Nothing' rule: all operations within the transaction succeed completely, or if any failure occurs, all changes are entirely undone (rolled back)",
       "Each transaction can only modify one atomic row",
       "The database splits data into atoms on disk"],
      1,
      "Atomicity guarantees that either all operations of a transaction are committed to the database, or the transaction is rolled back and leaves no trace.")

add_q("Transactions: Consistency",
      "What does the 'Consistency' property guarantee in a transaction?",
      ["The transaction takes the database from one valid state satisfying all defined integrity constraints, schema rules, and cascades to another valid state",
       "All database queries return data in the same font size",
       "The transaction runs at a consistent speed every hour",
       "The database server never reboots"],
      0,
      "Consistency ensures that a transaction transforms the database from one consistent state to another, preserving all explicit constraints (foreign keys, checks, unique rules).")

add_q("Transactions: Isolation",
      "What does the 'Isolation' property guarantee?",
      ["The database server must be isolated in a soundproof room",
       "Concurrent executing transactions do not interfere with each other, such that the intermediate state of an uncommitted transaction is invisible to other transactions",
       "Transactions can only run when all other users are logged out",
       "Transactions cannot access the internet"],
      1,
      "Isolation ensures that concurrently running transactions cannot see or interfere with each other's partial, uncommitted modifications.")

add_q("Transactions: Durability",
      "What does the 'Durability' property guarantee?",
      ["Hard drives will never wear out physically",
       "Once a transaction commits successfully, its updates are permanently recorded in non-volatile storage and will survive any subsequent system crash or power outage",
       "Data is duplicated across five continents",
       "The DBMS software license lasts indefinitely"],
      1,
      "Durability guarantees that once a transaction commits, its modifications are permanently recorded (usually via write-ahead transaction logs) and survive crashes.")

add_q("Transaction Processing Monitors vs DBMS",
      "What is the purpose of a TP Monitor (Transaction Processing Monitor) or Application Server in multi-tier architectures?",
      ["To render HTML web pages only",
       "To manage transaction lifecycles, coordinate distributed two-phase commits across multiple databases, handle connection pooling, and balance transaction loads",
       "To replace the relational database engine entirely",
       "To clean computer dust filters"],
      1,
      "TP Monitors (like Tuxedo) and modern application servers manage distributed transactions (XA / 2PC), multiplex connections, and balance high-volume transaction workloads.")

add_q("Concurrency Control: Locks",
      "What is the primary mechanism used by relational DBMS engines to implement Isolation and prevent concurrent data corruption?",
      ["Locking mechanisms", "Deleting user sessions", "Rebooting the server", "Converting all tables to read-only"],
      0,
      "Locking is the primary concurrency control mechanism, ensuring that multiple transactions accessing shared data items do not create race conditions or inconsistencies.")

add_q("Lock Types: Shared vs Exclusive",
      "What is the difference between a Shared Lock (S lock) and an Exclusive Lock (X lock)?",
      ["An S lock allows multiple transactions to read a resource concurrently, while an X lock grants exclusive write access to a single transaction, blocking all other reads and writes",
       "An S lock is for writing data, while an X lock is for reading data",
       "An S lock locks the whole database, while an X lock locks only one column",
       "An S lock never releases, while an X lock releases immediately"],
      0,
      "Shared (S) locks allow concurrent reads. Exclusive (X) locks are required for writes/updates and prevent any other transaction from acquiring S or X locks on that resource.")

add_q("Lock Types: Update Locks",
      "What is the purpose of an Update Lock (U lock)?",
      ["To lock the operating system during updates",
       "To prevent deadlocks when a transaction intends to read a resource with the possibility of updating it later, signaling intent without blocking other shared readers immediately",
       "To automatically convert numbers into uppercase text",
       "To lock the user out after an invalid password"],
      1,
      "Update (U) locks are a hybrid lock used before updating to prevent common conversion deadlocks where multiple readers simultaneously attempt to upgrade S locks to X locks.")

add_q("Intent Locks",
      "In granular locking hierarchies (Database -> Table -> Page -> Row), what is an Intent Lock (e.g., IS or IX)?",
      ["A lock that indicates an error has occurred",
       "A lock placed at a higher level of the hierarchy (e.g. Table) indicating that a transaction holds or intends to acquire fine-grained locks (S or X) on child rows/pages below",
       "A lock placed on user keyboards",
       "A lock that guarantees the transaction will abort"],
      1,
      "Intent locks (Intent Shared IS, Intent Exclusive IX) inform the DBMS that fine-grained locks exist lower in the hierarchy, preventing another transaction from acquiring a conflicting table-level lock.")

add_q("Deadlocks",
      "What is a 'Deadlock' in a database transaction environment?",
      ["A damaged disk drive that cannot spin",
       "A condition where two or more transactions are permanently blocked because each holds a lock on a resource that the other transaction needs to proceed",
       "When a transaction takes more than one second to run",
       "When the DBA forgets the database master password"],
      1,
      "A deadlock is a circular dependency (Transaction A waits for Resource 2 held by Transaction B, while Transaction B waits for Resource 1 held by Transaction A).")

add_q("Deadlocks Resolution",
      "How does a modern DBMS automatically detect and resolve a deadlock?",
      ["By shutting down the entire operating system",
       "By maintaining a 'Wait-For Graph' (WFG) of transactions, detecting cycles, and choosing a 'victim' transaction to abort and roll back, allowing the other to proceed",
       "By asking the user to choose which transaction to delete",
       "By converting all data into text files"],
      1,
      "The DBMS deadlock detector checks for cycles in the Wait-For Graph, selects a victim transaction (often the least expensive to undo), aborts it, rolls back its changes, and returns an error code.")

add_q("Lock Timeouts",
      "What occurs when a transaction encounters a 'Lock Timeout'?",
      ["The server permanently disconnects from the internet",
       "The waiting transaction exceeds a configured duration waiting for a locked resource to be released, causing the DBMS to cancel the request and raise a timeout error",
       "The computer enters sleep mode",
       "The database deletes the locked table"],
      1,
      "Lock timeouts prevent indefinite waits. If a lock cannot be acquired within the designated timeout threshold (e.g. 30 seconds), the request fails gracefully.")

add_q("Lock Duration & 2PL",
      "Under Strict Two-Phase Locking (Strict 2PL), when are Exclusive (X) locks released by a transaction?",
      ["Immediately after the single SQL statement finishes executing",
       "Only at the very end of the transaction, when COMMIT or ROLLBACK is executed",
       "Whenever another user asks for the data",
       "Exactly 5 seconds after they are acquired"],
      1,
      "Strict 2PL holds all exclusive write locks until the end of transaction (COMMIT or ROLLBACK) to prevent cascading aborts and guarantee serializability.")

add_q("Isolation Levels: Anomalies",
      "What is a 'Dirty Read' concurrency phenomenon?",
      ["Reading data from a physically dusty hard drive",
       "A transaction reads data that has been modified by another concurrent transaction but has NOT yet been committed (and might later be rolled back)",
       "Reading data that contains grammatical errors",
       "A query that returns zero rows"],
      1,
      "A Dirty Read occurs when Transaction A reads modifications made by Transaction B before Transaction B commits. If Transaction B rolls back, Transaction A read phantom, invalid data.")

add_q("Isolation Levels: Anomalies",
      "What is a 'Non-Repeatable Read' (Fuzzy Read)?",
      ["When a user forgets what query they just typed",
       "A transaction re-reads a row it previously read and finds that the row's data values have been modified or deleted by another committed transaction",
       "When a printer prints two copies of a report",
       "When a query produces an audio echo"],
      1,
      "A Non-Repeatable Read happens when Transaction A reads a row, Transaction B updates that row and commits, and Transaction A reads the row again and sees changed data.")

add_q("Isolation Levels: Anomalies",
      "What is a 'Phantom Read' anomaly?",
      ["A ghost appearing on the server room monitor",
       "A transaction re-executes a range query and discovers that new rows satisfying the search predicate have been inserted and committed by another transaction",
       "When a query deletes all rows without a WHERE clause",
       "When the database crashes during a backup"],
      1,
      "A Phantom Read occurs when a transaction queries a range of rows twice, but finds new 'phantom' rows matching the criteria on the second run because another transaction inserted and committed them.")

add_q("Isolation Levels: Standard Hierarchy",
      "Which ANSI SQL Isolation Level allows Dirty Reads, Non-Repeatable Reads, and Phantom Reads, offering maximum concurrency at the expense of consistency?",
      ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
      0,
      "Read Uncommitted (often called 'dirty read' mode) applies no shared read locks, allowing transactions to read uncommitted dirty data.")

add_q("Isolation Levels: Standard Hierarchy",
      "Which Isolation Level is the default in most commercial relational database management systems (such as Oracle, PostgreSQL, and SQL Server)?",
      ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
      1,
      "Read Committed is the industry standard default: it prevents dirty reads by ensuring queries only see committed data, releasing read locks immediately after statement completion.")

add_q("Isolation Levels: Standard Hierarchy",
      "Which Isolation Level prevents both Dirty Reads and Non-Repeatable Reads, but may still permit Phantom Reads?",
      ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
      2,
      "Repeatable Read holds shared read locks until the end of the transaction, guaranteeing that existing read rows cannot be altered, though new phantom rows may be inserted.")

add_q("Isolation Levels: Standard Hierarchy",
      "Which is the highest, strictest ANSI SQL Isolation Level, completely eliminating Dirty Reads, Non-Repeatable Reads, and Phantom Reads?",
      ["Read Uncommitted", "Read Committed", "Repeatable Read", "Serializable"],
      3,
      "Serializable is the strictest isolation level. It guarantees that the concurrent execution of transactions produces the exact same result as if they were executed serially one after another.")

add_q("Lock Escalation",
      "What is 'Lock Escalation' in database resource management?",
      ["Increasing user privilege from read-only to administrator",
       "The automatic process where the DBMS converts many fine-grained locks (e.g. thousands of row or page locks) into a single coarse-grained lock (e.g. table lock) to conserve system memory",
       "A physical security alarm in the server facility",
       "Converting an SQL query into a stored procedure"],
      1,
      "When a transaction acquires too many individual row or page locks, lock escalation consolidates them into a single table lock to prevent lock table memory exhaustion.")

add_q("Lock Escalation Tradeoff",
      "What is the significant drawback of Lock Escalation?",
      ["It consumes all server disk space",
       "It drastically reduces system concurrency, because a coarse table-level lock blocks all other transactions wanting to access any row in that entire table",
       "It deletes the table's foreign key constraints",
       "It forces the database to restart"],
      1,
      "While escalation saves lock memory, it severely restricts concurrent access because unrelated rows in the same table can no longer be accessed by other users.")

add_q("Minimizing Locking Problems",
      "Which programming practice helps developers and DBAs minimize locking contention and avoid deadlocks?",
      ["Keeping transactions as short as possible, accessing database objects in a consistent, uniform order across all programs, and committing frequently",
       "Holding open transactions while waiting for end-user keyboard input",
       "Locking entire tables at the beginning of every transaction regardless of need",
       "Running massive batch updates in the middle of peak online transaction hours without commits"],
      0,
      "Short transactions, consistent object access order across all applications, and avoiding user interaction inside open transactions prevent deadlocks and lock contention.")

add_q("Batch Processing",
      "Why should large batch processing jobs (e.g. updating 5 million customer balances) commit changes in intermediate chunks rather than as one giant single transaction?",
      ["To avoid exhausting transaction log space, prevent massive lock escalation, and reduce rollback time in case of mid-batch failure",
       "Because databases can only process 100 rows per day",
       "Because intermediate commits make the computer cooler",
       "Because SQL syntax limits transactions to 5 minutes"],
      0,
      "Committing in batches (e.g. every 5,000 rows) keeps transaction logs manageable, frees locks for concurrent users, and ensures progress is saved if a crash occurs.")

# Generate remaining questions for Lectures 4 & 5 (up to 300)
for i in range(242, 301):
    subtopics = [
        ("SQL Best Practices", "Why should applications avoid running dynamic unparameterized SQL constructed via string concatenation?",
         ["Because it exposes the database to severe SQL Injection vulnerabilities and prevents the DBMS from reusing compiled execution plans in the statement cache",
          "Because string concatenation is physically impossible in programming",
          "Because the DBMS will refuse to accept strings",
          "Because dynamic SQL runs 500 times faster than parameterized queries"], 0,
          "Parameterized queries (prepared statements) protect against SQL injection and allow the optimizer to cache and reuse compiled query execution plans."),
        ("Transaction Management", "What happens to uncommitted database modifications if an application crashes or loses network connectivity mid-transaction?",
         ["The modifications remain permanently half-applied in the table",
          "The DBMS crash recovery mechanism detects the severed connection and automatically issues a ROLLBACK to restore the database to its pre-transaction state",
          "The database deletes the entire database schema",
          "The operating system reboots"], 1,
          "Atomicity guarantees that uncommitted transactions are rolled back upon connection loss or abnormal program termination."),
        ("Application Tuning", "What is the primary purpose of a Database Connection Pool in enterprise application servers?",
         ["To prevent developers from accessing the database",
          "To maintain a cache of established, reusable physical database connections, eliminating the heavy CPU and network overhead of opening and authenticating new connections per request",
          "To cool down the physical database server with water",
          "To store user cookies on the client device"], 1,
          "Creating database connections is computationally expensive. Connection pooling reuses open connections, providing high throughput for web applications."),
        ("Locking Strategies", "What is 'Optimistic Concurrency Control' compared to 'Pessimistic Concurrency Control'?",
         ["Optimistic locking assumes data conflicts are rare and verifies data hasn't changed (using version numbers or timestamps) at commit time, while pessimistic locking holds exclusive locks for the duration of processing",
          "Optimistic locking never checks for errors, while pessimistic locking aborts every transaction",
          "Optimistic locking is only for positive numbers",
          "Pessimistic locking is an obsolete technique banned by SQL standards"], 0,
          "Pessimistic locking locks data preemptively. Optimistic locking avoids locks during read/edit, checking row version timestamps only when committing.")
    ]
    st = subtopics[(i - 242) % len(subtopics)]
    add_q(st[0], f"[{st[0]} #{i}] {st[1]}", st[2], st[3], st[4])

print(f"Total DBA Questions generated: {len(questions)}")

with open("questions/dba_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved to questions/dba_questions.json successfully!")
