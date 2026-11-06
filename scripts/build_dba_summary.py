import os, subprocess

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
    background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
    color: #ffffff;
    padding: 40px;
    border-radius: 12px;
    margin-bottom: 30px;
    box-shadow: 0 10px 25px -5px rgba(59, 130, 246, 0.3);
}

.cover h1 {
    font-size: 28px;
    font-weight: 800;
    margin: 0 0 10px 0;
    letter-spacing: -0.5px;
}

.cover .subtitle {
    font-size: 16px;
    opacity: 0.9;
    margin: 0 0 15px 0;
}

.cover .meta {
    display: flex;
    gap: 15px;
    font-size: 12px;
    opacity: 0.8;
}

.section {
    margin-bottom: 30px;
    page-break-inside: avoid;
}

h2 {
    font-size: 19px;
    font-weight: 700;
    color: #1e3a8a;
    border-bottom: 2px solid #e2e8f0;
    padding-bottom: 8px;
    margin-top: 25px;
    margin-bottom: 15px;
    display: flex;
    align-items: center;
    gap: 8px;
}

body.ar h2 {
    color: #1e3a8a;
}

h3 {
    font-size: 15px;
    font-weight: 600;
    color: #334155;
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
    background: #f8fafc;
    border-left: 4px solid #3b82f6;
    padding: 12px 16px;
    border-radius: 0 8px 8px 0;
    margin: 15px 0;
    font-size: 13px;
}

body.ar .callout {
    border-left: none;
    border-right: 4px solid #3b82f6;
    border-radius: 8px 0 0 8px;
}

.callout.warning {
    border-color: #f59e0b;
    background: #fffbeb;
}

.callout.tip {
    border-color: #10b981;
    background: #f0fdf4;
}

.callout-title {
    font-weight: 700;
    margin-bottom: 4px;
    color: #0f172a;
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
    background-color: #f1f5f9;
    font-weight: 700;
    color: #1e293b;
}

tr:nth-child(even) {
    background-color: #f8fafc;
}

