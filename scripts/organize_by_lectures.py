"""
Organizes all 1,000 questions (200 per subject across 5 subjects) into sequential lectures.
Adds explicit lecture metadata to every question:
- lecture_num: 1, 2, 3...
- lecture: "المحاضرة الأولى (Lecture 1)", etc.
- lecture_short: "المحاضرة 1 (Lec 1)", etc.
- lecture_title: Full bilingual lecture title
- subtopic: Clean subtopic title within the lecture
- topic: "المحاضرة 1 (Lec 1) • <subtopic>"
- lecture_q_num: 1-based index of the question inside its lecture
- lecture_q_total: Total questions in that lecture
Ensures questions are strictly ordered by (lecture_num, subtopic_order, original_index)
and re-indexes question IDs from 1 to 200.
"""

import json
import os
import subprocess
import sys

ARABIC_ORDINALS = {
    1: "المحاضرة الأولى (Lecture 1)",
    2: "المحاضرة الثانية (Lecture 2)",
    3: "المحاضرة الثالثة (Lecture 3)",
    4: "المحاضرة الرابعة (Lecture 4)",
    5: "المحاضرة الخامسة (Lecture 5)",
}

SHORT_LABELS = {
    1: "المحاضرة 1 (Lec 1)",
    2: "المحاضرة 2 (Lec 2)",
    3: "المحاضرة 3 (Lec 3)",
    4: "المحاضرة 4 (Lec 4)",
    5: "المحاضرة 5 (Lec 5)",
}


def strip_existing_prefix(topic_str):
    # If already prefixed with "المحاضرة ...", strip it to get clean subtopic
    if " • " in topic_str and topic_str.startswith("المحاضرة"):
        return topic_str.split(" • ", 1)[1].strip()
    return topic_str.strip()


def process_dba():
    path = "questions/dba_questions.json"
    qs = json.load(open(path, encoding="utf-8"))

    # Map subtopics to (lecture_num, subtopic_order, lecture_title)
    topic_map = {
        # Lecture 1 (Q1-Q65)
        "Introduction to DBA & Management Discipline": (
            1, 1, "المحاضرة الأولى (Lecture 1): Introduction to DBA & Management Discipline"
        ),
        "DA, SA, and DBA Roles & Responsibilities": (
            1, 2, "المحاضرة الأولى (Lecture 1): Introduction to DBA & Management Discipline"
        ),
        "DBA Types, Staffing, and Organizational Structure": (
            1, 3, "المحاضرة الأولى (Lecture 1): Introduction to DBA & Management Discipline"
        ),
        "Procedural DBA, Environments, and Cloud": (
            1, 4, "المحاضرة الأولى (Lecture 1): Introduction to DBA & Management Discipline"
        ),
        # Lecture 2 (Q66-Q108)
        "Physical Database Design & Rules of Thumb": (
            2, 1, "المحاضرة الثانية (Lecture 2): Physical Database Design, Storage & Indexing"
        ),
        "Column Ordering, Storage Planning & Free Space": (
            2, 2, "المحاضرة الثانية (Lecture 2): Physical Database Design, Storage & Indexing"
        ),
        "Index Architectures & Access Optimization": (
            2, 3, "المحاضرة الثانية (Lecture 2): Physical Database Design, Storage & Indexing"
        ),
        # Lecture 3 (Q109-Q135)
        "Partitioning, Hashing, Clustering, and Interleaving": (
            3, 1, "المحاضرة الثالثة (Lecture 3): Partitioning, Clustering & Denormalization"
        ),
        "Denormalization Strategies & Administration": (
            3, 2, "المحاضرة الثالثة (Lecture 3): Partitioning, Clustering & Denormalization"
        ),
        # Lecture 4 (Q136-Q167)
        "Database Application Development & SQL Paradigms": (
            4, 1, "المحاضرة الرابعة (Lecture 4): Application Development, SQL, Middleware & ORM"
        ),
        "SQL Middleware & APIs (ODBC, JDBC, SQLJ, OLE DB)": (
            4, 2, "المحاضرة الرابعة (Lecture 4): Application Development, SQL, Middleware & ORM"
        ),
        "Application Infrastructure (.NET and Java J2EE)": (
            4, 3, "المحاضرة الرابعة (Lecture 4): Application Development, SQL, Middleware & ORM"
        ),
        "Object-Relational Impedance Mismatch & ORM": (
            4, 4, "المحاضرة الرابعة (Lecture 4): Application Development, SQL, Middleware & ORM"
        ),
        "SQL Types, Coding for Performance, and XML": (
            4, 5, "المحاضرة الرابعة (Lecture 4): Application Development, SQL, Middleware & ORM"
        ),
        # Lecture 5 (Q168-Q200)
        "Transaction Management & ACID Properties": (
            5, 1, "المحاضرة الخامسة (Lecture 5): Transactions, ACID, Concurrency & Locking"
        ),
        "Concurrency Control & Database Locking": (
            5, 2, "المحاضرة الخامسة (Lecture 5): Transactions, ACID, Concurrency & Locking"
        ),
        "Lock Escalation, Deadlocks, and Batch Processing": (
            5, 3, "المحاضرة الخامسة (Lecture 5): Transactions, ACID, Concurrency & Locking"
        ),
    }

    decorated = []
    for idx, q in enumerate(qs):
        sub = strip_existing_prefix(q["topic"])
        if sub not in topic_map:
            raise ValueError(f"Unknown DBA topic: {sub}")
        lec_num, sub_ord, lec_title = topic_map[sub]
        decorated.append((lec_num, sub_ord, idx, q, sub, lec_title))

    decorated.sort(key=lambda x: (x[0], x[1], x[2]))
    return finalize_subject("dba", decorated, path)


