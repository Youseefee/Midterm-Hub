import sys
sys.path.insert(0, 'scripts')
import ir_part1

qs = ir_part1.part1_questions

# Q0 (index 0)
qs[0]["distractors"][0] = "The information need is formulated in natural language, whereas the query must strictly adhere to formal Boolean relational algebra."

# Q2 (index 2)
qs[2]["distractors"][1] = "Grep operates exclusively on uncompressed 7-bit ASCII files and cannot read modern document formats even with external preprocessing filters."

# Q4 (index 4)
qs[4]["distractors"][1] = "Recall measures the overall speed of postings list intersection; maximizing it increases dictionary memory overhead while maintaining precision."

# Q8 (index 8)
qs[8]["distractors"][1] = "Web engines shifted entirely from inverted indexes back to linear scans due to modern multi-core processor processing architecture."

# Q11 (index 11)
qs[11]["distractors"][0] = "It views each document simply as an unordered set of words without taking into account internal document narrative structure."

# Q13 (index 13)
qs[13]["distractors"][1] = "Precision remains completely unaffected because precision is mathematically independent of the total collection volume and distribution."

# Q14 (index 14)
qs[14]["distractors"][0] = "Finding any web page across the entire public internet that mentions the phrase 'deep learning' in general body text."

# Q23 (index 23)
qs[23]["distractors"][1] = "Bitwise operations produce non-deterministic result sets when handling Boolean queries containing more than three terms."

# Q25 (index 25)
qs[25]["distractors"][0] = "It cannot be indexed using memory hash tables or B-trees because matrix columns are restricted to fixed-width bit arrays."

# Q27 (index 27)
qs[27]["distractors"][0] = "000100 (matching document 4 only in the collection)."

# Q32 (index 32)
qs[32]["distractors"][0] = "It guarantees that documents with higher relevance scores are positioned strictly at the beginning of the list."

# Q35 (index 35)
qs[35]["distractors"][1] = "Primarily by term length in characters, and secondarily by document frequency in strictly descending order."

# Q36 (index 36)
qs[36]["distractors"][0] = "Each occurrence generates a separate posting with an identical docID appended consecutively to the underlying postings list."

# Q37 (index 37)
qs[37]["distractors"][0] = "The total number of times the term appears across all collection documents, stored inside each individual posting node."

# Q38 (index 38)
qs[38]["distractors"][0] = "Both the dictionary and postings lists are stored exclusively on magnetic tape archives to minimize long-term operating costs."

# Q39 (index 39)
qs[39]["distractors"][1] = "They provide instant O(1) random binary search access, but require contiguous blocks of pre-allocated physical memory."

# Q40 (index 40)
qs[40]["distractors"][0] = "Variable-length arrays allow instantaneous insertion of new postings directly in the middle of lists without memory reallocation."

# Q41 (index 41)
qs[41]["distractors"][0] = "A B-tree of hash tables where each internal hash bucket represents a distinct character encoding format standard."

# Q47 (index 47)
qs[47]["correct"] = "The matching docID is added to the result list, and both pointers advance to their next nodes."

# Q51 (index 51)
qs[51]["distractors"][0] = "The algorithm appends all remaining elements of the non-empty postings list directly into the final accumulated result list."

# Q54 (index 54)
qs[54]["distractors"][0] = "docID_Brutus is discarded from the result list, and the Caesar pointer is advanced forward to the next posting."

# Q57 (index 57)
qs[57]["distractors"][0] = "Terms must occur within the exact same section ('/s') or within the same page ('/p')."

# Q59 (index 59)
qs[59]["distractors"][1] = "They require all indexed documents to be translated into formal relational database tables and schemas before searching."

strictly_longest = sum(1 for q in qs if len(q['correct']) > max(len(d) for d in q['distractors']))
print(f"Updated Part 1 strictly longest: {strictly_longest} / {len(qs)}")
