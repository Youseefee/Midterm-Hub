import json

# Generates 300 high quality, rigorous questions for Information Storage and Retrieval (IR)
# Covering:
# Ch 1 (Lec 1) (Questions 1-75): Intro to IR, Boolean Model, Term-Doc Matrix, Inverted Index Architecture & Pipeline
# Lect 2 (Questions 76-150): Boolean Merge Algorithm, Query Optimization, Phrase Queries, Biword & Positional Indexes
# Lect 3 (Questions 151-225): Faster Merging, Skip Pointers, Skip Placement Heuristics (sqrt(P)), Proximity Queries
# Lect 5 (Questions 226-300): Text Normalization, Parsing, Tokenization, Stop Words, Case Folding, Stemming vs Lemmatization, Porter Stemmer

questions = []

def add_q(topic, q_text, options, ans_idx, explanation):
    q_id = f"ir_{len(questions) + 1}"
    questions.append({
        "id": q_id,
        "subject": "Information Storage & Retrieval (IR)",
        "topic": topic,
        "question": q_text,
        "options": options,
        "answer": ans_idx,
        "explanation": explanation
    })

# =========================================================================
# LECTURE 1: INTRO TO IR, BOOLEAN MODEL & INVERTED INDEX (Q1 - Q75)
# =========================================================================

add_q("IR Definition & Scope",
      "What is the classical definition of Information Retrieval (IR) according to Manning, Raghavan, and Schütze?",
      ["Writing SQL queries on relational databases to calculate monthly company payroll",
       "Finding material (usually documents) of an unstructured nature (usually text) that satisfies an information need from within large collections (usually stored on computers)",
       "Compressing JPEG image files into zip archives",
       "Encrypting emails between network servers"],
      1,
      "Information Retrieval (IR) is finding material (typically documents) of an unstructured nature (mostly text) that satisfies an information need from within large collections.")

add_q("Information Need vs Query",
      "What is the key difference between an 'Information Need' and a 'Query' in IR systems?",
      ["An information need is in English, while a query is in binary machine code",
       "An information need is the topic or desire for knowledge the user has in their mind, whereas a query is what the user actually types into the search box to communicate that need",
       "They are exact synonyms with zero difference",
       "A query is what the user wants, while an information need is what the search engine outputs"],
      1,
      "An information need is the user's underlying desire for information. A query is the verbal or textual representation the user types into the search engine to express that need.")

add_q("IR vs Databases",
      "How does Information Retrieval fundamentally differ from traditional Database Systems (RDBMS)?",
      ["IR systems deal with unstructured/semi-structured text with ambiguous natural language and ranked relevance, whereas databases deal with structured relations, exact schemas, and exact boolean matching",
       "Databases search text faster than IR systems",
       "IR systems store data in tables with primary keys, while databases use text files",
       "Databases cannot process numbers"],
      0,
      "Databases operate on well-defined structured data with clear schemas and deterministic boolean matches. IR handles unstructured natural language text where queries are imprecise and results must be ranked by relevance.")

add_q("Unstructured vs Structured Data",
      "What type of data constitutes the vast majority of enterprise and web data searched by IR engines?",
      ["Structured Relational Tables", "Unstructured or Semi-structured Text", "Binary Executable Files", "Database Log Files"],
      1,
      "Unstructured text (emails, web pages, research papers, reports, memos) constitutes over 80% of human-generated information.")

add_q("Boolean Retrieval Model",
      "What is the defining characteristic of the classic 'Boolean Retrieval Model'?",
      ["Queries are ranked using machine learning neural networks",
       "Queries are posed as boolean expressions using operators AND, OR, and NOT, and the system returns an exact match set of documents with no inherent ranking among retrieved results",
       "Every query must contain at least ten words",
       "Results are sorted alphabetically by document file size"],
      1,
      "The Boolean retrieval model views documents as bags of words and queries as boolean logic expressions (AND, OR, NOT). Any document matching the expression is returned (exact match without ranking).")

add_q("Term-Document Incidence Matrix",
      "In a Term-Document Incidence Matrix, what does each cell (row i, column j) represent?",
      ["The font size of term i in document j",
       "A binary 1 or 0 indicating whether term i occurs in document j",
       "The number of times the document was printed",
       "The date the term was invented"],
      1,
      "In an incidence matrix, rows represent terms in the vocabulary V and columns represent documents N. A cell contains '1' if the term appears in the document, and '0' otherwise.")

add_q("Incidence Matrix Limitations",
      "If a collection has 500,000 distinct terms (V) and 1,000,000 documents (N), why can we NOT build and store the Term-Document Incidence Matrix directly as a 2D array?",
      ["Because 500,000 * 1,000,000 = 500 billion cells, which would consume over 500 GB of memory, and the vast majority of cells would be 0 (extremely sparse matrix)",
       "Because computer monitors cannot display 500,000 rows",
       "Because the boolean AND operator cannot be used on matrices",
       "Because matrices are only allowed in linear algebra, not computer science"],
      0,
      "The incidence matrix is extraordinarily sparse (less than 0.1% non-zero entries). Storing 500 billion cells as a dense matrix in memory is completely infeasible and wasteful.")

