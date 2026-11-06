import sys
sys.path.insert(0, 'scripts')
import ir_part3

qs = ir_part3.part3_questions

# Q130 (index 0)
qs[0]["distractors"][0] = "Stripping all stop words from the dictionary and sorting the vocabulary in strictly alphabetical order across terms."

# Q131 (index 1)
qs[1]["distractors"][0] = "Different file formats use fundamentally different mathematical definitions of document frequency (df) across terms in the index."

# Q133 (index 3)
qs[3]["distractors"][0] = "It uses a fixed width of 32 bits per character, ensuring constant-time random access to any character offset in physical memory."

# Q134 (index 4)
qs[4]["distractors"][0] = "A marker indicating the end of a document's postings list used to signal early termination during linear postings merges on disk."

# Q136 (index 6)
qs[6]["distractors"][0] = "The indexer must discard the entire document because inverted indexes cannot process multilingual document content across collections."

# Q138 (index 8)
qs[8]["distractors"][0] = "Small units eliminate the need for tokenization, while large units eliminate the need for skip pointers in inverted index postings lists."

# Q139 (index 9)
qs[9]["distractors"][0] = "The document will be indexed correctly because modern stemmers automatically correct character encoding errors on the fly."

# Q140 (index 10)
qs[10]["distractors"][0] = "It prevents the dictionary from storing terms that contain vowel characters in their spellings across the inverted index."

# Q141 (index 11)
qs[11]["distractors"][0] = "The linguistic preprocessing and normalization engine."

# Q143 (index 13)
qs[13]["distractors"][0] = "An alphabetical entry in the system dictionary containing an accumulated document frequency count for search terms in the index."

# Q144 (index 14)
qs[14]["distractors"][0] = "A token is stored permanently on disk, while a term is an ephemeral variable discarded after sorting is complete."

# Q145 (index 15)
qs[15]["distractors"][0] = "It requires O(N^2) time complexity, making it too computationally expensive for modern microprocessors to execute."

# Q146 (index 16)
qs[16]["distractors"][0] = "Apostrophes cause variable-length arrays to overflow their allocated memory buffers during index construction on disk storage."

# Q147 (index 17)
qs[17]["distractors"][0] = "Splitting on hyphens doubles dictionary memory size, while keeping them whole eliminates all postings lists entirely from disk."

# Q148 (index 18)
qs[18]["distractors"][0] = "It causes the postings merge algorithm to take quadratic time O(x * y) for all subsequent Boolean queries evaluated."

# Q149 (index 19)
qs[19]["distractors"][0] = "Older systems indexed all numbers, whereas modern systems delete all numeric tokens to optimize vector ranking in main memory registers."

# Q150 (index 20)
qs[20]["distractors"][0] = "Date expressions automatically trigger Boolean negation operators if they contain forward slash characters in the query."

# Q152 (index 22)
qs[22]["distractors"][0] = "Chinese text contains no vowel characters, requiring phonetic soundex translation before tokenization can be performed."

# Q153 (index 23)
qs[23]["distractors"][0] = "Inverted indexes cannot store non-alphabetic character sets without corrupting skip pointer offsets in postings."

# Q155 (index 25)
qs[25]["distractors"][0] = "It is used exclusively for grammatical sentence particles and is discarded as stop words in every search engine implementation."

# Q156 (index 26)
qs[26]["distractors"][0] = "Text alternate direction on every second line (boustrophedon), requiring line inversion filters during text preprocessing."

# Q160 (index 30)
qs[30]["distractors"][0] = "Handling web-specific tokens like email addresses, URLs, Twitter hashtags, and internet domain names."

# Q161 (index 31)
qs[31]["distractors"][0] = "A misspelled word that causes syntax errors when parsed by a Boolean query optimizer during search processing across files."

# Q162 (index 32)
qs[32]["distractors"][0] = "The top 30 most common words account for less than 1% of all token occurrences in a collection of text documents."

# Q163 (index 33)
qs[33]["distractors"][0] = "Early computer hardware could not store words containing fewer than four alphabetical characters in memory registers."

# Q164 (index 34)
qs[34]["distractors"][0] = "Modern search engines expand stop lists to include over 10,000 common words to minimize RAM usage in index servers."

# Q165 (index 35)
qs[35]["distractors"][0] = "Magnetic hard drives were replaced with cloud tape archives that have infinite data storage capacity for text collections."

# Q167 (index 37)
qs[37]["distractors"][0] = "The search engine automatically translates the phrase into French and searches for 'Être ou ne pas être' in the corpus."

# Q170 (index 40)
qs[40]["distractors"][0] = "Between 5,000 and 10,000 words, covering all common nouns and adjectives across standard English language literature."

# Q171 (index 41)
qs[41]["distractors"][0] = "They immediately delete 'hotel' and 'Paris' and retrieve all documents containing the word 'in' from the index."

# Q172 (index 42)
qs[42]["distractors"][0] = "Removing stop words prevents users from searching for famous literary quotes, movie titles, and popular band names in the corpus."

# Q176 (index 46)
qs[46]["distractors"][0] = "Strictly adhering to 18th-century classical linguistic grammar rules regardless of actual modern user search behavior."

# Q177 (index 47)
qs[47]["distractors"][0] = "The search engine deletes the document postings list for 'window' and re-indexes the corpus dynamically in memory."

# Q178 (index 48)
qs[48]["distractors"][0] = "Asymmetric expansion requires 10 times more disk space to store postings lists than symmetric equivalence classes in dictionaries."

# Q180 (index 50)
qs[50]["distractors"][0] = "It causes the inverted index to consume three times more RAM memory than mixed-case text stored on persistent storage."

