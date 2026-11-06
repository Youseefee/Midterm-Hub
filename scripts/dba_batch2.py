# Batch 2: Questions 66 to 135 (Deck 2: DBA-Lec2&3.pptx)
# Topics:
# 5. Physical Database Design & Rules of Thumb (Q66 - Q79)
# 6. Column Ordering, Storage Planning & Free Space (Q80 - Q93)
# 7. Index Architectures & Access Optimization (Q94 - Q108)
# 8. Partitioning, Hashing, Clustering & Interleaving (Q109 - Q122)
# 9. Denormalization Strategies, Views & Temporal Data (Q123 - Q135)

BATCH2 = [
    # -------------------------------------------------------------------------
    # Topic 5: Physical Database Design & Rules of Thumb (Q66 - Q79)
    # -------------------------------------------------------------------------
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "Which set of technical competencies is essential for a DBA when translating a logical data model into a physical database?",
        "correct": "Knowledge of DBMS physical structures, indexing mechanics, configuration parameters, constraints, and DDL syntax",
        "distractors": [
            "Expertise in client-side CSS styling, web browser typography rendering, and vector graphic canvas animation",
            "Knowledge of enterprise sales forecasting, marketing lead generation funnels, and executive compensation plans",
            "Proficiency in assembling datacenter electrical switchgear and servicing uninterruptible lead-acid battery banks"
        ],
        "explanation": "Lec 2&3 slide 4 details physical design requirements: knowledge of database objects/structures, indexing, RI, constraints, data types, new/obsolete features, DBMS configuration parameters, and DDL skills."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "According to the physical design Rules of Thumb (ROTs), why should a DBA avoid relying on DBMS default settings?",
        "correct": "Default settings are rarely optimal for specific workloads, making it preferable to explicitly analyze and specify settings",
        "distractors": [
            "Commercial DBMS engines immediately crash and invalidate database licenses if default values remain unedited",
            "Default parameters automatically erase all user table data whenever the operating system reboots unexpectedly",
            "Using default configuration values permanently locks all physical storage disk drives into read-only mount modes"
        ],
        "explanation": "Slide 5 states: 'Avoid using default settings: They are rarely the best setting. It is better to know and explicitly state the actual setting you desire in each case.'"
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "What is the primary rationale behind the Rule of Thumb requiring synchronization between logical and physical data models?",
        "correct": "Any changes made to physical database objects must be mapped back to the logical model to maintain design accuracy and traceability",
        "distractors": [
            "Failure to synchronize causes the hardware storage controller to physically reject read and write commands",
            "The DBMS query compiler requires both models to be stored in CPU level-one cache memory to run SELECT queries",
            "Synchronizing models allows non-technical business users to write binary machine instructions directly to disk"
        ],
        "explanation": "Slide 5 emphasizes: 'Synchronize the logical and physical models: Always map changes in one to the other.'"
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "How does the physical design Rule of Thumb 'Performance before aesthetics' guide a DBA during schema optimization?",
        "correct": "Fully normalized structures are preferred, but DBAs must selectively deviate into denormalization when necessary to meet performance goals",
        "distractors": [
            "Aesthetic visual layout of tables on entity diagrams takes absolute precedence over transaction execution speeds",
            "All relational tables must be compressed to zero bytes on physical storage media regardless of application latency",
            "Database schemas should be designed strictly to look elegant on architectural posters without testing queries"
        ],
        "explanation": "Slide 5 explains: 'Performance before aesthetics: Meaning: prefer fully normalized but deviate when necessary to achieve performance goals.'"
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "Why does the author state the guiding Rule of Thumb: 'Almost never say always or never' in database administration?",
        "correct": "Physical database design requires trade-offs tailored to specific workloads, data access patterns, and hardware constraints",
        "distractors": [
            "Relational database management software is completely nondeterministic and executes queries randomly each run",
            "Legal regulatory standards prohibit database administrators from issuing definitive statements in technical logs",
            "Every commercial database vendor uses identical internal disk layout algorithms regardless of configuration"
        ],
        "explanation": "Slide 5 states: 'Almost never say always or never' because dogmatic design rules often fail when confronted with unique workload realities and physical engineering trade-offs."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "In the terminology comparison across computing disciplines, what relational database concept corresponds to an Object-Oriented 'Class'?",
        "correct": "Relational Table (Relation)",
        "distractors": [
            "Relational Tuple (Row)",
            "Relational Column (Attribute)",
            "Relational Foreign Key"
        ],
        "explanation": "Slide 3 compares terms: OO Type/Class = Relational Table/Relation = DP File = Design Entity."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "In the terminology comparison table, what relational concept corresponds to an Object-Oriented 'Object' or 'Instance'?",
        "correct": "Relational Tuple or Row",
        "distractors": [
            "Relational Schema",
            "Relational Table",
            "Relational Column"
        ],
        "explanation": "Slide 3 compares terms: OO Instance/Object = Relational Tuple/Row = DP Record = Design Row/Record."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "Which data processing (DP) term directly corresponds to the relational database concept of a 'Column'?",
        "correct": "Field (or Data Item / Data Element)",
        "distractors": [
            "File Folder (or Record Cabinet)",
            "Magnetic Tape (or Physical Volume)",
            "Block Directory (or Page Header)"
        ],
        "explanation": "Slide 3 maps Relational Column to DP Field / Data Item and Design Attribute."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "What is the primary constraint when transforming logical 'Domains' into physical database definitions?",
        "correct": "Commercial DBMSes generally do not support domains natively, so DBAs must map them to supported physical data types and check constraints",
        "distractors": [
            "Domains can only be stored if the database administrator installs specialized optical disc hardware drives",
            "Commercial DBMSes only allow one domain per relational table, forcing multi-attribute entities to be split",
            "Logical domains automatically convert into operating system user accounts with administrative login privileges"
        ],
        "explanation": "Slide 8 states: 'Transform Domains to Data Types: Commercial DBMSes do not support domains. Choose wisely; impacts data quality.'"
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "When choosing between fixed-length and variable-length character data types (e.g. CHAR vs VARCHAR), what must the DBA balance?",
        "correct": "Storage space conservation of variable columns versus the processing overhead, row expansion, and potential fragmentation",
        "distractors": [
            "Fixed-length columns require optical laser storage, whereas variable columns must reside in CPU cache",
            "Variable-length columns completely prevent application programs from performing string concatenation queries",
            "Fixed-length columns are automatically translated into binary floating-point numbers by the database compiler"
        ],
        "explanation": "Slide 8 highlights 'Variable or Fixed Length: Choose wisely; impacts data quality' as well as physical storage management, row expansion, and page splitting."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "Why is the decision to allow or disallow NULLs in a column critical to physical database design and query semantics?",
        "correct": "NULL indicates missing or inapplicable data and introduces three-valued logic, which complicates query expressions and indexing",
        "distractors": [
            "Enabling NULLs in any column permanently disables primary key referential integrity constraints across the database",
            "Columns that permit NULL values consume exactly double the storage space of standard integer columns on disk",
            "The DBMS automatically replaces all NULL values with zero or blank strings during transaction commit operations"
        ],
        "explanation": "Slides 8 and 10 emphasize that Nulls represent unknown/missing values and require careful design due to three-valued logic (TRUE, FALSE, UNKNOWN) and storage implications."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "When is it appropriate for a DBA to assign a surrogate key (e.g. Identity, Sequence, or ROWID) instead of a natural primary key?",
        "correct": "When the natural key is excessively wide, composite, subject to business changes, or nonexistent in the source data",
        "distractors": [
            "When the DBA wants to intentionally obscure the relational structure to prevent developers from writing SQL",
            "When the table contains fewer than ten total records and is expected to remain static over its entire lifecycle",
            "When the underlying storage hardware consists exclusively of solid state drives operating under RAID zero arrays"
        ],
        "explanation": "Slide 14 discusses relationships and keys, noting considerations such as key length, surrogate keys, and ROWID/SEQUENCE/Identity when natural keys are unsuitable."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "In relational database design, what is the primary role of Foreign Key constraints?",
        "correct": "Enforcing referential integrity by guaranteeing that column values in one table match valid primary keys in a related table",
        "distractors": [
            "Physically encrypting column values on disk using symmetric cryptographic keys to satisfy regulatory audits",
            "Automatically generating web service endpoints to expose relational table data directly to internet browsers",
            "Compressing table data pages to minimize the total number of physical input/output operations during table scans"
        ],
        "explanation": "Slide 14 stresses: 'Build referential constraints for all relationships: Foreign keys' to ensure valid relationships between entities."
    },
    {
        "topic": "Physical Database Design & Rules of Thumb",
        "question": "What is the primary danger of failing to synchronize logical data models with the physical database schema over several release cycles?",
        "correct": "The documentation diverges from production reality, impairing future impact analysis, maintenance, and enterprise data governance",
        "distractors": [
            "The physical database instance automatically rolls back to the initial schema creation state upon every server reboot",
            "Application programs immediately fail with operating system syntax errors whenever they attempt to issue SELECT queries",
            "Hardware storage controllers refuse to format new magnetic disk extents without an active conceptual diagram file"
        ],
        "explanation": "Slide 5 emphasizes synchronizing logical and physical models. Neglecting this leads to architectural debt, unmanageable schemas, and loss of data integrity control."
    },

    # -------------------------------------------------------------------------
    # Topic 6: Column Ordering, Storage Planning & Free Space (Q80 - Q93)
    # -------------------------------------------------------------------------
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "According to database administration physical design guidelines, what technical factor dictates the optimal ordering of columns within a row?",
        "correct": "Logging overhead during data modifications: place infrequently updated static columns first and frequently updated columns last",
        "distractors": [
            "Alphabetical ordering by column name to make raw database disk pages legible to human hardware technicians",
            "Placing all numeric columns before text columns to allow the central processing unit to execute integer addition faster",
            "Randomizing column positions across data pages to provide built-in cryptographic obfuscation against hackers"
        ],
        "explanation": "Slide 12 explicitly states: 'Sequence columns based on logging. For example: Infrequently updated non-variable columns first, Static (infrequently updated) variable columns, Frequently updated columns last.'"
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "In column ordering optimization, why should columns that are frequently updated together be placed adjacent to one another?",
        "correct": "It minimizes the number of byte ranges written to the transaction log, reducing logging volume and processing overhead",
        "distractors": [
            "It prevents the operating system from allocating multiple network packets when streaming query results to clients",
            "It forces the DBMS query optimizer to automatically generate composite clustered indexes on both columns",
            "It allows the storage controller to store the two columns on completely separate physical hard disk spindles"
        ],
        "explanation": "Slide 12 notes: 'Frequently modified together, place next to each other' (e.g. First Name and Address) to optimize log record construction and update efficiency."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "What is the correct sequential order of steps when conducting database storage planning for a new table?",
        "correct": "Determine row count -> Calculate row size -> Determine rows per page -> Calculate required pages -> Calculate total object size",
        "distractors": [
            "Purchase storage disks -> Allocate table partitions -> Write application code -> Determine row size -> Count users",
            "Calculate total object size -> Count tables -> Measure CPU speed -> Calculate row size -> Determine rows per page",
            "Determine rows per page -> Format hard drives -> Write DDL -> Multiply by database users -> Calculate row size"
        ],
        "explanation": "Slide 16 details the exact 5 steps: 1. Determine how many rows required; 2. Calculate row size; 3. Figure out rows per block/page; 4. Calculate pages required; 5. Calculate object size."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "Consider a STUDENT table designed to hold 10,000 rows. The row size is 60 bytes and the DBMS page size is 8,192 bytes. How many rows fit per page?",
        "correct": "Approximately 136 rows per page",
        "distractors": [
            "Approximately 250 rows per page",
            "Approximately 60 rows per page",
            "Approximately 500 rows per page"
        ],
        "explanation": "Slide 17 provides this calculation: Page size = 8,192 bytes; Row size = 60 bytes; 8192 / 60 = 136.53 -> 136 whole rows fit per page."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "Following the calculation for 10,000 students at 136 rows per page, approximately how many data pages are required (excluding free space)?",
        "correct": "Approximately 74 data pages",
        "distractors": [
            "Approximately 150 data pages",
            "Approximately 25 data pages",
            "Approximately 500 data pages"
        ],
        "explanation": "10,000 rows divided by 136 rows per page yields 73.53 pages, which rounds up to 74 pages to store all rows."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "What is the primary function of the PCTFREE storage parameter when creating a database table space?",
        "correct": "It reserves a percentage of free space on each data page during load/insert to accommodate future row expansion from updates",
        "distractors": [
            "It specifies how many empty pages to leave in the tablespace for future bulk batch inserts",
            "It defines the percentage of central processing unit time allocated exclusively to the database optimizer",
            "It configures the maximum percentage of uncommitted dirty reads permitted under cursor stability"
        ],
        "explanation": "Slide 18 explains: 'PCTFREE focuses on reserving space for updates... managing how free space is allocated within data pages.'"
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "What operational problem occurs if PCTFREE is set too low on a table subject to frequent updates on variable-length columns?",
        "correct": "Updated rows expand beyond remaining page space, causing page splits, row migration, and increased I/O overhead",
        "distractors": [
            "The DBMS automatically deletes the oldest rows in the table to create space for the expanded column data",
            "The storage area network controller permanently disables write caching across all physical disk arrays",
            "The database server converts all variable-length columns into fixed-length floating point binary values"
        ],
        "explanation": "Slide 18 warns that inadequate PCTFREE leads to performance bottlenecks related to page splits, row migrations, and excessive reorganizations."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "What is the specific purpose of the FREEPAGE parameter in database physical storage configuration?",
        "correct": "It leaves an entirely empty page after a specified number of allocated pages to provide space for clustered inserts",
        "distractors": [
            "It permanently removes corrupted data pages from disk without recording the deletion in the transaction log",
            "It allocates virtual swap space on the operating system to prevent database process out-of-memory errors",
            "It reserves an in-memory buffer pool segment dedicated exclusively to sorting ad-hoc reporting query results"
        ],
        "explanation": "Slide 18 notes: 'while FREEPAGE is used to manage space for frequent inserts. A careful balance of these two settings can help avoid performance bottlenecks...'"
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "Under what workload condition is setting a non-zero FREEPAGE parameter particularly beneficial?",
        "correct": "When a table has a clustered index and undergoes frequent ongoing inserts that need to maintain physical sequence",
        "distractors": [
            "When a table is strictly read-only and never experiences any insert, update, or delete operations",
            "When all database tables are stored in RAM memory caches without any persistent underlying disk storage",
            "When the application access pattern consists solely of full table scans without any index lookups"
        ],
        "explanation": "Slide 18 and slide 21 explain that FREEPAGE leaves empty pages periodically so new rows inserted in clustered key order have nearby space, avoiding distant splits."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "What is the major trade-off when a DBA configures excessively high values for PCTFREE and FREEPAGE?",
        "correct": "Pages contain fewer rows, increasing total disk storage, expanding the buffer pool footprint, and slowing full table scans",
        "distractors": [
            "The DBMS rejects all incoming user connections due to simulated artificial memory exhaustion errors",
            "Data corruption occurs because empty page bytes are misinterpreted as null pointer memory addresses",
            "Application programs are restricted to executing single-row transactions and cannot use batch commits"
        ],
        "explanation": "Reserving excessive free space lowers row density per page, requiring more disk pages, more memory buffers, and more I/O operations for full table scans."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "What are 'Raw Files' in physical database storage configuration, and why are they used?",
        "correct": "Storage files that bypass operating system file system caches, allowing the DBMS to manage I/O and caching directly",
        "distractors": [
            "Unformatted plain text files exported to floppy disks for external disaster recovery archival vaults",
            "Corrupted database data files that have suffered unrecoverable physical disk platter head crashes",
            "Temporary files created by client web browsers when downloading high-resolution image attachments"
        ],
        "explanation": "Slide 19 states: 'Raw Files: Can be used to bypass the O/S' file system caching, preventing double-buffering and giving the DBMS direct control over disk I/O."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "When should a DBA consider placing specific database objects on Solid State Devices (SSDs)?",
        "correct": "For performance-critical tables or high-traffic indexes that experience extreme I/O throughput requirements",
        "distractors": [
            "Only for cold historical data archives that are read once every five years by external regulatory auditors",
            "Exclusively for storing uncompressed audio and video multimedia files that exceed ten gigabytes each",
            "Only when the operating system kernel is running in single-user disaster recovery recovery mode"
        ],
        "explanation": "Slide 19 states: 'Solid State Devices: For performance-critical objects. Storing databases having extreme performance requirements on solid state devices instead of disk can improve performance...'"
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "A table experiences severe row migration where the DBMS frequently must store pointers on original pages pointing to overflow pages. What was the design flaw?",
        "correct": "PCTFREE was set too low for a table where rows expand significantly when variable columns are updated",
        "distractors": [
            "The DBA created too many clustered indexes on the underlying physical database tablespace",
            "The operating system file system format was incompatible with the server's optical storage drive",
            "The application developers wrote SQL statements that contained syntax errors in WHERE clauses"
        ],
        "explanation": "Slide 18 points out that inadequate PCTFREE causes row migration because expanded rows cannot fit on their home page and must be relocated with forwarding pointers."
    },
    {
        "topic": "Column Ordering, Storage Planning & Free Space",
        "question": "Which of the following database objects requires physical disk storage allocation from the database administrator?",
        "correct": "Both base table data structures and secondary index structures require dedicated physical storage space",
        "distractors": [
            "Only base table data structures require physical disk storage; indexes are stored entirely in CPU registers",
            "Only views require physical disk storage; base tables exist purely as virtual in-memory definitions",
            "Neither base tables nor indexes require storage because relational databases are purely conceptual models"
        ],
        "explanation": "Slide 19 explicitly notes under Type of Files: 'Data / Index: Both require storage.'"
    },

    # -------------------------------------------------------------------------
    # Topic 7: Index Architectures & Access Optimization (Q94 - Q108)
    # -------------------------------------------------------------------------
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What is the primary operational trade-off that a DBA must evaluate before creating secondary indexes on a relational table?",
        "correct": "Indexes accelerate read queries and avoid table scans, but impose a write overhead penalty on INSERT, UPDATE, and DELETE",
        "distractors": [
            "Indexes eliminate the need for primary keys, but permanently disable multi-column SQL join operations",
            "Indexes reduce server physical memory usage to zero, but increase the financial cost of software licenses",
            "Indexes enable unlimited concurrent user connections, but prevent the operating system from performing backups"
        ],
        "explanation": "Slide 21 notes: 'DBMS maintains all indexes (modifications incur cost)'. Indexes improve read access and avoid table scans, but slow down data modifications."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "Who or what ultimately decides whether an index will actually be used to execute a given SQL query?",
        "correct": "The DBMS cost-based query optimizer, based on catalog statistics, filter selectivity, and available access paths",
        "distractors": [
            "The application programmer, who must manually hardcode physical disk sector addresses into SQL syntax",
            "The operating system kernel scheduler, which assigns indexes based on CPU clock frequency variations",
            "The hardware storage area network controller, which inspects packet headers as they traverse fiber switches"
        ],
        "explanation": "Slide 21 explicitly states: 'Optimize data access: DBMS decides whether or not to use an index'."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "Why is it strongly recommended to create indexes on foreign key columns in a relational database?",
        "correct": "To speed up referential integrity checks and accelerate join operations between parent and child tables",
        "distractors": [
            "To prevent the parent table from ever being dropped or altered by the database administrator",
            "To force the foreign key column to automatically generate unique incremental sequence numbers",
            "To ensure that foreign key values are automatically encrypted with public key algorithms on disk"
        ],
        "explanation": "Slide 21 states: 'Recommended on foreign key columns to speed RI access' (referential integrity enforcement and join queries)."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What does the performance concept 'Index-Only Access' (IXO) mean in database query processing?",
        "correct": "The query can be satisfied entirely by retrieving columns from the index leaf pages without accessing base table pages",
        "distractors": [
            "The database table has zero columns and consists purely of an index directory file on physical disk",
            "The database administrator has revoked all user permissions except the ability to view index catalog metadata",
            "The query optimizer refuses to execute any SQL statements that do not contain an explicit ORDER BY clause"
        ],
        "explanation": "Slide 21 states: 'If all columns are in the index you can get index-only access (IXO)', completely eliminating base table page I/O."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What is the recommended design philosophy regarding how indexes should be created across an enterprise database?",
        "correct": "Create indexes based on application workload and query patterns rather than blindly indexing table columns",
        "distractors": [
            "Create an index on every single column of every table to ensure all conceivable queries run at maximum speed",
            "Only create indexes on tables that have fewer than one hundred rows to minimize operating system overhead",
            "Index only columns whose names begin with vowels to balance binary tree node distribution across disks"
        ],
        "explanation": "Slide 21 explicitly directs: 'Create indexes based on workload (not tables)'."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What are the structural components of a standard balanced B-Tree database index as illustrated in the course?",
        "correct": "A Root page at the top, intermediate Nonleaf directory pages, and bottom Leaf pages containing key values and row pointers",
        "distractors": [
            "A master boot record, an operating system file allocation table, and unorganized heap storage sectors",
            "A single flat sequential text file containing comma-separated key values sorted in descending order",
            "A circular ring buffer residing exclusively in CPU L2 cache memory without persistent disk pages"
        ],
        "explanation": "Slide 22 illustrates the B-Tree hierarchy: Root Page (Level 1), Nonleaf Pages (Levels 2-3), and Leaf Pages (Level 4 pointing to table data)."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "Why does a balanced B-Tree index ensure efficient search performance as a database table scales to millions of rows?",
        "correct": "Traversing the tree from root to leaf takes logarithmic time O(log N), keeping the number of page reads very small",
        "distractors": [
            "The B-Tree loads the entire table into memory and performs a sequential scan across all rows simultaneously",
            "The B-Tree converts all alphanumeric keys into 16-bit integer values that bypass operating system security",
            "The B-Tree eliminates all disk access by predicting user queries before they are submitted by applications"
        ],
        "explanation": "Slide 24 explains: 'The B-tree ensures that the search for 104 is done in logarithmic time, reducing the number of comparisons needed as the tree grows.'"
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "How is a Bitmap Index structured and represented internally within a database system?",
        "correct": "Each distinct column value has a bit string where each bit position corresponds to a row, set to 1 if matched and 0 if not",
        "distractors": [
            "It stores high-resolution graphical bitmap image files of each database record on optical storage media",
            "It maintains a sequential linked list of encrypted string values pointing to operating system swap files",
            "It replaces the relational table with a two-dimensional matrix of floating point numbers in RAM memory"
        ],
        "explanation": "Slides 25 and 26 describe bitmap indexes: distinct values have positional bit strings (e.g. 'Male' 1000011101, 'Female' 0110000010) where bit position matches row number."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "Under which of the following conditions is a Bitmap Index most effective and appropriate?",
        "correct": "On low-cardinality columns (such as Gender or Marital Status) in read-heavy analytical and ad-hoc query environments",
        "distractors": [
            "On high-cardinality primary keys undergoing thousands of concurrent online transactional inserts per second",
            "On large binary object (BLOB) columns containing raw video recordings and uncompressed audio streams",
            "On rapidly changing monetary balance fields in high-volume automated teller machine networks"
        ],
        "explanation": "Slides 25 and 26 demonstrate bitmap indexes on low-cardinality columns like Gender. Bitmap indexes suffer high locking overhead on OLTP updates but excel in read-heavy analytics."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "Why are Bitmap Indexes particularly powerful when executing complex queries with multiple WHERE filtering conditions?",
        "correct": "The DBMS can rapidly combine multiple bitmap strings using ultra-fast hardware-level bitwise Boolean operations (AND, OR, NOT)",
        "distractors": [
            "The DBMS automatically compiles the query into native assembly code that bypasses the operating system kernel",
            "Bitmap indexes convert SQL queries into high-resolution graphic images displayed on client workstations",
            "They allow the database to bypass all transactional logging and ACID guarantees during query execution"
        ],
        "explanation": "Bitmap indexes allow multi-column conditions (e.g., Gender = 'Female' AND Status = 'Active') to be evaluated by performing bitwise AND operations across bitmaps before touching data."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What is a Reverse Key Index, and how does it manipulate key values internally?",
        "correct": "A B-Tree index where the byte sequence of each indexed column value is reversed before insertion into the tree",
        "distractors": [
            "An index that sorts all database records in descending alphabetical order from Z to A on physical disk",
            "An index that encrypts primary keys with private cryptographic keys to prevent unauthorized user access",
            "An index that automatically deletes historical database records whenever new rows are inserted"
        ],
        "explanation": "Slide 27 defines Reverse Key Index: 'is a type of B-tree index where the order of bytes of each indexed column is reversed.'"
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What specific concurrency bottleneck is a Reverse Key Index designed to eliminate in high-volume transaction processing?",
        "correct": "Insert contention on the rightmost leaf block of a B-Tree caused by monotonically increasing sequential keys",
        "distractors": [
            "Network packet collisions between client web browsers and the enterprise border gateway router",
            "Operating system file system lock timeouts caused by concurrent full database backups at midnight",
            "Memory buffer pool corruption occurring when user queries execute cartesian product joins"
        ],
        "explanation": "Slide 27 states: 'This approach is particularly useful for reducing contention on frequently accessed keys.' Monotonic sequence keys (1001, 1002, 1003) all hit the rightmost leaf page; reversing bytes scatters inserts across different leaves."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What is the primary operational trade-off or limitation of implementing a Reverse Key Index?",
        "correct": "It efficiently supports point lookups but renders index range scans (e.g. BETWEEN or >) completely ineffective",
        "distractors": [
            "It permanently prevents the DBMS from enforcing unique primary key constraints on the indexed column",
            "It requires four times more physical disk storage space than a standard balanced B-Tree index structure",
            "It can only be created on text columns and cannot be used with integer or numeric sequence columns"
        ],
        "explanation": "Because adjacent sequential keys are scattered across completely different leaf blocks when bytes are reversed, range scanning (e.g., WHERE id BETWEEN 100 AND 200) cannot follow sequential leaf pointers."
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "What is a Partitioned Index as described in the course materials?",
        "correct": "A B-Tree index broken up into separate chunks or partitions matching table partitions to enhance performance and availability",
        "distractors": [
            "An index that is split between in-memory RAM caches and remote cloud tape archives for cost reduction",
            "An index created exclusively on temporary tables that are automatically dropped when sessions disconnect",
            "An index that randomly distributes index leaf pointers across unformatted operating system swap spaces"
        ],
        "explanation": "Slide 27 defines Partitioned Index: 'a b-tree index specifying how to break up the index (and perhaps the underlying table) into separate chunks, or partitions; to enhance performance and availability.'"
    },
    {
        "topic": "Index Architectures & Access Optimization",
        "question": "An EMPLOYEE table has 10 rows. A bitmap index on Gender has 'Male' as 1000011101 and 'Female' as 0110000010. Which rows represent female employees?",
        "correct": "Rows 2, 3, and 9",
        "distractors": [
            "Rows 1, 6, 7, 8, and 10",
            "Rows 4, 5, and 6",
            "Rows 1, 2, and 3"
        ],
        "explanation": "Slide 26 explains this exact example: '0110000010 ... indicate that rows 2, 3, and 9 are females (where bits at positions 2, 3, and 9 are 1).'"
    },

    # -------------------------------------------------------------------------
    # Topic 8: Partitioning, Hashing, Clustering & Interleaving (Q109 - Q122)
    # -------------------------------------------------------------------------
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "What is the primary architectural goal of implementing Table Partitioning in physical database design?",
        "correct": "To break large tables into smaller, manageable chunks across storage devices, enhancing performance, maintenance, and availability",
        "distractors": [
            "To convert all relational tables into flat comma-delimited text files to facilitate manual spreadsheet editing",
            "To eliminate the need for SQL query optimization by delegating all join processing to client workstations",
            "To prevent application programs from accessing more than one record at a time to reduce server power consumption"
        ],
        "explanation": "Slide 28 and 35 describe partitioning as breaking up tables and indexes into separate chunks to enhance performance, parallel processing, and management."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "Consider the following SQL DDL statement: 'CREATE TABLE Customers (...) PARTITION BY HASH (CustomerID) PARTITIONS 4;'. How does the DBMS distribute data?",
        "correct": "It applies an internal hash function to CustomerID to distribute rows evenly across 4 discrete physical partitions",
        "distractors": [
            "It duplicates all customer rows across four identical database server instances located in different countries",
            "It restricts the Customers table to storing a maximum of four total customer records in physical memory",
            "It creates four separate clustered indexes on CustomerID, each sorted in a different European language"
        ],
        "explanation": "Slide 35 demonstrates this exact syntax: hashing the CustomerID evenly distributes rows across the 4 specified partitions."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "How does a database Hashing algorithm determine the storage location for a given record key?",
        "correct": "It feeds the key value into a mathematical hash function (e.g. key % table_size) to compute the target slot address directly",
        "distractors": [
            "It performs a sequential binary search across all physical disk blocks until an empty slot is encountered",
            "It queries an external internet domain name server to obtain an authorized IP address for the data record",
            "It sorts all table records alphabetically in temporary memory buffers before writing them sequentially to disk"
        ],
        "explanation": "Slides 29 and 30 illustrate the hash algorithm: `def hash_function(user_id, table_size): return user_id % table_size` to calculate the direct storage index."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "In a hash-based storage architecture with table_size = 5 and hash_function = user_id % 5, which pair of user IDs will result in a collision?",
        "correct": "User ID 1 and User ID 6 (both evaluate to index 1)",
        "distractors": [
            "User ID 1 and User ID 2 (evaluating to index 1 and 2)",
            "User ID 3 and User ID 5 (evaluating to index 3 and 0)",
            "User ID 2 and User ID 4 (evaluating to index 2 and 4)"
        ],
        "explanation": "Slide 30 shows this exact collision example: 1 % 5 = 1, and 6 % 5 = 1, resulting in a collision handled by chaining."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "How are hash collisions typically resolved when multiple records hash to the same primary storage bucket or slot?",
        "correct": "Using collision chaining (linked lists of records) or directing colliding records into dedicated overflow pages",
        "distractors": [
            "The DBMS automatically overwrites and permanently deletes the older record to accommodate the new one",
            "The database server immediately raises a fatal hardware panic and terminates the database instance",
            "The DBMS rejects the insert operation and forces the client application to change the customer's primary key"
        ],
        "explanation": "Slides 29 and 30 show collision handling: chaining (each slot starts as an empty list for chaining) or overflow storage locations."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "What is a Clustered Index, and how does it physically organize data rows on storage media?",
        "correct": "It physically arranges the actual table data rows on disk in the exact sorted order of the clustered index key column",
        "distractors": [
            "It stores all database indexes on a multi-node cluster of servers while leaving table data on optical discs",
            "It compresses multiple relational tables into a single encrypted zip archive to reduce operating system storage",
            "It maintains pointers to randomly scattered data rows across disk without altering their physical sequence"
        ],
        "explanation": "Slides 21, 32, and 33 explain: 'Creating a Clustered Index... This will organize the rows of the Sales table physically based on the sale date.'"
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "Why can a relational database table have at most ONE clustered index?",
        "correct": "Because table data rows can only be physically arranged in one physical sequence on disk storage pages",
        "distractors": [
            "DBMS licensing restrictions legally prohibit more than one index of any type on a commercial table",
            "Operating system file systems only permit a single file pointer per directory entry on disk volumes",
            "The central processing unit cannot execute binary search algorithms on more than one index structure"
        ],
        "explanation": "Physical table rows can only reside in a single physical order on disk blocks. Therefore, only one index can dictate that physical clustered order."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "For which of the following query types does a Clustered Index provide the GREATEST performance improvement?",
        "correct": "Range-based retrieval queries (such as WHERE Sale_Date BETWEEN '2024-10-01' AND '2024-10-31')",
        "distractors": [
            "Random single-record primary key lookups across widely scattered unclustered partition buckets",
            "Ad-hoc count queries on tables with zero rows that execute without touching disk storage media",
            "Data Definition Language DROP TABLE commands executed by database administrators during maintenance"
        ],
        "explanation": "Slide 33 illustrates clustering on Sale_Date and executing `BETWEEN '2024-10-01' AND '2024-10-02'`. Because matching rows are physically contiguous on disk, I/O is minimized."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "What is the primary operational overhead associated with maintaining a Clustered Index during ongoing table modifications?",
        "correct": "Inserts of out-of-order keys force the DBMS to physically shift rows and cause page splits to maintain order",
        "distractors": [
            "Every SELECT query causes the operating system to reformat the physical disk drive partitions",
            "The DBMS must terminate all network connections and reboot the server after every hundred transactions",
            "Application developers must manually update index pointers in host programming code using pointers"
        ],
        "explanation": "Because rows must be maintained in physical key order, inserting a key into a full page requires page splits and shifting rows, incurring higher write I/O."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "What is 'Data Interleaving' as a physical performance design technique?",
        "correct": "Physically storing rows from two or more related tables (e.g. parent and child) together in the same physical disk block",
        "distractors": [
            "Alternating backup operations between magnetic tape reels and external cloud object storage buckets",
            "Splitting application program execution threads evenly across multiple physical central processing units",
            "Writing transaction log records alternately in uppercase and lowercase ASCII text characters on disk"
        ],
        "explanation": "Slide 34 illustrates Data Interleaving: storing Table 1 and Table 2 data together within the same database file blocks."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "What are the two common implementation methods for data interleaving mentioned in the course material?",
        "correct": "Row-Column Interleaving and Block Interleaving",
        "distractors": [
            "Optical Interleaving and Magnetic Tape Splicing",
            "Dynamic Assembly Interleaving and Static Compiling",
            "Serial Bus Interleaving and Parallel Port Multiplexing"
        ],
        "explanation": "Slide 34 lists: 'Row-Column Interleaving: Data is distributed across rows and columns... Block Interleaving: Blocks of data are distributed in a way that balances load...'"
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "What is the principal performance advantage of data interleaving, and what is its major trade-off?",
        "correct": "It speeds up joins between related parent-child tables on that block, but degrades performance for full table scans of a single table",
        "distractors": [
            "It eliminates all storage requirements for child tables, but prevents the database from using primary keys",
            "It allows tables to self-heal after hardware crashes, but doubles network bandwidth consumption for clients",
            "It makes SQL queries easier for human developers to read, but requires specialized solid-state hardware"
        ],
        "explanation": "Interleaving places related parent/child rows on the same block, satisfying joins in a single I/O read. However, scanning only Table 1 requires reading blocks cluttered with Table 2 data."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "A table experiences heavy analytical range queries filtering by transaction timestamp. Which physical structure should the DBA implement?",
        "correct": "A Clustered Index on the transaction timestamp column",
        "distractors": [
            "A Reverse Key Index on the customer telephone number column",
            "A Bitmap Index on a high-cardinality primary key column",
            "A non-clustered hash index stored in operating system swap space"
        ],
        "explanation": "Slide 33: Clustered indexes order rows physically by the indexed column (e.g. Sale_Date), providing optimal performance for range queries."
    },
    {
        "topic": "Partitioning, Hashing, Clustering, and Interleaving",
        "question": "In a distributed database cluster, how does Hash Partitioning help prevent storage 'hot spotting'?",
        "correct": "The hash algorithm randomizes key distribution, spreading incoming writes evenly across all available physical partition nodes",
        "distractors": [
            "It directs all incoming write operations exclusively to a single master disk while keeping other disks idle",
            "It compresses all partition data into a single read-only file that bypasses the operating system buffer pool",
            "It forces client applications to wait for periodic batch windows before inserting new transactional records"
        ],
        "explanation": "Hash partitioning computes target partition = hash(key) % N, spreading sequential or grouped keys uniformly across disks to eliminate hot spotting."
    },

    # -------------------------------------------------------------------------
    # Topic 9: Denormalization Strategies, Views & Temporal Data (Q123 - Q135)
    # -------------------------------------------------------------------------
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "According to the source material, what is the ONLY valid reason to ever denormalize a relational database design?",
        "correct": "To achieve acceptable or optimal performance when a fully normalized design cannot meet required workload SLAs",
        "distractors": [
            "To simplify database design diagrams so they fit onto standard letter-sized office printer paper",
            "To reduce the number of columns in the database catalog to comply with vendor software license tiers",
            "To allow junior programmers who do not understand relational algebra to write queries without joins"
        ],
        "explanation": "Slide 37 explicitly states: 'The only reason to denormalize, ever: To achieve optimal performance! If the database design achieve satisfactory performance fully normalized, then there is no need to denormalize.'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "Which critical prerequisite question must a DBA evaluate before deciding to implement a denormalized structure?",
        "correct": "Can the system achieve acceptable performance without denormalizing, and will the system be less reliable due to it?",
        "distractors": [
            "Does the operating system kernel support legacy twelve-bit ASCII character encoding sets?",
            "Can the database administrator rewrite the commercial DBMS query compiler in procedural assembly code?",
            "Will denormalizing allow the enterprise to cancel all data backup and disaster recovery tape subscriptions?"
        ],
        "explanation": "Slide 37 lists the questions: 'Can the system achieve acceptable performance without denormalizing? Will the performance after denormalizing still be unacceptable? Will the system be less reliable due to denormalization?'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "Why does denormalization impose a heavy ongoing administrative burden on the database administration team?",
        "correct": "It introduces redundant data, requiring documentation, synchronization propagation jobs, and ongoing integrity auditing",
        "distractors": [
            "It permanently corrupts the database catalog, requiring the DBA to manually reinstall the DBMS weekly",
            "It forces all client application queries to be routed through external third-party clearinghouses",
            "It eliminates the ability to use SQL DML statements, forcing manual byte manipulation via hexadecimal editors"
        ],
        "explanation": "Slide 38 details Denormalization Administration: documenting decisions, ensuring data validity, scheduling migration/propagation jobs, informing users, and periodic re-analysis."
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "Why should a DBA periodically re-analyze denormalized tables in an evolving enterprise environment?",
        "correct": "Hardware upgrades, DBMS optimizer improvements, or changing workload patterns may make denormalization unnecessary",
        "distractors": [
            "Denormalized tables automatically delete their own data after twelve months of continuous operational uptime",
            "Commercial software licensing agreements mandate that all redundant columns be purged annually before audits",
            "The operating system file system converts denormalized tables into unindexed binary graphics files over time"
        ],
        "explanation": "Slide 38 notes: 'Analyzing the database periodically to decide whether denormalization is still required.' New faster hardware or software might allow returning to a clean normalized schema."
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "How do Views contribute to physical database design and security even though they are conceptually part of logical design?",
        "correct": "They provide virtual representations that restrict row/column access, mask complex joins, and present derived calculations",
        "distractors": [
            "They allocate dedicated physical disk cylinders to store redundant copies of base table rows for fast lookups",
            "They automatically convert relational table data into compressed video files for playback in web browsers",
            "They eliminate the need for primary and foreign key constraints by enforcing physical clustering at runtime"
        ],
        "explanation": "Slides 40, 41, and 44 explain that views are virtual tables created from SELECT statements used for row/column security, efficient access paths, data derivation, and masking complexity."
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "Which of the following is an explicit 'View Usage Rule' highlighted in the database design course material?",
        "correct": "DO NOT create one view per base table, as this introduces unnecessary catalog bloat and maintenance overhead",
        "distractors": [
            "Every base table must have at least five distinct views before applications are permitted to issue SELECT queries",
            "Views must never contain WHERE clauses, restricting filtering operations exclusively to client host code",
            "Views can only be queried by system administrators and are completely hidden from regular application users"
        ],
        "explanation": "Slide 44 emphasizes in capital letters: 'DO NOT USE ONE VIEW PER BASE TABLE!' alongside rules on security, access, and masking complexity."
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "How does a view implement column-level and row-level security within a relational database?",
        "correct": "By selecting only permitted columns in the SELECT list and applying row filtering predicates in the view's WHERE clause",
        "distractors": [
            "By encrypting the physical server hard drive using biometric fingerprint authentication for each user",
            "By physically moving unauthorized rows to a separate database server located in a different data center",
            "By terminating the client network connection whenever an unauthorized user logs into the local operating system"
        ],
        "explanation": "Slide 44 lists 'Security - row and column level' as a primary view usage rule. Column-level security omits sensitive columns; row-level security uses WHERE predicates."
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "Which SQL category encompasses the GRANT and REVOKE commands used to administer database permissions and security?",
        "correct": "Data Control Language (DCL)",
        "distractors": [
            "Data Definition Language (DDL)",
            "Data Manipulation Language (DML)",
            "Data Extraction Language (DEL)"
        ],
        "explanation": "Slide 46 defines: 'Data Control Language (DCL) - Security & Access Control. Used to control user access and security within the database: GRANT, REVOKE.'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "Which SQL category encompasses the CREATE, ALTER, and DROP statements used to define and modify physical database structures?",
        "correct": "Data Definition Language (DDL)",
        "distractors": [
            "Data Manipulation Language (DML)",
            "Data Control Language (DCL)",
            "Dynamic Execution Language (DEL)"
        ],
        "explanation": "Slide 47 defines: 'Data Definition Language (DDL) - Structure Definition. Used to define, modify, and delete database objects like tables, indexes, and schemas.'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "In temporal database design, what does 'Business Time' (also known as Valid Time or Application Time) represent?",
        "correct": "The real-world timeframe during which a business fact or state is valid and true (e.g. policy term or contract period)",
        "distractors": [
            "The physical timestamp recorded on magnetic storage media when a disk sector was formatted by the OS",
            "The exact number of CPU clock cycles elapsed while the query optimizer evaluated execution plans in memory",
            "The standard business operating hours during which end users are permitted to submit transactional updates"
        ],
        "explanation": "Slides 51 and 53 define Business Time: 'Business Time represents the period during which a fact or record is valid or true in the real world... defined by the application (valid_from, valid_to).'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "In temporal database architectures, how is 'System Time' (also known as Transaction Time) defined and managed?",
        "correct": "It tracks when a record was stored, updated, or deleted in the system, and is automatically maintained by the DBMS engine",
        "distractors": [
            "It records the employee's personal work shift hours and is manually entered by payroll clerks via forms",
            "It tracks the warranty expiration date of the physical server chassis and is managed by hardware technicians",
            "It specifies how long a client web browser cookie remains valid before requiring user re-authentication"
        ],
        "explanation": "Slides 51 and 55 define System Time: 'System Time refers to the period during which a record is stored in the database... automatically managed by the database and is useful for auditing.'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "How are Business Time and System Time physically maintained within the underlying database architecture?",
        "correct": "Business Time is typically tracked in a single table, whereas System Time uses two tables (current table and history table)",
        "distractors": [
            "Business Time is stored exclusively in client memory buffers, while System Time is stored on magnetic tape drives",
            "Business Time requires twenty relational tables, while System Time requires zero persistent storage structures",
            "Both must be stored in external flat text files outside the relational database management system"
        ],
        "explanation": "Slide 58 explicitly contrasts the physical implementation: 'Business Time is tracked in a single table... System Time is tracked using two tables. One table contains the current data. Another, history table, contains non-current data.'"
    },
    {
        "topic": "Denormalization Strategies & Administration",
        "question": "An insurance enterprise must determine exactly what insurance coverage terms were active for a customer on April 15, 2012. What database feature natively supports this?",
        "correct": "Temporal Data Support (querying historical state using Business Time and System Time periods)",
        "distractors": [
            "Reverse Key B-Tree Indexing on the customer's policy identification number",
            "Data Control Language REVOKE commands applied to historical audit tables",
            "Full table scans executed across raw operating system file system caches"
        ],
        "explanation": "Slides 49, 50, and 59 use the insurance company scenario to demonstrate why temporal data management is necessary: determining what coverage was in effect at a past point in time."
    }
]

print(f"Loaded Batch 2 with {len(BATCH2)} questions.")