def process_ecom():
    path = "questions/ecom_questions.json"
    qs = json.load(open(path, encoding="utf-8"))

    # Note: In original ecom_questions.json:
    # - Batch 1 (50 Qs): Lecture 1 (Intro, Classifications, Benefits & Limitations)
    # - Batch 2 (50 Qs): Lecture 2 / Ch 2 (Business Models, Revenue Models, B2C, B2B)
    # - Batch 4 (50 Qs): Lecture 3 / Lec 4 (Building an EC Site: SDLC, Hardware, Software, Scalability)
    # - Batch 3 (50 Qs): Lecture 4 / Ch 5 (Online Security, Threats, Encryption, Payment Systems)
    # Wait: If already reordered once, check q.get('lecture_num') first!
    decorated = []
    for idx, q in enumerate(qs):
        sub = strip_existing_prefix(q["topic"])
        qtext = q["question"]

        # Determine which of the 4 lectures this question belongs to based on content/batch
        if "lecture_num" in q:
            lec_num = q["lecture_num"]
        else:
            # Original ordering: 0..49 = Lec 1, 50..99 = Lec 2, 100..149 = Lec 4 (Security), 150..199 = Lec 3 (Building EC Site)
            if idx < 50:
                lec_num = 1
            elif idx < 100:
                lec_num = 2
            elif idx < 150:
                lec_num = 4
            else:
                lec_num = 3

        # Fix the 5 subtopic labels that were generic in batch2/batch4:
        if lec_num == 2 and sub == "EC Definitions & Framework":
            sub = "Emerging EC Models & Enablers"
        if lec_num == 3 and sub == "Security Dimensions & Policy":
            sub = "Website Privacy & Accessibility Policies"

        lec_titles = {
            1: "المحاضرة الأولى (Lecture 1): Introduction to E-Commerce, Classifications & Benefits",
            2: "المحاضرة الثانية (Lecture 2 - Ch 2): E-Commerce Business Models & Revenue Concepts",
            3: "المحاضرة الثالثة (Lecture 3 - Ch 4): Building an E-Commerce Site, SDLC & Architecture",
            4: "المحاضرة الرابعة (Lecture 4 - Ch 5): Online Security, Encryption & Payment Systems",
        }

        sub_orders = {
            # Lec 1
            "EC Definitions & Framework": 1,
            "EC Classifications & Dimensions": 2,
            "Benefits & Limitations of EC": 3,
            # Lec 2
            "Revenue Models & 8 Key Elements": 1,
            "B2C Models": 2,
            "B2B Models": 3,
            "Emerging EC Models & Enablers": 4,
            # Lec 3
            "Building an EC Site: SDLC": 1,
            "Hardware, Software & Scalability": 2,
            "Website Privacy & Accessibility Policies": 3,
            # Lec 4
            "Security Dimensions & Policy": 1,
            "Security Threats": 2,
            "Encryption & Security Solutions": 3,
            "Payment Systems": 4,
        }

        sub_ord = sub_orders.get(sub, 9)
        decorated.append((lec_num, sub_ord, idx, q, sub, lec_titles[lec_num]))

    decorated.sort(key=lambda x: (x[0], x[1], x[2]))
    return finalize_subject("ecom", decorated, path)


