# scripts/build_isapp_final.py
# Assembles, balances, validates, and writes the 200 IS Applications questions bank.

import json
import random
import re
import sys
import subprocess
from collections import Counter

sys.path.insert(0, 'scripts')
import isapp_part1
import isapp_part2
import isapp_part3
import isapp_part4
import tune_isapp

all_raw = (
    isapp_part1.part1_questions +
    isapp_part2.part2_questions +
    isapp_part3.part3_questions +
    isapp_part4.part4_questions
)

print(f"Total raw questions loaded: {len(all_raw)}")
assert len(all_raw) == 200, f"Expected exactly 200 questions, got {len(all_raw)}"

def norm(t):
    return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()

# Check question uniqueness
seen_questions = {}
for i, q in enumerate(all_raw):
    n = norm(q['question'])
    if n in seen_questions:
        raise ValueError(f"Duplicate question detected at #{i} and #{seen_questions[n]}: {q['question']}")
    seen_questions[n] = i

# Target answers: exactly 50 each of 0, 1, 2, 3
random.seed(42)
target_answers = [0] * 50 + [1] * 50 + [2] * 50 + [3] * 50
random.shuffle(target_answers)

final_questions = []
longest_count = 0

for i, raw in enumerate(all_raw):
    q_id = f"isapp_{i+1}"
    ans = target_answers[i]
    correct = raw["correct"]
    distractors = list(raw["distractors"])
    
    # Place options
    options = [None] * 4
    options[ans] = correct
    
    # Distribute distractors deterministically into remaining slots
    d_indices = [k for k in range(4) if k != ans]
    for slot, dist in zip(d_indices, distractors):
        options[slot] = dist
        
    # Check options uniqueness
    norm_opts = list(map(norm, options))
    if len(set(norm_opts)) != 4:
        raise ValueError(f"Duplicate options in question #{i+1}: {options}")
        
    lens = [len(o) for o in options]
    if lens[ans] == max(lens) and lens.count(max(lens)) == 1:
        longest_count += 1
        
    final_questions.append({
        "id": q_id,
        "subject": "Information Systems Applications (IS App)",
        "topic": raw["topic"],
        "question": raw["question"],
        "options": options,
        "answer": ans,
        "explanation": raw["explanation"]
    })

# Output file
output_path = "questions/isapp_questions.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(final_questions, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(final_questions)} questions to {output_path}")
pos_counts = Counter(q["answer"] for q in final_questions)
print(f"Answer distribution: {dict(sorted(pos_counts.items()))}")
print(f"Correct is longest in {longest_count} / {len(final_questions)} ({100*longest_count/len(final_questions):.1f}%)")

# Run validator
res = subprocess.run([sys.executable, "scripts/validate_questions.py", output_path], capture_output=True, text=True)
print("\n--- VALIDATOR OUTPUT ---")
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)
print(f"Validator exit code: {res.returncode}")
sys.exit(res.returncode)
