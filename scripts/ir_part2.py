# Part 2: Questions 63 to 129
# Topics:
# 5. Query Optimization (Q63 to Q78)
# 6. Biword Indexes & Extended Biwords (Q79 to Q93)
# 7. Positional Indexes & Proximity Queries (Q94 to Q111)
# 8. Skip Pointers & Faster Postings Merges (Q112 to Q129)

part2_questions = [
    # -------------------------------------------------------------
    # Topic 5: Query Optimization (Q63 - Q78)
    # -------------------------------------------------------------
    {
        "topic": "Query Optimization",
        "question": "What is the fundamental optimization rule when processing a multi-term Boolean conjunction query such as Q = term1 AND term2 AND ... AND termN?",
        "correct": "Process terms in order of increasing document frequency (df), starting with the two shortest postings lists.",
        "distractors": [
            "Process terms in order of decreasing document frequency (df), starting with the most frequent terms.",
            "Process terms in alphabetical order of the term strings as they are stored in the dictionary.",
            "Process terms in the exact syntactic order in which the user typed them into the search interface."
        ],
        "explanation": "Processing in order of increasing document frequency (shortest lists first) prunes the candidate set immediately, minimizing work for later merges."
    },
    {
        "topic": "Query Optimization",
        "question": "Why does processing multi-term conjunctions in order of increasing document frequency minimize the total computation time?",
        "correct": "The size of an intermediate intersection can never exceed the smallest input list, rapidly pruning candidates for subsequent merges.",
        "distractors": [
            "The dictionary data structure can only locate postings lists in ascending numerical order of their document frequency values.",
            "Sorting by increasing frequency allows the CPU to skip all comparison operations during the final postings list intersection.",
            "It ensures that all stop words are evaluated first, eliminating the need to read longer postings lists from magnetic disk storage."
        ],
        "explanation": "Because |A ∩ B| <= min(|A|, |B|), intersecting the smallest sets first ensures intermediate lists are small, drastically reducing later comparisons."
    },
    {
        "topic": "Query Optimization",
        "question": "Given the document frequencies df(Calpurnia) = 4, df(Brutus) = 8, and df(Caesar) = 16, what is the optimal execution order for the query 'Calpurnia AND Brutus AND Caesar'?",
        "correct": "Execute the query as (Calpurnia AND Brutus) AND Caesar.",
        "distractors": [
            "Execute the query as (Caesar AND Brutus) AND Calpurnia.",
            "Execute the query as (Caesar AND Calpurnia) AND Brutus.",
            "Execute the query as Calpurnia AND (Caesar AND Brutus)."
        ],
        "explanation": "Lecture 2 slide 14: Calpurnia (4) and Brutus (8) are the two smallest lists. Their intersection is at most 4 items, which is then intersected with Caesar (16)."
    },
    {
        "topic": "Query Optimization",
        "question": "If df(TermA) = 15, df(TermB) = 300, and df(TermC) = 5,000, what is the maximum possible number of document IDs in the intermediate result after evaluating (TermA AND TermB)?",
        "correct": "At most 15 document IDs, bounded strictly by the smaller postings list of TermA.",
        "distractors": [
            "At most 300 document IDs, bounded by the larger postings list of TermB.",
            "At most 315 document IDs, representing the sum of both postings list lengths.",
            "At most 5,000 document IDs, bounded by the largest postings list in the query."
        ],
        "explanation": "An intersection of two sets cannot contain more elements than the smaller set. Here, min(15, 300) = 15."
    },
    {
        "topic": "Query Optimization",
        "question": "For terms X (len=10), Y (len=1,000), and Z (len=10,000), what is the maximum number of postings comparisons in the first merge if processed worst-order (Y AND Z) versus optimal (X AND Y)?",
        "correct": "Worst-order requires up to 11,000 comparisons (1,000 + 10,000), while optimal requires up to 1,010 comparisons (10 + 1,000).",
        "distractors": [
            "Worst-order requires up to 1,010 comparisons, while optimal requires up to 11,000 comparisons.",
            "Worst-order requires up to 10,000,000 comparisons, while optimal requires up to 10,000 comparisons.",
            "Worst-order requires up to 100 comparisons, while optimal requires up to 10 comparisons."
        ],
        "explanation": "Linear merge of lists x and y takes at most x + y comparisons. Worst order (Y and Z): 1,000 + 10,000 = 11,000. Optimal (X and Y): 10 + 1,000 = 1,010."
    },
    {
        "topic": "Query Optimization",
        "question": "In the formal algorithm INTERSECT(t1, ..., tn) presented in Lecture 2, what is the first step executed before any postings lists are merged?",
        "correct": "Sort the query terms in ascending order based on their document frequencies retrieved from the dictionary.",
        "distractors": [
            "Load all postings lists into a unified hash table and compute bitwise AND across all document vectors.",
            "Eliminate all terms that appear in more than 50% of the documents in the collection as stop words.",
            "Allocate a variable-length result array sized to the sum of all document frequencies across the terms."
        ],
        "explanation": "Lecture 2 slide 17: Line 1 of INTERSECT is 'terms <- SORTBYINCREASINGFREQUENCY((t1, ... tn))'."
    },
    {
        "topic": "Query Optimization",
        "question": "When optimizing a query of the form (Term1 OR Term2) AND (Term3 OR Term4), how does the query optimizer determine which disjunctive clause to process first?",
        "correct": "It estimates the size of each OR clause as df(TermA) + df(TermB) and evaluates the clause with the smaller estimate first.",
        "distractors": [
            "It computes the exact set intersection of all four terms before determining the order of disjunctive operations.",
            "It always evaluates the second disjunctive clause first because Boolean algebra requires right-to-left evaluation.",
            "It converts both disjunctions into equivalent biword phrases and performs an immediate positional merge."
        ],
        "explanation": "Lecture 2 slide 15: Estimate the size of each OR by the sum of its document frequencies (conservative), then process in increasing order of OR sizes."
    },
    {
        "topic": "Query Optimization",
        "question": "Why is estimating the size of (Term1 OR Term2) as df(Term1) + df(Term2) described as a 'conservative' estimate?",
        "correct": "It represents an upper bound assuming the terms never co-occur; if documents contain both terms, the actual union is smaller.",
        "distractors": [
            "It represents a lower bound assuming all documents containing Term1 also contain Term2 simultaneously.",
            "It guarantees that the intermediate result will exactly match the bitwise XOR of the two incidence vectors.",
            "It assumes that both terms are stop words and will be eliminated during linguistic preprocessing."
        ],
        "explanation": "|A ∪ B| = |A| + |B| - |A ∩ B|. The sum |A| + |B| is an upper bound (conservative) assuming no overlap (|A ∩ B| = 0)."
    },
    {
        "topic": "Query Optimization",
        "question": "Consider the query from Lecture 2: (tangerine OR trees) AND (marmalade OR skies) AND (kaleidoscope OR eyes). Given df(tangerine)=10, df(trees)=20, df(marmalade)=50, df(skies)=5, df(kaleidoscope)=30, df(eyes)=10. What is the optimal evaluation order?",
        "correct": "(tangerine OR trees) first [est. 30], then (kaleidoscope OR eyes) [est. 40], then (marmalade OR skies) [est. 55].",
        "distractors": [
            "(marmalade OR skies) first [est. 55], then (kaleidoscope OR eyes) [est. 40], then (tangerine OR trees) [est. 30].",
            "(kaleidoscope OR eyes) first [est. 40], then (tangerine OR trees) [est. 30], then (marmalade OR skies) [est. 55].",
            "(tangerine OR trees) first [est. 30], then (marmalade OR skies) [est. 55], then (kaleidoscope OR eyes) [est. 40]."
        ],
        "explanation": "Estimates: (tangerine OR trees) = 10+20=30; (marmalade OR skies) = 50+5=55; (kaleidoscope OR eyes) = 30+10=40. Increasing order: 30, then 40, then 55."
    },
    {
        "topic": "Query Optimization",
        "question": "Why is the document frequency (df) of each term stored directly in the dictionary entry rather than at the head of the postings list on disk?",
        "correct": "It allows the query optimizer to inspect frequencies and determine the optimal merge order in memory without disk I/O.",
        "distractors": [
            "It prevents the postings list on disk from exceeding standard physical sector allocation limits.",
            "It allows the tokenizer to calculate term syllable measures during Porter stemming operations.",
            "It is required by the operating system file system to allocate variable-length memory arrays."
        ],
        "explanation": "Storing df in memory inside the dictionary allows the optimizer to sort query terms by frequency before fetching or reading any postings from disk."
    },
    {
        "topic": "Query Optimization",
        "question": "For a query structured as (A AND B) OR (C AND D), how does a Boolean query optimizer typically organize execution?",
        "correct": "It evaluates each conjunction independently using increasing df order, and then merges the two sorted result lists via an OR merge.",
        "distractors": [
            "It merges all four terms simultaneously using a four-pointer linear traversal without intermediate sorting.",
            "It converts the entire expression into a single incidence matrix and computes bitwise XOR across terms.",
            "It drops terms B and D to simplify the query into an approximate disjunction of single terms."
        ],
        "explanation": "Conjunctions (AND) are evaluated first in optimal order, yielding two intermediate postings lists, which are then combined using an OR merge."
    },
    {
        "topic": "Query Optimization",
        "question": "In multi-term conjunction evaluation INTERSECT(result, postings(next_term)), what happens to the previous intermediate result list in memory?",
        "correct": "Its memory can be reclaimed or overwritten by the newly pruned intersection, keeping working memory footprint minimal.",
        "distractors": [
            "It must be written to permanent disk storage to allow the user to backtrack through query history.",
            "It is appended to the dictionary as a new synthetic compound term for future query caching.",
            "It must be replicated across all CPU cores to prevent memory bus contention during subsequent merges."
        ],
        "explanation": "Intermediate results can be overwritten or discarded after each step, meaning memory usage is bounded by the smallest postings list."
    },
    {
        "topic": "Query Optimization",
        "question": "In the query 'rare_word AND common_word', where df(rare_word) = 2 and df(common_word) = 500,000, how does query optimization protect system resources?",
        "correct": "It initializes the result with the 2 docIDs of rare_word, making the subsequent merge do at most a few comparisons.",
        "distractors": [
            "It scans the 500,000 docIDs of common_word first to populate CPU cache lines before checking rare_word.",
            "It converts common_word into an extended biword to prevent memory buffer overflow during intersection.",
            "It deletes rare_word from the query because its low document frequency indicates a probable spelling error."
        ],
        "explanation": "Processing rare_word first creates a candidate set of size 2. When intersecting with common_word, it requires only a few checks (especially with skips)."
    },
    {
        "topic": "Query Optimization",
        "question": "Which of the following is NOT an effective strategy for optimizing Boolean query processing?",
        "correct": "Processing terms in decreasing order of document frequency so that large candidate sets are formed immediately.",
        "distractors": [
            "Using document frequency stored in the memory dictionary to plan intersection order before accessing postings on disk.",
            "Estimating disjunctive clause sizes using the sum of term frequencies to sequence conjunctions of disjunctions.",
            "Terminating an AND merge early as soon as the shorter postings list has been completely traversed."
        ],
        "explanation": "Processing in decreasing order of frequency is the worst possible order, creating large intermediate sets that maximize comparisons."
    },
    {
        "topic": "Query Optimization",
        "question": "When query optimization sequences a very short postings list (e.g., length 5) to intersect with a very long list (length 50,000), how do skip pointers on the long list provide maximum benefit?",
        "correct": "The few docIDs from the short list act as distant targets, enabling the long list to skip large blocks of non-matching postings.",
        "distractors": [
            "The short list is augmented with extra skip pointers every two elements to match the stride of the long list.",
            "Skip pointers on the long list are temporarily removed to prevent pointer comparison overhead during merging.",
            "The long list is inverted using bitwise NOT so that both lists contain approximately equal numbers of postings."
        ],
        "explanation": "When targets are sparse, skip pointers on the long list can skip hundreds or thousands of non-matching postings in single jumps."
    },
    {
        "topic": "Query Optimization",
        "question": "For the query 'A AND B AND NOT C', what is the most efficient order of evaluation?",
        "correct": "Intersect A and B first in order of increasing frequency, and then subtract postings matching C from the intermediate result.",
        "distractors": [
            "Compute NOT C first across the entire collection of documents, and then intersect the resulting huge set with A and B.",
            "Intersect B and C first, take the complement, and then evaluate the conjunction with term A.",
            "Convert the query into 'NOT (A AND B AND C)' using De Morgan's laws before accessing the dictionary."
        ],
        "explanation": "Evaluating positive terms A and B first creates a small intermediate result. Then subtract C from that small list, avoiding computing NOT C over all documents."
    },

    # -------------------------------------------------------------
    # Topic 6: Biword Indexes & Extended Biwords (Q79 - Q93)
    # -------------------------------------------------------------
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "What is a 'biword index' in information retrieval?",
        "correct": "An index where every consecutive pair of terms appearing in the text is treated and indexed as an individual dictionary term.",
        "distractors": [
            "An index that stores two separate postings lists for every term: one for titles and one for body text.",
            "An index where each document ID is represented as a pair of 16-bit integers to support larger collections.",
            "An index that maps each word to exactly two synonym equivalence classes using a pre-compiled thesaurus."
        ],
        "explanation": "A biword index treats every consecutive pair of terms in the text as a phrase term in the dictionary."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Given the text string 'Friends, Romans, Countrymen', which set of biword terms will be generated for the dictionary?",
        "correct": "'friends romans' and 'romans countrymen'.",
        "distractors": [
            "'friends countrymen' and 'romans friends'.",
            "'friends romans countrymen' and 'countrymen romans'.",
            "'friends' and 'romans' and 'countrymen'."
        ],
        "explanation": "Consecutive word pairs in 'Friends, Romans, Countrymen' are 'friends romans' and 'romans countrymen'."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "How is a two-word phrase query such as 'solar energy' processed using a standard biword index?",
        "correct": "As an immediate single-term lookup in the dictionary, retrieving the postings list for the biword 'solar energy'.",
        "distractors": [
            "As an expensive two-pointer intersection between the single-word postings lists of 'solar' and 'energy'.",
            "By loading the raw document texts and performing a linear grep search for the string 'solar energy'.",
            "By expanding the query into an asymmetric equivalence class containing all solar-related vocabulary."
        ],
        "explanation": "In a biword index, 'solar energy' is a dictionary term; processing a 2-word phrase query is an immediate single lookup."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "How is a longer phrase query such as 'stanford university palo alto' processed in a biword indexing system?",
        "correct": "As a Boolean conjunction of adjacent biwords: 'stanford university' AND 'university palo' AND 'palo alto'.",
        "distractors": [
            "As a single four-word dictionary lookup in a specialized quad-word vocabulary index.",
            "As a disjunction of biwords: 'stanford university' OR 'university palo' OR 'palo alto'.",
            "By searching for the first and last words ('stanford' AND 'alto') in the standard inverted index."
        ],
        "explanation": "Lecture 2 slide 21: A phrase like 'stanford university palo alto' is decomposed into the Boolean conjunction of its biwords."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Why can evaluating the Boolean query ('stanford university' AND 'university palo' AND 'palo alto') produce false positives for the phrase 'stanford university palo alto'?",
        "correct": "A document could contain all three biwords in disparate, non-contiguous sections without containing the complete 4-word phrase.",
        "distractors": [
            "The biwords might match documents that contain synonyms of 'stanford' instead of the literal search string.",
            "Boolean conjunction algorithms cannot evaluate more than two biwords simultaneously without causing merge errors.",
            "Biword tokens are automatically stemmed using Porter's algorithm, causing terms with different suffixes to match."
        ],
        "explanation": "A document can contain all three biwords in different paragraphs or sentences, satisfying the Boolean AND without having the 4 words in contiguous order."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Because biword index queries for phrases longer than two words can produce false positives, what additional step is required to guarantee accuracy?",
        "correct": "The candidate documents matching the Boolean biword query must be fetched and inspected to verify literal phrase occurrence.",
        "distractors": [
            "The query optimizer must re-execute the search using a term-document incidence matrix to verify bit alignment.",
            "All biwords in the candidate documents must be re-indexed dynamically using a variable-length linked list.",
            "The user must be prompted to manually confirm whether each retrieved document contains the desired phrase."
        ],
        "explanation": "As noted in Lecture 2 slide 21: 'Without the docs, we cannot verify that the docs matching the above Boolean query do contain the phrase.'"
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "What is the primary architectural drawback of indexing all possible biwords across a large collection?",
        "correct": "Massive expansion of the dictionary vocabulary size, which can approach O(V^2) potential distinct terms.",
        "distractors": [
            "Extreme CPU latency caused by sorting postings lists in reverse numerical order of document identifiers.",
            "Complete inability to process single-word keyword queries using the underlying inverted index.",
            "The requirement that all indexed documents must be translated into 7-bit ASCII before tokenization."
        ],
        "explanation": "Indexing all consecutive term pairs creates an explosion in vocabulary size (approaching V^2 potential biwords), causing significant index blowup."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Why do search engines not extend the biword concept to triwords, quadwords, or general n-words for all text phrases?",
        "correct": "Vocabulary explosion makes storing all n-grams computationally and physically prohibitive for arbitrary text corpora.",
        "distractors": [
            "Postings merge algorithms cannot mathematically process postings lists for phrases containing more than two words.",
            "Higher-order n-grams cannot be sorted alphabetically in the dictionary due to Unicode character limitations.",
            "Web search users never submit queries containing more than two consecutive words in production systems."
        ],
        "explanation": "The number of unique 3-word and 4-word combinations explodes exponentially, making comprehensive n-gram indexes unfeasible."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "What core NLP technique is utilized to create 'extended biwords' and avoid the uncontrolled vocabulary explosion of standard biword indexes?",
        "correct": "Part-of-speech (POS) tagging to identify meaningful grammatical patterns while grouping function words into class X.",
        "distractors": [
            "Soundex phonetic hashing to replace all vowels with numbers before generating consecutive word pairs.",
            "Complete case folding combined with unconditional deletion of all non-alphanumeric punctuation symbols.",
            "External merge sorting of all document sentences in descending order of character token length."
        ],
        "explanation": "Lecture 3 slide 16: Extended biwords use POS tagging to categorize words into Nouns (N) and function words/prepositions (X)."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "In the extended biword framework described in Lecture 3, what does the pattern NX*N represent?",
        "correct": "A sequence consisting of a Noun (N), followed by zero or more function words/prepositions (X), followed by a Noun (N).",
        "distractors": [
            "A sequence of N numbers (N) separated by arbitrary punctuation symbols (X) and terminating with a numeral (N).",
            "A non-positional posting (N) linked via an external pointer (X) to a normalized dictionary term (N).",
            "A phrase where N stop words surround an un-stemmed noun (X) within a single sentence boundary."
        ],
        "explanation": "NX*N matches noun phrases such as 'catcher in the rye' (N X X N) or 'cost of living' (N X N)."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Applying the NX*N pattern to the title 'catcher in the rye', where 'catcher' and 'rye' are Nouns (N) and 'in' and 'the' are function words (X), what extended biword is formed?",
        "correct": "'catcher rye' (representing the grammatical structure N X X N).",
        "distractors": [
            "'catcher in' and 'the rye' (representing two separate standard biwords).",
            "'in the' (representing the function word sequence X X).",
            "'catcher in the' (representing a triword sequence N X X)."
        ],
        "explanation": "Lecture 3 slide 16 gives this exact example: 'catcher in the rye' -> N X X N -> extended biword 'catcher rye'."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "How does an IR system process a user's natural language phrase query when an extended biword index is available?",
        "correct": "It parses the query with POS tagging, extracts matching NX*N patterns, and looks up the corresponding extended biword terms.",
        "distractors": [
            "It strips all nouns from the query and performs a conjunction search exclusively on function words.",
            "It converts all query terms to Soundex codes and executes an exact-match linear scan across disk blocks.",
            "It generates all possible permutations of words in the query and executes separate OR merges for each."
        ],
        "explanation": "The query is POS tagged to extract noun phrases matching the extended biword templates, which are then searched in the index."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Which of the following is a key limitation of the extended biword indexing approach?",
        "correct": "It cannot answer arbitrary phrase queries that do not conform to the predefined noun-phrase patterns (e.g., verb phrases or idioms).",
        "distractors": [
            "It consumes more dictionary space than indexing all arbitrary consecutive word pairs in the document collection.",
            "It requires all indexed documents to be stored in uncompressed raw text format on magnetic tape storage.",
            "It prevents the search engine from supporting Boolean conjunction queries between single-word terms."
        ],
        "explanation": "Extended biwords only capture phrases matching specific templates (like NX*N); phrases containing verbs, adjectives, or arbitrary idioms cannot be answered directly."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "A document contains: 'The president of Stanford spoke today. Tomorrow he visits the University of Tokyo in Palo Alto.' Why does the biword query ('stanford university' AND 'university palo' AND 'palo alto') fail here?",
        "correct": "It falsely matches this document because all three biwords occur, even though the phrase 'Stanford University Palo Alto' never appears.",
        "distractors": [
            "It fails to retrieve this document because 'Stanford' and 'University' are separated by a sentence boundary.",
            "It returns an empty result set because 'Tokyo' acts as an automatic query negation operator.",
            "It causes a system crash because the term 'Palo Alto' contains an uppercase character."
        ],
        "explanation": "The document contains 'Stanford' and 'University' in one sentence, and 'University' and 'Palo Alto' in another, yielding all 3 biwords despite no contiguous 4-word phrase."
    },
    {
        "topic": "Biword Indexes & Extended Biwords",
        "question": "Which of the following is NOT true regarding standard biword indexes?",
        "correct": "They completely eliminate the need for storing single-word terms in the dictionary.",
        "distractors": [
            "They allow instantaneous processing of two-word phrase queries with a single postings list lookup.",
            "They substantially increase the dictionary size compared to a standard unigram inverted index.",
            "They can produce false positive candidate documents when evaluating queries of three or more words."
        ],
        "explanation": "Single-word terms are still needed for single-word queries; biword indexes add pairs to the vocabulary rather than replacing unigrams."
    },

    # -------------------------------------------------------------
    # Topic 7: Positional Indexes & Proximity Queries (Q94 - Q111)
    # -------------------------------------------------------------
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "In a positional inverted index, what information is stored in the postings list for each term?",
        "correct": "Each posting contains a document ID (docID) followed by a list of the exact token positions where the term appears in that document.",
        "distractors": [
            "Each posting contains a document ID followed by the byte offset of the document file on the physical disk.",
            "Each posting contains a document ID followed by a list of all synonyms and hypernyms associated with the term.",
            "Each posting contains a document ID followed by the total count of distinct words in the entire collection."
        ],
        "explanation": "A positional index stores for each term: docID and the sequence of token positions (offsets) within that document."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "Which of the following accurately depicts the structural representation of an entry in a positional index?",
        "correct": "<term, df; docID1: pos1, pos2, ...; docID2: pos1, pos2, ...; ...>.",
        "distractors": [
            "<term, docID; length; byte_start, byte_end; skip_pointer>.",
            "<term, total_tokens; docID1, docID2; character_encoding>.",
            "<term, hash_code; position1: doc1, doc2; position2: doc1, doc2>."
        ],
        "explanation": "As shown in Lecture 2 slide 23 and Lecture 3 slide 18: <term, df; doc1: pos1, pos2 ...; doc2: pos1, pos2 ...; etc.>."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "How does an IR system evaluate a phrase query like 'information retrieval' using a positional index?",
        "correct": "It merges the docIDs, and for matching documents, intersects their position lists checking whether pos(retrieval) == pos(information) + 1.",
        "distractors": [
            "It merges single-word postings lists and then inspects the raw text files on disk to find the phrase.",
            "It converts both words into biwords and verifies that the sum of their document frequencies exceeds 100.",
            "It computes the bitwise AND of their incidence vectors and verifies that both words have identical stem lengths."
        ],
        "explanation": "For matching documents, the positional merge algorithm checks if position of term2 equals position of term1 + 1."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "Why does a positional index completely avoid the false positive problem inherent in biword phrase query processing?",
        "correct": "The exact relative word positions within the document are verified directly from the postings list before returning results.",
        "distractors": [
            "Positional indexes only store phrases that have been verified by human editors during indexing.",
            "The positional index automatically deletes documents that contain duplicate or ambiguous word tokens.",
            "It restricts queries to exact two-word combinations that match pre-defined extended biword patterns."
        ],
        "explanation": "Because token offsets are recorded in the index, the system verifies contiguity directly in memory without retrieving documents."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "In proximity searching, what does the query expression 'cat /3 dog' mean?",
        "correct": "Find documents where 'cat' and 'dog' appear within 3 words of each other.",
        "distractors": [
            "Find documents where 'cat' appears exactly 3 times and 'dog' appears at least once.",
            "Find documents where 'cat' is located in paragraph 3 and 'dog' is located in paragraph 1.",
            "Find documents where the term frequency of 'cat' divided by that of 'dog' is equal to 3."
        ],
        "explanation": "In proximity queries, /k means 'within k words of each other' (|pos1 - pos2| <= k)."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "Why can a positional index easily execute arbitrary proximity queries like 'statute /5 fraud', whereas a biword index cannot?",
        "correct": "Positional indexes record variable token positions, allowing distance calculations, while biwords only capture immediate adjacency.",
        "distractors": [
            "Biword indexes only store document titles, whereas positional indexes store entire document character streams.",
            "Positional indexes use skip pointers to calculate Euclidean distances between words across different documents.",
            "Biword indexes cannot store words longer than five characters in their internal dictionary data structures."
        ],
        "explanation": "Biword indexes only capture immediate word pairs (k = 1). Positional indexes store explicit positions, enabling any distance check |p1 - p2| <= k."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "Using the lecture index: fools (doc2: 1, 17, 74, 222; doc4: 8, 78, 108, 458; doc7: 3, 13, 23, 193), rush (doc2: 2, 66; doc4: 9, 69; doc7: 4, 14, 404), in (doc2: 3, 37; doc4: 10, 20; doc7: 5, 15, 25). Which documents match the phrase 'fools rush in'?",
        "correct": "Documents 2, 4, and 7 all contain valid contiguous positions for 'fools rush in'.",
        "distractors": [
            "Documents 2 and 4 only, because Doc 7 has positions that exceed the maximum phrase length.",
            "Document 4 only, because its matching positions are centered within the first 10 tokens of the document.",
            "Document 2 only, because its match begins at position 1."
        ],
        "explanation": "Doc 2 matches at 1, 2, 3. Doc 4 matches at 8, 9, 10. Doc 7 matches at 3, 4, 5 (and also at 13, 14, 15). All three documents match."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "In the same lecture index, 'angels fear to tread' has entries: angels (doc4: 12), fear (doc4: 13), to (doc4: 14), tread (doc4: 15). Which document(s) satisfy the query: 'fools rush in' AND 'angels fear to tread'?",
        "correct": "Document 4 only.",
        "distractors": [
            "Documents 2 and 4.",
            "Documents 4 and 7.",
            "Documents 2, 4, and 7."
        ],
        "explanation": "Doc 4 is the only document containing 'angels fear to tread' (positions 12, 13, 14, 15), and it also contains 'fools rush in' (positions 8, 9, 10)."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "According to the empirical rules of thumb in Lecture 3, how much larger is a positional index compared to a standard non-positional index?",
        "correct": "It is roughly 2 to 4 times as large as a non-positional index.",
        "distractors": [
            "It is roughly 10 to 20 times as large as a non-positional index.",
            "It is roughly the exact same size because positions replace document identifiers.",
            "It is roughly 50 to 100 times as large as a non-positional index."
        ],
        "explanation": "Lecture 3 slide 25: 'Rule of thumb: A positional index is 2-4 times as large as a non-positional index.'"
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "According to the rule of thumb in the textbook, what is the typical compressed size of a positional index relative to the volume of original text?",
        "correct": "Approximately 35% to 50% of the volume of the original uncompressed text.",
        "distractors": [
            "Approximately 5% to 10% of the volume of the original uncompressed text.",
            "Approximately 150% to 200% of the volume of the original uncompressed text.",
            "Exactly 1% to 2% of the volume of the original uncompressed text."
        ],
        "explanation": "Lecture 3 slide 25: 'Compressed positional index size 35-50% of volume of original text.'"
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "Why does the size of a positional index depend heavily on the average length of documents in the collection?",
        "correct": "A frequent term appears many times in a long document, requiring an entry for every occurrence rather than a single docID.",
        "distractors": [
            "Long documents cause the dictionary hash table to expand exponentially regardless of vocabulary size.",
            "Long documents force the tokenizer to switch from UTF-8 encoding to 32-bit fixed Unicode characters.",
            "Positional offsets cannot be stored in variable-length arrays if a document exceeds 1,000 words."
        ],
        "explanation": "In non-positional indexes, a document generates 1 posting per term regardless of length. In a positional index, each occurrence adds an offset."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "What is the worst-case time complexity of intersecting two positional postings lists for a phrase query across matching documents?",
        "correct": "O(T), where T is the total number of token occurrences of the two terms across all documents in the collection.",
        "distractors": [
            "O(M * log N), where M is vocabulary size and N is total document count.",
            "O(1) constant time, because position offsets are indexed using direct array subscripting.",
            "O(N^3), where N is the total number of documents in the collection."
        ],
        "explanation": "The positional merge compares position lists. In the worst case, every occurrence of both terms across all documents is scanned, which is O(T)."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "What motivated the development of combined indexing schemes (e.g., Williams, Zobel, and Bahle 2004) using both biwords and positional indexes?",
        "correct": "Repeatedly merging long positional postings lists for extremely frequent phrases (e.g., 'The Who', 'New York') is inefficient.",
        "distractors": [
            "Positional indexes cannot be stored on magnetic hard disk drives due to read head seek limitations.",
            "Biword indexes are required by web browsers to display highlighted keyword snippets in search results.",
            "Combining indexes allows search engines to bypass tokenization and character encoding detection entirely."
        ],
        "explanation": "Frequent phrases like 'New York' or 'The Who' have huge positional lists that take long to merge. Precomputing biwords for frequent phrases eliminates this cost."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "In the empirical evaluation by Williams et al. (2004) cited in the slides, how did the combined index perform compared to a pure positional index?",
        "correct": "A typical web query mixture was executed in roughly one-fourth (1/4) of the time required by a pure positional index.",
        "distractors": [
            "The query mixture executed at the exact same speed, but reduced disk storage consumption by 90%.",
            "The query mixture executed 100 times slower due to the overhead of synchronizing two different index structures.",
            "The query mixture executed in half the time, but doubled the error rate on proximity queries."
        ],
        "explanation": "Lecture 3 slide 26: 'Williams et al. (2004) evaluate a more sophisticated mixed indexing scheme... A typical web query mixture was executed in 1/4 the time.'"
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "In a hybrid combination indexing architecture, which types of phrase queries are routed to the biword index rather than the positional index?",
        "correct": "High-frequency, common phrases and idioms that appear frequently in user query logs.",
        "distractors": [
            "Rare, low-frequency phrases that contain misspelled words or unusual foreign terms.",
            "Proximity queries that specify variable distance constraints such as /5 or /10.",
            "Complex Boolean queries that contain negation operators applied to single terms."
        ],
        "explanation": "Common, popular phrases ('Michael Jackson', 'Britney Spears') are answered from biword postings; rare and arbitrary phrases use the positional index."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "To compress the position values within a document's positional postings list, what mathematical encoding strategy is standardly applied?",
        "correct": "Storing successive position differences (gaps or d-gaps) rather than absolute integer offsets from the beginning of the file.",
        "distractors": [
            "Storing IEEE 754 floating-point percentages representing the relative location within the document.",
            "Hashing each position offset using the Soundex phonetic algorithm to reduce integer byte length.",
            "Rounding all position values to the nearest multiple of 100 to eliminate low-order binary bits."
        ],
        "explanation": "Positions within a document are increasing integers. Storing difference gaps (d-gaps) yields small integers that compress efficiently."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "During positional intersection for a phrase query 'w1 w2' within a document, if pos(w1) = 14 and pos(w2) = 8, how should the position pointers advance?",
        "correct": "The pointer in w2's position list is advanced because pos(w2) is less than pos(w1) + 1.",
        "distractors": [
            "The pointer in w1's position list is advanced because pos(w1) is greater than pos(w2).",
            "Both position pointers are advanced simultaneously and document ID is added to the result.",
            "The entire document is immediately discarded from consideration for all subsequent phrase queries."
        ],
        "explanation": "To match 'w1 w2', we need pos(w2) == pos(w1) + 1. Since pos(w2) = 8 < 15, w2 is too early, so w2's pointer must advance."
    },
    {
        "topic": "Positional Indexes & Proximity Queries",
        "question": "Which of the following is NOT an advantage of positional indexes over biword indexes?",
        "correct": "Positional indexes require substantially less total storage space on disk than standard non-positional indexes.",
        "distractors": [
            "Positional indexes support arbitrary phrase queries of any length without vocabulary explosion.",
            "Positional indexes support proximity queries with arbitrary word distance thresholds like /k.",
            "Positional indexes eliminate false positive phrase matches without inspecting original document texts."
        ],
        "explanation": "Positional indexes are 2-4x larger than non-positional indexes; reduced disk storage is definitely NOT an advantage."
    },

    # -------------------------------------------------------------
    # Topic 8: Skip Pointers & Faster Postings Merges (Q112 - Q129)
    # -------------------------------------------------------------
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What is the primary operational motivation for augmenting inverted index postings lists with 'skip pointers'?",
        "correct": "To bypass large sequences of non-matching postings during AND intersections without inspecting every individual element.",
        "distractors": [
            "To allow search engines to traverse postings lists in reverse chronological order during dynamic updates.",
            "To enable instant constant-time O(1) evaluation of Boolean disjunction (OR) queries.",
            "To eliminate the requirement of sorting postings lists by document ID during index construction."
        ],
        "explanation": "Skip pointers provide forward shortcuts in sorted postings lists, allowing the merge algorithm to jump past non-matching docIDs."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What structural property of postings lists is strictly required for skip pointers to function correctly during list intersection?",
        "correct": "The postings list must be sorted in ascending order of document identifiers (docIDs).",
        "distractors": [
            "The postings list must be stored in uncompressed contiguous memory blocks on physical magnetic tape.",
            "The postings list must contain an even number of postings elements to allow symmetrical pointer splits.",
            "The postings list must be stored in a circular linked list that loops back to the dictionary header."
        ],
        "explanation": "Skip pointers rely on monotonic ordering: if the target of a skip pointer is <= the other list's docID, all intermediate elements are also smaller and can be safely skipped."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "During the intersection of list P1 with list P2, when pointer p1 is at node x with a skip pointer pointing to target node y (with docID d_skip), under what condition should the skip pointer be followed?",
        "correct": "If d_skip is less than or equal to the current docID pointed to in P2 (d_skip <= d_p2).",
        "distractors": [
            "If d_skip is strictly greater than the current docID pointed to in P2 (d_skip > d_p2).",
            "If the distance between x and y is exactly equal to the square root of the vocabulary size.",
            "Only when pointer p1 has reached the end of its postings list and must loop back to the beginning."
        ],
        "explanation": "If d_skip <= d_p2, we can jump forward to d_skip without missing any potential match, because all skipped nodes are strictly less than d_p2."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What action is taken by the skip merge algorithm if the skip pointer target docID d_skip is strictly greater than the target docID in P2?",
        "correct": "The algorithm does not follow the skip pointer; it advances pointer p1 normally by one step to its immediate successor.",
        "distractors": [
            "The algorithm immediately terminates the entire merge operation and outputs the current result list.",
            "The algorithm advances pointer p2 to match d_skip, discarding all intermediate postings in P2.",
            "The algorithm inverts the skip pointer to jump backwards to the preceding checkpoint in P1."
        ],
        "explanation": "If d_skip > d_p2, jumping would overshoot the target d_p2 and potentially skip a match. Thus, the skip is NOT taken, and p1 advances normally."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What is the classic heuristic rule of thumb for placing skip pointers in a postings list of length P?",
        "correct": "Place skip pointers at evenly spaced intervals of approximately \\sqrt{P} postings throughout the list.",
        "distractors": [
            "Place skip pointers at intervals of log2(P) postings, starting from the middle of the list.",
            "Place skip pointers exclusively at the first and last postings nodes of every term's list.",
            "Place skip pointers at every posting whose document ID is an even multiple of 1,000."
        ],
        "explanation": "Lecture 3 slide 8: 'Simple heuristic: for postings of length L, use √L evenly-spaced skip pointers.'"
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What is the algorithmic tradeoff between placing too many skip pointers versus placing too few skip pointers in a postings list?",
        "correct": "More skips give shorter spans and higher jump probability but incur pointer comparison overhead; fewer skips check fewer pointers but rarely jump.",
        "distractors": [
            "More skips reduce disk storage consumption, while fewer skips increase CPU register caching efficiency.",
            "More skips allow faster phrase searches, while fewer skips eliminate false positives in biword queries.",
            "More skips prevent memory leaks during sorting, while fewer skips allow dynamic insertions without re-indexing."
        ],
        "explanation": "Lecture 3 slide 7: Tradeoff: More skips -> shorter skip spans => more likely to skip, but lots of pointer comparisons. Fewer skips -> few pointer comparisons, but long spans => few skips."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "For a postings list containing P = 16 entries, what is the suggested skip length under the standard \\sqrt{P} heuristic?",
        "correct": "A skip length of 4 postings between consecutive skip pointers (\\sqrt{16} = 4).",
        "distractors": [
            "A skip length of 8 postings between consecutive skip pointers (16 / 2 = 8).",
            "A skip length of 2 postings between consecutive skip pointers (log2(16) / 2 = 2).",
            "A skip length of 16 postings, meaning only a single skip pointer spans the entire list."
        ],
        "explanation": "Under the heuristic, skip spacing = \\sqrt{16} = 4 postings."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "If a postings list contains P = 10,000 document IDs, how many skip pointers will be created and what will be their spacing under the \\sqrt{P} rule?",
        "correct": "100 skip pointers placed at evenly spaced intervals of 100 postings (\\sqrt{10000} = 100).",
        "distractors": [
            "50 skip pointers placed at intervals of 200 postings throughout the list.",
            "1,000 skip pointers placed at intervals of 10 postings throughout the list.",
            "10 skip pointers placed at intervals of 1,000 postings throughout the list."
        ],
        "explanation": "\\sqrt{10000} = 100. There will be 100 skip pointers, spaced 100 postings apart."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "In Exercise 1 from Lecture 3, intersecting List 1 (with skips) and List 2: List 1 = [3, 5, 9, 15, 24, 39, 60, 68, 75, 81, 84, 89, 92, 96, 97, 100, 115] and List 2 = [3, 5, 89, 95, 97, 99, 100, 101]. How many times was a skip pointer successfully followed?",
        "correct": "Exactly 1 time (the skip pointer from 24 jumped directly to 75).",
        "distractors": [
            "Exactly 4 times (at docIDs 5, 24, 84, and 97).",
            "Exactly 0 times (all skip targets overshot the current target in List 2).",
            "Exactly 8 times (at every evenly spaced interval of length 4)."
        ],
        "explanation": "Lecture 3 slide 10 explicitly gives the solution: 'A. How often is a skip pointer followed? 1 time, 24->75'."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "In the same Lecture 3 Exercise 1, how many total postings comparisons were made by the algorithm using skip pointers versus without skip pointers?",
        "correct": "18 comparisons with skip pointers versus 19 comparisons without skip pointers.",
        "distractors": [
            "8 comparisons with skip pointers versus 34 comparisons without skip pointers.",
            "12 comparisons with skip pointers versus 12 comparisons without skip pointers.",
            "25 comparisons with skip pointers versus 15 comparisons without skip pointers."
        ],
        "explanation": "Lecture 3 slide 10 solution: 'B. How many comparisons with skip pointers? 18. C. Comparisons without skip pointers? 19.'"
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "In Lecture 3 Exercise 2, a 16-entry list [4,6,10,12,14,16,18,20,22,32,47,81,120,122,157,180] is intersected with the single-entry list [47]. How many comparisons are made using standard linear merge without skips?",
        "correct": "11 comparisons (evaluating elements from 4 up through 47 sequentially).",
        "distractors": [
            "16 comparisons (scanning through all elements to the end of the list).",
            "5 comparisons (skipping all even numbers smaller than 47).",
            "1 comparison (directly indexing the element at offset 47)."
        ],
        "explanation": "In standard linear merge, the pointer checks 4, 6, 10, 12, 14, 16, 18, 20, 22, 32, 47 against 47. This is exactly 11 comparisons."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "Why are skip pointers ineffective and unused for processing Boolean disjunction queries of the form 'TermX OR TermY'?",
        "correct": "In an OR query, every document ID from both lists must be included in the union; skipping elements would cause missing results.",
        "distractors": [
            "Boolean OR queries cannot be evaluated on sorted postings lists using two-pointer algorithms.",
            "The union of two postings lists automatically inverts the direction of all internal memory pointers.",
            "Operating systems do not permit skip pointers to be read during disjunctive database operations."
        ],
        "explanation": "In an OR query (union), every document in both lists must be retained. Skipping elements would omit valid documents from the search result."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "Why does maintaining skip pointers become problematic in dynamic search environments where documents are frequently added or deleted?",
        "correct": "Adding or deleting postings changes list lengths, corrupting fixed \\sqrt{P} spacing and requiring expensive pointer restructuring.",
        "distractors": [
            "Dynamic documents force the search engine to convert all postings into uncompressed incidence matrices.",
            "The operating system file system automatically deletes skip pointers when files are modified on disk.",
            "Dynamic updates cause docIDs to be assigned in reverse order, breaking the sorted list prerequisite."
        ],
        "explanation": "Lecture 3 slide 8: 'Easy if the index is relatively static; harder if L keeps changing because of updates.'"
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What did empirical research by Bahle et al. (2002) demonstrate regarding skip pointers on modern computing hardware?",
        "correct": "The extra I/O cost of loading a larger index containing skip pointers from disk can outweigh in-memory CPU merge savings.",
        "distractors": [
            "Modern 64-bit CPU architectures cannot execute pointer comparison instructions without pipeline stalls.",
            "Skip pointers cause unrecoverable hardware faults when executed across multi-core processors.",
            "Memory bus bandwidth is so slow that linear scans are 1,000 times faster than pointer jumps in RAM."
        ],
        "explanation": "Lecture 3 slide 8: 'The I/O cost of loading a bigger postings list can outweigh the gains from quicker in memory merging! (Bahle et al. 2002)'"
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "What theoretical guarantee is provided by multilevel skip lists (Pugh 1990) when applied to search structures?",
        "correct": "They provide O(log N) search and merge efficiency comparable to balanced binary search trees while retaining simple list structures.",
        "distractors": [
            "They eliminate the need for storing term strings in the dictionary by encoding words into pointer addresses.",
            "They guarantee that every postings list occupies exactly 64 bytes of memory regardless of document count.",
            "They allow postings lists to be searched without loading any document identifiers into main memory."
        ],
        "explanation": "Lecture 3 slide 27: 'Skip Lists theory: Pugh (1990). Multilevel skip lists give same O(log n) efficiency as trees.'"
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "Why is placing skips strictly based on the \\sqrt{P} heuristic considered 'query-blind'?",
        "correct": "It spaces pointers uniformly based on list length alone, ignoring actual query term co-occurrence and access patterns.",
        "distractors": [
            "It places skip pointers exclusively on stop words while ignoring high-value domain terminology.",
            "It requires the user to manually specify the skip interval when typing a search query into the engine.",
            "It assumes all documents in the collection contain the exact same number of distinct words."
        ],
        "explanation": "Lecture 3 slide 8 notes: 'This ignores the distribution of query terms.' It spaces skips purely based on list length L."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "Why do intermediate result lists generated during multi-term conjunction evaluation (e.g. intermediate = P1 AND P2) typically lack skip pointers?",
        "correct": "Generating skip pointers dynamically for ephemeral intermediate results in memory would incur more overhead than it saves.",
        "distractors": [
            "Intermediate result lists are stored on magnetic disk where skip pointers are physically illegal.",
            "Intermediate results are always stored in binary incidence vectors where skip pointers cannot exist.",
            "Intermediate lists are automatically deleted by the query optimizer before the next merge begins."
        ],
        "explanation": "Intermediate postings lists are created on the fly in memory and immediately merged with the next list; adding skip pointers dynamically is not worth the CPU cost."
    },
    {
        "topic": "Skip Pointers & Faster Postings Merges",
        "question": "Which of the following is NOT an advantage of adding skip pointers to an inverted index?",
        "correct": "They reduce the total amount of disk and memory storage space required to store the postings lists.",
        "distractors": [
            "They significantly reduce the number of postings comparisons required to intersect long and short lists.",
            "They allow the merge algorithm to bypass large contiguous blocks of non-matching document identifiers.",
            "They preserve linear worst-case performance bounds while offering substantial sub-linear average-case speedups."
        ],
        "explanation": "Skip pointers add extra pointer and docID data to the index, increasing storage space rather than reducing it."
    }
]