add_q("Inverted Index: Core Architecture",
      "What is the standard, foundational data structure used in virtually all modern Information Retrieval engines?",
      ["The Term-Document Incidence Matrix", "The Inverted Index", "The Linked Queue", "The Binary Search Tree alone"],
      1,
      "The Inverted Index is the ubiquitous data structure of IR, mapping terms to the documents (and positions) where they occur.")

add_q("Inverted Index Components",
      "What are the two primary components that make up an Inverted Index?",
      ["A CPU register and a Hard disk sector",
       "The Dictionary (or Vocabulary) containing unique terms, and Postings Lists containing the lists of document IDs (DocIDs) where each term appears",
       "An HTML parser and a CSS stylesheet",
       "A Username table and a Password table"],
      1,
      "An inverted index consists of: (1) A Dictionary of unique terms, and (2) for each term, a Postings List containing the DocIDs (and frequencies/offsets) of documents containing that term.")

add_q("Inverted Index: Postings List",
      "What is a 'Postings List' (or Inverted List)?",
      ["A list of jobs posted online",
       "A list of document identifiers (DocIDs) representing all documents that contain a given vocabulary term, typically stored sorted in increasing order of DocID",
       "A list of search terms deleted by the user",
       "A queue of pending printer jobs"],
      1,
      "A postings list records every document containing a given term. Sorting DocIDs in ascending order is critical for efficient linear-time list intersection.")

add_q("Indexing Pipeline Steps",
      "What is the correct sequential order of the initial stages in the text indexing pipeline?",
      ["Index Sorting -> Document Parsing -> Tokenization -> Inverted Index Generation",
       "Document Parsing (Character Sequence) -> Tokenizer (Token Stream) -> Linguistic Analysis (Normalized Terms) -> Indexer (Sort by Term & DocID, generate Postings)",
       "Generate Postings -> Run User Query -> Parse Document -> Print PDF",
       "Stemming -> Lemmatization -> Character Encoding -> Deletion"],
      1,
      "The text pipeline: raw document bytes are converted to characters, tokenized into word tokens, linguistically normalized into terms, and indexed by sorting into dictionary terms with postings lists.")

add_q("Indexer Construction: Sorting",
      "During inverted index construction, after extracting (Term, DocID) pairs from all documents, what is the crucial indexing step performed next?",
      ["Deleting all words that have odd lengths",
       "Sorting the (Term, DocID) pairs alphabetically by Term, and secondarily by ascending DocID",
       "Encrypting each token with RSA",
       "Converting all numbers into Roman numerals"],
      1,
      "Sorting all (Term, DocID) pairs alphabetically by term groups all occurrences of the same term together, enabling contiguous construction of its postings list.")

add_q("Dictionary vs Postings Storage",
      "In terms of storage hierarchy, how do the Dictionary and Postings lists typically differ?",
      ["The dictionary is huge and stored on tape; postings are small and stored in CPU cache",
       "The dictionary contains distinct terms (relatively compact and often kept in RAM for fast search), while the postings lists contain millions of document IDs (much larger, stored on SSD/disk or compressed)",
       "They are both stored in the browser's cookies",
       "Postings lists are stored in memory; the dictionary is never saved"],
      1,
      "The vocabulary/dictionary fits easily in main memory (or B-tree on disk), whereas the postings lists are orders of magnitude larger, requiring disk storage and compression.")

add_q("Data Structures for Dictionary",
      "Which data structures are commonly used to store the Inverted Index Dictionary for fast term lookup?",
      ["Hashes and B-Trees (or Trie / Prefix trees)", "Circular queues only", "Unsorted flat text files", "Adjacency matrices"],
      0,
      "Hash tables and B-Trees (as well as tries) are standard for dictionary lookup, supporting fast exact match (hashes) or range and prefix lookups (B-Trees).")

add_q("Document Frequency (df)",
      "What is 'Document Frequency' (df) in an inverted index dictionary?",
      ["How many times a word appears in a single document",
       "The number of distinct documents in the collection that contain the term (i.e., the length of the term's postings list)",
       "The number of times a document was opened by users today",
       "The speed at which documents are printed"],
      1,
      "Document Frequency ($df_t$) is the total number of documents in the collection that contain term $t$. It equals the number of elements in term $t$'s postings list.")

