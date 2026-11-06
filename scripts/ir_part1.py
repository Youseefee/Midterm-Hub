# Part 1: Questions 1 to 62
# Topics:
# 1. IR Fundamentals & Retrieval Models (Q1 to Q15)
# 2. Term-Document Incidence Matrix (Q16 to Q30)
# 3. Inverted Index Architecture & Construction (Q31 to Q46)
# 4. Postings Merge & Boolean Query Processing (Q47 to Q62)

part1_questions = [
    # -------------------------------------------------------------
    # Topic 1: IR Fundamentals & Retrieval Models (Q1 - Q15)
    # -------------------------------------------------------------
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "In information retrieval theory, how is a user's underlying 'information need' formally differentiated from a 'query'?",
        "correct": "The information need is the desire for knowledge in the user's mind, whereas the query is the explicit text typed into the engine.",
        "distractors": [
            "The information need is written in natural language, whereas the query must strictly adhere to formal Boolean relational algebra.",
            "The information need represents the list of retrieved documents, whereas the query represents the list of filtered index terms.",
            "The information need is formulated automatically by the crawler, whereas the query is an internal document vector representation."
        ],
        "explanation": "An information need is the user's topic of interest or desire for knowledge. A query is the concrete textual string or representation submitted by the user to the IR system."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "Why does the classical introductory model of Information Retrieval assume a static document collection?",
        "correct": "It simplifies index construction and postings merge analysis by decoupling retrieval logic from dynamic document updates.",
        "distractors": [
            "Real-world enterprise and web collections never experience document additions, deletions, or edits after system deployment.",
            "Inverted index data structures are mathematically incapable of inserting new documents once dictionary memory is set.",
            "Assuming a static collection completely eliminates the algorithmic need for postings intersection and query optimization."
        ],
        "explanation": "Assuming a static collection allows introductory analysis of basic indexing and query processing algorithms without the complexities of real-time dynamic index updates."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "Which of the following best explains why linear scanning tools like Unix grep fail as primary retrieval mechanisms for large corpora?",
        "correct": "Linear scanning scales with O(N) time complexity across text size and lacks efficient support for ranked results and proximity queries.",
        "distractors": [
            "Linear scanning requires allocating an enormous static incidence matrix in main memory before any pattern match can execute.",
            "Grep operates exclusively on 7-bit ASCII files and cannot read modern document formats even with external preprocessing filters.",
            "String matching algorithms cannot handle basic conjunction queries containing more than two simultaneous search terms."
        ],
        "explanation": "Linear scanning (grep) is O(N) in text size, which is far too slow for large collections. It also lacks index structures needed for ranked retrieval, complex Boolean operations, and proximity searches."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "A search engine retrieves 40 documents for a user query. Human evaluators judge that 24 of these retrieved documents are relevant. If the total corpus contains 80 relevant documents, what are the system's precision and recall?",
        "correct": "Precision is 60.0% (24/40) and recall is 30.0% (24/80).",
        "distractors": [
            "Precision is 30.0% (24/80) and recall is 60.0% (24/40).",
            "Precision is 50.0% (40/80) and recall is 30.0% (24/80).",
            "Precision is 60.0% (24/40) and recall is 50.0% (40/80)."
        ],
        "explanation": "Precision = relevant retrieved / total retrieved = 24 / 40 = 60%. Recall = relevant retrieved / total relevant in corpus = 24 / 80 = 30%."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "How is recall defined in IR system evaluation, and what typically happens when an IR system is adjusted to maximize recall?",
        "correct": "Recall is the fraction of all relevant documents that are retrieved; maximizing it usually retrieves more documents and lowers precision.",
        "distractors": [
            "Recall is the fraction of retrieved documents that are relevant; maximizing it restricts search results to only top-scoring documents.",
            "Recall measures the speed of postings list intersection; maximizing it increases dictionary memory overhead while maintaining precision.",
            "Recall is the proportion of distinct terms matched in a query; maximizing it eliminates the need for linguistic preprocessing steps."
        ],
        "explanation": "Recall measures the fraction of relevant documents retrieved. System adjustments that broaden retrieval to capture more relevant documents usually retrieve more non-relevant documents, lowering precision."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "When comparing unstructured free text to structured relational database records, which search capability is uniquely characteristic of unstructured IR?",
        "correct": "Evaluating conceptual similarity and returning ranked relevance lists for ambiguous natural language queries.",
        "distractors": [
            "Executing deterministic range queries over numeric fields with strict mathematical boundary validation.",
            "Enforcing foreign key integrity constraints across relational tables using predefined relational database schemas.",
            "Guaranteeing ACID transactional consistency during simultaneous document modifications across distributed nodes."
        ],
        "explanation": "Unstructured IR searches free text with vague or ambiguous information needs, returning ranked results based on relevance, unlike relational databases which execute exact boolean/range queries against rigid schemas."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "How does an IR system handle 'semi-structured' data compared to purely unstructured free text?",
        "correct": "It leverages distinct metadata fields or document zones such as Title, Author, and Abstract to restrict or weight term matches.",
        "distractors": [
            "It converts all textual content into strict third normal form relational database tables before generating index terms.",
            "It disregards document markup and zone boundaries entirely, treating all text fields as an undifferentiated stream of characters.",
            "It replaces the inverted index with a relational B-tree index to guarantee exact field-level schema compliance during lookup."
        ],
        "explanation": "Semi-structured data contains both free text and identified structural zones (e.g. Title, Author, Date). IR systems facilitate semi-structured search by restricting or weighting matches within specific zones."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "In the context of evaluating information retrieval systems, how does 'query evaluation' differ from 'system evaluation'?",
        "correct": "Query evaluation measures how well documents correspond to a query, while system evaluation assesses overall search effectiveness.",
        "distractors": [
            "Query evaluation determines the disk space occupied by postings, while system evaluation measures the speed of lexical tokenization.",
            "Query evaluation measures precision and recall metrics, while system evaluation verifies grammatical correctness of search terms.",
            "Query evaluation checks character encoding standards, while system evaluation executes Boolean logic across distributed query nodes."
        ],
        "explanation": "Query evaluation asks 'to what extent does a document correspond to a query?', while system evaluation asks 'how good is the system overall?' (e.g. precision, recall, and user satisfaction)."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "What significant trend in corporate and web data storage between 1996 and today influenced the prominence of Information Retrieval?",
        "correct": "The volume of unstructured and semi-structured text grew exponentially, far outstripping the growth of structured database tables.",
        "distractors": [
            "Relational databases completely replaced inverted indexes due to rapid advancements in SQL full-text search extensions.",
            "Web engines shifted entirely from inverted indexes back to linear scans due to modern multi-core processor processing power.",
            "Enterprise text collections standardized on fixed-size schemas, making traditional IR techniques obsolete in modern software."
        ],
        "explanation": "As illustrated in Lecture 1 slides, the proportion and sheer volume of unstructured free text grew tremendously from 1996 to 2009 and today, making IR techniques central to computing."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "Why do traditional relational database management systems struggle with 'concept queries' such as finding documents dealing with 'drug abuse'?",
        "correct": "Relational databases match exact keywords or explicit SQL conditions and lack built-in mechanisms to assess semantic relatedness.",
        "distractors": [
            "Relational databases cannot store variable-length character text strings longer than standard 255-character database column limits.",
            "Relational database transaction managers automatically reject queries that contain Boolean disjunction operators across text attributes.",
            "Relational tables require pre-sorting of all stored words alphabetically before any query can be parsed by the database engine."
        ],
        "explanation": "Relational databases are designed for exact match and numerical range queries on structured attributes. They lack statistical and semantic models to match broad concepts expressed in free text."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "In IR system evaluation, what does the concept of 'effectiveness' fundamentally encompass?",
        "correct": "The quality of the search results, primarily evaluated through the statistical metrics of precision and recall.",
        "distractors": [
            "The raw query processing throughput measured strictly in queries evaluated per second across clustered servers.",
            "The compression ratio achieved when transforming raw text documents into binary term-document incidence vectors.",
            "The rate at which the web crawler discovers and downloads newly published web documents across the internet."
        ],
        "explanation": "Effectiveness in IR assesses the quality of the search results, answering whether the retrieved documents satisfy the user's information need, captured by precision and recall."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "Which of the following is NOT a characteristic of the classical Boolean retrieval model?",
        "correct": "It automatically assigns ranked relevance scores to retrieved documents based on term frequency within each document.",
        "distractors": [
            "It views each document simply as a set of words without taking into account internal document narrative structure.",
            "It requires query expressions to be formulated using explicit Boolean operators such as AND, OR, and NOT.",
            "It produces binary match results where each document either strictly satisfies the Boolean query or does not."
        ],
        "explanation": "Classical Boolean retrieval is an exact match model: documents either match the Boolean expression or do not. It does not provide graded ranking scores based on term frequencies."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "In retrieval terminology, what does a 'false positive' (or false drop) represent during query execution?",
        "correct": "A document returned by the retrieval system that does not actually satisfy the user's information need.",
        "distractors": [
            "A relevant document in the collection that the search engine failed to retrieve during index traversal.",
            "A query term that fails to match any existing dictionary entry within the system inverted index.",
            "An error caused by corrupted character encodings when parsing raw binary document streams into tokens."
        ],
        "explanation": "A false positive (or false drop) is a non-relevant document retrieved by the system that fails to satisfy the user's information need."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "An enterprise collection triples its document count while retaining the same subject domain. How do precision and recall typically behave if the query mechanism remains unadjusted?",
        "correct": "Precision often declines as more non-relevant documents match query terms, while finding all relevant documents becomes harder.",
        "distractors": [
            "Precision and recall both automatically increase proportionally to the cube root of the new total document count.",
            "Precision remains completely unaffected because precision is mathematically independent of the total collection volume.",
            "Recall automatically reaches 100% because larger document collections guarantee higher term overlap with user queries."
        ],
        "explanation": "As collections grow, the pool of potential distractors increases, making it harder to maintain high precision without more specific queries, while retrieving all relevant items becomes more difficult."
    },
    {
        "topic": "IR Fundamentals & Retrieval Models",
        "question": "Which of the following search scenarios is an example of semi-structured retrieval rather than purely unstructured search?",
        "correct": "Finding conference papers where the string 'deep learning' appears in the Abstract and 'Hinton' is an Author.",
        "distractors": [
            "Finding any web page across the entire public internet that mentions the term 'deep learning' in body text.",
            "Running a linear grep scan across a set of raw text files for the literal string 'Geoffrey Hinton'.",
            "Scanning an unindexed plain text novel to locate all occurrences of the character name 'Oliver Twist'."
        ],
        "explanation": "Searching within identified document zones or metadata fields (like Abstract and Author) while evaluating text content is the definition of semi-structured retrieval."
    },

    # -------------------------------------------------------------
    # Topic 2: Term-Document Incidence Matrix (Q16 - Q30)
    # -------------------------------------------------------------
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "In a term-document incidence matrix representing a collection of N documents with a vocabulary of M distinct terms, what do the rows and columns represent?",
        "correct": "Rows represent distinct vocabulary terms, and columns represent documents in the collection.",
        "distractors": [
            "Rows represent documents in the collection, and columns represent positional offsets of words.",
            "Rows represent Boolean query operators, and columns represent postings lists for terms.",
            "Rows represent document frequencies, and columns represent character token sequences."
        ],
        "explanation": "In a term-document incidence matrix, each row corresponds to a unique term in the vocabulary, and each column corresponds to a document in the collection."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "Given the incidence vectors for two terms in a 6-document collection, TermA = 110100 and TermB = 110111, which documents satisfy the query 'TermA AND TermB'?",
        "correct": "Documents 1, 2, and 4 (resulting bit vector 110100).",
        "distractors": [
            "Documents 1, 2, 4, 5, and 6 (resulting bit vector 110111).",
            "Documents 3, 5, and 6 (resulting bit vector 001011).",
            "Documents 1 and 2 only (resulting bit vector 110000)."
        ],
        "explanation": "Bitwise AND of 110100 and 110111 gives 110100, which corresponds to Document 1, Document 2, and Document 4."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "For a collection of 6 documents, if TermA has the incidence vector 101010 and TermB has the incidence vector 011011, what is the result of the query 'TermA AND NOT TermB'?",
        "correct": "Document 1 only (resulting bit vector 100000).",
        "distractors": [
            "Documents 1, 3, and 5 (resulting bit vector 101010).",
            "Documents 2 and 6 only (resulting bit vector 010001).",
            "Documents 3 and 5 only (resulting bit vector 001010)."
        ],
        "explanation": "NOT TermB = NOT(011011) = 100100. Then TermA AND NOT TermB = 101010 AND 100100 = 100000 (only Document 1)."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "In the classic Shakespeare example from the textbook, if Brutus = 110100, Caesar = 110111, and Calpurnia = 010000, what is the resulting vector for 'Brutus AND Caesar AND NOT Calpurnia'?",
        "correct": "100100 (matching documents 1 and 4).",
        "distractors": [
            "110100 (matching documents 1, 2, and 4).",
            "010100 (matching documents 2 and 4).",
            "100111 (matching documents 1, 4, 5, and 6)."
        ],
        "explanation": "Brutus AND Caesar = 110100. NOT Calpurnia = 101111. 110100 AND 101111 = 100100 (documents 1 and 4)."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "Suppose a corpus contains N = 1,000,000 documents and M = 500,000 distinct terms. How many total entries (0s and 1s) would the full term-document incidence matrix contain?",
        "correct": "500,000,000,000 entries (half a trillion cells).",
        "distractors": [
            "500,000,000 entries (five hundred million cells).",
            "50,000,000,000 entries (fifty billion cells).",
            "5,000,000,000 entries (five billion cells)."
        ],
        "explanation": "Matrix size = M * N = 500,000 * 1,000,000 = 500,000,000,000 (0.5 trillion cells)."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "In a corpus of 1,000,000 documents where each document contains an average of 1,000 words and the vocabulary has 500,000 terms, what is the maximum percentage of matrix cells that can contain a 1?",
        "correct": "At most 0.2% of cells contain a 1, meaning at least 99.8% of the matrix consists of zeroes.",
        "distractors": [
            "At most 2.0% of cells contain a 1, meaning at least 98.0% of the matrix consists of zeroes.",
            "At most 0.02% of cells contain a 1, meaning at least 99.98% of the matrix consists of zeroes.",
            "Exactly 5.0% of cells contain a 1, meaning exactly 95.0% of the matrix consists of zeroes."
        ],
        "explanation": "Max total 1s = 1,000,000 docs * 1,000 terms = 1 billion 1s. Out of 500 billion cells, 1B / 500B = 0.002 = 0.2% maximum 1s (>= 99.8% zeroes)."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "If 1,000,000 documents average 1,000 words each at 6 bytes per word (including spaces), the raw text takes 6 GB. Why is storing the 500K x 1M incidence matrix in memory impractical compared to the raw text?",
        "correct": "A 500K x 1M bit matrix requires ~62.5 GB of memory to store mostly redundant zeroes, dwarfing the raw text size.",
        "distractors": [
            "A 500K x 1M bit matrix requires 500 terabytes of memory, exceeding the capacity of any distributed computing cluster.",
            "Bitwise Boolean operations on incidence vectors require O(N^2) CPU cycles per document during query processing.",
            "Matrix columns cannot be read sequentially into processor registers because text characters require 32-bit words."
        ],
        "explanation": "500 billion bits = 500 * 10^9 / 8 bytes ≈ 62.5 GB. Storing 62.5 GB of mostly zeroes in memory when the raw text is only 6 GB is grossly inefficient."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "What fundamental observation about the term-document incidence matrix led directly to the adoption of the inverted index?",
        "correct": "Because the incidence matrix is extremely sparse, it is far more efficient to record only the positions where 1s occur.",
        "distractors": [
            "Because incidence vectors cannot be processed with bitwise AND operations, an alternative algebraic model was required.",
            "Because vocabulary size decreases as more documents are added, making inverted list structures smaller than vectors.",
            "Because incidence matrices cannot support Boolean negation, requiring specialized postings pointers for exclusion."
        ],
        "explanation": "With over 99.8% of the incidence matrix consisting of zeroes, recording only the 1 positions (documents where terms actually occur) yields the inverted index."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "While bitwise operations on incidence vectors are fast on CPU hardware, what is their primary operational disadvantage for large-scale retrieval?",
        "correct": "They require scanning and loading entire vectors of length N even when a term appears in only two or three documents.",
        "distractors": [
            "Bitwise registers cannot execute logical NOT operations without completely clearing existing memory buffers.",
            "Bitwise operations produce non-deterministic result sets when handling queries containing more than three terms.",
            "They cannot distinguish between documents of different lengths when storing binary term incidence values."
        ],
        "explanation": "Incidence vectors have fixed length N. Even if a term appears in only one document, an entire vector of N bits must be processed, wasting time and memory bandwidth."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "If a collection grows from 100,000 documents to 1,000,000 documents and the vocabulary grows from 100,000 to 500,000 terms, by what factor does the incidence matrix cell count increase?",
        "correct": "It increases by a factor of 50 (from 10 billion cells to 500 billion cells).",
        "distractors": [
            "It increases by a factor of 10 (from 10 billion cells to 100 billion cells).",
            "It increases by a factor of 5 (from 100 billion cells to 500 billion cells).",
            "It increases by a factor of 25 (from 20 billion cells to 500 billion cells)."
        ],
        "explanation": "Initial = 100,000 * 100,000 = 10^10 cells. Final = 1,000,000 * 500,000 = 5 * 10^11 cells. Ratio = (5 * 10^11) / 10^10 = 50."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "Why is a standard binary term-document incidence matrix inadequate for modern ranked retrieval algorithms like BM25 or TF-IDF?",
        "correct": "It only records binary presence or absence (0 or 1) and completely discards how many times a term occurs in a document.",
        "distractors": [
            "It cannot be indexed using hash tables or B-trees because matrix columns are restricted to fixed-width bit arrays.",
            "It forces terms to be sorted alphabetically, preventing the calculation of inverse document frequency scores.",
            "It automatically deletes terms that occur in fewer than 1% of the documents to prevent excessive matrix sparsity."
        ],
        "explanation": "Binary incidence matrices record only whether a term occurs (1) or not (0), losing term frequency (tf) information required for ranking."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "Let Doc1 = [1, 0, 1], Doc2 = [1, 1, 0], Doc3 = [0, 1, 1] for terms [Alpha, Beta, Gamma]. What is the result of the query 'Alpha AND NOT Gamma'?",
        "correct": "Doc2 only (Alpha is present in Doc2, and Gamma is absent).",
        "distractors": [
            "Doc1 only (Alpha is present in Doc1, and Gamma is present).",
            "Doc3 only (Alpha is absent in Doc3, and Gamma is present).",
            "Doc1 and Doc2 (Alpha is present in both Doc1 and Doc2)."
        ],
        "explanation": "Alpha is in Doc1 and Doc2. Gamma is in Doc1 and Doc3. NOT Gamma means Doc2. Alpha AND NOT Gamma matches Doc2 only."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "Given TermX = 010101 and TermY = 100110 in a 6-document collection, which bit vector represents the Boolean query 'TermX OR TermY'?",
        "correct": "110111 (matching documents 1, 2, 4, 5, and 6).",
        "distractors": [
            "000100 (matching document 4 only).",
            "110011 (matching documents 1, 2, 5, and 6).",
            "010111 (matching documents 2, 4, 5, and 6)."
        ],
        "explanation": "Bitwise OR of 010101 and 100110 is 110111 (all documents except Document 3)."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "Which of the following is NOT an inherent limitation of the binary term-document incidence matrix?",
        "correct": "Inability to execute Boolean conjunction and disjunction queries using bitwise logic.",
        "distractors": [
            "Inability to store positional information needed for phrase and proximity searches.",
            "Severe memory waste due to storing enormous quantities of zeroes for sparse terms.",
            "Inability to record term frequencies to differentiate minor mentions from major topics."
        ],
        "explanation": "Incidence matrices can execute Boolean conjunction and disjunction via bitwise AND and OR very easily; their failure lies in sparsity, size, and lack of positions/frequencies."
    },
    {
        "topic": "Term-Document Incidence Matrix",
        "question": "What operational overhead occurs when a new document is added to a collection represented by a term-document incidence matrix?",
        "correct": "A new column of M bits must be appended across all M rows, expanding the width of the entire matrix.",
        "distractors": [
            "The entire vocabulary must be re-sorted and all existing cell bits must be inverted using bitwise NOT.",
            "All previous document vectors must be deleted and reconstructed from scratch to preserve column alignment.",
            "Every existing row must be split into multiple sub-matrices to accommodate the new document serial number."
        ],
        "explanation": "Adding a document requires appending a new bit to every one of the M term rows in the matrix, altering the layout of the entire matrix structure."
    },

    # -------------------------------------------------------------
    # Topic 3: Inverted Index Architecture & Construction (Q31 - Q46)
    # -------------------------------------------------------------
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "In information retrieval terminology, what is the precise distinction between 'vocabulary' and 'dictionary'?",
        "correct": "The vocabulary is the conceptual set of unique terms, while the dictionary is the actual data structure storing them and their metadata.",
        "distractors": [
            "The vocabulary contains English words, while the dictionary contains words translated into international languages.",
            "The vocabulary is stored on disk with postings lists, while the dictionary is stored in the operating system kernel.",
            "The vocabulary stores document IDs, while the dictionary stores word positional offsets within individual documents."
        ],
        "explanation": "As stated in Lecture 1: 'We use dictionary for the data structure and vocabulary for the set of terms.'"
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "What is a 'posting' in the context of an inverted index?",
        "correct": "An individual entry in a postings list recording that a specific term appears in a particular document (identified by docID).",
        "distractors": [
            "The alphabetical header in the dictionary that defines the term string and its character length.",
            "A temporary disk buffer used during external merge sort to hold unsorted character tokens.",
            "The user query string submitted to the search engine after stop words have been filtered out."
        ],
        "explanation": "A posting is an item in a postings list recording that a term appeared in a document (at minimum storing the document ID)."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "Why is it crucial that postings lists in an inverted index are maintained in sorted order by document ID (docID)?",
        "correct": "It allows postings lists to be intersected in linear time O(x + y) using a simultaneous two-pointer walk.",
        "distractors": [
            "It guarantees that documents with higher relevance scores are positioned at the beginning of the list.",
            "It prevents duplicate term occurrences within a single document from being stored in the dictionary.",
            "It enables constant-time O(1) random access to arbitrary documents without traversing preceding nodes."
        ],
        "explanation": "Sorting by docID is what allows the linear merge algorithm to intersect two lists in O(x + y) time by scanning forward simultaneously."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "What is the correct chronological sequence of steps in constructing a basic inverted index?",
        "correct": "Collect documents -> Tokenize text -> Perform linguistic preprocessing -> Sort (term, docID) pairs -> Create dictionary and postings.",
        "distractors": [
            "Collect documents -> Sort raw text -> Tokenize text -> Create dictionary -> Perform linguistic preprocessing.",
            "Tokenize text -> Collect documents -> Create postings -> Sort terms -> Perform linguistic preprocessing.",
            "Linguistic preprocessing -> Tokenize text -> Collect documents -> Create dictionary -> Sort postings lists."
        ],
        "explanation": "Standard pipeline: 1. Collect documents; 2. Tokenize text; 3. Linguistic preprocessing (normalization, stemming); 4. Sort (term, docID) pairs; 5. Create dictionary and postings."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "During index construction, what is the immediate output of the tokenizer and linguistic preprocessor before any sorting occurs?",
        "correct": "A sequential stream of (modified term, docID) pairs reflecting the order of words appearing in the documents.",
        "distractors": [
            "A fully sorted dictionary with finalized document frequencies and compressed postings pointers.",
            "A binary term-document incidence matrix with bitwise compression applied to each document vector.",
            "A set of disjoint postings lists linked together by skip pointers in ascending alphabetical order."
        ],
        "explanation": "The tokenizer and linguistic modules emit a sequence of (term, docID) pairs in document order, which are subsequently sorted by term and docID."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "In the core indexing step of inverted index construction, how are the (term, docID) pairs sorted?",
        "correct": "Primarily alphabetically by term, and secondarily in ascending numerical order by document ID (docID).",
        "distractors": [
            "Primarily by document ID in ascending order, and secondarily alphabetically by term string.",
            "Primarily by term length in characters, and secondarily by document frequency in descending order.",
            "Primarily by document frequency, and secondarily by the chronological creation timestamp of the file."
        ],
        "explanation": "The core indexing step sorts pairs primarily by term (so all occurrences of a term are contiguous) and secondarily by docID (so postings are sorted)."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "When aggregating sorted (term, docID) pairs into final postings lists, how are multiple occurrences of the same term within a single document handled?",
        "correct": "They are merged into a single posting for that docID, and the document frequency (df) of the term is incremented by one.",
        "distractors": [
            "Each occurrence generates a separate posting with an identical docID appended consecutively to the postings list.",
            "The term is flagged as ambiguous and moved to a separate auxiliary dictionary for phrase query processing.",
            "Duplicate occurrences are retained in the dictionary, creating multiple identical vocabulary entries for each term."
        ],
        "explanation": "In a non-positional index, multiple occurrences of a term in the same doc are merged into a single posting (optionally recording term frequency tf), incrementing df."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "What is 'document frequency' (df) in an inverted index, and where is it typically stored?",
        "correct": "The count of distinct documents containing the term, stored in the dictionary alongside the term and postings pointer.",
        "distractors": [
            "The total number of times the term appears across all documents, stored inside each individual posting node.",
            "The length of the document in total word tokens, stored in the document header table on physical disk.",
            "The position of the term within a specific document, stored in the positional index skip pointer structure."
        ],
        "explanation": "Document frequency (df) is the number of documents that contain the term (the length of its postings list) and is stored in the dictionary entry for the term."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "Where are the dictionary and postings lists typically placed in the storage hierarchy of a production IR system?",
        "correct": "The dictionary is generally kept in fast main memory, while the bulkier postings lists are stored on disk or flash storage.",
        "distractors": [
            "Both the dictionary and postings lists are stored exclusively on magnetic tape archives to minimize operating costs.",
            "Postings lists are stored in CPU L1 cache, while the dictionary is stored in remote network-attached database tables.",
            "The dictionary is stored on disk in raw character files, while postings lists are generated dynamically on demand."
        ],
        "explanation": "The dictionary is relatively compact and accessed for every query term, so it is kept in RAM. Postings lists are much larger and typically stored on disk or SSD."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "What is a major advantage and a major disadvantage of using linked lists to implement postings lists in memory?",
        "correct": "They support dynamic insertions and deletions easily, but suffer from memory pointer overhead and poor cache locality.",
        "distractors": [
            "They eliminate the need for docID sorting, but restrict the postings list to a maximum length of 256 documents.",
            "They provide instant O(1) random binary search, but require contiguous blocks of pre-allocated physical memory.",
            "They compress postings integers automatically, but prevent the implementation of skip pointers during query merges."
        ],
        "explanation": "Linked lists make inserting/deleting postings easy when documents change, but each node requires a pointer (wasting memory) and non-contiguous memory harms cache locality."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "Why do many high-performance search engines use variable-length arrays rather than linked lists for postings lists?",
        "correct": "Contiguous memory storage offers superior CPU cache locality and zero pointer overhead, speeding up sequential traversal.",
        "distractors": [
            "Variable-length arrays allow instantaneous insertion of new postings in the middle of lists without memory reallocation.",
            "Variable-length arrays eliminate the requirement of assigning unique numerical docIDs to indexed documents.",
            "They allow postings lists to be searched in constant time O(1) regardless of list length or query complexity."
        ],
        "explanation": "Variable-length arrays store postings contiguously in memory, eliminating pointer overhead and allowing fast sequential memory access with optimal CPU cache performance."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "As described in the textbook and slides, what is the hybrid data structure scheme for storing postings lists?",
        "correct": "A linked list of fixed-length array blocks, balancing ease of dynamic insertion with reduced pointer overhead.",
        "distractors": [
            "A B-tree of hash tables where each hash bucket represents a distinct character encoding format.",
            "A skip list that alternates between 7-bit ASCII strings and 64-bit IEEE floating-point numbers.",
            "A circular doubly linked list that stores postings in reverse chronological order across disk sectors."
        ],
        "explanation": "Lecture 1 slide 41: 'We can use a hybrid scheme, with linked list of fixed length arrays for each term.' This amortizes pointer overhead while allowing dynamic expansion."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "Why is allocating a single fixed-length array for every term's postings list unacceptable in inverted index design?",
        "correct": "Term frequencies vary wildly by Zipf's Law; fixed arrays either waste massive space for rare terms or overflow on common terms.",
        "distractors": [
            "Fixed-size arrays cannot store integers larger than 16 bits, restricting the corpus size to 65,535 documents.",
            "Modern operating systems do not allow fixed-length arrays to be written sequentially to disk storage blocks.",
            "Fixed-size arrays prevent the query optimizer from reading document frequency values from the dictionary."
        ],
        "explanation": "Because word frequencies follow a power law (Zipf's Law), some terms appear in millions of docs while others appear in only one doc. Fixed-size arrays are completely unworkable."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "According to the storage analysis in Lecture 1 ('Where do we pay in storage?'), which components consume index space?",
        "correct": "Dictionary terms and counts, postings document ID lists, and structural memory pointers.",
        "distractors": [
            "Only the dictionary term strings; postings lists occupy zero persistent storage space.",
            "Only the raw document text copies; inverted index files are deleted after query evaluation.",
            "Operating system process identifiers and network socket transmission protocol control blocks."
        ],
        "explanation": "As shown in Lecture 1 slide 40, storage costs comprise terms and counts in the dictionary, pointers (in dictionary and linked lists), and lists of docIDs in postings."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "Why are document IDs (docIDs) in an inverted index typically assigned as sequential integers (1, 2, 3...) rather than arbitrary hashes?",
        "correct": "Sequential numbering yields compact integer representations and enables efficient sorting and difference-gap compression.",
        "distractors": [
            "Arbitrary hashes cannot be compared using greater-than or less-than relational operators in standard programming languages.",
            "Sequential integers are required by the operating system kernel to open multiple document files simultaneously.",
            "Hash values prevent the tokenizer from recognizing punctuation and whitespace characters in document text streams."
        ],
        "explanation": "Sequential integer docIDs take minimal space, are trivial to sort, and enable delta/gap compression (storing differences between successive docIDs)."
    },
    {
        "topic": "Inverted Index Architecture & Construction",
        "question": "In a standard non-positional inverted index, which of the following is NOT typically stored directly inside the dictionary entry for a term?",
        "correct": "The complete list of all document IDs containing that term.",
        "distractors": [
            "The normalized term string itself (the word type).",
            "The document frequency (df) indicating the number of documents containing the term.",
            "A pointer or memory address referencing the start of the term's postings list."
        ],
        "explanation": "The dictionary entry stores the term, its document frequency (df), and a pointer to the postings list. The postings list itself stores the document IDs."
    },

    # -------------------------------------------------------------
    # Topic 4: Postings Merge & Boolean Query Processing (Q47 - Q62)
    # -------------------------------------------------------------
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "In the standard linear merge algorithm for intersecting two sorted postings lists, what action is taken when docID1 is strictly less than docID2?",
        "correct": "The pointer for the first postings list (docID1) is advanced to its next node.",
        "distractors": [
            "The pointer for the second postings list (docID2) is advanced to its next node.",
            "Both pointers are advanced simultaneously, and docID1 is added to the result list.",
            "The algorithm terminates immediately because the document IDs do not match."
        ],
        "explanation": "Because postings lists are sorted in ascending order, if docID1 < docID2, docID1 cannot appear in the second list, so pointer 1 must advance."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "During the intersection of two sorted postings lists, what occurs when the pointers in both lists point to identical document IDs?",
        "correct": "The matching docID is appended to the result list, and both pointers are advanced to their respective next nodes.",
        "distractors": [
            "The docID is added to the result list, but only the pointer in the shorter postings list is advanced.",
            "The docID is discarded because Boolean conjunction requires distinct document identifiers from each list.",
            "The algorithm jumps backwards to the beginning of the second postings list to search for duplicate entries."
        ],
        "explanation": "When docID1 == docID2, a common document is found. It is added to the result set and both pointers are advanced."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "What is the worst-case time complexity of intersecting two sorted postings lists of lengths x and y using the linear merge algorithm?",
        "correct": "O(x + y) comparisons, linear in the sum of the lengths of the two postings lists.",
        "distractors": [
            "O(x * y) comparisons, quadratic in the product of the lengths of the two postings lists.",
            "O(log(x + y)) comparisons, logarithmic in the total number of document identifiers.",
            "O(x^2 + y^2) comparisons, polynomial in the square of individual list dimensions."
        ],
        "explanation": "Each comparison advances at least one pointer. At most x + y comparisons can be made before one list is exhausted, giving O(x + y) linear time."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "Given postings list P1 = [2, 4, 8, 16, 32, 64] and postings list P2 = [1, 2, 3, 5, 8, 13, 21], what is the intersection result for the query 'Term1 AND Term2'?",
        "correct": "Documents 2 and 8.",
        "distractors": [
            "Documents 1, 2, 4, and 8.",
            "Documents 2, 8, 16, and 32.",
            "Document 2 only."
        ],
        "explanation": "Comparing elements: 2 appears in both, and 8 appears in both. No other elements are shared. The intersection is [2, 8]."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "When intersecting list A = [2, 8] and list B = [1, 2, 3, 5, 8], how many element comparisons are performed by the standard linear merge algorithm until both lists are traversed?",
        "correct": "6 comparisons (1 vs 2, 2 vs 2, 3 vs 8, 5 vs 8, 8 vs 8, and end of list check).",
        "distractors": [
            "2 comparisons (matching only elements 2 and 8 directly).",
            "10 comparisons (evaluating every Cartesian product pair).",
            "4 comparisons (skipping elements that are odd numbers)."
        ],
        "explanation": "Pointers trace: 2 vs 1 (B advances), 2 vs 2 (match, both advance), 8 vs 3 (B advances), 8 vs 5 (B advances), 8 vs 8 (match, both advance). Total element comparisons = 5 (plus list exhaustion check)."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "What occurs in the linear AND merge algorithm when one of the two postings lists reaches its end before the other?",
        "correct": "The merge loop terminates immediately, because no remaining elements in the non-empty list can appear in the empty list.",
        "distractors": [
            "The algorithm appends all remaining elements of the non-empty postings list directly into the final result list.",
            "The algorithm resets the exhausted list pointer back to the beginning to verify if any elements were skipped.",
            "The algorithm raises a runtime exception and discards all previously matched document identifiers."
        ],
        "explanation": "In an AND merge, a document must appear in both lists. Once one list is exhausted, no further matches are possible, so the algorithm terminates."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "How does the postings merge algorithm for a Boolean disjunction (Term1 OR Term2) differ from an AND merge when docID1 < docID2?",
        "correct": "In an OR merge, docID1 is added to the result list before advancing pointer 1, whereas in an AND merge it is discarded.",
        "distractors": [
            "In an OR merge, pointer 2 is advanced while pointer 1 remains stationary until docID2 exceeds docID1.",
            "In an OR merge, both pointers must be reset to the beginning whenever unequal document IDs are encountered.",
            "In an OR merge, docID1 is only added if it also appears in an auxiliary stop word postings list."
        ],
        "explanation": "In an OR merge (union), every document in either list must appear in the result. When docID1 < docID2, docID1 is output and pointer 1 advances."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "When processing an OR merge (Term1 OR Term2) and the first postings list is exhausted, what must the algorithm do with the second list?",
        "correct": "It must append all remaining docIDs from the second postings list into the result list.",
        "distractors": [
            "It must terminate immediately and discard any remaining docIDs in the second postings list.",
            "It must delete the results collected so far because complete list symmetry was not achieved.",
            "It must restart the intersection from the beginning using a binary search algorithm."
        ],
        "explanation": "In a union (OR), all elements from both lists are included. When one list is exhausted, all remaining elements of the other list must be appended."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "To process the query 'Brutus AND NOT Caesar', how should the postings merge algorithm advance pointers when docID_Brutus < docID_Caesar?",
        "correct": "docID_Brutus is added to the result list because it does not match Caesar, and the Brutus pointer is advanced.",
        "distractors": [
            "docID_Brutus is discarded from the result list, and the Caesar pointer is advanced to the next posting.",
            "Both pointers are advanced simultaneously and docID_Caesar is added to the result list.",
            "The merge terminates immediately because a negative condition cannot be resolved with linear pointers."
        ],
        "explanation": "In 'Brutus AND NOT Caesar', we want Brutus documents that do NOT contain Caesar. If docID_Brutus < docID_Caesar, it cannot match Caesar, so it is kept."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "WestLaw is highlighted in Lecture 2 as a premier example of commercial Boolean search. What characterizes its user base and query style?",
        "correct": "Hundreds of thousands of legal professionals executing long, complex, incrementally refined Boolean queries with proximity operators.",
        "distractors": [
            "Millions of casual web searchers typing single-word keyword queries without Boolean operators.",
            "Automated robotic crawlers downloading plain text documents using simple linear grep scans.",
            "Academic researchers testing vector space ranking algorithms on small experimental collections."
        ],
        "explanation": "WestLaw has ~700,000 paying professional subscribers who prefer precise Boolean queries with structural and proximity operators."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "In the WestLaw Boolean query syntax described in the course slides, what does a whitespace between terms represent?",
        "correct": "A disjunction (Boolean OR), contrasting with typical modern web search engines where whitespace implies AND.",
        "distractors": [
            "A conjunction (Boolean AND), requiring both terms to be present in the document.",
            "A strict negation (Boolean NOT), excluding the second term from retrieved documents.",
            "An exact phrase requirement, enforcing that the terms appear in consecutive sequence."
        ],
        "explanation": "In WestLaw syntax, space represents disjunction (OR), while modern web search engines treat space as conjunction (AND)."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "In WestLaw query syntax, what do the operators '/s' and '/p' specify?",
        "correct": "Terms must occur within the same sentence ('/s') or within the same paragraph ('/p').",
        "distractors": [
            "Terms must occur within the same section ('/s') or within the same page ('/p').",
            "Terms must match synonym equivalence ('/s') or phonetic soundex ('/p').",
            "Terms must be stemmed with Porter ('/s') or lemmatized with WordNet ('/p')."
        ],
        "explanation": "In WestLaw, '/s' is the same-sentence proximity operator, and '/p' is the same-paragraph proximity operator."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "What is the classic 'feast or famine' dilemma encountered by users in exact-match Boolean retrieval systems?",
        "correct": "Queries either return too few results (famine, often 0 docs) if too specific, or too many results (feast, thousands of docs) if too broad.",
        "distractors": [
            "Storage costs fluctuate between overflowing memory during tokenization and starving disk buffers during sorting.",
            "Search engines either consume all CPU cycles during skip pointer jumps or idle completely during dictionary lookups.",
            "Indexers either produce completely empty postings lists for rare terms or duplicate postings lists for common terms."
        ],
        "explanation": "In exact Boolean search, adding terms (AND) often results in 0 documents (famine), while removing terms (OR) returns thousands of unranked documents (feast)."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "Why do standard Boolean retrieval systems typically fail to satisfy casual web users compared to ranked retrieval systems?",
        "correct": "They treat all matching documents equally without ranking them by relevance, forcing users to browse unordered results.",
        "distractors": [
            "They cannot execute queries that contain more than one Boolean operator in a single search session.",
            "They require all indexed documents to be translated into formal relational database schemas before searching.",
            "They cannot process queries in linear time, resulting in several minutes of latency per search request."
        ],
        "explanation": "Boolean retrieval gives an unordered set of matches with no relevance ranking, which is overwhelming for web users who only look at the top few results."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "Caesar's postings list is [1, 2, 4, 11, 31, 45, 173] and Calpurnia's postings list is [2, 31, 54, 101]. What is the output of 'Caesar AND Calpurnia'?",
        "correct": "Documents 2 and 31.",
        "distractors": [
            "Documents 1, 2, 4, 11, and 31.",
            "Documents 2, 31, 45, and 54.",
            "Document 2 only."
        ],
        "explanation": "Intersecting [1, 2, 4, 11, 31, 45, 173] and [2, 31, 54, 101] yields [2, 31]."
    },
    {
        "topic": "Postings Merge & Boolean Query Processing",
        "question": "Which of the following is NOT a reason why legal and intelligence experts often prefer Boolean retrieval over ranked retrieval?",
        "correct": "Boolean queries automatically correct spelling mistakes and expand synonyms through machine learning models.",
        "distractors": [
            "Boolean retrieval offers transparent, deterministic, and predictable results that can be legally audited.",
            "Professional searchers have precise control over exactly which terms must or must not appear in matching documents.",
            "Complex Boolean expressions with proximity operators allow exhaustive retrieval of all legally mandated documents."
        ],
        "explanation": "Boolean retrieval does not use machine learning to alter queries or expand synonyms; its value to experts is precision, transparency, and strict determinism."
    }
]
