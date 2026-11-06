import sys
sys.path.insert(0, 'scripts')
import ir_part2

qs = ir_part2.part2_questions

# Q63 (index 0)
qs[0]["distractors"][0] = "Process terms in order of decreasing document frequency (df), starting with the most frequent terms in the collection."

# Q64 (index 1)
qs[1]["distractors"][0] = "The dictionary data structure can only locate postings lists in strictly ascending numerical order of their document frequency values."

# Q66 (index 3)
qs[3]["distractors"][0] = "At most 300 document IDs, bounded strictly by the larger postings list of TermB."

# Q68 (index 5)
qs[5]["distractors"][0] = "Load all postings lists into a unified memory hash table and compute bitwise AND across all document vectors."

# Q69 (index 6)
qs[6]["distractors"][1] = "It always evaluates the second disjunctive clause first because Boolean algebra requires strict right-to-left clause evaluation."

# Q70 (index 7)
qs[7]["distractors"][0] = "It represents a lower bound assuming all documents containing Term1 also contain Term2 simultaneously across the entire text corpus."

# Q72 (index 9)
qs[9]["distractors"][0] = "It prevents the postings list on disk from exceeding standard physical sector allocation limits on persistent storage drives."

# Q74 (index 11)
qs[11]["distractors"][0] = "It must be written to permanent disk storage to allow the user to backtrack through previous query history steps in the current session."

# Q75 (index 12)
qs[12]["distractors"][0] = "It scans the 500,000 docIDs of common_word first to populate CPU cache lines before checking rare_word entries in the dictionary."

# Q77 (index 14)
qs[14]["distractors"][0] = "The short list is augmented with extra skip pointers every two elements to match the stride of the long postings list on disk."

# Q78 (index 15)
qs[15]["distractors"][0] = "Compute NOT C first across the entire collection of documents, and then intersect the resulting huge set with terms A and B in memory."

# Q79 (index 16)
qs[16]["distractors"][0] = "An index that stores two separate postings lists for every term: one for document titles and one for general body paragraph text."

# Q81 (index 18)
qs[18]["distractors"][0] = "As an expensive two-pointer intersection between the single-word postings lists of individual terms 'solar' and 'energy'."

# Q82 (index 19)
qs[19]["distractors"][0] = "As a single four-word dictionary lookup in a specialized quad-word vocabulary index structure stored in main memory."

# Q83 (index 20)
qs[20]["distractors"][0] = "The biwords might match documents that contain synonyms of 'stanford' instead of the literal search string entered by the user."

# Q84 (index 21)
qs[21]["distractors"][0] = "The query optimizer must re-execute the search using a term-document incidence matrix to verify internal bit alignment across words."

# Q86 (index 23)
qs[23]["distractors"][0] = "Postings merge algorithms cannot mathematically process postings lists for phrases containing more than two words in queries."

# Q87 (index 24)
qs[24]["distractors"][0] = "Soundex phonetic hashing to replace all vowels with numbers before generating consecutive word pairs for the dictionary."

# Q88 (index 25)
qs[25]["distractors"][0] = "A sequence of N numbers (N) separated by arbitrary punctuation symbols (X) and terminating with a trailing numeral (N)."

# Q90 (index 27)
qs[27]["distractors"][0] = "It strips all nouns from the query and performs a conjunction search exclusively on function words across all documents in the index."

# Q91 (index 28)
qs[28]["distractors"][0] = "It consumes more dictionary space than indexing all arbitrary consecutive word pairs in the underlying document collection on disk."

# Q94 (index 31)
qs[31]["distractors"][0] = "Each posting contains a document ID followed by the byte offset of the document file on the physical magnetic hard disk storage array."

# Q95 (index 32)
qs[32]["distractors"][0] = "<term, docID; length; byte_start, byte_end; skip_pointer_offset_value>."

# Q99 (index 36)
qs[36]["distractors"][0] = "Biword indexes only store document titles, whereas positional indexes store entire document character streams on persistent disk."

# Q104 (index 41)
qs[41]["distractors"][0] = "Long documents cause the dictionary hash table to expand exponentially regardless of vocabulary size in the underlying text corpus."

# Q106 (index 43)
qs[43]["distractors"][0] = "Positional indexes cannot be stored on magnetic hard disk drives due to physical read head seek latency limitations on tracks."

# Q107 (index 44)
qs[44]["distractors"][0] = "The query mixture executed at the exact same speed, but reduced overall disk storage consumption by over ninety percent."

# Q108 (index 45)
qs[45]["distractors"][0] = "Rare, low-frequency phrases that contain misspelled words or unusual foreign terms across the text collection."

# Q111 (index 48)
qs[48]["distractors"][0] = "Positional indexes support arbitrary phrase queries of any length without vocabulary explosion across the dictionary."

# Q112 (index 49)
qs[49]["distractors"][0] = "To allow search engines to traverse postings lists in reverse chronological order during dynamic document collection updates."

# Q115 (index 52)
qs[52]["distractors"][0] = "The algorithm immediately terminates the entire merge operation and outputs the current intermediate result list to the caller."

# Q116 (index 53)
qs[53]["distractors"][0] = "Place skip pointers at intervals of log2(P) postings, starting uniformly from the middle of the postings list."

# Q119 (index 56)
qs[56]["distractors"][0] = "50 skip pointers placed at evenly spaced intervals of 200 postings throughout the entire postings list."

# Q122 (index 59)
qs[59]["distractors"][0] = "16 comparisons (scanning through all elements to the end of the list sequentially)."

# Q125 (index 62)
qs[62]["distractors"][0] = "Modern 64-bit CPU architectures cannot execute pointer comparison instructions without experiencing pipeline stalls in hardware."

# Q127 (index 64)
qs[64]["distractors"][0] = "It places skip pointers exclusively on stop words while ignoring high-value domain terminology across the collection index."

strictly_longest = sum(1 for q in qs if len(q['correct']) > max(len(d) for d in q['distractors']))
print(f"Updated Part 2 strictly longest: {strictly_longest} / {len(qs)}")