def process_ir():
    path = "questions/ir_questions.json"
    qs = json.load(open(path, encoding="utf-8"))

    topic_map = {
        # Lecture 1 (Ch 1 - 46 Qs)
        "IR Fundamentals & Retrieval Models": (
            1, 1, "المحاضرة الأولى (Lecture 1 - Ch 1): IR Fundamentals, Incidence Matrix & Inverted Index"
        ),
        "Term-Document Incidence Matrix": (
            1, 2, "المحاضرة الأولى (Lecture 1 - Ch 1): IR Fundamentals, Incidence Matrix & Inverted Index"
        ),
        "Inverted Index Architecture & Construction": (
            1, 3, "المحاضرة الأولى (Lecture 1 - Ch 1): IR Fundamentals, Incidence Matrix & Inverted Index"
        ),
        # Lecture 2 (Lec 2 - 65 Qs)
        "Postings Merge & Boolean Query Processing": (
            2, 1, "المحاضرة الثانية (Lecture 2): Boolean Query Processing, Optimization & Phrase Queries"
        ),
        "Query Optimization": (
            2, 2, "المحاضرة الثانية (Lecture 2): Boolean Query Processing, Optimization & Phrase Queries"
        ),
        "Biword Indexes & Extended Biwords": (
            2, 3, "المحاضرة الثانية (Lecture 2): Boolean Query Processing, Optimization & Phrase Queries"
        ),
        "Positional Indexes & Proximity Queries": (
            2, 4, "المحاضرة الثانية (Lecture 2): Boolean Query Processing, Optimization & Phrase Queries"
        ),
        # Lecture 3 (Lec 3 - 18 Qs)
        "Skip Pointers & Faster Postings Merges": (
            3, 1, "المحاضرة الثالثة (Lecture 3): Skip Pointers & Faster Postings Merges"
        ),
        # Lecture 4 (Lec 5 PDF - 71 Qs)
        "Document Parsing & Character Encodings": (
            4, 1, "المحاضرة الرابعة (Lecture 4 - Lec 5): Document Parsing, Tokenization, Normalization & Stemming"
        ),
        "Tokenization Challenges & Multi-language Processing": (
            4, 2, "المحاضرة الرابعة (Lecture 4 - Lec 5): Document Parsing, Tokenization, Normalization & Stemming"
        ),
        "Stop Words & Vocabulary Management": (
            4, 3, "المحاضرة الرابعة (Lecture 4 - Lec 5): Document Parsing, Tokenization, Normalization & Stemming"
        ),
        "Normalization, Equivalence Classes & Soundex": (
            4, 4, "المحاضرة الرابعة (Lecture 4 - Lec 5): Document Parsing, Tokenization, Normalization & Stemming"
        ),
        "Stemming & Lemmatization": (
            4, 5, "المحاضرة الرابعة (Lecture 4 - Lec 5): Document Parsing, Tokenization, Normalization & Stemming"
        ),
    }

    decorated = []
    for idx, q in enumerate(qs):
        sub = strip_existing_prefix(q["topic"])
        if sub not in topic_map:
            raise ValueError(f"Unknown IR topic: {sub}")
        lec_num, sub_ord, lec_title = topic_map[sub]
        decorated.append((lec_num, sub_ord, idx, q, sub, lec_title))

    decorated.sort(key=lambda x: (x[0], x[1], x[2]))
    return finalize_subject("ir", decorated, path)


