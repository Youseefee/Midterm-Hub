# Batch 3: Questions 136 to 200 (Deck 3: DBA-Lec4&5.pptx)
# Topics:
# 10. Database Application Development, APIs & Infrastructure (Q136 - Q151)
# 11. Object-Relational Impedance Mismatch, SQL Styles & XML (Q152 - Q167)
# 12. Transaction Management & ACID Properties (Q168 - Q182)
# 13. Concurrency Control, Locking & Batch Processing (Q183 - Q200)

BATCH3 = [
    # -------------------------------------------------------------------------
    # Topic 10: Database Application Development, APIs & Infrastructure (Q136 - Q151)
    # -------------------------------------------------------------------------
    {
        "topic": "Database Application Development & SQL Paradigms",
        "question": "What is the primary defining characteristic of SQL as a declarative, set-at-a-time database programming language?",
        "correct": "It specifies WHAT data is required rather than the procedural algorithmic steps of HOW to navigate storage to retrieve it",
        "distractors": [
            "It requires developers to write explicit memory allocation loops for every byte read from physical hard disk platters",
            "It compiles queries directly into low-level operating system assembly code that must be recompiled for each user session",
            "It processes only one single record per query invocation, requiring client applications to manage sequential record pointers"
        ],
        "explanation": "Lec 4&5 slide 4 states: 'SQL focuses on what data you want specify what data is needed, not how to get it. It's a declarative language, meaning you specify the result you want, and the database engine decides how to execute the query.'"
    },
    {
        "topic": "Database Application Development & SQL Paradigms",
        "question": "In relational database theory, what is the principle of 'Relational Closure' during SQL query processing?",
        "correct": "Every relational operation performed on one or more relational tables always produces another relational table as its result",
        "distractors": [
            "The database server automatically closes all network socket connections upon completing an individual query execution",
            "Every database transaction must permanently encrypt its data pages before closing the connection handle",
            "All relational tables must be locked against concurrent reads while an application program evaluates a WHERE clause"
        ],
        "explanation": "Slides 6 and 7 explain Relational Closure: 'Every operation performed on a relational database operates on a table (or set of tables) and results in another table. This is called relational closure.'"
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "How does Open Database Connectivity (ODBC) enable client application programs to interact with relational database management systems?",
        "correct": "It provides a standardized Call-Level Interface (CLI) of callable C functions to allocate handles, connect, and execute SQL",
        "distractors": [
            "It compiles SQL statements directly into optical laser pulses transmitted across local datacenter fiber cables",
            "It replaces relational database engines with client-side flat text files stored in user desktop home directories",
            "It forces all client applications to be written in mainframe COBOL before communicating with database instances"
        ],
        "explanation": "Slides 9 and 10 describe ODBC as a Call-Level Interface (CLI) using callable routines like SQLAllocHandle, SQLConnect, SQLExecDirect, and SQLFetch."
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "In the standard ODBC architecture, what is the primary operational role of the 'Driver Manager'?",
        "correct": "It sits between the application and database drivers, loading the appropriate vendor ODBC driver based on the requested DSN",
        "distractors": [
            "It physically calibrates the rotational spindle velocity of server hard drives during heavy batch transaction processing",
            "It automatically converts relational database tables into spreadsheet formats for business accounting departments",
            "It encrypts client network traffic using proprietary military-grade symmetric encryption keys stored in RAM buffers"
        ],
        "explanation": "Slide 13 defines Driver Manager: 'It manages the communication between the application and the ODBC drivers. It loads the appropriate driver for the specific database being accessed.'"
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "What is the role of a Data Source Name (DSN) when configuring database connectivity through ODBC?",
        "correct": "It stores the connection parameters, driver path, database name, and network credentials needed to establish a session",
        "distractors": [
            "It specifies the exact physical memory address where the operating system kernel stores its process scheduling table",
            "It acts as a public domain name registry that exposes internal database servers directly to global internet search engines",
            "It defines the corporate intellectual property license agreement between the software vendor and the client company"
        ],
        "explanation": "Slide 13 states: 'Data Source Name (DSN): A DSN provides the necessary information to connect to a database, such as the database type, name, and how to access it.'"
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "How does Java Database Connectivity (JDBC) enable Java applications to interact with relational databases?",
        "correct": "It provides a standard set of Java classes and interfaces supporting direct socket drivers or bridges to native database APIs",
        "distractors": [
            "It forces all Java bytecode to be compiled directly into mainframe machine assembly instructions before running",
            "It requires the DBA to write custom operating system device drivers for every table created in the schema",
            "It converts all relational database tables into HTML web pages displayed inside client desktop browsers"
        ],
        "explanation": "Slide 11 notes: 'JDBC enables Java to access relational databases. Similar to ODBC, JDBC consists of a set of classes and interfaces that can be used to access relational data.'"
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "How does SQLJ (SQL for Java) fundamentally differ from standard JDBC in its approach to database programming?",
        "correct": "SQLJ embeds static SQL directly within Java code, using a precompiler and database bind to create optimized access packages",
        "distractors": [
            "SQLJ eliminates the Java Virtual Machine, executing all database access routines directly on server motherboard firmware",
            "SQLJ converts relational tables into flat text files that are parsed at runtime by client operating system scripts",
            "SQLJ requires applications to be written in procedural C++ while using Java exclusively for graphical user interfaces"
        ],
        "explanation": "Slide 14 explains: 'SQLJ (SQL for Java) is an extension of the Java programming language that allows developers to embed SQL statements directly within Java code. A precompiler translates the embedded SQL... and a database bind operation creates packaged access routines.'"
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "What architectural capability distinguishes Microsoft OLE DB from earlier database call-level interfaces like ODBC?",
        "correct": "Built on the Component Object Model (COM), it provides a generic object interface for both relational and non-relational data",
        "distractors": [
            "It can only connect to databases that are stored on optical compact disc media inside local workstations",
            "It forces all database transactions to be committed sequentially in single-user mode without concurrency",
            "It completely replaces SQL with proprietary assembly language routines that bypass database optimizers"
        ],
        "explanation": "Slide 15 defines OLE DB: built on COM, presents an object-oriented interface for generic data access across both relational and nonrelational data, divided into consumers and providers."
    },
    {
        "topic": "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)",
        "question": "In the OLE DB conceptual framework, what is the operational distinction between 'Consumers' and 'Providers'?",
        "correct": "Consumers are applications that request data, while Providers are software components that implement the interface to supply data",
        "distractors": [
            "Consumers are physical server hard drives, while Providers are operating system virtual memory management tables",
            "Consumers are network router switches, while Providers are software programmers who write business documentation",
            "Consumers are corporate accounting executives, while Providers are junior interns responsible for data entry"
        ],
        "explanation": "Slide 15 states: 'consumers are the applications that need access to the data... providers are the software components that implement the interface and thereby provide the data to the consumer.'"
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "What are the core technical components of a traditional mainframe application infrastructure as described in the slides?",
        "correct": "IBM zSeries hardware running z/OS, DB2 relational database, CICS transaction processor, and COBOL applications",
        "distractors": [
            "ARM-based mobile processors running Android operating systems, SQLite databases, and Swift graphical client apps",
            "Commodity desktop computers running Windows 95, Microsoft Access databases, and Visual Basic script files",
            "Decentralized peer-to-peer microcontrollers communicating via serial cables without persistent disk storage"
        ],
        "explanation": "Slide 17 describes Mainframe infrastructure: 'IBM z Series hardware. Running z/OS, DB2, CICS, with application programs written in COBOL. Typically, applications consist of both batch and online workload.'"
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "What is the primary role of the Common Language Runtime (CLR) within the Microsoft .NET application framework?",
        "correct": "It is the execution engine that runs .NET programs, actively managing memory allocation, security, and exception handling",
        "distractors": [
            "It formats physical hard disk sectors and assigns RAID parity blocks across server storage area network arrays",
            "It acts as a public domain name resolver converting internet website names into standard 32-bit IP addresses",
            "It compiles procedural SQL queries into graphical vector diagrams for display in executive boardrooms"
        ],
        "explanation": "Slide 19 defines CLR: 'Common Language Runtime: This is the execution engine that runs .NET programs and manages memory, security, and error handling.'"
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "Within the Microsoft .NET framework, what is ADO.NET and how does it typically manage application data interactions?",
        "correct": "A data access architecture enabling developers to interact with memory-resident datasets in a predominantly disconnected fashion",
        "distractors": [
            "A continuous open socket protocol requiring constant physical connection to the database server motherboard",
            "A proprietary graphical styling language used exclusively to render button controls inside web browsers",
            "An operating system kernel extension designed to format magnetic tape reels for disaster recovery vaults"
        ],
        "explanation": "Slide 20 defines ADO.NET: technologies enabling developers to interact with data in standard, structured, and predominantly disconnected ways, managing both in-memory and external database data using XML and DLLs."
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "In the Java 2 Enterprise Edition (J2EE) multitier architecture, what is the specific role of Enterprise JavaBeans (EJB)?",
        "correct": "Modular server-side software components that encapsulate and execute core business logic within the application tier",
        "distractors": [
            "Client-side desktop web browser extensions that render animated graphical banners for internet users",
            "Physical memory chips installed on server motherboards to store temporary database query results",
            "Command-line terminal scripts used by systems administrators to monitor network router bandwidth"
        ],
        "explanation": "Slides 22, 23, and 24 define EJBs as components that contain the business logic for a J2EE application within the Business Tier."
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "How does the core design philosophy of Java compare with that of the Microsoft .NET framework as stated in the course slides?",
        "correct": "Java enables deployment across any platform provided code is written in Java; .NET enables multiple languages on Windows",
        "distractors": [
            "Java is strictly interpreted line-by-line in hardware, while .NET executes exclusively on optical laser discs",
            "Java forbids access to relational databases, while .NET requires all corporate data to be stored in flat files",
            "Java requires dedicated supercomputer hardware, while .NET runs exclusively on battery-powered mobile phones"
        ],
        "explanation": "Slide 26 contrasts them succinctly: Java is 'designed to enable applications to be deployed on any platform as long as they are written in Java'; .NET is 'designed to enable development in multiple languages as long as the application is deployed on Windows.'"
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "Why is it essential for a modern DBA to understand the Java programming language and its database frameworks?",
        "correct": "To effectively participate in design reviews and determine whether performance bottlenecks originate in Java code or in SQL",
        "distractors": [
            "Because modern commercial DBMS software packages will not install unless the DBA rewrites the engine in Java",
            "To eliminate the need for SQL by converting all database tables into compiled Java applet binaries on disk",
            "Because Java programs automatically bypass all database security permissions unless monitored by a DBA"
        ],
        "explanation": "Slide 25 stresses the impact of Java on DBA: 'Must understand Java... To provide guidance during design reviews... Is the problem in the SQL or the application? How can you tune the application if you do not understand the language?'"
    },
    {
        "topic": "Application Infrastructure (.NET and Java J2EE)",
        "question": "Which of the following is an example of a commercial or enterprise Application Server discussed in the course slides?",
        "correct": "IBM WebSphere Application Server",
        "distractors": [
            "Apache HTTP Web Server Engine",
            "Microsoft Windows 11 Server OS",
            "Cisco Catalyst Network Switch"
        ],
        "explanation": "Slide 48 lists application server examples: WebSphere (IBM), Zend Server, and Base4 Application Server."
    },

    # -------------------------------------------------------------------------
    # Topic 11: Object-Relational Impedance Mismatch, SQL Styles & XML (Q152 - Q167)
    # -------------------------------------------------------------------------
    {
        "topic": "Object-Relational Impedance Mismatch & ORM",
        "question": "What is the root cause of the 'Object-Relational Impedance Mismatch' when developing modern database applications?",
        "correct": "The conflict between the object paradigm (encapsulation, inheritance, navigation) and relational paradigm (tables, keys, set math)",
        "distractors": [
            "The electrical voltage variance between server central processing units and internal cooling fans in datacenters",
            "The difference in network transmission speeds between local Ethernet cables and wireless cellular phone towers",
            "The inability of relational database management systems to store numeric floating-point values accurately"
        ],
        "explanation": "Slides 29 and 30 define the Impedance Mismatch: OO programs deal with objects (encapsulation, inheritance), while RDBMSs deal with relations (tables, set-based mathematical queries), causing structural incompatibility."
    },
    {
        "topic": "Object-Relational Impedance Mismatch & ORM",
        "question": "Why are applications that store data in relational databases NOT 'object-oriented' in the purest theoretical sense?",
        "correct": "Because data resides in public relational tables and is not encapsulated within the object methods that operate upon it",
        "distractors": [
            "Because relational database tables can only be queried using compiled procedural C assembly language routines",
            "Because relational database management systems automatically delete object definitions whenever users log off",
            "Because object-oriented programming languages are legally prohibited from executing SQL SELECT queries"
        ],
        "explanation": "Slide 30 states: 'Applications will not be object-oriented in the \"true\" sense of the word because the data will not be encapsulated within the method (that is, the program).'"
    },
    {
        "topic": "Object-Relational Impedance Mismatch & ORM",
        "question": "What is the primary operational drawback of resolving the impedance mismatch by using 'Object Serialization' to flat files?",
        "correct": "Serialization creates slow, opaque files that cannot be queried or shared effectively across different applications",
        "distractors": [
            "Serialization causes physical disk heads to crash into spinning magnetic storage platters during read operations",
            "Serialization converts all numeric data values into high-resolution graphical bitmap files on the server",
            "Serialization requires developers to manually rewrite the operating system kernel before every transaction"
        ],
        "explanation": "Slide 31 notes under Serialization: 'Saving data using a flat file representation of the object. This approach can be slow and difficult to use across applications.'"
    },
    {
        "topic": "Object-Relational Impedance Mismatch & ORM",
        "question": "How do Object-Relational Mapping (ORM) frameworks like Hibernate, NHibernate, and LINQ bridge the impedance mismatch?",
        "correct": "They map class attributes to table columns, abstracting persistence behind high-level object manipulation methods",
        "distractors": [
            "They physically convert all relational tables into unindexed sequential punch-card images on magnetic tape",
            "They eliminate database servers entirely by storing all corporate data in client desktop RAM cache buffers",
            "They force the database engine to execute all queries in single-user mode to prevent concurrent transaction locks"
        ],
        "explanation": "Slide 32 describes ORM: 'With ORM an object's attributes are stored in one or more columns of a relational table... Hibernate is a popular ORM library for Java; NHibernate is an adaptation... LINQ provides .NET extensions for ORM.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "What is the defining operational distinction between 'Planned SQL' and 'Unplanned SQL' (ad-hoc queries)?",
        "correct": "Planned SQL is embedded in applications and pre-tested for performance, whereas unplanned SQL is written on the fly by end users",
        "distractors": [
            "Planned SQL is stored exclusively on optical storage media, while unplanned SQL resides on magnetic tape reels",
            "Planned SQL can only update numbers, while unplanned SQL is restricted exclusively to text string modifications",
            "Planned SQL requires manual typing by the DBA, while unplanned SQL is generated automatically by network routers"
        ],
        "explanation": "Slide 33 defines Planned vs Unplanned SQL: Planned SQL is embedded, designed, and tested for efficiency. Unplanned (ad-hoc) SQL is written on the fly by users for analysis, difficult to tune, and a major source of inefficiency."
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "Why is unplanned, ad-hoc SQL frequently a major source of operational inefficiency and performance problems for a DBA?",
        "correct": "Because queries are created dynamically without performance tuning, varying widely and consuming excessive server resources",
        "distractors": [
            "Because ad-hoc queries automatically delete underlying database indexes whenever they encounter a table join",
            "Because the DBMS permanently shuts down all network listener ports when an ad-hoc query executes a WHERE clause",
            "Because ad-hoc SQL queries are executed exclusively by the operating system printer spooler daemon"
        ],
        "explanation": "Slide 33 explains: 'Unplanned, ad hoc SQL requests can be a significant source of inefficiency and are difficult to tune. How do you tune requests that are constantly written, rewritten, and changed?'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "What is the difference between Static SQL and Dynamic SQL regarding compilation and access path optimization?",
        "correct": "Static SQL is compiled and optimized prior to execution; Dynamic SQL is parsed, verified, and optimized at runtime",
        "distractors": [
            "Static SQL can only read from flat text files; Dynamic SQL can only read from physical magnetic disk tracks",
            "Static SQL requires constant internet connectivity; Dynamic SQL operates exclusively in disconnected offline caches",
            "Static SQL is executed by database hardware controllers; Dynamic SQL is interpreted by client monitor screens"
        ],
        "explanation": "Slide 33 states: 'A dynamic SQL statement is optimized at run time... Static SQL, on the other hand, is optimized prior to execution and cannot change without reprogramming.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "From a security and application stability standpoint, why does the source material recommend favoring Static SQL over Dynamic SQL?",
        "correct": "Static SQL minimizes the vulnerability of the application to SQL injection attacks and guarantees predictable performance",
        "distractors": [
            "Static SQL completely eliminates the need for user passwords and database authentication credentials",
            "Dynamic SQL requires four times more physical hard drive storage space to store individual table records",
            "Static SQL allows application programs to run even when the database server hardware is powered down"
        ],
        "explanation": "Slide 33 explicitly advises: 'Favor static SQL to minimize the possibility of SQL injection attacks.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "According to the course guidelines for SQL coding performance, what fundamental design rule should developers follow?",
        "correct": "Let the DBMS optimize and filter data using SQL instead of retrieving large result sets to filter procedurally in host code",
        "distractors": [
            "Retrieve entire raw database tables into application memory loops to avoid using database query optimizer features",
            "Never use WHERE clauses in SQL statements because filtering operations cause physical disk head fragmentation",
            "Execute separate single-row SELECT queries for every record in a table to maximize CPU thread utilization"
        ],
        "explanation": "Slide 35 stresses: 'Let SQL do the work instead of coding it in host language program. The less data brought from the DBMS to the program the better performance will be.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "What is the primary structural difference between XML and HTML as described in the course materials?",
        "correct": "HTML uses predefined tags to describe display appearance, while XML uses customizable tags to describe the data itself",
        "distractors": [
            "HTML is compiled into binary executable code, while XML exists purely as unformatted analog sound waves",
            "HTML can only store numeric database records, while XML is restricted exclusively to boolean true/false flags",
            "HTML requires dedicated mainframe hardware, while XML runs exclusively on portable handheld calculator chips"
        ],
        "explanation": "Slide 36 notes: 'HTML uses tags to describe the appearance of data on a page, whereas XML uses tags to describe the data itself, instead of its appearance.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "What is a Document Type Definition (DTD) in the context of XML data management?",
        "correct": "A dictionary storing definitions of valid tag sets and structural relationships for specific industries or documents",
        "distractors": [
            "A binary compiler that converts XML markup into relational database tablespace storage partitions on disk",
            "An operating system security protocol that encrypts local hard disk drives to prevent unauthorized file copying",
            "A hardware network router configuration table that controls packet forwarding across wide area subnets"
        ],
        "explanation": "Slide 36 explains: 'These languages are collected in dictionaries called DTDs Document Type Definitions. The DTD stores definitions of tags for specific industries or fields of knowledge.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "What is XQuery, and what query syntax does it utilize to navigate and address specific parts of an XML document?",
        "correct": "A query and functional programming language designed for XML collections that utilizes XPath expression syntax",
        "distractors": [
            "A low-level assembly language compiler that uses C++ pointer arithmetic to locate text files on disk",
            "A graphical drag-and-drop tool that converts relational database schemas into vector animation sequences",
            "A command-line terminal utility used by system administrators to format optical laser storage platters"
        ],
        "explanation": "Slide 38 states: 'XQUERY: is a query and programming language designed to query collections of XML data. XQuery uses XPath expression syntax to address specific parts of an XML document.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "In XQuery processing, what are the five clauses that constitute a FLWOR expression for performing joins and constructing documents?",
        "correct": "FOR, LET, WHERE, ORDER BY, and RETURN",
        "distractors": [
            "FETCH, LOAD, WRITE, OPEN, and READ",
            "FORMAT, LINK, WHEN, OPTIMIZE, and ROLLBACK",
            "FILE, LOCK, WHILE, OVERWRITE, and REPEAT"
        ],
        "explanation": "Slide 38 details FLWOR: 'A FLWOR expression is constructed from the five clauses after which it is named: FOR, LET, WHERE, ORDER BY, and RETURN.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "Which of the following operational capabilities is explicitly NOT supported by native XQuery as described in the slides?",
        "correct": "XQuery contains no native features for updating XML documents/databases and does not provide full-text search",
        "distractors": [
            "XQuery cannot perform joins between multiple XML elements using FLWOR expressions",
            "XQuery cannot construct new XML documents from queried source information",
            "XQuery cannot navigate hierarchical tag trees using XPath path expressions"
        ],
        "explanation": "Slide 38 explicitly states: 'there are no features in XQuery for updating XML documents or databases. does not provide full text search capability.'"
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "Which standard SQL/XML function is used to concatenate two or more XML elements to return a forest of XML elements?",
        "correct": "XMLCONCAT",
        "distractors": [
            "XMLDOCUMENT",
            "XMLAGG",
            "XMLTABLE"
        ],
        "explanation": "Slide 39 states: 'XMLCONCAT (which returns a forest of XML elements generated from a concatenation of two or more elements)'."
    },
    {
        "topic": "SQL Types, Coding for Performance, and XML",
        "question": "A developer writes an application loop that fetches 50,000 customer rows across the network and discards 49,990 in host memory. What DBA rule is violated?",
        "correct": "Let SQL do the work in the DBMS to minimize data volume transferred over the network and reduce client memory bloat",
        "distractors": [
            "All relational queries must be written in procedural C++ rather than structured query language syntax",
            "Customer records can only be queried if the database server is running in single-user recovery mode",
            "Applications are legally prohibited from querying more than ten customer records per calendar month"
        ],
        "explanation": "Slide 35 stresses: 'Let SQL do the work instead of coding it in host language program. The less data brought from the DBMS to the program the better performance will be.'"
    },

    # -------------------------------------------------------------------------
    # Topic 12: Transaction Management & ACID Properties (Q168 - Q182)
    # -------------------------------------------------------------------------
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "What is the formal definition of a Database Transaction as presented in Chapter 5?",
        "correct": "An atomic unit of work in a database system where all operations are treated as a single, indivisible action",
        "distractors": [
            "An annual financial contract negotiated between software vendors and corporate procurement officers",
            "A physical hardware interrupt generated by a storage controller when a hard drive sector fails",
            "A scheduled operating system script that rotates backup tapes in external datacenter storage vaults"
        ],
        "explanation": "Slide 41 states: 'A transaction is an atomic unit of work in a database system - meaning all its operations are treated as a single, indivisible action.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "What is the permanent operational effect of issuing a COMMIT command at the conclusion of a database transaction?",
        "correct": "It makes all database modifications permanent and irrevocable, ensuring changes survive system restarts",
        "distractors": [
            "It temporarily hides modified rows until the client workstation disconnects from the local network",
            "It rolls back all data modifications made during the transaction to their prior starting values",
            "It permanently converts the relational database tables into unindexed flat comma-separated files"
        ],
        "explanation": "Slide 41 states: 'COMMIT Command: When all the steps of a transaction are successfully completed, the system issues a COMMIT. Effect: Makes all changes permanent in the database. The transaction cannot be undone after this point.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "What is the operational effect of issuing a ROLLBACK command prior to committing a transaction?",
        "correct": "It undoes all changes made by the transaction, returning the database to its previous consistent state",
        "distractors": [
            "It permanently deletes the entire database schema and erases all physical tablespace storage files",
            "It writes an unrecoverable corruption error to the operating system kernel and halts the server CPU",
            "It forces the client application to re-authenticate with the database using administrative credentials"
        ],
        "explanation": "Slide 41 explains: 'ROLLBACK Command: If an error or failure occurs before COMMIT, a ROLLBACK is used. Effect: Undoes all changes made by the transaction. Returns the database to its previous consistent state...'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "What is the primary operational role of the DBMS Transaction Log in supporting transaction integrity?",
        "correct": "It records before and after images of all operations to enable UNDO for rollbacks and REDO for crash recovery",
        "distractors": [
            "It stores human-readable employee attendance logs for review by corporate human resources managers",
            "It acts as an optical character recognition buffer for scanning paper receipts into database tables",
            "It prints hardcopy diagnostic receipts on datacenter paper spoolers whenever a query finishes"
        ],
        "explanation": "Slides 42 and 44 describe the Transaction Log: records all operations, original values for rollback (UNDO), and new values for crash recovery (REDO)."
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "In the classic bank transfer scenario ($500 transferred from Account A to Account B), why must debit and credit reside in the SAME transaction?",
        "correct": "To ensure atomicity: either both balance updates complete successfully, or both are aborted to prevent lost or created funds",
        "distractors": [
            "To prevent the operating system from allocating additional memory buffers for concurrent background processes",
            "Because relational database management systems forbid executing more than one SQL statement per calendar day",
            "To force the transaction log to write all account balance records to external optical disc media immediately"
        ],
        "explanation": "Slides 43 and 44 explain the transfer scenario: subtracting $500 from A and adding $500 to B must happen together or not at all to guarantee balance integrity."
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "Which ACID property guarantees that all operations within a transaction execute completely or none of them execute at all?",
        "correct": "Atomicity",
        "distractors": [
            "Consistency",
            "Isolation",
            "Durability"
        ],
        "explanation": "Slide 45 defines Atomicity: 'Means that a transaction is executed completely or not at all.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "Which ACID property guarantees that a transaction leaves the database in a valid state adhering to all defined rules and constraints?",
        "correct": "Consistency",
        "distractors": [
            "Atomicity",
            "Isolation",
            "Durability"
        ],
        "explanation": "Slide 45 defines Consistency: 'Ensures that after any transaction, the database remains in a valid and correct state, following all defined rules and constraints.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "Which ACID property ensures that concurrent transactions execute without interfering with one another, as if each were running in isolation?",
        "correct": "Isolation",
        "distractors": [
            "Atomicity",
            "Durability",
            "Consistency"
        ],
        "explanation": "Slide 45 defines Isolation: 'Means that each transaction runs as if it were the only one interacting with the database at that moment, even if multiple transactions are running concurrently.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "Which ACID property ensures that once a transaction commits, its modifications are permanent and will survive catastrophic system failure?",
        "correct": "Durability",
        "distractors": [
            "Atomicity",
            "Consistency",
            "Isolation"
        ],
        "explanation": "Slide 45 defines Durability: 'Ensures that once a transaction is successfully committed, its changes are permanent - even if the system crashes or loses power afterward.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "How is a 'Unit of Work' (UOW) defined in the context of database transaction management?",
        "correct": "A series of instructions and messages that guarantees data integrity, which can represent all or part of a business transaction",
        "distractors": [
            "The physical quantity of electricity in kilowatt-hours consumed by a server rack during query execution",
            "The total number of keystrokes typed by an application developer while writing an individual stored procedure",
            "The physical weight of storage area network hard disk drive enclosures mounted in datacenter server racks"
        ],
        "explanation": "Slide 46 states: 'A UOW is a series of instructions and messages that guarantees data integrity. UOW is not necessarily a complete business process... and a group of units of work can constitute a single transaction.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "Why can an overall business transaction comprise multiple distinct Units of Work (UOWs)?",
        "correct": "Complex business processes involve discrete stages (e.g. reserving inventory, validating credit, finalizing order) that each preserve integrity",
        "distractors": [
            "Because commercial database management systems only permit ten SQL statements per transaction log file",
            "To allow system administrators to manually edit customer account numbers between intermediate operations",
            "Because database locks automatically expire and release after exactly sixty seconds of execution time"
        ],
        "explanation": "Slide 46 notes: 'A transaction can consist of several Units of Work', reflecting intermediate stages of a business workflow where integrity must be preserved."
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "In the ATM banking withdrawal example cited in the slides, what constitutes the complete Unit of Work?",
        "correct": "Both the subtraction of money from the customer's account and the physical delivery of cash to the customer",
        "distractors": [
            "Only the debiting of the customer's electronic checking account balance in the database",
            "Only the customer inserting the plastic debit card into the automated teller machine card reader",
            "Only the printing of an electronic transaction receipt on thermal paper inside the machine"
        ],
        "explanation": "Slide 46 explains: 'Withdrawal of $20: The transaction must involve both the subtraction of $20 from your account and the delivery of $20 to you. Only doing one or the other is not a complete unit of work.'"
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "What is the primary role of a Transaction Processing (TP) System or Transaction Server compared to basic DBMS stored procedures?",
        "correct": "TP systems coordinate workflows and two-phase commits across multiple distributed, heterogeneous databases and presentation clients",
        "distractors": [
            "TP systems eliminate all physical database storage by caching all transactional data permanently in CPU L1 cache",
            "TP systems compile host programming code directly into optical laser signals for satellite internet transmission",
            "TP systems force all application users to enter data sequentially in single-user mode to avoid locking conflicts"
        ],
        "explanation": "Slide 47 contrasts DBMS stored procedures with TP Systems/Transaction Servers managing multi-database distributed transactions and workflow controllers."
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "A server suffers an abrupt power outage ten seconds after committing a major financial transaction. Upon restart, which ACID mechanism recovers committed changes?",
        "correct": "The Durability guarantee, implemented via the transaction log REDO mechanism reapplying committed modifications",
        "distractors": [
            "The Isolation guarantee, implemented via exclusive page locks held on client workstation memory",
            "The Consistency guarantee, implemented via operating system file system defragmentation routines",
            "The Atomicity guarantee, implemented via discarding all changes made during the preceding calendar week"
        ],
        "explanation": "Slides 42 and 45 show that Durability ensures committed changes survive crashes, using REDO logging to restore committed transactions to disk."
    },
    {
        "topic": "Transaction Management & ACID Properties",
        "question": "During a multi-row payroll update, an unexpected constraint violation triggers an unhandled error. What command must the application issue to preserve integrity?",
        "correct": "ROLLBACK, to discard all partial updates and return the payroll tables to their pre-transaction state",
        "distractors": [
            "COMMIT, to force the partially updated records permanently into the database tables",
            "GRANT, to transfer administrative ownership of the payroll tables to the active user",
            "ALTER, to permanently drop the violating constraint from the physical database schema"
        ],
        "explanation": "Slides 41 and 44 emphasize issuing ROLLBACK upon error to undo all changes and return the database to its consistent starting state."
    },

    # -------------------------------------------------------------------------
    # Topic 13: Concurrency Control, Locking & Batch Processing (Q183 - Q200)
    # -------------------------------------------------------------------------
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What is the primary purpose of the DBMS locking mechanism in multi-user database environments?",
        "correct": "To enable multiple concurrent users to access and modify data simultaneously while automatically guaranteeing data integrity",
        "distractors": [
            "To physically prevent unauthorized hardware engineers from opening server chassis doors in the datacenter",
            "To encrypt table data pages with private cryptographic keys so that only the database administrator can read them",
            "To prevent application programs from executing SQL statements during normal weekday business hours"
        ],
        "explanation": "Slide 49 states: 'The DBMS uses a locking mechanism to enable multiple, concurrent users to access and modify data in the database. By using locks, the DBMS automatically guarantees the integrity of data.'"
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "Which of the following correctly orders locking granularity from the finest level to the coarsest level?",
        "correct": "Row -> Page (or Block) -> Table -> Table Space -> Database",
        "distractors": [
            "Database -> Table Space -> Table -> Page -> Row",
            "Table -> Row -> Database -> Page -> Table Space",
            "Page -> Table Space -> Row -> Database -> Table"
        ],
        "explanation": "Slide 49 lists Locking Granularity: Row, Page (or Block), Table, Table Space, Database."
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What is the operational behavior of a Shared Lock (S Lock) on a database resource?",
        "correct": "It is acquired when reading data without intent to update; other users can read concurrently, but cannot modify the data",
        "distractors": [
            "It grants exclusive write access to a single user while disconnecting all other users from the database instance",
            "It automatically converts all numeric table columns into text string format to facilitate multi-user sharing",
            "It allows other users to update and delete the locked row, but prevents them from executing SELECT queries"
        ],
        "explanation": "Slide 50 defines Shared Lock: 'Taken when data is read with no intent to update it. If a shared lock has been taken on a row, page, or table, other processes or users are permitted to read the same data.'"
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What is the operational behavior of an Exclusive Lock (X Lock) on a database resource?",
        "correct": "It is acquired when data is modified; no other concurrent user or process can read or modify the locked data",
        "distractors": [
            "It allows unlimited concurrent read and write operations across all connected application user sessions",
            "It is acquired only during full database backups and has zero effect on regular transaction updates",
            "It locks only the database catalog metadata while leaving table data rows completely unprotected"
        ],
        "explanation": "Slide 50 defines Exclusive Lock: 'Taken when data is modified. While an exclusive lock is held, no other user can read or modify that same data. Ensures that only one transaction is working with that data at a time.'"
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What is the purpose of an Update Lock (U Lock) in relational database concurrency control?",
        "correct": "It indicates intent to modify data currently being read, and is promoted to an X lock if modified, preventing conversion deadlocks",
        "distractors": [
            "It permanently converts a relational table into an unindexed flat text file stored on optical media",
            "It prevents the operating system kernel from allocating virtual memory swap space to the DBMS",
            "It allows two concurrent transactions to update the exact same data row with different values simultaneously"
        ],
        "explanation": "Slide 50 defines Update Lock: 'Taken when data must first be read before it is changed or deleted... indicates that the data may be modified... DBMS will promote the update lock to an exclusive lock.'"
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What are Intent Locks (such as IS and IX), and how do they resolve concurrency conflicts in hierarchical locking?",
        "correct": "Placed on tables/tablespaces to signal that fine-grained child locks exist, forcing coarse table operations to wait",
        "distractors": [
            "Placed on client workstation web browsers to inform users that an ad-hoc query is currently running in memory",
            "Placed on physical datacenter cooling equipment to regulate airflow temperature during peak transaction processing",
            "Placed on operating system network drivers to prevent TCP/IP packets from being routed across foreign subnets"
        ],
        "explanation": "Slide 52 defines Intent Locks: placed on higher-level objects (table or tablespace) when lower-level locks are held on data pages or rows, informing other transactions that rows are in use so full table locks wait."
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What is a 'Lock Timeout' in a relational database management system?",
        "correct": "An error raised when a transaction waits longer than a configured threshold to acquire a lock held by another process",
        "distractors": [
            "A hardware failure occurring when server motherboard clock batteries lose electrical charge during execution",
            "An automatic disconnect triggered when an end user leaves their desktop workstation unattended for five minutes",
            "A scheduled maintenance window where the DBMS shuts down all user connections to format disk drives"
        ],
        "explanation": "Slide 53 and slide 60 address lock timeouts: when a process waits beyond the lock timeout threshold for a held lock, the DBMS aborts the request with a lock timeout error."
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "What constitutes a Database Deadlock between two concurrent transactions?",
        "correct": "A cyclic dependency where Transaction A holds Lock 1 and waits for Lock 2, while Transaction B holds Lock 2 and waits for Lock 1",
        "distractors": [
            "A condition where two users attempt to log into the database using identical username and password credentials",
            "A physical disk head crash that prevents the storage area network controller from reading magnetic tracks",
            "A scenario where a database table contains zero rows and an application submits a SELECT query"
        ],
        "explanation": "Slide 54 defines Deadlocks: 'A deadlock happens when two or more transactions are waiting for each other to release locks, so none of them can continue - the system gets stuck.'"
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "How does the DBMS engine automatically resolve a deadlock condition once it is detected?",
        "correct": "It selects one of the deadlocked transactions as a victim, aborts it, rolls back its modifications, and releases its locks",
        "distractors": [
            "It permanently shuts down the server hardware and sends an emergency text message to local emergency services",
            "It merges both transactions into a single operating system thread and combines their updates into one row",
            "It prompts the business end users with an interactive desktop dialog box asking them to vote on which query to run"
        ],
        "explanation": "When the DBMS deadlock detection algorithm discovers a cycle in the wait-for graph, it breaks the freeze by rolling back a chosen 'victim' transaction."
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What two primary system parameters dictate the duration of time that a lock remains held by the DBMS?",
        "correct": "The transaction Isolation Level and the Acquire/Release specifications",
        "distractors": [
            "The physical rotational speed of the hard drive and the server power supply wattage",
            "The length of the table name and the alphabetical order of the database schema owner",
            "The monitor resolution of the client workstation and the version of desktop operating system"
        ],
        "explanation": "Slide 55 explicitly states: 'Two parameters impact lock duration: Isolation level, Acquire/Release.'"
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "Which transaction isolation level permits 'Dirty Reads', allowing transactions to view uncommitted modifications of other sessions?",
        "correct": "Read Uncommitted (permits dirty reads)",
        "distractors": [
            "Read Committed (uses cursor stability)",
            "Repeatable Read (allows phantom rows)",
            "Serializable (full transaction lock)"
        ],
        "explanation": "Slide 56 lists isolation levels: 'Read uncommitted: aka dirty read'."
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "Which transaction isolation level releases shared read locks as soon as the database cursor moves off the current row or page?",
        "correct": "Read Committed (uses cursor stability)",
        "distractors": [
            "Read Uncommitted (permits dirty reads)",
            "Repeatable Read (allows phantom rows)",
            "Serializable (full transaction lock)"
        ],
        "explanation": "Slide 56 lists 'Read committed: aka cursor stability', where locks are held only on current records to prevent dirty reads while maximizing concurrency."
    },
    {
        "topic": "Concurrency Control & Database Locking",
        "question": "What does the 'Acquire/Release Specification' control regarding database locking behavior?",
        "correct": "Whether intent locks are acquired immediately or iteratively, and whether they are released at commit or per unit of work",
        "distractors": [
            "Whether database software licenses are purchased annually or leased monthly from commercial vendors",
            "Whether physical hard drives are formatted with NTFS or EXT4 operating system file systems",
            "Whether client workstations connect to the server via wireless radio frequencies or wired Ethernet"
        ],
        "explanation": "Slide 57 states: 'Acquire/Release Specification: Controls when Intent locks are acquired and released... acquired either immediately... or iteratively... released when the transaction completes or when no longer required...'"
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "What is 'Lock Escalation' in database management system concurrency control?",
        "correct": "The automated process of converting many fine-grained locks (rows/pages) into a coarse-grained lock (table) when a threshold is exceeded",
        "distractors": [
            "The legal process of suing a software developer for writing inefficient queries that consume server CPU",
            "The automated process of increasing server cooling fan speeds when database CPU temperatures rise",
            "The physical replacement of mechanical disk drives with high-speed solid-state drives during operations"
        ],
        "explanation": "Slide 58 defines Lock Escalation: 'Lock escalation is the process of increasing the lock granularity for a process or program... page locks (or row locks) can be escalated to table locks.'"
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "What is the primary operational penalty or risk caused by lock escalation occurring in a high-volume database?",
        "correct": "It drastically impairs concurrency by locking the entire table, blocking other concurrent processes and causing timeouts",
        "distractors": [
            "It permanently corrupts the database transaction log, requiring an immediate full restore from tape",
            "It causes server memory chips to overheat and permanently lose stored data configuration bits",
            "It converts all table column data types into unindexed variable-length character string fields"
        ],
        "explanation": "Slide 58 warns: 'Can cause concurrency issues: If the entire table is locked other processes cannot access the data.'"
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "Which programming technique is strongly recommended in the course slides to avoid deadlocks across application programs?",
        "correct": "Enforcing a consistent access and update sequence across all programs (for example, alphabetical order by table name)",
        "distractors": [
            "Executing all database updates inside client-side web browser JavaScript loops before sending SQL",
            "Disabling the DBMS transaction log so updates are written directly to disk without logging overhead",
            "Creating separate database user accounts for every individual SQL statement executed by an application"
        ],
        "explanation": "Slide 59 recommends: 'Avoid deadlocks by coding updates in the same sequence regardless of program. For example, alphabetical order by table name.'"
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "Why should data modification SQL statements (INSERT, UPDATE, DELETE) be coded as close to the end of a Unit of Work as possible?",
        "correct": "Holding exclusive locks for the shortest possible duration minimizes lock contention and reduces timeout risks for other users",
        "distractors": [
            "Executing modifications at the end allows the operating system to completely skip transaction logging",
            "The DBMS query optimizer refuses to generate execution plans for statements coded at the start of a program",
            "It ensures that table data is permanently compressed before being written to physical storage sectors"
        ],
        "explanation": "Slide 59 advises: 'Issue data modification SQL statements as close to the end of the UOW as possible. The later in the UOW the update occurs, the shorter the duration of the lock.'"
    },
    {
        "topic": "Lock Escalation, Deadlocks, and Batch Processing",
        "question": "When designing batch processing applications that update thousands of rows, what critical strategy must be implemented?",
        "correct": "Plan and implement an intermediate COMMIT strategy throughout the batch run rather than holding locks until program completion",
        "distractors": [
            "Treat the database tables like sequential flat files and disable all relational integrity checking rules",
            "Execute the entire batch program exclusively in single-user recovery mode with network cables unplugged",
            "Store all batch transaction records in operating system print queues to be processed manually by staff"
        ],
        "explanation": "Slide 60 highlights Batch Processing best practices: 'Think relationally instead of file processing. Plan and implement a COMMIT strategy in all batch application programs instead of holding locks until the end of the program. Otherwise you will experience a lot of lock timeouts.'"
    }
]

print(f"Loaded Batch 3 with {len(BATCH3)} questions.")
