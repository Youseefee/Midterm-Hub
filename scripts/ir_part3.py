# Part 3: Questions 130 to 200
# Topics:
# 9. Document Parsing & Character Encodings (Q130 to Q142)
# 10. Tokenization Challenges & Multi-language Processing (Q143 to Q160)
# 11. Stop Words & Vocabulary Management (Q161 to Q172)
# 12. Normalization, Equivalence Classes & Soundex (Q173 to Q186)
# 13. Stemming & Lemmatization (Q187 to Q200)

part3_questions = [
    # -------------------------------------------------------------
    # Topic 9: Document Parsing & Character Encodings (Q130 - Q142)
    # -------------------------------------------------------------
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "In the indexing pipeline described in Lecture 5, what is the very first task required before tokenization can begin?",
        "correct": "Obtaining the character sequence from the raw document byte stream by decoding its file format and character set.",
        "distractors": [
            "Stripping all stop words from the dictionary and sorting the vocabulary in alphabetical order.",
            "Generating extended biword tokens and tagging parts of speech across the document sentences.",
            "Constructing a term-document incidence matrix and verifying its percentage of zero cells."
        ],
        "explanation": "Lecture 5 slide 9: '1. Obtaining the character sequence in a document'. Before tokenization, raw bytes must be decoded into characters."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "Why is determining document format (e.g., PDF, Word, Excel, HTML) treated as a classification problem in document parsing?",
        "correct": "Real-world files often lack correct file extensions or MIME headers, requiring content heuristics to choose the right parser.",
        "distractors": [
            "Different file formats use fundamentally different mathematical definitions of document frequency (df).",
            "Operating systems prohibit search engines from reading files unless their binary schemas are converted to SQL tables.",
            "Each document format requires a dedicated physical hard drive partition to allow postings list sorting."
        ],
        "explanation": "Lecture 5 slide 10 notes that determining format, language, and character set are classification problems, often resolved heuristically."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "How does the Unicode character encoding standard resolve the historical limitations of 7-bit ASCII and 8-bit ISO 8859 standards?",
        "correct": "It provides a unified, universal repertoire capable of encoding virtually all written characters and scripts across world languages.",
        "distractors": [
            "It compresses all text characters into single binary bits to allow instant incidence matrix processing.",
            "It eliminates the need for tokenization by inserting explicit word boundary markers between all characters.",
            "It restricts character sets to English and Western European languages to prevent vocabulary explosion."
        ],
        "explanation": "Unicode provides a universal character set mapping code points for all world languages, eliminating the fragmentation of legacy ASCII and ISO 8859 encodings."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "What is the primary operational advantage of UTF-8 compared to UTF-16 and UTF-32 in web text indexing?",
        "correct": "It is backward compatible with 7-bit ASCII and uses variable-length byte encoding (1-4 bytes), saving space on Western text.",
        "distractors": [
            "It uses a fixed width of 32 bits per character, ensuring constant-time random access to any character offset.",
            "It automatically stems English words during the byte decoding phase before tokens reach the indexer.",
            "It eliminates all non-printable control characters and punctuation symbols directly at the hardware layer."
        ],
        "explanation": "UTF-8 encodes ASCII characters in 1 byte (100% backward compatible) and uses up to 4 bytes for other scripts, saving massive storage over fixed-width schemes."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "What is a Byte Order Mark (BOM) in character stream parsing, and what is its purpose?",
        "correct": "A specific magic byte sequence at the file start indicating Unicode encoding and byte endianness (big-endian vs little-endian).",
        "distractors": [
            "A marker indicating the end of a document's postings list used to signal early termination during merges.",
            "A cryptographic checksum used to verify that no copyright-protected terms are indexed into the dictionary.",
            "A special punctuation token emitted by the tokenizer to separate sentences during proximity searches."
        ],
        "explanation": "A BOM (e.g. 0xFEFF) indicates that the text stream is Unicode and reveals the byte order (endianness) used in UTF-16 or UTF-32."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "Why must language identification be performed during or immediately after character decoding in the indexing pipeline?",
        "correct": "Subsequent tokenization, stop word filtering, and stemming rules are fundamentally language-specific.",
        "distractors": [
            "Modern search engines can only index documents written in the official language of the hosting server country.",
            "Language detection is required to determine whether docIDs should be assigned in ascending or descending order.",
            "Inverted indexes cannot store terms from different languages within the same physical postings list file."
        ],
        "explanation": "Lecture 5 slide 33: Tokenization, normalization, and stemming are language-specific transformations. The system must know the language to choose the right tools."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "What complication arises in document parsing when handling a document such as a French email with an attached German PDF report?",
        "correct": "The parsing pipeline must segment the document into distinct linguistic zones and apply different language-specific modules.",
        "distractors": [
            "The indexer must discard the entire document because inverted indexes cannot process multilingual content.",
            "The German attachment must be translated into French using machine translation before tokens can be emitted.",
            "The system must convert all German nouns into French extended biwords to preserve grammatical consistency."
        ],
        "explanation": "Lecture 5 slide 11: 'Complications: French email with a German pdf attachment.' Different parts of a document may require different parsers and tokenizers."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "In IR system architecture, what is meant by the 'granularity' or definition of a 'document unit'?",
        "correct": "Deciding the physical scope of what constitutes an individual searchable document (e.g., a book vs a chapter vs a page).",
        "distractors": [
            "Deciding whether the dictionary should be stored in volatile RAM or on persistent flash memory.",
            "Determining the maximum number of skip pointers permitted in a postings list of length P.",
            "Measuring the clock frequency of the processor registers executing the linear merge algorithm."
        ],
        "explanation": "Lecture 5 slide 11: 'What is a unit document?' (e.g., an entire book, a chapter, a single paragraph, or a web page)."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "What is the primary tradeoff between choosing small document units (e.g., individual paragraphs) versus large document units (e.g., entire books)?",
        "correct": "Small units improve precision and snippet generation but inflate index size; large units capture broad context but harm precision.",
        "distractors": [
            "Small units eliminate the need for tokenization, while large units eliminate the need for skip pointers.",
            "Small units prevent the calculation of term frequencies, while large units cause memory bus overflow in RDBMS.",
            "Small units force queries to use Boolean disjunction, while large units restrict searches to single keywords."
        ],
        "explanation": "Smaller document units locate exact matches and provide concise snippets, but produce more documents (larger postings). Larger units lose precision."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "What happens to retrieval effectiveness if a document encoded in UTF-8 is erroneously decoded as ISO-8859-1 (Latin-1)?",
        "correct": "Multi-byte characters become garbled mojibake, creating corrupted terms that will never match legitimate user queries.",
        "distractors": [
            "The document will be indexed correctly because modern stemmers automatically correct character encoding errors.",
            "The inverted index will automatically duplicate the document's postings list across all dictionary entries.",
            "The query optimizer will treat the corrupted characters as skip pointers, causing rapid merge termination."
        ],
        "explanation": "Decoding UTF-8 as Latin-1 turns multi-byte sequences into garbled characters (mojibake), meaning the indexed terms won't match queries."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "When parsing HTML or XML documents, what is the architectural benefit of retaining tags as zone metadata rather than stripping them entirely?",
        "correct": "It enables semi-structured parametric searches, allowing users to query specific fields such as <title> or <author>.",
        "distractors": [
            "It prevents the dictionary from storing terms that contain vowel characters in their spellings.",
            "It reduces the total postings list length by converting all HTML tags into binary incidence vectors.",
            "It eliminates the requirement of running the Porter stemmer on body paragraph text tokens."
        ],
        "explanation": "Retaining structural tags as metadata zones allows parametric and field-restricted searches (e.g. title:search author:Manning)."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "Which component in the basic indexing pipeline is directly responsible for converting raw byte streams into clean character text?",
        "correct": "The document parser and character decoder.",
        "distractors": [
            "The linguistic preprocessor.",
            "The postings list sorter.",
            "The positional merge engine."
        ],
        "explanation": "The document parser handles format detection and character decoding, producing the sequence of characters that is passed to the tokenizer."
    },
    {
        "topic": "Document Parsing & Character Encodings",
        "question": "Which of the following is NOT an inherent challenge during the document parsing phase of an IR system?",
        "correct": "Balancing answer index positions to ensure uniform distribution across multiple-choice questions.",
        "distractors": [
            "Accurately detecting the character encoding of a file when no HTTP headers or BOMs are present.",
            "Extracting clean text from proprietary binary file formats like Microsoft Word or Adobe PDF.",
            "Identifying the correct natural language of short text fragments with mixed linguistic vocabulary."
        ],
        "explanation": "Encoding detection, binary format extraction, and language identification are all major document parsing challenges."
    },

    # -------------------------------------------------------------
    # Topic 10: Tokenization Challenges & Multi-language Processing (Q143 - Q160)
    # -------------------------------------------------------------
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "In the formal indexing pipeline, what is the precise definition of a 'token'?",
        "correct": "An instance of a sequence of characters in a particular document that are grouped together as a useful semantic unit.",
        "distractors": [
            "An alphabetical entry in the system dictionary containing an accumulated document frequency count.",
            "A 32-bit unique numerical identifier assigned to each distinct document in the collection.",
            "A skip pointer attached to a postings node indicating the memory offset of a future document."
        ],
        "explanation": "Lecture 5 slide 13: 'A token is an instance of a sequence of characters in a particular document that are grouped together as a useful semantic unit for processing.'"
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "What is the relationship between a 'token' and an 'indexing term'?",
        "correct": "A token is an extracted raw surface instance, while a term is a normalized word type entered into the dictionary.",
        "distractors": [
            "A token is stored permanently on disk, while a term is an ephemeral variable discarded after sorting.",
            "Tokens exist only in spoken language search, while terms exist only in written document retrieval.",
            "A token represents a complete phrase query, while a term represents a single character encoding byte."
        ],
        "explanation": "A token is an occurrence of a word in text. A term is a normalized word type that serves as a dictionary entry."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Why is naive whitespace splitting (e.g. splitting text on space characters) insufficient for robust text tokenization?",
        "correct": "It fails on punctuation, apostrophes, hyphenated compounds, phone numbers, and languages that do not use spaces.",
        "distractors": [
            "It requires O(N^2) time complexity, making it too computationally expensive for modern microprocessors.",
            "It automatically converts all uppercase letters to lowercase, destroying acronym distinctions.",
            "It prevents the indexer from assigning sequential document identifiers to collected text files."
        ],
        "explanation": "Whitespace splitting cannot handle punctuation attached to words, contractions, hyphens, numbers, or unsegmented scripts like Chinese."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "In the sentence 'Mr. O'Neill thinks that the boy's stories aren't amusing', why does tokenizing apostrophes pose a dilemma?",
        "correct": "Apostrophes represent diverse linguistic functions: proper name prefixes (O'Neill), possession (boy's), and contractions (aren't).",
        "distractors": [
            "Apostrophes cause variable-length arrays to overflow their allocated memory buffers during index construction.",
            "Inverted indexes cannot store punctuation characters within dictionary entries under any circumstance.",
            "The Porter stemmer crashes if a word containing an apostrophe is passed to Phase 1 reduction rules."
        ],
        "explanation": "Lecture 5 slide 15: Apostrophes can indicate a name (O'Neill), possessive (boy's), or contraction (aren't), each requiring different tokenization."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "What trade-off occurs when tokenizing hyphenated sequences such as 'state-of-the-art' or 'Hewlett-Packard'?",
        "correct": "Splitting on hyphens loses multi-word entity identity, but keeping them whole prevents matching individual component words.",
        "distractors": [
            "Splitting on hyphens doubles dictionary memory size, while keeping them whole eliminates all postings lists.",
            "Keeping hyphens whole causes search engines to treat the words as negative Boolean NOT constraints.",
            "Hyphenated terms cannot be sorted alphabetically in the dictionary because hyphens lack ASCII codes."
        ],
        "explanation": "Lecture 5 slide 16: If you split on hyphens, queries for 'state-of-the-art' lose compound identity; if you don't split, users searching for 'Hewlett' won't match."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Why can indiscriminately discarding all punctuation and hyphens during tokenization severely degrade search effectiveness for technical queries?",
        "correct": "It destroys critical identifiers such as model numbers (B-52, F-16), programming languages (C++), and IP addresses.",
        "distractors": [
            "It causes the postings merge algorithm to take quadratic time O(x * y) for all subsequent Boolean queries.",
            "It forces the dictionary to store terms using 64-bit floating-point numbers rather than strings.",
            "It prevents the web crawler from downloading files that contain numeric characters in their URLs."
        ],
        "explanation": "Lecture 5 slide 17: Stripping punctuation destroys essential terms like B-52, C++, 192.168.1.1, PGP keys, and error codes."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "How has the treatment of numbers in IR tokenization shifted from legacy systems to modern search engines?",
        "correct": "Older systems often ignored numbers to save space; modern systems index them because users frequently search dates, codes, and IDs.",
        "distractors": [
            "Older systems indexed all numbers, whereas modern systems delete all numeric tokens to optimize vector ranking.",
            "Modern systems convert all numbers into written English words (e.g., '55' converted to 'fifty-five') before indexing.",
            "Modern systems only index numbers if they appear inside mathematical formulas or financial spreadsheet cells."
        ],
        "explanation": "Lecture 5 slide 17: 'Older IR systems may not index numbers. But often very useful: think about things like looking up error codes/stacktraces on the web.'"
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Why do date expressions such as '3/20/91', 'Mar. 20, 1991', and '20/3/91' require specialized tokenization and normalization?",
        "correct": "They represent the same calendar entity using disparate surface punctuation, orderings, and textual abbreviations.",
        "distractors": [
            "Date expressions automatically trigger Boolean negation operators if they contain forward slash characters.",
            "Inverted indexes cannot store numeric values alongside alphabetical terms within the same dictionary.",
            "Date expressions must be converted into Unix epoch timestamps to allow linear postings list merging."
        ],
        "explanation": "Dates appear in many different formats and notations across countries; normalizing them ensures a query matches documents regardless of notation."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Why does tokenizing German text require a specialized compound splitter (decompounding module)?",
        "correct": "German forms long compound nouns without spaces (e.g. Lebensversicherungsgesellschaftsangestellter) that must be split to match component queries.",
        "distractors": [
            "German text is written from right to left, requiring character reversing before standard whitespace splitting.",
            "German nouns do not have grammatical gender, making standard part-of-speech tagging mathematically impossible.",
            "German words cannot be stemmed using rule-based algorithms due to strict European copyright legislation."
        ],
        "explanation": "Lecture 5 slide 18: German noun compounds are not segmented with spaces (e.g. 'life insurance company employee'). Without decompounding, queries for 'insurance' fail to match."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "What fundamental orthographic characteristic makes tokenizing Chinese text significantly more complex than English?",
        "correct": "Chinese text is written as a continuous stream of ideographic characters without spaces between adjacent words.",
        "distractors": [
            "Chinese text contains no vowel characters, requiring phonetic soundex translation before tokenization.",
            "Chinese characters cannot be represented in Unicode and must be encoded using 7-bit ASCII approximations.",
            "Chinese sentences do not use grammatical verbs, preventing the extraction of valid indexing terms."
        ],
        "explanation": "Lecture 5 slide 19: Chinese has no spaces between words. Word segmentation algorithms must be used to group characters into words."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Why can word segmentation in Chinese lead to retrieval errors if performed naively?",
        "correct": "Character sequences can often be segmented in multiple valid ways, producing completely different word meanings.",
        "distractors": [
            "Inverted indexes cannot store non-alphabetic character sets without corrupting skip pointer offsets.",
            "Different segmentations cause the operating system to allocate fixed-size postings lists of zero length.",
            "Chinese characters change their visual glyph shapes depending on whether they appear in titles or body text."
        ],
        "explanation": "Lecture 5 slide 19: 'Not always guaranteed a unique tokenization'. Character combinations can form different words depending on where boundaries are placed."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Which four distinct writing systems are intermingled in standard Japanese text, complicating the tokenization process?",
        "correct": "Kanji, Hiragana, Katakana, and Romaji.",
        "distractors": [
            "Cyrillic, Greek, Latin, and Arabic.",
            "Pinyin, Bopomofo, Hangul, and Hanzi.",
            "Cuneiform, Hieroglyphics, Phoenician, and Aramaic."
        ],
        "explanation": "Lecture 5 slide 19: Japanese text intermingles Kanji (Chinese ideographs), Hiragana (grammatical inflections), Katakana (loanwords), and Romaji (Latin script)."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "In Japanese text processing, what is Katakana primarily used for, and how does it impact tokenization?",
        "correct": "It is used for foreign loan words and names; words may have multiple transliterated spelling variants that need normalization.",
        "distractors": [
            "It is used exclusively for grammatical sentence particles and is discarded as stop words in every search engine.",
            "It represents mathematical formulas and numbers, which are indexed into a separate numeric database.",
            "It is written vertically from right to left, requiring image rotation filters before character decoding."
        ],
        "explanation": "Katakana is used for foreign loanwords and names, where phonetic transliteration often leads to multiple alternate spellings for the same word."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "What bidirectional text challenge is encountered when tokenizing Arabic or Hebrew documents?",
        "correct": "Text is written primarily right-to-left, but numerals and embedded Latin phrases are written left-to-right.",
        "distractors": [
            "Text alternate direction on every second line (boustrophedon), requiring line inversion filters.",
            "Characters are stored backwards on disk and must be sorted alphabetically before byte extraction.",
            "Punctuation marks are placed at the beginning of words rather than at sentence boundaries."
        ],
        "explanation": "Lecture 5 slide 20: Arabic is written right-to-left, but items like numbers are written left-to-right, requiring bidirectional handling."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "What linguistic feature of Arabic creates major challenges for word-level tokenization?",
        "correct": "Prepositions, conjunctions, and articles (clitics like wa-, bi-, al-) attach directly to base words as prefixes and suffixes.",
        "distractors": [
            "Arabic words never exceed three characters in length, causing extreme dictionary hash collisions.",
            "Arabic sentences omit all consonants, requiring the indexer to guess root meanings phonetically.",
            "Arabic verbs do not conjugate, forcing search engines to rely entirely on biword indexes."
        ],
        "explanation": "In Arabic, grammatical clitics (articles like 'al-', conjunctions like 'wa-', prepositions like 'bi-') attach directly to words, requiring morphological segmentation."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "How do Arabic letterforms behave visually and computationally within words?",
        "correct": "Letters form complex ligatures where character glyph shapes change dramatically depending on their position (initial, medial, final).",
        "distractors": [
            "Letters are separated by fixed-width whitespace, allowing naive single-character tokenization.",
            "Characters are represented by 16-bit soundex codes that cannot be decoded into standard Unicode.",
            "Letters change their alphabetical order dynamically based on the document frequency of the word."
        ],
        "explanation": "Lecture 5 slide 20: 'Words are separated, but letter forms within a word form complex ligatures' depending on whether they are initial, medial, final, or isolated."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "What is the cardinal rule regarding the relationship between the document indexing tokenizer and the query tokenizer?",
        "correct": "The exact same tokenization rules and linguistic filters MUST be applied to both indexed documents and user queries.",
        "distractors": [
            "The query tokenizer should apply more aggressive stop word removal than the document indexing tokenizer.",
            "The document tokenizer must preserve all punctuation, while the query tokenizer must strip all non-alphanumeric chars.",
            "The query tokenizer must run in constant time O(1), while the document tokenizer can run in exponential time."
        ],
        "explanation": "Lecture 5 slide 24: 'Crucial: Need to \"normalize\" indexed text as well as query terms into the same form'. If rules differ, terms won't match."
    },
    {
        "topic": "Tokenization Challenges & Multi-language Processing",
        "question": "Which of the following is NOT a recognized challenge in modern text tokenization?",
        "correct": "Inverted indexes requiring terms to have exactly eight characters to match hardware bus widths.",
        "distractors": [
            "Handling web-specific tokens like email addresses, URLs, Twitter hashtags, and domain names.",
            "Deciding whether compound words like 'lowercase' and 'lower-case' should map to the same term.",
            "Segmenting continuous character streams in languages that do not separate words with spaces."
        ],
        "explanation": "Hardware bus width has no bearing on token length. URLs, hyphens, and whitespace-free scripts are authentic tokenization challenges."
    },

    # -------------------------------------------------------------
    # Topic 11: Stop Words & Vocabulary Management (Q161 - Q172)
    # -------------------------------------------------------------
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "What is the formal definition of a 'stop word' in classical Information Retrieval?",
        "correct": "An extremely high-frequency word that carries minimal semantic content or discriminative value (e.g., 'the', 'is', 'at').",
        "distractors": [
            "A misspelled word that causes syntax errors when parsed by a Boolean query optimizer.",
            "A word that appears in only one document in the entire corpus, contributing to matrix sparsity.",
            "A foreign-language term that lacks a direct translation in the system's primary language dictionary."
        ],
        "explanation": "Lecture 5 slide 21: Stop words are common words excluded because 'they have little semantic content: the, a, and, to, be'."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "According to the empirical statistics cited in Lecture 5, what proportion of all text tokens is accounted for by the top 30 stop words?",
        "correct": "The top 30 most common words account for approximately 30% of all token occurrences in a typical collection.",
        "distractors": [
            "The top 30 most common words account for less than 1% of all token occurrences in a collection.",
            "The top 30 most common words account for approximately 80% of all token occurrences in a collection.",
            "The top 30 most common words account for exactly 50% of the distinct terms in the vocabulary."
        ],
        "explanation": "Lecture 5 slide 21: 'There are a lot of them: ~30% of postings for top 30 words'."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "Why did early information retrieval systems almost universally remove stop words using pre-compiled stop lists?",
        "correct": "Eliminating stop words saved massive disk storage space (~30%) and drastically reduced postings list merge times.",
        "distractors": [
            "Early computer hardware could not store words containing fewer than four alphabetical characters.",
            "Stop words caused mathematical division-by-zero errors in early vector space ranking equations.",
            "International copyright laws prohibited the commercial storage of common English function words."
        ],
        "explanation": "Because top stop words account for ~30% of postings, eliminating them reduced index size by ~30% and sped up queries on early hardware."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "What is the prevailing trend in modern web search engines regarding the use of stop lists?",
        "correct": "Modern search engines generally do NOT drop stop words; they keep them indexed in the inverted index.",
        "distractors": [
            "Modern search engines expand stop lists to include over 10,000 common words to minimize RAM usage.",
            "Modern engines replace all stop words with random numeric hashes to obfuscate document contents.",
            "Modern engines only index stop words if they appear inside quotation marks in document titles."
        ],
        "explanation": "Lecture 5 slide 21: 'But the trend is away from doing this'. Modern search engines retain stop words to support phrases and precise queries."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "What technological advancement in index storage made indexing stop words practical and cost-effective?",
        "correct": "Sophisticated postings compression techniques make the physical storage cost for common words negligible.",
        "distractors": [
            "Magnetic hard drives were replaced with cloud tape archives that have infinite data storage capacity.",
            "Modern operating systems compress ASCII text into binary incidence vectors at the hardware level.",
            "Stop word postings lists are stored in CPU L1 cache, eliminating the need for persistent disk storage."
        ],
        "explanation": "Lecture 5 slide 21: 'Good compression techniques (Ch. 5) means the space for including stopwords in a system is very small'."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "How do modern query optimizers mitigate the performance penalty of including stop words in the index during query execution?",
        "correct": "They process selective terms first, pruning candidates so that stop word postings lists need only be touched for tiny candidate sets.",
        "distractors": [
            "They automatically convert all stop words into wildcards that match any arbitrary character string.",
            "They evaluate stop words using linear grep scans across raw documents rather than accessing inverted lists.",
            "They cap the number of postings comparisons to 10 regardless of the actual length of the stop word list."
        ],
        "explanation": "Lecture 5 slide 21: 'Good query optimization techniques (Ch. 7) mean you pay little at query time for including stop words.'"
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "If an IR system completely excludes stop words from its index, what happens when a user searches for 'To be or not to be'?",
        "correct": "All four words are stripped, leaving an empty query that returns zero results or causes an execution error.",
        "distractors": [
            "The search engine automatically translates the phrase into French and searches for 'Être ou ne pas être'.",
            "The engine returns all documents in the corpus because an empty query matches every document ID.",
            "The system converts the phrase into a biword index query matching 'to be' and 'not to'."
        ],
        "explanation": "In 'To be or not to be', every word is a stop word. Stripping stop words leaves an empty query, returning nothing."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "Which of the following popular queries would suffer severe precision loss or complete failure if common stop words were dropped?",
        "correct": "Famous titles such as 'The Who', 'Take That', and 'Let It Be'.",
        "distractors": [
            "Technical terms such as 'electromagnetism' and 'photosynthesis'.",
            "Proper names such as 'William Shakespeare' and 'Julius Caesar'.",
            "Numerical queries such as error code 'HTTP 404' or year '1999'."
        ],
        "explanation": "Lecture 5 slide 21: 'You need them for phrase queries: \"King of Denmark\", various song titles, etc.: \"Let it be\", \"To be or not to be\".'"
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "In the query 'flights to London' versus 'flights from London', why is preserving the stop words 'to' and 'from' vital?",
        "correct": "The prepositions define the essential relational semantics; stripping them makes both queries identical to 'flights London'.",
        "distractors": [
            "The words 'to' and 'from' are used by the tokenizer to identify the currency format of ticket prices.",
            "Without prepositions, the postings merge algorithm cannot sort document IDs in ascending order.",
            "The query optimizer requires prepositions to assign skip pointers to intermediate result lists."
        ],
        "explanation": "Lecture 5 slide 21: Stop words are needed for '\"Relational\" queries: \"flights to London\"' vs 'flights from London'."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "In classical IR literature, what was the typical size range of a standard general-purpose English stop list?",
        "correct": "Between 30 and 150 words (sometimes extending to several hundred words in aggressive stop lists).",
        "distractors": [
            "Between 2 and 5 words exclusively (only 'the', 'a', and 'and').",
            "Between 5,000 and 10,000 words, covering all common nouns and adjectives.",
            "Exactly 1,000,000 words to match the document count of the standard corpus."
        ],
        "explanation": "Standard stop lists in IR traditionally contained 30 to 150 high-frequency grammatical function words."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "How do modern search engines typically handle stop words when a user submits an unquoted query like 'hotel in Paris'?",
        "correct": "They index 'in', but during unquoted ranking they weight 'hotel' and 'Paris' heavily while treating 'in' with low weight.",
        "distractors": [
            "They immediately delete 'hotel' and 'Paris' and retrieve all documents containing the word 'in'.",
            "They reject the query and prompt the user to re-enter search terms without prepositional stop words.",
            "They translate 'in' into an extended biword and execute a positional proximity search of width 1."
        ],
        "explanation": "Stop words are indexed, but their low idf gives them low score weight in unquoted bag-of-words ranking unless a phrase query is specified."
    },
    {
        "topic": "Stop Words & Vocabulary Management",
        "question": "Which of the following is NOT a valid justification for retaining stop words in a modern search index?",
        "correct": "Stop words have high inverse document frequency (idf) and provide the strongest discriminative power between documents.",
        "distractors": [
            "Removing stop words prevents users from searching for famous literary quotes, movie titles, and band names.",
            "High-performance index compression algorithms have made the storage overhead of stop words negligible.",
            "Relational queries relying on prepositions (such as destinations versus origins) require stop words to convey meaning."
        ],
        "explanation": "Stop words appear in almost all documents, so they have very LOW inverse document frequency (idf), NOT high idf."
    },

    # -------------------------------------------------------------
    # Topic 12: Normalization, Equivalence Classes & Soundex (Q173 - Q186)
    # -------------------------------------------------------------
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "What is the primary objective of 'normalization' in the text preprocessing pipeline?",
        "correct": "To map linguistic variants of words and query terms into identical canonical forms so that they match during retrieval.",
        "distractors": [
            "To compress postings integer lists into variable-byte encoded disk blocks.",
            "To calculate the term frequency and inverse document frequency weights for all documents.",
            "To translate all foreign-language document texts into standard American English."
        ],
        "explanation": "Lecture 5 slide 22: 'We need to normalize words in indexed text as well as query words into the same form... to match U.S.A. and USA.'"
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "What is a 'term' in information retrieval terminology?",
        "correct": "A normalized word type that serves as an entry in the IR system dictionary.",
        "distractors": [
            "An unparsed sequence of bytes read from a raw binary document file.",
            "A document serial number stored inside an inverted postings list.",
            "A skip pointer indicating the memory address of an intermediate merge list."
        ],
        "explanation": "Lecture 5 slide 22: 'A term is a (normalized) word type, which is an entry in our IR system dictionary.'"
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "How does the 'equivalence class' method achieve normalization between surface forms such as 'U.S.A.' and 'USA'?",
        "correct": "It defines a mapping where both forms are reduced to a single canonical term (e.g., 'usa') in both document index and queries.",
        "distractors": [
            "It creates two separate dictionary entries and duplicates the postings list under both headings.",
            "It stores both forms in an auxiliary biword index and links them via skip pointers.",
            "It deletes both forms from the index and prompts the user to type 'United States' instead."
        ],
        "explanation": "Lecture 5 slide 22: We define equivalence classes of terms, mapping 'U.S.A.' and 'USA' to the same dictionary headword."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "When normalizing French words like 'résumé' versus 'resume', or German umlauts like 'Tübingen' versus 'Tuebingen', what is the most important criterion?",
        "correct": "Aligning normalization with how users actually formulate queries, since users frequently omit accents in search boxes.",
        "distractors": [
            "Strictly adhering to 18th-century classical linguistic grammar rules regardless of user behavior.",
            "Ensuring that all accented characters are converted into 32-bit floating-point numeric codes.",
            "Converting all accented vowels into stop words to prevent vocabulary explosion in the dictionary."
        ],
        "explanation": "Lecture 5 slide 23: 'Most important criterion: How are your users likely to write their queries for these words? Even in languages that standardly have accents, users often may not type them.'"
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "As an alternative to equivalence classing, what does 'asymmetric expansion' do when a user searches for 'window'?",
        "correct": "The document index remains unmerged, but the query 'window' is expanded to search for 'window OR windows'.",
        "distractors": [
            "The search engine deletes the document postings list for 'window' and re-indexes the corpus dynamically.",
            "The query is converted into a biword search for 'window window' across all indexed documents.",
            "The system restricts search results exclusively to documents that contain uppercase 'Windows'."
        ],
        "explanation": "Lecture 5 slide 26: 'An alternative to equivalence classing is to do asymmetric expansion: Enter: window -> Search: window, windows; Enter: Windows -> Search: Windows.'"
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "What is the primary trade-off of asymmetric query expansion compared to symmetric equivalence classing?",
        "correct": "Asymmetric expansion offers greater precision and flexibility, but increases query processing complexity and execution time.",
        "distractors": [
            "Asymmetric expansion requires 10 times more disk space to store postings lists than equivalence classes.",
            "Asymmetric expansion prevents the use of two-pointer linear merge algorithms for Boolean conjunction.",
            "Equivalence classes can only be implemented in relational databases, while asymmetric expansion requires grep."
        ],
        "explanation": "Lecture 5 slide 26: Asymmetric expansion is 'potentially more powerful, but less efficient' because queries become multi-term disjunctions."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "What does 'case folding' refer to in the text normalization pipeline?",
        "correct": "Converting all alphabetical characters in tokens and queries to lowercase.",
        "distractors": [
            "Compressing long variable-length character strings into 16-bit integer hashes.",
            "Merging uppercase and lowercase postings lists into a single binary incidence matrix.",
            "Folding adjacent sentences into single document paragraphs during parsing."
        ],
        "explanation": "Lecture 5 slide 25: 'Case folding: Reduce all letters to lower case'."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "Why can aggressive, unconditional case folding degrade search precision?",
        "correct": "It conflates proper nouns, acronyms, and common words (e.g., 'Bush' vs 'bush', 'Fed' vs 'fed', 'SAIL' vs 'sail').",
        "distractors": [
            "It causes the inverted index to consume three times more RAM memory than mixed-case text.",
            "It invalidates the ascending numerical order of document identifiers in postings lists.",
            "It forces the query optimizer to process all Boolean queries in reverse chronological order."
        ],
        "explanation": "Lecture 5 slide 25: Lowercasing everything conflates General Motors vs motors, Bush vs bush, Fed vs fed, SAIL vs sail."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "In the Google search example discussed in Lecture 5, what occurred when users queried 'C.A.T.'?",
        "correct": "Case folding and punctuation removal caused the top result to be about domestic cats (Lolcats) rather than Caterpillar Inc.",
        "distractors": [
            "The search engine crashed because period characters were treated as regular expression wildcards.",
            "The search engine returned only documents written in computer-aided tomography medical journals.",
            "The search engine automatically redirected the user to a commercial heavy machinery dealership website."
        ],
        "explanation": "Lecture 5 slide 25: 'Google example: Query C.A.T. -> #1 result is for \"cat\" (well, Lolcats) not Caterpillar Inc.'"
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "How does an IR system use a hand-constructed thesaurus (e.g. mapping 'car' and 'automobile') during indexing or querying?",
        "correct": "It can index both words under a unified compound term (e.g. car-automobile) or expand query terms to include synonyms.",
        "distractors": [
            "It deletes all occurrences of 'automobile' and forces writers to use 'car' in all indexed documents.",
            "It converts synonyms into skip pointers that jump between disparate document postings lists.",
            "It uses the thesaurus to calculate syllable measures for Phase 2 of Porter's stemming algorithm."
        ],
        "explanation": "Lecture 5 slide 27: Synonyms can be rewritten to form equivalence-class terms (index under car-automobile) or used to expand queries."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "What was the original purpose of the Soundex algorithm developed by Robert Russell and Margaret Odell?",
        "correct": "To group surname spelling variants together based on phonetic pronunciation rather than literal orthography.",
        "distractors": [
            "To compress audio speech files into text tokens for voice recognition retrieval.",
            "To calculate term frequency weights for documents stored in relational databases.",
            "To detect the natural language of a document by analyzing vowel frequencies."
        ],
        "explanation": "Soundex is a phonetic algorithm developed for census surname matching, clustering homophones and spelling variations."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "How does the Soundex algorithm generate a 4-character code for an English word?",
        "correct": "It keeps the first letter, maps subsequent consonants to phonetic digit classes (1-6), drops vowels/H/W/Y, and pads with zeroes.",
        "distractors": [
            "It computes an MD5 cryptographic checksum of the word string and truncates it to four hex characters.",
            "It counts the number of syllables and creates a code representing consonant-vowel transitions.",
            "It maps every character to its 7-bit ASCII value and computes the binary XOR of the character sequence."
        ],
        "explanation": "Soundex retains the initial letter, maps consonants to digits 1-6 according to sound class, deletes vowels and H/W/Y, and pads to letter+3 digits."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "Under the Soundex algorithm, why do the names 'Hermann' and 'Herman' produce the identical code H655?",
        "correct": "Both start with 'H', ignore vowels, and map the consonants 'r', 'm', 'n' to the same phonetic digits in sequence.",
        "distractors": [
            "Both words have the exact same number of letters when case folded to lowercase.",
            "The Soundex algorithm automatically strips all double consonants before computing character lengths.",
            "They share the same dictionary postings list because both are recognized as German proper nouns."
        ],
        "explanation": "Hermann and Herman both begin with H; e is ignored; r=6, m=5, n=5. Double letters merge. Both yield H655."
    },
    {
        "topic": "Normalization, Equivalence Classes & Soundex",
        "question": "Which of the following is NOT typically handled via equivalence class normalization in IR?",
        "correct": "Calculating the mathematical relevance score of a document using cosine vector similarity.",
        "distractors": [
            "Removing diacritics and umlauts so that 'Tübingen' matches queries for 'Tuebingen'.",
            "Stripping periods from acronyms so that 'U.S.A.' matches queries for 'USA'.",
            "Standardizing date formats so that '7/30' matches queries for 'July 30'."
        ],
        "explanation": "Scoring documents with cosine vector similarity is part of the ranking/scoring stage, not textual normalization into equivalence classes."
    },

    # -------------------------------------------------------------
    # Topic 13: Stemming & Lemmatization (Q187 - Q200)
    # -------------------------------------------------------------
    {
        "topic": "Stemming & Lemmatization",
        "question": "What is the fundamental difference between 'stemming' and 'lemmatization'?",
        "correct": "Stemming chops affixes heuristically without a vocabulary; lemmatization uses full morphological analysis and dictionary headwords.",
        "distractors": [
            "Stemming is used exclusively for English, while lemmatization is used exclusively for Asian languages.",
            "Stemming increases precision while harming recall; lemmatization increases recall while harming precision.",
            "Stemming operates during query execution, while lemmatization operates exclusively during document downloading."
        ],
        "explanation": "Lecture 5 slide 28 & 29: Lemmatization does proper reduction to dictionary headwords using grammatical analysis. Stemming is crude affix chopping without a dictionary."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "When processing the sentence 'the boy's cars are different colors', what output would a true lemmatizer produce?",
        "correct": "'the boy car be different color' (reducing inflections to grammatical base lemmas).",
        "distractors": [
            "'the boy car are differ col' (crudely chopping suffixes from word endings).",
            "'boy car color' (stripping all function words and verbs from the sentence).",
            "'the boys car is different colors' (converting all nouns to plural and verbs to singular)."
        ],
        "explanation": "Lecture 5 slide 28 gives this exact example: 'the boy's cars are different colors -> the boy car be different color' (are -> be, cars -> car, boy's -> boy)."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "When processing the words 'automate', 'automatic', and 'automation', what root does a standard stemmer like Porter typically produce?",
        "correct": "'automat' (crude morphological root common to all three forms).",
        "distractors": [
            "'automate' (the canonical infinitive dictionary headword).",
            "'auto' (stripping all characters after the first four letters).",
            "'automation' (retaining the longest noun form as the indexing term)."
        ],
        "explanation": "Lecture 5 slide 29: 'e.g., automate(s), automatic, automation all reduced to automat.'"
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "What is the architectural design of Martin Porter's stemming algorithm (1980)?",
        "correct": "It consists of five sequential phases of rule-based reductions applied progressively to word suffixes.",
        "distractors": [
            "It uses a single-pass lookup table containing 250,000 pre-compiled English root words.",
            "It trains a deep neural network to predict morphological prefixes from character n-grams.",
            "It executes an external merge sort on word character streams using variable-length arrays."
        ],
        "explanation": "Lecture 5 slide 30: Porter's algorithm has 5 phases applied sequentially, each with a set of suffix-reduction commands."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "In Porter's algorithm, what rule convention is applied when multiple conflicting commands match within a single phase?",
        "correct": "Select the single rule that applies to the longest matching suffix of the word.",
        "distractors": [
            "Select the rule that removes the fewest characters from the end of the word.",
            "Apply all matching rules simultaneously and concatenate the resulting word stems.",
            "Skip the phase entirely and advance the word directly to Phase 5 reduction."
        ],
        "explanation": "Lecture 5 slide 30: 'sample convention: Of the rules in a compound command, select the one that applies to the longest suffix.'"
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "In Porter's algorithm notation [C](VC)^m[V], what does the measure 'm' represent?",
        "correct": "The number of alternating vowel-consonant sequences in the word stem, measuring its phonetic weight.",
        "distractors": [
            "The total count of consonant letters appearing before the first vowel in the word.",
            "The document frequency of the word stored in the system dictionary.",
            "The number of skip pointers attached to the term's inverted postings list."
        ],
        "explanation": "In Porter's algorithm, m is the measure of a word stem, defined as the count of VC (vowel-consonant) blocks representing word weight."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "In Phase 1a of Porter's algorithm, what transformations are applied to words ending in 'sses', 'ies', 'ss', and 's'?",
        "correct": "sses -> ss, ies -> i, ss -> ss, and s -> null (e.g. caresses -> caress, ponies -> poni, cats -> cat).",
        "distractors": [
            "sses -> s, ies -> ies, ss -> s, and s -> s (reducing all s-endings to a single 's').",
            "sses -> null, ies -> y, ss -> null, and s -> null (deleting all plural indicators completely).",
            "sses -> ss, ies -> y, ss -> s, and s -> ed (converting nouns into past-tense verb stems)."
        ],
        "explanation": "Lecture 5 slide 31 lists Phase 1a rules: sses -> ss, ies -> i, ss -> ss, s -> null."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "Porter's rule '(m > 1) EMENT -> null' reduces 'replacement' to 'replac', but leaves 'cement' unchanged as 'cement'. Why?",
        "correct": "'cement' has a stem measure m <= 1, so the rule condition (m > 1) fails, preventing erroneous over-stemming.",
        "distractors": [
            "'cement' is classified as a proper noun by the part-of-speech tagger, exempting it from stemming.",
            "'cement' is included in the system stop list, preventing it from entering Phase 4 reduction.",
            "The word 'cement' contains an odd number of letters, triggering an automatic rule bypass."
        ],
        "explanation": "Lecture 5 slide 31: Weight-sensitive rule (m>1) EMENT -> null: 'replacement -> replac' (m=2 > 1), but 'cement -> cement' (m=1, condition fails)."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "How does the Lovins stemmer differ fundamentally in approach from the Porter stemmer?",
        "correct": "It is a single-pass algorithm that removes the longest suffix from a rule base of ~250 rules, making it more aggressive.",
        "distractors": [
            "It uses a 10-phase pipeline that preserves all plural noun endings and verb participles.",
            "It requires an external dictionary of 500,000 words to perform full morphological analysis.",
            "It operates exclusively on prefixes (e.g. un-, re-, dis-) rather than word suffixes."
        ],
        "explanation": "Lecture 5 slide 32: 'Lovins stemmer: Single-pass, longest suffix removal (about 250 rules)'. It is single-pass and heavier than Porter."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "In the lecture example, how does aggressive stemming harm search precision for queries like 'operational research' or 'operating systems'?",
        "correct": "'operative', 'operational', and 'operating' all reduce to 'oper', causing completely unrelated topics to conflate.",
        "distractors": [
            "The word 'oper' is treated as a Boolean operator equivalent to OR, distorting query syntax.",
            "It causes the postings lists for all three terms to be deleted from disk due to identical stem length.",
            "It forces the query optimizer to process all subsequent terms using uncompressed incidence vectors."
        ],
        "explanation": "Lecture 5 slide 32: 'E.g., operative (dentistry) => oper, operational (research) => oper, operating (systems) => oper'. Over-stemming conflates distinct meanings."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "What is 'under-stemming', and what is its negative impact on information retrieval effectiveness?",
        "correct": "Words with the same conceptual root are not reduced to the same term (e.g. cylinder / cylindrical), harming recall.",
        "distractors": [
            "Words with different meanings are erroneously merged into the same dictionary term, harming precision.",
            "Postings lists are split into multiple fragments, increasing disk head seek latency during merges.",
            "Skip pointers are placed too close together, causing the merge algorithm to check excessive pointers."
        ],
        "explanation": "Under-stemming occurs when related words fail to reduce to the same stem, preventing matching and thus harming recall."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "While stemming provides modest, mixed retrieval gains in English, what did the slides note regarding languages like Finnish?",
        "correct": "Stemming provides dramatic retrieval performance gains (around 30% improvement) due to rich agglutinative morphology.",
        "distractors": [
            "Stemming causes a 50% drop in retrieval effectiveness because Finnish words do not have vowel endings.",
            "Finnish text cannot be stemmed because Finnish uses the Cyrillic script rather than Latin characters.",
            "Stemming eliminates the need for dictionary storage because all Finnish words reduce to the same stem."
        ],
        "explanation": "Lecture 5 slide 32: 'Definitely useful for Spanish, German, Finnish, ... 30% performance gains for Finnish!'"
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "What do research evaluations conclude regarding the benefits of full grammatical morphological analysis over simple stemmers in English IR?",
        "correct": "Full morphological analysis provides at most modest benefits for retrieval effectiveness compared to simple stemmers.",
        "distractors": [
            "Full morphological analysis improves retrieval precision by 500% over rule-based stemmers like Porter.",
            "Full morphological analysis completely eliminates the need for inverted index postings lists.",
            "Full morphological analysis is 1,000 times faster to compute than simple heuristic suffix stripping."
        ],
        "explanation": "Lecture 5 slide 32: 'Full morphological analysis - at most modest benefits for retrieval'."
    },
    {
        "topic": "Stemming & Lemmatization",
        "question": "How are stemmers, lemmatizers, and language tokenizers architecturally integrated into an enterprise IR indexing pipeline?",
        "correct": "As modular, language-specific and application-specific 'plug-in' components inserted between tokenizer and indexer.",
        "distractors": [
            "As hard-coded microcode instructions burned permanently into search engine server CPU silicon chips.",
            "As standalone relational database stored procedures that execute after the complete query result is returned.",
            "As client-side web browser JavaScript extensions that modify search query terms before transmission."
        ],
        "explanation": "Lecture 5 slide 33: 'These are \"plug-in\" addenda to the indexing process. Both open source and commercial plug-ins are available for handling these.'"
    }
]