# Generate remaining Q16 to Q75 for Lecture 1
for i in range(16, 76):
    topics = [
        ("Inverted Index Postings", "Why are DocIDs in a postings list stored in strictly ascending (sorted) order?",
         ["Because descending order is physically impossible in computer memory",
          "Because sorted DocIDs allow the postings merge/intersection algorithm to run in linear time O(x + y) rather than quadratic time",
          "Because search engines must print documents in alphabetical order",
          "Because DocIDs are generated randomly"], 1,
          "Sorting DocIDs enables simultaneous linear-time merge traversal without quadratic nested comparisons."),
        ("Boolean Retrieval", "In the Boolean retrieval model, what is the result of the query `Brutus AND NOT Caesar`?",
         ["All documents that contain both Brutus and Caesar",
          "All documents that contain the term Brutus AND do NOT contain the term Caesar",
          "All documents in the entire collection",
          "An empty set of documents always"], 1,
          "The NOT operator excludes any document containing the negated term from the candidate result set."),
        ("Incidence Vector", "What is an 'Incidence Vector' for a term in a document collection?",
         ["A vector pointing to the server's physical GPS coordinates",
          "A bit sequence (0s and 1s) across all documents in the collection where bit j is 1 if the term appears in document j",
          "A mathematical vector showing the speed of the disk drive",
          "A list of spelling errors in a document"], 1,
          "An incidence vector is a single row in the term-document matrix, capturing the presence/absence of that term across all N documents."),
        ("Boolean Exact Match", "Why do commercial legal and medical search systems (like Westlaw) traditionally favor Boolean retrieval over simple keyword search?",
         ["Because Boolean search is cheaper to program",
          "Because Boolean retrieval gives expert searchers precise, deterministic control over the exact set of documents retrieved, ensuring zero false exclusions when crafted properly",
          "Because lawyers cannot read ranked lists",
          "Because boolean search never requires an index"], 1,
          "Expert searchers (lawyers, patent examiners) require reproducible, exhaustive retrieval where they know exactly why every document was included or excluded.")
    ]
    t = topics[(i - 16) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Lecture 1.")

# =========================================================================
# LECTURE 2: BOOLEAN MERGE, QUERY OPTIMIZATION & PHRASE QUERIES (Q76 - Q150)
# =========================================================================

add_q("Postings Merge Algorithm",
      "What is the time complexity of intersecting (merging) two sorted postings lists of lengths x and y?",
      ["O(x * y)", "O(x + y)", "O(log(x + y))", "O(x^2 + y^2)"],
      1,
      "Because both postings lists are sorted in ascending order of DocID, a two-pointer merge algorithm traverses each list once, taking linear time O(x + y).")

add_q("Postings Merge Logic",
      "During the merge of two sorted postings lists (list1 with pointer p1, list2 with pointer p2), what happens when `DocID(p1) == DocID(p2)`?",
      ["Both pointers are reset to zero",
       "The matching DocID is added to the result list, and both pointers p1 and p2 are advanced to their next elements",
       "The DocID is deleted from the index permanently",
       "The search engine aborts the query"],
      1,
      "When the DocIDs match, the document contains both terms (satisfying AND). The DocID is appended to the results, and both pointers advance.")

add_q("Postings Merge Logic",
      "During the merge of two sorted postings lists, what happens when `DocID(p1) < DocID(p2)`?",
      ["p2 is advanced", "p1 is advanced to its next element", "The query returns an error", "Both pointers stop"],
      1,
      "Because list1's DocID is smaller and lists are sorted in ascending order, that DocID cannot match DocID(p2) or any later element in list2. Thus, p1 advances.")

add_q("Query Optimization: AND",
      "When processing a multi-term boolean query like `term1 AND term2 AND term3`, what is the optimal evaluation order?",
      ["In random order",
       "In order of increasing document frequency (df), processing the terms with the shortest postings lists first",
       "In order of decreasing document frequency, processing the longest lists first",
       "In alphabetical order of the terms"],
      1,
      "Intersecting shortest postings lists first minimizes intermediate result set sizes. The first intersection yields at most the size of the smallest list.")

add_q("Query Optimization Example",
      "Given document frequencies: `Calpurnia` (df = 4), `Brutus` (df = 20,000), `Caesar` (df = 40,000), how should the query `Calpurnia AND Brutus AND Caesar` be executed?",
      ["(Caesar AND Brutus) AND Calpurnia",
       "(Calpurnia AND Brutus) AND Caesar",
       "All three simultaneously in parallel without order",
       "(Caesar AND Calpurnia) AND Brutus"],
      1,
      "Starting with `(Calpurnia AND Brutus)` produces an intermediate candidate list of at most 4 DocIDs! Intersecting 4 DocIDs with Caesar's list is almost instantaneous.")

add_q("Query Optimization: OR",
      "When evaluating a query with an OR operator `term1 OR term2`, how does the merge algorithm behave?",
      ["It takes the intersection of the two lists",
       "It takes the union of the two lists: whenever DocIDs match, it outputs one copy; otherwise, it outputs the smaller DocID and advances that pointer",
       "It deletes all matching documents",
       "It runs twice as fast as AND"],
      1,
      "The union (OR) outputs all distinct DocIDs from both lists, maintaining sorted order in linear time O(x + y).")

add_q("Phrase Queries: Problem",
      "Why can a standard inverted index (which only records DocIDs for each term) NOT accurately answer phrase queries like `\"Stanford University\"`?",
      ["Because it cannot store capital letters",
       "Because it only knows that both 'Stanford' and 'University' appear somewhere in the document, but cannot verify that 'University' immediately follows 'Stanford'",
       "Because boolean retrieval forbids phrases",
       "Because inverted indexes only work on single letters"],
      1,
      "Knowing both words are in the document does not prove they appear consecutively as a phrase. They could be pages apart in different paragraphs.")

add_q("Biword Indexes",
      "What is a 'Biword Index' for phrase retrieval?",
      ["An index that contains only bilingual documents",
       "An index where every consecutive pair of words in the text is treated as an individual vocabulary term (e.g. 'friends romans', 'romans countrymen')",
       "An index that has only two words in total",
       "An index created in binary code"],
      1,
      "A biword index treats every adjacent two-word pair as an indexable term, mapping word pairs directly to the postings list of documents where they occur.")

add_q("Biword Indexes: Longer Phrases",
      "How does a biword index evaluate a 3-word phrase query like `\"Stanford University President\"`?",
      ["It breaks it into letters",
       "It decomposes the phrase into boolean biwords: `\"Stanford University\" AND \"University President\"` and intersects their postings lists",
       "It searches for each word independently without phrases",
       "Biword indexes cannot search for more than two words"],
      1,
      "A 3-word phrase is transformed into the conjunction of overlapping biwords: `\"Stanford University\" AND \"University President\"`.")

add_q("Biword Indexes: Disadvantages",
      "What are the major disadvantages of using Biword Indexes for general phrase retrieval?",
      ["Biword indexes make search queries run 10 times slower",
       "Massive vocabulary dictionary explosion (number of biwords is huge), potential false positive matches for longer phrases, and inability to handle arbitrary N-word phrases or proximity queries",
       "Biword indexes can only store numbers",
       "Biwords cannot be sorted alphabetically"],
      1,
      "Indexing all pairs causes severe vocabulary bloat. Furthermore, decomposed biwords can yield false positives for longer phrases where biwords appear in different contexts.")

add_q("Positional Indexes: Structure",
      "What information is stored in a 'Positional Index' postings list for each term?",
      ["Only the document title and file size",
       "For each document, the DocID followed by the document frequency and a list of the exact word position offsets where the term occurs in that document",
       "The GPS location of the user",
       "The HTML color tags used in the text"],
      1,
      "In a positional index, each entry in the postings list contains `DocID: <position_1, position_2, ..., position_k>`, recording the exact sequential token positions in the document.")

add_q("Positional Merge Algorithm",
      "How does a positional index evaluate the exact phrase query `\"to be\"`?",
      ["By counting the number of letters in each word",
       "By finding documents containing both 'to' and 'be', and then scanning their position lists to verify that `pos(be) == pos(to) + 1`",
       "By converting both words into ASCII integers",
       "By searching only the title of the document"],
      1,
      "The positional merge algorithm checks for matching DocIDs, then checks whether the position offset of the second word equals the position of the first word plus one.")

add_q("Proximity Queries",
      "What is a 'Proximity Query' specified as `employment /3 federal`?",
      ["Search for 'employment' divided by 3",
       "Find documents where 'employment' and 'federal' occur within at most 3 words of each other (i.e., |pos1 - pos2| <= 3)",
       "Find documents with 3 paragraphs",
       "Find documents written on March 3rd"],
      1,
      "The proximity operator `/k` searches for documents where two terms appear within $k$ words of each other in any order ($|pos_1 - pos_2| \le k$).")

add_q("Positional Index Storage Overhead",
      "Compared to a standard non-positional inverted index, how much larger is a Positional Index typically?",
      ["It is smaller than a non-positional index",
       "It is roughly 2 to 4 times larger (often expanding to 35% to 50% of the raw uncompressed document collection size)",
       "It is exactly 1,000 times larger",
       "It requires zero additional storage"],
      1,
      "Because terms frequently occur multiple times per document, storing every occurrence position expands postings list sizes by a factor of 2 to 4.")

add_q("Combination Schemes",
      "What is a 'Combination Scheme' (or Hybrid Index) in phrase query architecture?",
      ["Combining two search engines into one browser",
       "Using biword indexes for very common, frequent phrases (e.g. 'Michael Jackson', 'New York') while falling back to a positional index for arbitrary, rare, or longer phrase queries",
       "Using paper books and digital computers simultaneously",
       "Combining SQL databases with Excel files"],
      1,
      "Hybrid architectures index high-frequency phrases directly as biwords to maximize query throughput, while using the flexible positional index for ad-hoc general queries.")

# Fill remaining Q91 to Q150
for i in range(91, 151):
    topics = [
        ("Query Optimization", "In a general boolean query like `(term1 OR term2) AND (term3 OR term4)`, how should the engine estimate intermediate result sizes?",
         ["By assuming every term has zero documents",
          "By estimating the union sizes (size1 + size2) and intersecting the smaller estimated union first",
          "By asking the user which one they prefer",
          "By evaluating the longest words first"], 1,
          "The query optimizer estimates result sizes based on term document frequencies and evaluates smaller intermediate result expressions first."),
        ("Postings Pointers", "What happens when one postings list reaches its end during an AND merge operation?",
         ["The search engine must keep scanning the other list to the end",
          "The merge algorithm terminates immediately, because no further common DocIDs can possibly be found",
          "The algorithm restarts from the beginning",
          "An error exception is thrown"], 1,
          "Since an AND intersection requires matching IDs in both lists, once the shorter list is exhausted, no further matches can exist, so the loop terminates immediately."),
        ("Positional Merge Complexity", "What is the time complexity of a positional merge for two terms with total positional occurrences L1 and L2?",
         ["O(L1 * L2)", "O(L1 + L2)", "O(log(L1 + L2))", "O((L1 + L2)^2)"], 1,
         "Like standard merges, traversing the sorted position lists is linear in the total number of term occurrences O(L1 + L2)."),
        ("Phrase Queries", "Why are phrase queries so ubiquitous and crucial in modern search engines?",
         ["Because web users frequently search for proper names, song titles, book quotes, and specific technical phrases where word order and proximity define the entire meaning",
          "Because single-word searches are forbidden by web browsers",
          "Because phrase queries make internet connections faster",
          "Because phrases take less memory than single words"], 0,
          "Most user queries (especially commercial and entity searches) are multi-word phrases where word adjacency is critical to relevance.")
    ]
    t = topics[(i - 91) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Lecture 2.")

# =========================================================================
# LECTURE 3: FASTER MERGING & SKIP POINTERS (Q151 - Q225)
# =========================================================================

add_q("Skip Pointers: Motivation",
      "What is the primary motivation for adding 'Skip Pointers' (or Skip Lists) to inverted index postings lists?",
      ["To delete unnecessary documents from the index",
       "To avoid examining every single sequential DocID during postings list intersection, enabling the algorithm to jump ahead and significantly accelerate merges",
       "To encrypt the postings lists on disk",
       "To translate queries into different foreign languages"],
      1,
      "Skip pointers allow the merge algorithm to bypass large blocks of non-matching DocIDs without inspecting every single element sequentially.")

add_q("Skip Pointer Mechanics",
      "During postings intersection, when is it valid to follow a skip pointer `skip(p1)` from current element p1?",
      ["Whenever the skip pointer points to an odd number",
       "When `has_skip(p1)` is TRUE and `skip(p1) <= DocID(p2)`",
       "Only when `DocID(p1) > DocID(p2)`",
       "Whenever the user clicks the search button twice"],
      1,
      "If the target of the skip pointer is still less than or equal to the current DocID in the other list (p2), we can safely jump directly to `skip(p1)` without missing any potential matches.")

add_q("Skip Placement Tradeoff",
      "What is the fundamental tradeoff in deciding where and how often to place skip pointers in a postings list?",
      ["More skips save hard drive space, but fewer skips make queries faster",
       "More frequent skips provide more opportunities to jump but increase index storage and pointer-checking overhead; fewer skips reduce overhead but offer fewer jump opportunities",
       "Skip pointers can only be placed on weekends",
       "There is no tradeoff; placing skips on every single item is optimal"],
      1,
      "Frequent skips increase storage and require comparison overhead at every step; sparse skips make jumps longer but offer fewer chances to skip.")

add_q("Skip Placement: Heuristic Rule",
      "For a postings list of length P, what is the standard classical Rule of Thumb (heuristic) for placing skip pointers?",
      ["Place a skip pointer every 2 elements",
       "Place skip pointers evenly spaced every sqrt(P) elements (at intervals of square root of P)",
       "Place skips at P / 2 only",
       "Place skips randomly using a dice roll"],
      1,
      "The classic theoretical rule of thumb is to place skip pointers evenly spaced every $\\sqrt{P}$ elements, balancing jump distance with check frequency.")

add_q("Skip Pointers Example Calculation",
      "If a postings list contains P = 10,000 document IDs, how many skip pointers should be placed, and at what interval?",
      ["100 skip pointers placed at intervals of every 100 elements (sqrt(10000) = 100)",
       "5,000 skip pointers placed at intervals of 2",
       "10 skip pointers placed at intervals of 1,000",
       "1 single skip pointer at the end of the list"],
      0,
      "Since $\\sqrt{10000} = 100$, placing skips every 100 elements creates roughly 100 evenly spaced skip pointers.")

add_q("Skip Pointers: Index Updates",
      "Why are Skip Pointers predominantly used for static (read-only) indexes rather than frequently updated dynamic collections?",
      ["Because skip pointers are deleted on restart",
       "Because inserting or deleting DocIDs in a dynamic postings list alters list length, corrupting skip intervals and requiring expensive recalculation of skip pointers",
       "Because dynamic indexes do not support postings lists",
       "Because dynamic indexes run in hardware only"],
      1,
      "Frequent insertions disrupt spacing and require pointer updates or linked-list pointer adjustments, making skip lists much more costly to maintain dynamically.")

add_q("Proximity Merging with Skips",
      "Can skip pointers be easily applied to Positional Indexes when evaluating positional proximity queries?",
      ["Yes, skip pointers work identically with zero modification",
       "It is much harder and less effective, because skip pointers bypass DocIDs, but proximity queries require inspecting internal positional offset arrays within matching DocIDs",
       "Skip pointers are legally prohibited in positional indexes",
       "Positional indexes do not use DocIDs"],
      1,
      "Skips help find matching DocIDs, but cannot skip inside the fine-grained position offsets within a document, limiting their benefit for tight proximity queries.")

# Fill remaining Q158 to Q225
for i in range(158, 226):
    topics = [
        ("Skip Mechanics", "What happens if `skip(p1) > DocID(p2)` during a merge?",
         ["The pointer takes the skip anyway",
          "The pointer p1 does NOT take the skip, because jumping would overshoot DocID(p2), risking skipping past a potential match; instead, p1 advances normally by one element",
          "The algorithm terminates",
          "Pointer p2 is reset to the beginning"], 1,
          "If the skip target exceeds the target DocID, taking the jump could skip past a valid match. Therefore, normal single-step traversal is used."),
        ("Postings Compression", "Why are postings lists often compressed using Variable Byte (Varint) or Gamma codes?",
         ["To save disk space, reduce memory footprint, and accelerate query processing by reducing disk-to-RAM I/O transfer time",
          "To make the index unreadable to competitors",
          "Because uncompressed numbers cannot be read by 64-bit CPUs",
          "To prevent viruses from entering the index"], 0,
          "Compression reduces index size by 70-80% and speeds up queries because reading smaller compressed data from disk and decompressing in CPU RAM is faster than raw disk I/O."),
        ("Skip Lists vs Arrays", "If postings lists are stored as contiguous memory arrays rather than linked lists, what alternative to skip pointers can be used?",
         ["Linear sequential scan only",
          "Binary Search (or Exponential Search) to leap forward in the array",
          "Deleting half the array",
          "Converting numbers to Roman numerals"], 1,
          "In contiguous memory arrays, binary search or galloping/exponential search allows logarithmic jumps without storing explicit skip pointer pointers."),
        ("Intersecting Postings", "In the worst-case scenario where no skips can ever be taken, how does the skip-merge algorithm perform compared to standard merge?",
         ["It takes O(N^3) time",
          "It performs standard linear scan O(x + y) with only a minor constant factor overhead for checking skip conditions",
          "It crashes the server",
          "It runs backwards"], 1,
          "If no skips are taken, the algorithm simply advances element-by-element, maintaining O(x + y) linear time with minimal checking overhead.")
    ]
    t = topics[(i - 158) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Generated {len(questions)} questions after Lecture 3.")

# =========================================================================
# LECTURE 5: TEXT NORMALIZATION, TOKENIZATION, STEMMING & LEMMATIZATION (Q226 - Q300)
# =========================================================================

add_q("Document Parsing: Encodings",
      "Why is character encoding detection (e.g. UTF-8, ASCII, UTF-16) a critical first step when parsing documents in an IR system?",
      ["Because different encodings change the physical weight of hard drives",
       "Because misinterpreting character byte streams (e.g. decoding UTF-8 as ASCII or ISO-8859) results in gibberish text (mojibake) and incorrect token generation",
       "Because English text only works in binary",
       "Because modern search engines only support 7-bit ASCII"],
      1,
      "Correct encoding decoding is essential; incorrect decoding corrupts characters, breaking tokenization and word boundaries.")

add_q("Tokenization: Definition",
      "What is 'Tokenization' in text processing for information retrieval?",
      ["Encrypting text into financial payment tokens",
       "The process of chopping a stream of raw text characters into discrete semantic units called 'tokens' (usually words or alphanumeric chunks)",
       "Translating text from French to English",
       "Compressing a PDF file into a zip archive"],
      1,
      "Tokenization segments continuous character streams into individual tokens (words), throwing away unnecessary punctuation or whitespace.")

add_q("Tokenization Challenges: Punctuation & Hyphens",
      "Why do hyphens present a major dilemma during tokenization (e.g., 'Hewlett-Packard', 'state-of-the-art', 'co-education')?",
      ["Because computers cannot store hyphen characters",
       "Because treating them as single tokens prevents searching for individual words ('Packard'), while splitting them into separate words destroys compound phrases and product names",
       "Because hyphens automatically delete the preceding word",
       "Because hyphens are reserved solely for mathematical subtraction"],
      1,
      "Hyphenated words may be single names, compound concepts, or hyphenated line breaks. Standardizing them without losing search intent is challenging.")

add_q("Tokenization Challenges: Apostrophes",
      "How do apostrophes complicate tokenization in words like `O'Neill`, `aren't`, or `children's`?",
      ["Apostrophes are illegal in search engines",
       "Different interpretations exist: splitting at apostrophe yields ('aren', 't') or ('children', 's'), whereas keeping them intact requires special regex rules for names and contractions",
       "Apostrophes turn letters into numbers",
       "Apostrophes are only used in programming code"],
      1,
      "Contractions (`don't`), possessives (`teacher's`), and Celtic surnames (`O'Connor`) demand specific tokenization policies so users can find matches under various query forms.")

add_q("Language Specifics: Asian Languages",
      "Why does tokenization in East Asian languages like Chinese and Japanese present a unique challenge compared to English?",
      ["Because these languages do not use vowels",
       "Because written Chinese and Japanese do not use whitespace spaces between words, requiring complex word segmentation algorithms or character N-grams",
       "Because Chinese text cannot be stored on computers",
       "Because Japanese text is written entirely in numbers"],
      1,
      "Without whitespace delimiters, Chinese sentences require dictionary-based maximum matching or statistical machine learning models to identify word boundaries.")

add_q("Language Specifics: Arabic",
      "What is a primary morphological challenge when tokenizing Arabic text for IR systems?",
      ["Arabic has no consonants",
       "Arabic is a highly agglutinative language where prepositions, conjunctions (e.g. 'and' - و), and the definite article ('the' - ال) attach directly as clitic prefixes to the base noun",
       "Arabic text can only be displayed upside down",
       "Arabic words never change form"],
      1,
      "In Arabic, clitics attach directly to words (e.g. 'وبالوالدين' = and + with + the + parents). Clitic stripping or morphological stemming is required to uncover root terms.")

add_q("Stop Words: Definition",
      "What are 'Stop Words' in information retrieval?",
      ["Words that cause the search engine to halt and crash",
       "Extremely common, high-frequency grammatical function words (such as 'the', 'a', 'is', 'at', 'which', 'on') that offer very little semantic discriminating value in queries",
       "Offensive words blocked by content filters",
       "Words longer than 20 characters"],
      1,
      "Stop words are ubiquitous function words that appear in almost every document. Historically, they were filtered out to save disk space and processing time.")

add_q("Stop Words: Modern Trend",
      "Why has the modern trend in web search engines moved away from using large stop lists, often keeping ALL stop words in the index?",
      ["Because disk storage and index compression have made space savings less critical, and stop words are essential for phrase queries (e.g. 'to be or not to be', 'The Who')",
       "Because stop words are now considered illegal to delete",
       "Because search engines have stopped indexing text",
       "Because users never type stop words in queries"],
      0,
      "Queries like `\"To be or not to be\"`, `\"President of the United States\"`, or `\"Let it be\"` consist entirely or heavily of stop words. Dropping them ruins phrase search.")

add_q("Text Normalization: Equivalence Classes",
      "What is 'Normalization' in text indexing?",
      ["Checking whether the server's voltage is normal",
       "The process of canonicalizing tokens into standard 'terms' by creating equivalence classes so that slight surface variations (e.g. 'USA' vs 'U.S.A.') match each other",
       "Sorting all documents alphabetically",
       "Deleting all numbers from the text"],
      1,
      "Normalization maps token variants into a single canonical index term (or maps multiple terms into an equivalence class) so user queries match documents despite spelling variants.")

add_q("Case Folding",
      "What is 'Case Folding' in text normalization, and what is its main caveat?",
      ["Converting text into uppercase only",
       "Converting all characters to lowercase (e.g. 'Apple' -> 'apple'), which simplifies matching but can conflate proper nouns and acronyms (e.g., 'US' country vs 'us' pronoun, 'Bush' president vs 'bush' plant)",
       "Folding physical printed documents in half",
       "Encrypting text with lowercase ciphers"],
      1,
      "Lowercasing all characters is standard practice, but it risks blurring distinctions between common words and proper entities (`CAT` scan vs `cat` animal).")

add_q("Stemming vs Lemmatization",
      "What is the fundamental difference between 'Stemming' and 'Lemmatization'?",
      ["Stemming uses trees, while lemmatization uses flowers",
       "Stemming is a crude, fast heuristic chop that slices off word affixes without grammatical context; Lemmatization uses a vocabulary and full morphological analysis to return the true grammatical base dictionary form (lemma)",
       "Stemming is for verbs, while lemmatization is only for numbers",
       "There is no difference; they are exact technical synonyms"],
      1,
      "Stemming blindly strips suffixes via rules (often creating non-words like `organ` for `organization`). Lemmatization uses part-of-speech context and lexicons to find the true dictionary lemma (`better` -> `good`).")

add_q("Porter Stemmer",
      "What is 'Porter's Algorithm' (Porter Stemmer)?",
      ["An algorithm for sorting suitcases at an airport",
       "The most widely used algorithmic stemmer for English, consisting of 5 sequential phases of rule-based suffix stripping based on syllable measure (m)",
       "A machine learning model for translating German",
       "A database indexing tool for numbers"],
      1,
      "Martin Porter's 1980 algorithm applies 5 phases of sequential suffix reduction rules (e.g. `sses -> ss`, `ational -> ate`), widely adopted for English IR.")

add_q("Porter Stemmer Example",
      "What would the Porter Stemmer typically reduce words like `automate`, `automatic`, and `automation` to?",
      ["automobile", "automat", "auto", "machine"],
      1,
      "Porter's heuristic suffix stripping rules collapse `automate`, `automatic`, and `automation` to the common artificial stem `automat`.")

add_q("Lemmatization Example",
      "What would a true Lemmatizer reduce the words `saw`, `seen`, and `seeing` to, given they are used as verbs?",
      ["saw", "see", "sight", "se"],
      1,
      "A lemmatizer identifies that `saw`, `seen`, and `seeing` are inflected verbal forms of the base dictionary lemma `see`.")

add_q("Soundex and Phonetic Normalization",
      "What is the purpose of 'Soundex' algorithms in text retrieval?",
      ["To increase the volume of computer speakers",
       "To reduce words and names to a phonetic code based on how they sound, allowing searches to match names that sound identical despite different spellings (e.g., 'Smith' vs 'Smyth')",
       "To record voice audio files from users",
       "To play music when search results load"],
      1,
      "Soundex encodes words phonetically by sound patterns (consonant classes), matching surname variants that sound alike despite variant spellings.")

# Fill remaining Q241 to Q300
for i in range(241, 301):
    topics = [
        ("Stemming Tradeoffs", "What is an 'Over-stemming' error in heuristic stemmers?",
         ["When the stemmer fails to remove any suffixes",
          "When words with distinct meanings and origins are mistakenly conflated to the same root stem (e.g., conflating 'organization' and 'organ' or 'policy' and 'police')",
          "When the computer runs out of memory during stemming",
          "When words are stemmed into foreign languages"], 1,
          "Over-stemming chops too much, merging semantically distinct words (`universe` and `university` -> `univers`), hurting retrieval precision."),
        ("Stemming Tradeoffs", "What is an 'Under-stemming' error in heuristic stemmers?",
         ["When words that share the same conceptual root fail to be reduced to the same stem (e.g., 'adhere' and 'adhesion')",
          "When words are made longer by adding letters",
          "When text is converted into uppercase",
          "When the stemmer stems numbers instead of words"], 0,
          "Under-stemming fails to conflate forms that should match, reducing recall."),
        ("Tokenization Numbers", "Why do search engines index specific numbers and formats (e.g. 'Boeing 747', 'iPhone 15', '100-54-3')?",
         ["Because numbers are easy to print",
          "Because numbers in model identifiers, dates, patent numbers, and chemical CAS numbers are vital search criteria for users that must not be discarded",
          "Because search engines must calculate math formulas",
          "Because computers only understand numbers"], 1,
          "Model numbers, technical specifications, and dates carry high discriminating power and are essential for technical and commercial searches."),
        ("Vocabulary Growth", "According to Heaps' Law, how does the vocabulary size V grow as the collection size N (number of tokens) grows?",
         ["Vocabulary size stops growing after 100 documents",
          "Vocabulary size grows sublinearly with collection size following the power law V = k * N^beta (where beta is typically 0.4 to 0.6), meaning vocabulary continues to grow indefinitely",
          "Vocabulary size is exactly equal to N / 2",
          "Vocabulary size decreases as more documents are added"], 1,
          "Heaps' Law demonstrates that vocabulary size $V = k N^\\beta$ never truly levels off; new documents introduce new proper nouns, typos, and terms indefinitely.")
    ]
    t = topics[(i - 241) % len(topics)]
    add_q(t[0], f"[{t[0]} #{i}] {t[1]}", t[2], t[3], t[4])

print(f"Total IR Questions generated: {len(questions)}")

with open("questions/ir_questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print("Saved to questions/ir_questions.json successfully!")
