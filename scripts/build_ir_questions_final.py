import json
import random
import re
from collections import Counter
import sys
import subprocess

sys.path.insert(0, 'scripts')
import ir_part1
import tune_part1

import ir_part2
import tune_part2

import ir_part3
import tune_part3

all_raw = (
    ir_part1.part1_questions +
    ir_part2.part2_questions +
    ir_part3.part3_questions
)

print(f"Total raw questions: {len(all_raw)}")
assert len(all_raw) == 200, f"Expected 200, got {len(all_raw)}"

def norm(t):
    return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()

# Target answers: exactly 50 of each (0, 1, 2, 3)
# To ensure reproducible shuffling and balanced distribution across topics:
random.seed(42)
target_answers = [0]*50 + [1]*50 + [2]*50 + [3]*50
random.shuffle(target_answers)

final_questions = []
longest_count = 0

for i, raw in enumerate(all_raw):
    q_id = f"ir_{i+1}"
    ans = target_answers[i]
    correct = raw["correct"]
    distractors = list(raw["distractors"])
    
    # Place options
    options = [None] * 4
    options[ans] = correct
    
    # Place distractors into the other 3 slots
    d_indices = [k for k in range(4) if k != ans]
    for slot, dist in zip(d_indices, distractors):
        options[slot] = dist
        
    lens = [len(o) for o in options]
    if lens[ans] == max(lens) and lens.count(max(lens)) == 1:
        longest_count += 1
        
    final_questions.append({
        "id": q_id,
        "subject": "Information Storage & Retrieval (IR)",
        "topic": raw["topic"],
        "question": raw["question"],
        "options": options,
        "answer": ans,
        "explanation": raw["explanation"]
    })

print(f"Correct strictly longest count: {longest_count} ({longest_count/len(final_questions)*100:.1f}%)")
pos_counts = Counter(q["answer"] for q in final_questions)
print(f"Answer positions: {dict(sorted(pos_counts.items()))}")

# Check questions duplicates
seen_q = {}
dups_q = 0
for i, q in enumerate(final_questions):
    nq = norm(q["question"])
    if nq in seen_q:
        print(f"DUPLICATE QUESTION: #{i} duplicate of #{seen_q[nq]}")
        dups_q += 1
    seen_q[nq] = i

# Check option duplicates
dups_opt = 0
for i, q in enumerate(final_questions):
    opts = q["options"]
    n_opts = [norm(o) for o in opts]
    if len(set(n_opts)) != 4:
        print(f"DUPLICATE OPTIONS in #{i}: {opts}")
        dups_opt += 1

assert dups_q == 0, f"Found {dups_q} duplicate questions!"
assert dups_opt == 0, f"Found {dups_opt} questions with duplicate options!"

# Write to questions/ir_questions.json
with open("questions/ir_questions.json", "w", encoding="utf-8") as f:
    json.dump(final_questions, f, indent=2, ensure_ascii=False)

print("Successfully written 200 questions to questions/ir_questions.json")