# Q181 (index 51)
qs[51]["distractors"][0] = "The search engine crashed because period characters were treated as regular expression wildcards in search queries on the web."

# Q182 (index 52)
qs[52]["distractors"][0] = "It deletes all occurrences of 'automobile' and forces writers to use 'car' in all indexed documents across the collection."

# Q185 (index 55)
qs[55]["distractors"][0] = "Both words have the exact same number of letters when case folded to lowercase characters in the dictionary and postings."

# Q186 (index 56)
qs[56]["distractors"][0] = "Removing diacritics and umlauts so that 'Tübingen' matches queries for 'Tuebingen' across indexed German documents."

# Q187 (index 57)
qs[57]["distractors"][0] = "Stemming is used exclusively for English, while lemmatization is used exclusively for complex Asian writing systems in corpora."

# Q190 (index 60)
qs[60]["distractors"][0] = "It uses a single-pass lookup table containing 250,000 pre-compiled English root words stored in fast memory."

# Q192 (index 62)
qs[62]["distractors"][0] = "The total count of consonant letters appearing before the first vowel in the word stem being analyzed."

# Q193 (index 63)
qs[63]["distractors"][0] = "sses -> s, ies -> ies, ss -> s, and s -> s (reducing all s-endings to a single 's' across all matching words)."

# Q194 (index 64)
qs[64]["distractors"][0] = "'cement' is classified as a proper noun by the part-of-speech tagger, exempting it from stemming in the pipeline."

# Q196 (index 66)
qs[66]["distractors"][0] = "The word 'oper' is treated as a Boolean operator equivalent to OR, distorting query syntax during search evaluation."

# Q197 (index 67)
qs[67]["distractors"][0] = "Words with different meanings are erroneously merged into the same dictionary term, harming precision significantly."

# Q198 (index 68)
qs[68]["distractors"][0] = "Stemming causes a 50% drop in retrieval effectiveness because Finnish words do not have vowel endings in grammar rules."

# Q199 (index 69)
qs[69]["distractors"][0] = "Full morphological analysis improves retrieval precision by 500% over rule-based stemmers like Porter in benchmark tests."

# Q200 (index 70)
qs[70]["distractors"][0] = "As hard-coded microcode instructions burned permanently into search engine server CPU silicon chips in hardware registers."

# Additional adjustments:
# Q130 (index 0)
qs[0]["distractors"][0] = "Stripping all stop words from the dictionary and sorting the vocabulary in strictly alphabetical order across collection terms."

# Q131 (index 1)
qs[1]["distractors"][0] = "Different file formats use fundamentally different mathematical definitions of document frequency (df) across terms in the inverted index."

# Q133 (index 3)
qs[3]["distractors"][0] = "It uses a fixed width of 32 bits per character, ensuring constant-time random access to any character offset in physical memory blocks."

# Q134 (index 4)
qs[4]["distractors"][0] = "A marker indicating the end of a document's postings list used to signal early termination during linear postings merges on disk drives."

# Q136 (index 6)
qs[6]["distractors"][0] = "The indexer must discard the entire document because inverted indexes cannot process multilingual document content across collections."

# Q138 (index 8)
qs[8]["distractors"][0] = "Small units eliminate the need for tokenization, while large units eliminate the need for skip pointers in inverted index postings lists."

# Q140 (index 10)
qs[10]["distractors"][0] = "It prevents the dictionary from storing terms that contain vowel characters in their spellings across the inverted index structure."

# Q143 (index 13)
qs[13]["distractors"][0] = "An alphabetical entry in the system dictionary containing an accumulated document frequency count for search terms in the index structure."

# Q146 (index 16)
qs[16]["distractors"][0] = "Apostrophes cause variable-length arrays to overflow their allocated memory buffers during index construction on physical disk storage arrays."

# Q147 (index 17)
qs[17]["distractors"][0] = "Splitting on hyphens doubles dictionary memory size, while keeping them whole eliminates all postings lists entirely from physical storage."

# Q149 (index 19)
qs[19]["distractors"][0] = "Older systems indexed all numbers, whereas modern systems delete all numeric tokens to optimize vector ranking in main memory registers."

# Q161 (index 31)
qs[31]["distractors"][0] = "A misspelled word that causes syntax errors when parsed by a Boolean query optimizer during search processing across indexed document files."

# Q171 (index 41)
qs[41]["distractors"][0] = "They immediately delete 'hotel' and 'Paris' and retrieve all documents containing the word 'in' from the inverted index collection."

# Q178 (index 48)
qs[48]["distractors"][0] = "Asymmetric expansion requires 10 times more disk space to store postings lists than symmetric equivalence classes in system dictionaries."

# Q181 (index 51)
qs[51]["distractors"][0] = "The search engine crashed because period characters were treated as regular expression wildcards in search queries on the web interface."

# Q185 (index 55)
qs[55]["distractors"][0] = "Both words have the exact same number of letters when case folded to lowercase characters in the dictionary and postings lists."

# Q187 (index 57)
qs[57]["distractors"][0] = "Stemming is used exclusively for English, while lemmatization is used exclusively for complex Asian writing systems in text corpora."

# Q198 (index 68)
qs[68]["distractors"][0] = "Stemming causes a 50% drop in retrieval effectiveness because Finnish words do not have vowel endings in grammar rules and syntax."

# Q200 (index 70)
qs[70]["distractors"][0] = "As hard-coded microcode instructions burned permanently into search engine server CPU silicon chips in hardware register logic."

strictly_longest = sum(1 for q in qs if len(q['correct']) > max(len(d) for d in q['distractors']))
print(f"Updated Part 3 strictly longest: {strictly_longest} / {len(qs)}")