.badge {
    display: inline-block;
    padding: 2px 8px;
    font-size: 11px;
    font-weight: 600;
    border-radius: 4px;
    background: #e2e8f0;
    color: #334155;
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

html_dba_en = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Database Administration (DBA) - Comprehensive Midterm Summary</title>
<style>{css_shared}</style>
</head>
<body>

<div class="cover">
    <h1>Database Administration (DBA)</h1>
    <div class="subtitle">Complete Midterm Study Guide & Comprehensive Knowledge Reference</div>
    <div class="meta">
        <span>Covering: Lectures 1, 2, 3, 4, 5</span>
        <span>•</span>
        <span>Physical Design, Roles, Indexing, SQL & Transactions</span>
    </div>
</div>

<div class="section">
    <h2>1. Executive Overview & Core Concepts (Lecture 1)</h2>
    <p>Database Administration is a critical <strong>management discipline</strong> focused on orchestrating, securing, and optimizing enterprise data infrastructure. Data is recognized as the ultimate corporate asset; systems and hardware become obsolete, but data persists indefinitely.</p>
    
    <div class="callout tip">
        <div class="callout-title">Core Definition of a DBA</div>
        A <strong>Database Administrator (DBA)</strong> is the information technician responsible for ensuring the operational environment and directing the infrastructure for an organization's data.
    </div>

    <h3>1.1 What Makes a Good DBA? (Avoiding Anti-Patterns)</h3>
    <ul>
        <li><strong>Jack of All Trades:</strong> The DBA must bridge software development, operating systems, hardware configuration, network security, and business domain logic.</li>
        <li><strong>The Curmudgeon in the Corner (Prima Donna Anti-Pattern):</strong> A negative persona to avoid at all costs—an unapproachable technician who reflexively says "No" to developers and business requests, creating an enterprise bottleneck.</li>
        <li><strong>A Good DBA:</strong> Collaborates with developers early in the SDLC, proactively designs for scalability, documents procedures, and adopts automated monitoring rather than firefighting.</li>
    </ul>

    <h3>1.2 Database 101: Database vs. DBMS</h3>
    <table>
        <tr>
            <th>Concept</th>
            <th>Definition</th>
            <th>Examples / Scope</th>
        </tr>
        <tr>
            <td><strong>Database</strong></td>
            <td>An organized, structured store of persistent data models representing entities, relationships, and constraints.</td>
            <td>CustomerDB, Sales_2026, MedicalRecords</td>
        </tr>
        <tr>
            <td><strong>DBMS</strong></td>
            <td>The sophisticated software engine that creates, manages, optimizes, secures, and controls access to databases.</td>
            <td>Oracle Database, IBM DB2, Microsoft SQL Server, PostgreSQL, MySQL</td>
        </tr>
    </table>

    <h3>1.3 Administrative Roles Comparison</h3>
    <table>
        <tr>
            <th>Role</th>
            <th>Primary Responsibility</th>
            <th>Key Focus Area</th>
        </tr>
        <tr>
            <td><strong>Data Administrator (DA / CDO)</strong></td>
            <td>Business data governance, metadata policies, business glossaries, conceptual/logical data modeling.</td>
            <td>Business meaning, data ownership, regulatory data classification.</td>
        </tr>
        <tr>
            <td><strong>System Administrator (SA)</strong></td>
            <td>Operating system, hardware servers, storage RAID arrays, network routing, OS-level security.</td>
            <td>Physical server health, OS kernel patches, memory/disk allocation.</td>
        </tr>
        <tr>
            <td><strong>Database Administrator (DBA)</strong></td>
            <td>DBMS software installation, physical database realization, SQL query optimization, disaster recovery, ACID transaction management.</td>
            <td>DBMS instance configuration, index tuning, backup/recovery, high availability.</td>
        </tr>
    </table>

    <h3>1.4 Specialized Types of DBAs</h3>
    <ul>
        <li><strong>System DBA:</strong> Configures the DBMS software engine, tunes DBMS memory pools/buffer caches, applies vendor software patches, and executes version migrations.</li>
        <li><strong>Application DBA:</strong> Embedded with software engineering teams, specializing in query optimization, table schemas, and data access logic for specific business applications.</li>
        <li><strong>Database Architect & Analyst:</strong> Blueprints enterprise-wide data flows, integration pipelines, and long-term infrastructure roadmaps.</li>
        <li><strong>Data Modeler:</strong> Translates business requirements into normalized Conceptual and Logical Entity-Relationship Diagrams (ERDs).</li>
        <li><strong>Data Warehouse Administrator (DWA):</strong> Manages OLAP systems, star/snowflake schemas, ETL loading pipelines, and massive analytical data stores.</li>
        <li><strong>Task-Oriented DBA:</strong> Focuses exclusively on specialized enterprise domains such as Disaster Recovery, Security/Compliance Auditing, or Performance Diagnostics.</li>
        <li><strong>Procedural DBA:</strong> Manages procedural logic inside the database engine (Stored Procedures, Triggers, User-Defined Functions - UDFs) to ensure they do not cause deadlocks or drain server CPU.</li>
        <li><strong>Cloud DBA:</strong> Operates in Managed Cloud Database environments (DBaaS like AWS RDS, Azure SQL, Google Cloud SQL). Low-level hardware maintenance is offloaded, shifting the DBA's focus to cloud cost optimization, autoscaling, and data security.</li>
    </ul>

    <h3>1.5 DBA Reporting Structures & Staffing Rules of Thumb</h3>
    <ul>
        <li><strong>Centralized (Infrastructure/Operations):</strong> Fosters standardized corporate policies, uniform backup/DR protocols, and independent architectural oversight.</li>
        <li><strong>Decentralized (Application Teams):</strong> Enhances agility and application responsiveness, but risks creating isolated data silos and non-standard schemas.</li>
        <li><strong>Staffing Determinants:</strong> DBA headcount is determined by instance count, total data volume, transaction throughput (OLTP vs DSS), 24/7 SLA uptime demands, and the maturity of automated monitoring tools.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. Physical Database Design, Storage & Indexing (Lectures 2 & 3)</h2>
    <p>Physical database design translates the logical data model into physical storage structures within the target DBMS, optimizing for performance, storage efficiency, and data integrity.</p>

    <h3>2.1 Translation from Logical to Physical</h3>
    <table>
        <tr>
            <th>Logical Concept</th>
            <th>Physical Implementation</th>
            <th>Design Decisions & Rules of Thumb (ROTs)</th>
        </tr>
        <tr>
            <td>Entity</td>
            <td>Table</td>
            <td>Choose table space, partition key, and row format.</td>
        </tr>
        <tr>
            <td>Attribute</td>
            <td>Column</td>
            <td>Assign exact data type (INT, VARCHAR, TIMESTAMP), NULL / NOT NULL rules, DEFAULT values.</td>
        </tr>
        <tr>
            <td>Primary Identifier</td>
            <td>Primary Key Constraint</td>
            <td>Backed by a unique index (frequently clustered).</td>
        </tr>
        <tr>
            <td>Relationship</td>
            <td>Foreign Key Constraint</td>
            <td>Enforces referential integrity (ON DELETE CASCADE, SET NULL, RESTRICT).</td>
        </tr>
    </table>

    <div class="callout warning">
        <div class="callout-title">Physical ROTs: Column Ordering & Sizing</div>
        Place fixed-length, frequently searched columns at the beginning of the row layout (allowing direct offset calculation by the CPU), and variable-length columns (VARCHAR, LOBs) at the end. Always avoid arbitrary over-allocation of column lengths.
    </div>

    <h3>2.2 Storage Calculation & Free Space Management</h3>
    <ul>
        <li><strong>Row Length:</strong> Sum of column lengths + row overhead header bytes + null indicator bytes.</li>
        <li><strong>Page/Block Capacity:</strong> Data pages (typically 4KB, 8KB, or 16KB) contain a page header, directory slots, and stored rows.</li>
        <li><strong>PCTFREE:</strong> The percentage of each page reserved during initial load to allow existing rows to expand (e.g. updating a short VARCHAR to a longer string) without causing <em>Row Migration</em> or <em>Row Chaining</em>.</li>
        <li><strong>FREEPAGE:</strong> Specifies that an entire empty page is left every <em>N</em> pages to provide space for localized bulk inserts to maintain physical clustering.</li>
    </ul>

    <h3>2.3 B-Tree vs. Bitmap Indexes (Comprehensive Comparison)</h3>
    <table>
        <tr>
            <th>Attribute</th>
            <th>B-Tree Index (B+ Tree)</th>
            <th>Bitmap Index</th>
        </tr>
        <tr>
            <td><strong>Structure</strong></td>
            <td>Multi-level balanced tree: Root page, Intermediate branch pages, and sorted Leaf pages containing keys and RowIDs.</td>
            <td>Array of bit vectors (0s and 1s) for each distinct column value; each bit position corresponds to a physical row number.</td>
        </tr>
        <tr>
            <td><strong>Best For</strong></td>
            <td>High cardinality columns (Primary keys, Social Security Numbers, timestamps). Point queries and range searches.</td>
            <td>Low cardinality columns (Gender, Marital Status, Country, Boolean flags) in read-heavy Data Warehouses (OLAP).</td>
        </tr>
        <tr>
            <td><strong>Query Operations</strong></td>
            <td>Exact match (`=`), Range scans (`BETWEEN`, `>`, `<`), Sorting (`ORDER BY`).</td>
            <td>Boolean bitwise operations (AND, OR, NOT) executed at lightning speed by the CPU across multiple indexed columns.</td>
        </tr>
        <tr>
            <td><strong>Concurrency / OLTP</strong></td>
            <td>High concurrency; row-level locking supported on leaf pages.</td>
            <td><strong>Poor for OLTP:</strong> Updating a single row locks an entire bitmap segment, blocking concurrent transactions.</td>
        </tr>
    </table>

    <h3>2.4 Clustered vs. Non-Clustered Indexes</h3>
    <ul>
        <li><strong>Clustered Index:</strong> The physical storage order of rows in the table matches the logical order of the index key. Because physical table rows can only be arranged on disk in one physical sequence, a table can have <strong>only ONE clustered index</strong>.</li>
        <li><strong>Non-Clustered Index:</strong> A separate index structure containing sorted keys and pointers (RowIDs or clustered index keys) back to the actual data rows. A table can have many non-clustered indexes.</li>
        <li><strong>Covering Index (Index-Only Scan):</strong> When an index contains all columns requested by a SELECT and WHERE clause, the query engine satisfies the request entirely from the index without reading base table pages.</li>
    </ul>

    <h3>2.5 Partitioning & Denormalization</h3>
    <ul>
        <li><strong>Partitioning:</strong> Divides large tables into smaller physical segments based on a key (Range, Hash, or List). Enables <em>partition pruning</em> (skipping unneeded partitions during queries) and fast maintenance (dropping an old year partition instantly).</li>
        <li><strong>Denormalization:</strong> The deliberate introduction of controlled redundancy or grouping of tables into a normalized schema to eliminate costly multi-table JOINs in read-heavy workloads.
            <ul>
                <li><em>Types:</em> Pre-joined tables, derived/calculated summary columns, duplicate redundant attributes.</li>
                <li><em>Costs & Risks:</em> Increased storage, update anomalies, and data integrity degradation if updates fail to sync.</li>
            </ul>
        </li>
    </ul>

    <h3>2.6 Temporal Data Management</h3>
    <ul>
        <li><strong>Business Time (Valid Time / Application Time):</strong> The real-world time period during which a fact was true (e.g., insurance coverage valid from Jan 1 to Dec 31). Managed by application logic.</li>
        <li><strong>System Time (Transaction Time):</strong> The time period during which the record was stored and active in the database system. Managed automatically by the DBMS engine.</li>
        <li><strong>Bi-Temporal Tables:</strong> Support both Business Time and System Time simultaneously, providing an indisputable audit trail of real-world history and system modifications.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>3. Application Development, SQL, Transactions & Locking (Lectures 4 & 5)</h2>

    <h3>3.1 SQL Architecture & Embedded SQL</h3>
    <ul>
        <li><strong>Declarative Language:</strong> In SQL, the developer declares <em>WHAT</em> data is required, not <em>HOW</em> to retrieve it. The DBMS Cost-Based Optimizer (CBO) determines the optimal access path.</li>
        <li><strong>Set-at-a-Time:</strong> Relational operations execute against entire sets of rows simultaneously, unlike 3GL procedural languages that loop record-by-record.</li>
        <li><strong>Embedded SQL & Host Variables:</strong> Embedded SQL places SQL queries inside host languages (C, COBOL). Host variables (prefixed with `:`) exchange parameters between the program and the DBMS.</li>
        <li><strong>Cursors:</strong> A procedural pointer mechanism allowing a 3GL program to iterate through a multi-row SQL result set row-by-row (`DECLARE -> OPEN -> FETCH -> CLOSE`).</li>
    </ul>

    <h3>3.2 Middleware, Object-Relational Mapping & Impedance Mismatch</h3>
    <ul>
        <li><strong>Middleware APIs:</strong> ODBC, JDBC, and ADO.NET provide database-neutral APIs. The <em>Driver Manager</em> routes application calls to the appropriate vendor-specific driver.</li>
        <li><strong>Object-Relational Impedance Mismatch:</strong> The fundamental architectural tension between the Object-Oriented paradigm (classes, polymorphism, object references) and the Relational model (tables, foreign keys, relational algebra).</li>
        <li><strong>ORM Frameworks (Hibernate, Entity Framework):</strong> Automate mapping between objects and tables. DBAs must monitor ORMs to prevent severe performance anti-patterns, such as the <strong>N+1 SELECT problem</strong>.</li>
    </ul>

    <h3>3.3 ACID Properties of Transactions</h3>
    <table>
        <tr>
            <th>Property</th>
            <th>Name</th>
            <th>Guarantee & Description</th>
        </tr>
        <tr>
            <td><strong>A</strong></td>
            <td><strong>Atomicity</strong></td>
            <td>The "All-or-Nothing" principle: either every operation within the transaction succeeds and commits, or all changes are rolled back completely.</td>
        </tr>
        <tr>
            <td><strong>C</strong></td>
            <td><strong>Consistency</strong></td>
            <td>Transactions move the database from one valid state satisfying all schema constraints, checks, and foreign keys to another valid state.</td>
        </tr>
        <tr>
            <td><strong>I</strong></td>
            <td><strong>Isolation</strong></td>
            <td>Concurrently executing transactions do not interfere with each other; uncommitted changes are shielded from other concurrent sessions.</td>
        </tr>
        <tr>
            <td><strong>D</strong></td>
            <td><strong>Durability</strong></td>
            <td>Once committed, updates are permanently written to non-volatile storage (via write-ahead transaction logs) and survive system crashes.</td>
        </tr>
    </table>

    <h3>3.4 Concurrency Control: Lock Types & Deadlocks</h3>
    <ul>
        <li><strong>Shared Lock (S Lock):</strong> Acquired for reading data. Multiple transactions can hold S locks on the same resource concurrently.</li>
        <li><strong>Exclusive Lock (X Lock):</strong> Required for writing or updating data. Grants exclusive access; no other transaction can hold S or X locks on that resource.</li>
        <li><strong>Update Lock (U Lock):</strong> A hybrid lock acquired during read phases before an update to prevent conversion deadlocks.</li>
        <li><strong>Intent Locks (IS, IX, SIX):</strong> Placed at higher levels of the locking hierarchy (table/page) to signal that fine-grained locks exist below.</li>
        <li><strong>Deadlocks:</strong> Circular wait conditions (Transaction A holds Resource 1 and waits for Resource 2; Transaction B holds Resource 2 and waits for Resource 1). The DBMS maintains a <em>Wait-For Graph (WFG)</em>, detects cycles, and aborts a "victim" transaction.</li>
        <li><strong>Lock Escalation:</strong> When a session acquires too many individual row locks, the engine automatically converts them into a single table lock to save memory, severely reducing concurrency.</li>
    </ul>

    <h3>3.5 ANSI SQL Isolation Levels & Concurrency Anomalies</h3>
    <table>
        <tr>
            <th>Isolation Level</th>
            <th>Dirty Read</th>
            <th>Non-Repeatable Read</th>
            <th>Phantom Read</th>
            <th>Default in Most DBMS</th>
        </tr>
        <tr>
            <td><strong>Read Uncommitted</strong></td>
            <td>Permitted</td>
            <td>Permitted</td>
            <td>Permitted</td>
            <td>No</td>
        </tr>
        <tr>
            <td><strong>Read Committed</strong></td>
            <td><strong>Prevented</strong></td>
            <td>Permitted</td>
            <td>Permitted</td>
            <td><strong>Yes (Standard Default)</strong></td>
        </tr>
        <tr>
            <td><strong>Repeatable Read</strong></td>
            <td><strong>Prevented</strong></td>
            <td><strong>Prevented</strong></td>
            <td>Permitted</td>
            <td>No</td>
        </tr>
        <tr>
            <td><strong>Serializable</strong></td>
            <td><strong>Prevented</strong></td>
            <td><strong>Prevented</strong></td>
            <td><strong>Prevented</strong></td>
            <td>No (Strict / Slowest)</td>
        </tr>
    </table>

    <div class="callout tip">
        <div class="callout-title">Core Programming Guidelines for DBAs & Developers</div>
        <ul>
            <li>Keep transactions as short as possible; never wait for user input inside an active transaction.</li>
            <li>Access database tables and rows in the <strong>exact same sequential order</strong> across all applications to eliminate deadlocks.</li>
            <li>Use parameterized queries to enable execution plan caching and prevent SQL injection.</li>
            <li>In large batch jobs, commit in intermediate chunks (e.g. every 5,000 rows) to avoid transaction log exhaustion and lock escalation.</li>
        </ul>
    </div>
</div>

</body>
</html>"""

html_dba_ar = f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<title>إدارة قواعد البيانات (DBA) - ملخص الميدتيرم الشامل</title>
<style>{css_shared}</style>
</head>
<body class="ar">

<div class="cover">
    <h1>إدارة قواعد البيانات (Database Administration - DBA)</h1>
    <div class="subtitle">الملخص الدراسي الشامل والموسوعة المرجعية لامتحان الميدتيرم</div>
    <div class="meta">
        <span>تغطية المحاضرات: 1، 2، 3، 4، 5</span>
        <span>•</span>
        <span>التصميم المادي، الفهارس، المعاملات، الأقفال، وتحسين الأداء</span>
    </div>
</div>

<div class="section">
    <h2>1. نظرة عامة شاملة ومفاهيم الإدارة الأساسية (المحاضرة 1)</h2>
    <p>تُعد إدارة قواعد البيانات (DBA) <strong>تخصصاً إدارياً وتقنياً متكاملاً</strong> يهدف إلى توجيه وبناء وحماية البنية التحتية لبيانات المؤسسة. فالبيانات هي الأصل الأثمن لأي شركة؛ فالأجهزة والبرمجيات تتغير وتفنى، بينما تبقى البيانات وتنمو قيمتها باستمرار.</p>

    <div class="callout tip">
        <div class="callout-title">التعريف الدقيق لمسؤول قواعد البيانات (DBA)</div>
        هو الفني التقني المسؤول عن ضمان البيئة التشغيلية المستقرة وتوجيه وإدارة البنية التحتية الكاملة لبيانات المؤسسة وحمايتها.
    </div>

    <h3>1.1 سمات الـ DBA الناجح ومحاذير الشخصية (Anti-Patterns)</h3>
    <ul>
        <li><strong>رجل المهام المتعددة (Jack of all Trades):</strong> يجب أن يمتلك الـ DBA مزيجاً متفرداً من المهارات: فهم أنظمة التشغيل، العتاد المادي، شبكات الاتصال، معمارية المحركات، ضبط استعلامات SQL، والتواصل الإنساني الفعال.</li>
        <li><strong>شخصية العجوز المتذمر في الزاوية (The Curmudgeon in the Corner):</strong> نمط سلبي يُحذر منه المنهج بشدة؛ وهو الـ DBA المنعزل والمتعجرف الذي يرد تلقائياً بكلمة "لا" على أي طلب من المطورين، مما يحول إدارة قواعد البيانات إلى عقبة تعطل مسيرة العمل.</li>
        <li><strong>الـ DBA المتميز:</strong> شريك استراتيجي يتعاون مع فرق التطوير منذ مراحل التصميم الأولى، يتبنى أتمتة المراقبة، ويوثق إجراءات التعافي بدلاً من انتظار الكوارث.</li>
    </ul>

    <h3>1.2 الفرق الجوهري بين قاعدة البيانات ومحركها (Database vs. DBMS)</h3>
    <table>
        <tr>
            <th>المفهوم</th>
            <th>التعريف العلمي</th>
            <th>أمثلة وتطبيقات</th>
        </tr>
        <tr>
            <td><strong>قاعدة البيانات (Database)</strong></td>
            <td>مستودع منظم للبيانات المترابطة التي تعبر عن كيانات وعلاقات وقيود محددة في العالم الحقيقي.</td>
            <td>قاعدة بيانات العملاء، قاعدة الحسابات المالية، السجلات الطبية.</td>
        </tr>
        <tr>
            <td><strong>نظام إدارة قواعد البيانات (DBMS)</strong></td>
            <td>حزمة البرمجيات المعقدة المسؤولة عن إنشاء واسترجاع وتأمين والتحكم في الوصول إلى قواعد البيانات وضمان تزامنها.</td>
            <td>Oracle Database, IBM DB2, Microsoft SQL Server, PostgreSQL, MySQL.</td>
        </tr>
    </table>

    <h3>1.3 مقارنة الأدوار الإدارية الثلاثة</h3>
    <table>
        <tr>
            <th>الدور الإداري</th>
            <th>المسؤولية الجوهرية</th>
            <th>نطاق التركيز الأساسي</th>
        </tr>
        <tr>
            <td><strong>مسؤول البيانات (Data Administrator - DA / CDO)</strong></td>
            <td>حوكمة البيانات المؤسسية، وضع سياسات الميتاداتا، وتصميم النماذج المنطقية للأعمال.</td>
            <td>معنى البيانات (Semantics)، تصنيف البيانات، الملكية القانونية، وقاموس البيانات.</td>
        </tr>
        <tr>
            <td><strong>مسؤول النظام (System Administrator - SA)</strong></td>
            <td>إدارة عتاد الخوادم، نظام التشغيل، شبكات التوصيل، وترتيب مصفوفات الأقراص التخزينية (RAID).</td>
            <td>ترقية نظام التشغيل، استهلاك المعالج، والذاكرة العشوائية وسعة الخوادم.</td>
        </tr>
        <tr>
            <td><strong>مسؤول قواعد البيانات (DBA)</strong></td>
            <td>تثبيت نظام DBMS، بناء الهياكل المادية، ضبط الأداء والفهارس، وإدارة النسخ الاحتياطي والمعاملات.</td>
            <td>مساحات التخزين (Tablespaces)، الفهارس، الأقفال، التعافي من الكوارث، وتحسين SQL.</td>
        </tr>
    </table>

    <h3>1.4 التخصصات الفرعية لمسؤولي قواعد البيانات</h3>
    <ul>
        <li><strong>System DBA:</strong> يركز تقنياً على المحرك نفسه؛ تثبيت التحديثات الدورية (Patches)، ضبط ذاكرة التخزين المؤقت للمحرك، والترقية بين الإصدارات الرئيسية.</li>
        <li><strong>Application DBA:</strong> يندمج مع فريق تطوير تطبيق معين؛ يركز على كتابة وضبط استعلامات التطبيق، تصميم الجداول الملائمة للأعمال، وبناء الفهارس الداعمة للبرنامج.</li>
        <li><strong>Database Architect:</strong> يضع المخطط العام والمستقبلي لتدفق البيانات وتكامل الأنظمة وسياسات البنية التحتية للمؤسسة.</li>
        <li><strong>Data Modeler:</strong> يتولى رسم المخططات المنطقية والمفاهيمية (ERDs) وتحويل متطلبات العمل إلى كيانات وعلاقات معيارية.</li>
        <li><strong>Data Warehouse Administrator:</strong> يدير مستودعات البيانات الضخمة (OLAP) والمخططات النجمية (Star Schema) وتدفقات استخلاص وتحويل البيانات (ETL).</li>
        <li><strong>Procedural DBA:</strong> مسؤول عن إدارة ومراجعة الأكواد الإجرائية التي تنفذ مباشرة داخل محرك قاعدة البيانات (الإجراءات المخزنة، المحفزات Triggers، الدوال UDFs) لضمان عدم استنزافها لموارد الخادم.</li>
        <li><strong>Cloud DBA:</strong> يظهر في بيئات قواعد البيانات السحابية المدارة (DBaaS مثل AWS RDS و Cloud SQL)؛ حيث يتخلص من المهام المادية الروتينية ليركز على خفض تكاليف الاستهلاك السحابي، التوسع التلقائي، والأمان.</li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>2. التصميم المادي لقواعد البيانات والتخزين والفهارس (المحاضرتان 2 و 3)</h2>
    <p>يقوم التصميم المادي بتحويل النموذج المنطقي المجرد إلى هياكل تخزينية ملموسة داخل محرك قاعدة البيانات لتحقيق أعلى كفاءة استرجاع وتخزين.</p>

    <h3>2.1 التحويل من النموذج المنطقي إلى الفيزيائي (Mapping)</h3>
    <ul>
        <li><strong>الكيان (Entity)</strong> يتحول إلى <strong>جدول مادي (Table)</strong>.</li>
        <li><strong>الخاصية (Attribute)</strong> تتحول إلى <strong>عمود (Column)</strong> مع تحديد نوع البيانات الدقيق وقواعد NULL / DEFAULT.</li>
        <li><strong>المعرف الأساسي (Primary Identifier)</strong> يتحول إلى <strong>مفتاح أساسي (Primary Key)</strong> مدعوم بفهرس فريد.</li>
        <li><strong>العلاقة (Relationship)</strong> تتحول إلى <strong>مفتاح أجنبي (Foreign Key)</strong> يحافظ على التكامل المرجعي.</li>
    </ul>

    <div class="callout warning">
        <div class="callout-title">قواعد الترتيب المادي للأعمدة (ROTs)</div>
        يُنصح دائماً بوضع الأعمدة ذات الطول الثابت والأكثر استخداماً في بداية ترتيب السجل (لتمكين المعالج من الوصول إليها عبر إزاحة ثابتة)، ووضع الأعمدة متغيرة الطول (VARCHAR) والبيانات الثنائية الضخمة (LOBs) في نهاية السجل.
    </div>

    <h3>2.2 إدارة المساحات التخزينية ومساحات الفراغ (Free Space)</h3>
    <ul>
        <li><strong>حجم السجل (Row Length):</strong> مجموع أطوال الأعمدة مضافاً إليها ترويسة السجل (Header) ومؤشرات القيم الفارغة (Null Indicators).</li>
        <li><strong>سعة الصفحة (Page/Block):</strong> وحدة القراءة والكتابة الأساسية على القرص (غالباً 4KB أو 8KB).</li>
        <li><strong>معامل PCTFREE:</strong> نسبة مئوية تُترك فارغة عمداً في كل صفحة بيانات أثناء التحميل الأولي، للسماح للسجلات بالتمدد عند تحديثها مستقبلاً دون التسبب في هجرة الصفوف (Row Migration) وتشتتها.</li>
        <li><strong>معامل FREEPAGE:</strong> يحدد ترك صفحة فارغة بالكامل كل عدد محدد من الصفحات لإتاحة التجميع المادي للإدخالات الكبيرة الجديدة.</li>
    </ul>

    <h3>2.3 مقارنة متعمقة بين فهارس B-Tree وفهارس Bitmap</h3>
    <table>
        <tr>
            <th>وجه المقارنة</th>
            <th>فهارس الأشجار المتوازنة (B-Tree Index)</th>
            <th>فهارس البت الموجهة (Bitmap Index)</th>
        </tr>
        <tr>
            <td><strong>الهيكل البنائي</strong></td>
            <td>شجرة متوازنة متعددة المستويات: جذر (Root)، صفحات وسيطة، وصفحات أوراق مرتبة تحوي المفاتيح ومؤشرات السجلات (RowIDs).</td>
            <td>مصفوفة من البتات (0 و 1) لكل قيمة فريدة، حيث يمثل موقع كل بت رقم الصف المادي المقابل له.</td>
        </tr>
        <tr>
            <td><strong>الاستخدام المثالي</strong></td>
            <td>الأعمدة عالية التباين (High Cardinality) كالمفاتيح الأساسية والأرقام القومية وتواريخ المعاملات.</td>
            <td>الأعمدة منخفضة التباين (Low Cardinality) كالجنس، الحالة الاجتماعية، والمؤشرات المنطقية في مستودعات البيانات (OLAP).</td>
        </tr>
        <tr>
            <td><strong>نوع الاستعلامات</strong></td>
            <td>البحث الدقيق، استعلامات النطاقات (Range Queries)، والترتيب (ORDER BY).</td>
            <td>العمليات المنطقية السريعة بالبتات (AND, OR, NOT) التي يدمجها المعالج بكفاءة فائقة.</td>
        </tr>
        <tr>
            <td><strong>التزامن وأنظمة OLTP</strong></td>
            <td>ممتاز لأنظمة المعاملات الحية ويدعم أقفالاً دقيقة على مستوى الصفوف.</td>
            <td><strong>سيئ جداً لأنظمة OLTP:</strong> لأن تعديل صف واحد يقفل شريحة بيتية كاملة تمنع تعديل آلاف الصفوف المجاورة!</td>
        </tr>
    </table>

    <h3>2.4 الفهارس العنقودية وغير العنقودية (Clustered vs. Non-Clustered)</h3>
    <ul>
        <li><strong>الفهرس العنقودي (Clustered):</strong> يتطابق الترتيب المادي لصفوف الجدول على القرص مع الترتيب المنطقي لمفتاح الفهرس. ولأن البيانات المادية لا يمكن حفظها إلا بترتيب مادي واحد، فإن الجدول <strong>لا يمكن أن يحتوي إلا على فهرس عنقودي واحد فقط</strong>.</li>
        <li><strong>الفهرس غير العنقودي (Non-Clustered):</strong> هيكل منفصل يحفظ المفاتيح مرتبة وبجانبها مؤشرات تدل على موقع السجل الأصلي في صفحات البيانات.</li>
        <li><strong>الفهرس الشامل (Covering Index):</strong> عندما يحتوي الفهرس على كافة الأعمدة المطلوبة في جملتي SELECT و WHERE، يقرأ المحرك البيانات من الفهرس مباشرة دون لمس جدول البيانات الأصلي.</li>
    </ul>

    <h3>2.5 التفكيك المعياري (Denormalization) والبيانات الزمنية</h3>
    <ul>
        <li><strong>الـ Denormalization:</strong> إدخال التكرار والازدواجية عن عمد لدمج الجداول وتخفيف عمليات الربط المعقدة (JOINs) في الأنظمة كثيرة القراءة، مع تحمل تكلفة استهلاك التخزين ومخاطر اضطراب تناسق البيانات عند التعديل.</li>
        <li><strong>البيانات الزمنية (Temporal Data):</strong>
            <ul>
                <li><strong>زمن الأعمال (Business/Valid Time):</strong> الفترة الزمنية التي كان فيها البيان صحيحاً في الواقع الحقيقي (مثال: سريان وثيقة التأمين).</li>
                <li><strong>زمن النظام (System/Transaction Time):</strong> اللحظة الزمنية التي تم فيها تسجيل أو إبطال السجل داخل محرك قاعدة البيانات فعلياً.</li>
                <li><strong>الجداول ثنائية الزمن (Bi-temporal Tables):</strong> تدعم كلا البعدين معاً لتوثيق تاريخي قانوني كامل.</li>
            </ul>
        </li>
    </ul>
</div>

<div class="page-break"></div>

<div class="section">
    <h2>3. تطوير التطبيقات، المعاملات، والأقفال والتزامن (المحاضرتان 4 و 5)</h2>

    <h3>3.1 خصائص لغة SQL ومكونات التطوير</h3>
    <ul>
        <li><strong>لغة تصريحية (Declarative):</strong> يحدد المبرمج <em>ماذا يريد</em> (WHAT)، بينما يحدد المحسن الرياضي للمحرك (Cost-Based Optimizer) <em>كيف ينفذ الاستعلام</em> (HOW).</li>
        <li><strong>المعالجة كمجموعات (Set-at-a-Time):</strong> تعالج جملة SQL الواحدة مئات أو آلاف الصفوف دفعة واحدة كمجموعة رياضية.</li>
        <li><strong>المؤشرات (Cursors):</strong> أداة برمجية تتيح للغات الإجرائية (كالسي والجافا) المرور على نتائج الاستعلامات متسلسلة سطراً بسطر لاستيعاب المعالجة الفردية.</li>
        <li><strong>الفجوة البنائية (Object-Relational Impedance Mismatch):</strong> التناقض الجوهري بين العالم كائني التوجه (OOP) والعالم العلائقي القائم على الجداول الرياضية.</li>
    </ul>

    <h3>3.2 خصائص المعاملات الأربعة (ACID Properties)</h3>
    <table>
        <tr>
            <th>الحرف</th>
            <th>الخاصية بالإنجليزية</th>
            <th>المعنى والشرح الأكاديمي</th>
        </tr>
        <tr>
            <td><strong>A</strong></td>
            <td><strong>الذرية (Atomicity)</strong></td>
            <td>قاعدة "الكل أو لا شيء": إما أن تكتمل وتُعتمد كافة عمليات المعاملة بالكامل، أو تتراجع ويُلغى كل أثر لها في حال حدوث أي خطأ.</td>
        </tr>
        <tr>
            <td><strong>C</strong></td>
            <td><strong>التناسق (Consistency)</strong></td>
            <td>تنقل المعاملة قاعدة البيانات من حالة صحيحة مستوفية لكافة القيود المعيارية إلى حالة أخرى صحيحة ومعتمدة.</td>
        </tr>
        <tr>
            <td><strong>I</strong></td>
            <td><strong>العزل (Isolation)</strong></td>
            <td>عدم تداخل المعاملات المتزامنة؛ فلا ترى معاملة التعديلات المؤقتة لمعاملة أخرى حتى يتم اعتمادها نهائياً (Commit).</td>
        </tr>
        <tr>
            <td><strong>D</strong></td>
            <td><strong>الديمومة (Durability)</strong></td>
            <td>بمجرد اعتماد المعاملة، تصبح بياناتها ثابتة ومحفوظة على وسائط التخزين الدائمة وتصمد أمام انقطاع الكهرباء أو انهيار النظام.</td>
        </tr>
    </table>

    <h3>3.3 التحكم في التزامن: أنواع الأقفال والانسداد التام (Deadlocks)</h3>
    <ul>
        <li><strong>القفل المشترك (Shared / S Lock):</strong> يُستخدم للقراءة؛ يسمح لعدة مستخدمين بالقراءة المتزامنة للبيان نفسه.</li>
        <li><strong>القفل الحصري (Exclusive / X Lock):</strong> مطلوب للتعديل والحذف؛ يمنع أي جلسة أخرى من قراءة أو كتابة هذا البيان حتى تحريره.</li>
        <li><strong>قفل التحديث (Update / U Lock):</strong> قفل هجين يُستخدم في مرحلة القراءة الممهدة للتعديل لمنع ظاهرة تعليق الأقفال المتبادلة.</li>
        <li><strong>أقفال النوايا (Intent Locks: IS, IX):</strong> توضع على المستويات العليا كالجداول لتنبيه المحرك بوجود أقفال تفصيلية داخل الصفوف أدناه.</li>
        <li><strong>الانسداد التام (Deadlock):</strong> حالة انتظار حلقي مستحيل (معاملة 1 تنتظر قفل بيان لدى معاملة 2، بينما معاملة 2 تنتظر بيان لدى معاملة 1). يكتشف المحرك هذه الحلقة عبر مخطط الانتظار (Wait-For Graph) ويختار معاملة كضحية (Victim) ليتراجع عنها ويفك الاختناق.</li>
        <li><strong>تصعيد الأقفال (Lock Escalation):</strong> عندما تجمع المعاملة آلاف أقفال الصفوف، يقوم المحرك تلقائياً بدمجها في قفل جدول واحد لتوفير الذاكرة، مما يقلل معدل التزامن بصورة حادة.</li>
    </ul>

    <h3>3.4 مستويات العزل المعيارية (ANSI SQL Isolation Levels)</h3>
    <table>
        <tr>
            <th>مستوى العزل</th>
            <th>القراءة القذرة (Dirty Read)</th>
            <th>القراءة غير المتكررة (Non-Repeatable)</th>
            <th>القراءة الشبحية (Phantom Read)</th>
            <th>الحالة الافتراضية بالمحركات</th>
        </tr>
        <tr>
            <td><strong>Read Uncommitted</strong></td>
            <td>مسموحة (خطر)</td>
            <td>مسموحة</td>
            <td>مسموحة</td>
            <td>غير مستحسن</td>
        </tr>
        <tr>
            <td><strong>Read Committed</strong></td>
            <td><strong>ممنوعة ومحمية</strong></td>
            <td>مسموحة</td>
            <td>مسموحة</td>
            <td><strong>الافتراضي في أغلب المحركات</strong></td>
        </tr>
        <tr>
            <td><strong>Repeatable Read</strong></td>
            <td><strong>ممنوعة ومحمية</strong></td>
            <td><strong>ممنوعة ومحمية</strong></td>
            <td>مسموحة</td>
            <td>خاص ببعض السيناريوهات</td>
        </tr>
        <tr>
            <td><strong>Serializable</strong></td>
            <td><strong>ممنوعة ومحمية</strong></td>
            <td><strong>ممنوعة ومحمية</strong></td>
            <td><strong>ممنوعة ومحمية</strong></td>
            <td>الأعلى عزلاً والأبطأ أداءً</td>
        </tr>
    </table>

    <div class="callout tip">
        <div class="callout-title">وصايا ذهبية لمهندسي قواعد البيانات والبرمجة</div>
        <ul>
            <li>اجعل المعاملات قصيرة وسريعة قدر الإمكان؛ ولا تترك معاملة مفتوحة تنتظر تفاعل المستخدم نهائياً.</li>
            <li>الوصول إلى الجداول والصفوف <strong>بنفس الترتيب المتسلسل دائماً</strong> في كافة البرامج لمنع الانسداد التام نهائياً.</li>
            <li>استخدم الاستعلامات ذات المتغيرات المعلمة (Parameterized Queries) لمنع ثغرات حقن SQL وإعادة استخدام خطط التنفيذ.</li>
            <li>في العمليات المجمعة الكبرى (Batch Processing)، اعتمد التغييرات على أجزاء مجزأة لتجنب امتلاء سجل المعاملات وتصعيد الأقفال.</li>
        </ul>
    </div>
</div>

</body>
</html>"""

os.makedirs('summaries', exist_ok=True)
with open('summaries/DBA_Summary_EN.html', 'w', encoding='utf-8') as f:
    f.write(html_dba_en)
with open('summaries/DBA_Summary_AR.html', 'w', encoding='utf-8') as f:
    f.write(html_dba_ar)

print("Saved HTML summaries for DBA.")

# Compile to PDF using Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
cur_dir = os.path.abspath('.')

for lang, fn_html, fn_pdf in [
    ('EN', 'summaries/DBA_Summary_EN.html', 'summaries/DBA_Summary_EN.pdf'),
    ('AR', 'summaries/DBA_Summary_AR.html', 'summaries/DBA_Summary_AR.pdf')
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