def process_ba():
    path = "questions/business_questions.json"
    qs = json.load(open(path, encoding="utf-8"))

    topic_map = {
        # Lecture 1 (Module 1 - 66 Qs)
        "Data Definition & Value Chain": (
            1, 1, "المحاضرة الأولى (Lecture 1 - Module 1): Introduction to Data Analytics & Analytical Types"
        ),
        "Data Analysis vs Data Analytics": (
            1, 2, "المحاضرة الأولى (Lecture 1 - Module 1): Introduction to Data Analytics & Analytical Types"
        ),
        "The Four Types of Analytics": (
            1, 3, "المحاضرة الأولى (Lecture 1 - Module 1): Introduction to Data Analytics & Analytical Types"
        ),
        "Translating Questions & Analytics Roles": (
            1, 4, "المحاضرة الأولى (Lecture 1 - Module 1): Introduction to Data Analytics & Analytical Types"
        ),
        # Lecture 2 (Chapter 2 - 67 Qs)
        "Model Definition & Forms": (
            2, 1, "المحاضرة الثانية (Lecture 2 - Ch 2): Decision Models, Break-Even & Optimization"
        ),
        "Decision Model Architecture": (
            2, 2, "المحاضرة الثانية (Lecture 2 - Ch 2): Decision Models, Break-Even & Optimization"
        ),
        "Descriptive Models & Break-Even": (
            2, 3, "المحاضرة الثانية (Lecture 2 - Ch 2): Decision Models, Break-Even & Optimization"
        ),
        "Demand Prediction Models": (
            2, 4, "المحاضرة الثانية (Lecture 2 - Ch 2): Decision Models, Break-Even & Optimization"
        ),
        "Prescriptive Models & Optimization": (
            2, 5, "المحاضرة الثانية (Lecture 2 - Ch 2): Decision Models, Break-Even & Optimization"
        ),
        # Lecture 3 (Chapter 3 - 67 Qs)
        "Lifecycle Overview & Need": (
            3, 1, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Phase 1: Discovery": (
            3, 2, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Phase 2: Data Preparation": (
            3, 3, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Phase 3: Model Planning": (
            3, 4, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Phase 4: Model Building": (
            3, 5, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Phase 5: Communicate Results": (
            3, 6, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Phase 6: Operationalize": (
            3, 7, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "Analytics Project Roles": (
            3, 8, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
        "The 4 Core Deliverables": (
            3, 9, "المحاضرة الثالثة (Lecture 3 - Ch 3): Data Analytics Lifecycle, Roles & Deliverables"
        ),
    }

    decorated = []
    for idx, q in enumerate(qs):
        sub = strip_existing_prefix(q["topic"])
        if sub not in topic_map:
            raise ValueError(f"Unknown BA topic: {sub}")
        lec_num, sub_ord, lec_title = topic_map[sub]
        decorated.append((lec_num, sub_ord, idx, q, sub, lec_title))

    decorated.sort(key=lambda x: (x[0], x[1], x[2]))
    return finalize_subject("ba", decorated, path)


def process_isapp():
    path = "questions/isapp_questions.json"
    qs = json.load(open(path, encoding="utf-8"))

    topic_map = {
        # Lecture 1 (Chapter 1 - 100 Qs)
        "IS Definition & Purpose": (
            1, 1, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "Data vs. Information": (
            1, 2, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "5 Components of an IS": (
            1, 3, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "IS Operations & Cycle": (
            1, 4, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "CS vs. IT vs. IS": (
            1, 5, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "Major Types of IS": (
            1, 6, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "IS Applications & Emerging Tech": (
            1, 7, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        "University IS Case Study": (
            1, 8, "المحاضرة الأولى (Lecture 1 - Ch 1): Introduction to Information Systems & Core Components"
        ),
        # Lecture 2 (Chapter 2 - 100 Qs)
        "Organizations & 5 Resources": (
            2, 1, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Organizational Functional Areas": (
            2, 2, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Management Levels & Info Needs": (
            2, 3, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Decision Types & Alignment": (
            2, 4, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Enterprise Systems Hierarchy": (
            2, 5, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Business Processes: Taxonomy": (
            2, 6, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Cross-Functional Systems & ERP": (
            2, 7, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
        "Competitive Advantage & Case Study": (
            2, 8, "المحاضرة الثانية (Lecture 2 - Ch 2): Information Systems in Organizations, ERP & Strategy"
        ),
    }

    decorated = []
    for idx, q in enumerate(qs):
        sub = strip_existing_prefix(q["topic"])
        if sub not in topic_map:
            raise ValueError(f"Unknown ISApp topic: {sub}")
        lec_num, sub_ord, lec_title = topic_map[sub]
        decorated.append((lec_num, sub_ord, idx, q, sub, lec_title))

    decorated.sort(key=lambda x: (x[0], x[1], x[2]))
    return finalize_subject("isapp", decorated, path)


def finalize_subject(prefix, decorated, out_path):
    # Count questions per lecture
    lec_counts = {}
    for lec_num, _, _, _, _, _ in decorated:
        lec_counts[lec_num] = lec_counts.get(lec_num, 0) + 1

    lec_Counters = {}
    output = []
    for i, (lec_num, sub_ord, orig_idx, q, sub, lec_title) in enumerate(decorated):
        lec_Counters[lec_num] = lec_Counters.get(lec_num, 0) + 1
        q_in_lec = lec_Counters[lec_num]
        total_in_lec = lec_counts[lec_num]

        lec_label = ARABIC_ORDINALS[lec_num]
        lec_short = SHORT_LABELS[lec_num]

        new_q = {
            "id": f"{prefix}_{i+1}",
            "subject": q["subject"],
            "lecture_num": lec_num,
            "lecture": lec_label,
            "lecture_short": lec_short,
            "lecture_title": lec_title,
            "lecture_q_num": q_in_lec,
            "lecture_q_total": total_in_lec,
            "subtopic": sub,
            "topic": f"{lec_short} • {sub}",
            "question": q["question"],
            "options": q["options"],
            "answer": q["answer"],
            "explanation": q["explanation"],
        }
        output.append(new_q)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"=== {prefix.upper()} ({out_path}) ===")
    for ln in sorted(lec_counts.keys()):
        first_q = next(idx + 1 for idx, item in enumerate(output) if item["lecture_num"] == ln)
        last_q = max(idx + 1 for idx, item in enumerate(output) if item["lecture_num"] == ln)
        title = next(item["lecture_title"] for item in output if item["lecture_num"] == ln)
        print(f"  Q{first_q:3d}-Q{last_q:3d} ({lec_counts[ln]:3d} Qs) | {title}")
    return out_path


if __name__ == "__main__":
    paths = [
        process_dba(),
        process_ecom(),
        process_ir(),
        process_ba(),
        process_isapp(),
    ]
    print("\nRunning validator on all 5 question files...")
    res = subprocess.run([sys.executable, "scripts/validate_questions.py"] + paths)
    sys.exit(res.returncode)
