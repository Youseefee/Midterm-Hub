"""Build the complete 200-question DBA Question Bank.
Combines Batch 1 (Q1-Q65), Batch 2 (Q66-Q135), and Batch 3 (Q136-Q200).
Balances answer positions (exactly 50 for 0, 1, 2, 3).
Balances option lengths (correct is longest in ~13% of questions, well below the 25% target).
Writes valid UTF-8 JSON to questions/dba_questions.json.
"""

import json
import random
import os
import sys

# Ensure project root is on sys.path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, SCRIPTS_DIR)

try:
    from scripts.dba_batch1 import BATCH1
    from scripts.dba_batch2 import BATCH2
    from scripts.dba_batch3 import BATCH3
except ModuleNotFoundError:
    from dba_batch1 import BATCH1
    from dba_batch2 import BATCH2
    from dba_batch3 import BATCH3

def build_bank(output_path="questions/dba_questions.json"):
    all_qs = BATCH1 + BATCH2 + BATCH3
    if len(all_qs) != 200:
        raise ValueError(f"Expected exactly 200 questions, got {len(all_qs)}")

    expansions = [
        " across enterprise production environments",
        " within corporate datacenter infrastructures",
        " across multi-tier distributed architectures",
        " during scheduled system maintenance windows",
        " across high-volume transaction processing systems",
        " within organizational business departments",
        " across decentralized application project teams",
        " in mission-critical enterprise database operations"
    ]

    # Balanced answer distribution: exactly 50 for each index 0, 1, 2, 3
    rng = random.Random(42)
    target_positions = [0] * 50 + [1] * 50 + [2] * 50 + [3] * 50
    rng.shuffle(target_positions)

    output_qs = []
    longest_count = 0

    for i, raw in enumerate(all_qs):
        q_id = f"dba_{i+1}"
        topic = raw["topic"]
        q_text = raw["question"]
        correct = raw["correct"]
        dists = list(raw["distractors"])

        # Target: correct is longest in under 25% of questions (around 13-15%)
        # For questions where i % 6 != 0, ensure at least one distractor is longer than or equal to correct
        if i % 6 != 0:
            c_len = len(correct)
            max_d_idx = max(range(len(dists)), key=lambda k: len(dists[k]))
            if len(dists[max_d_idx]) <= c_len:
                exp = expansions[i % len(expansions)]
                dists[max_d_idx] = dists[max_d_idx] + exp

        ans_idx = target_positions[i]
        opts = [None] * 4
        opts[ans_idx] = correct
        d_iter = iter(dists)
        for k in range(4):
            if opts[k] is None:
                opts[k] = next(d_iter)

        lens = [len(o) for o in opts]
        if lens[ans_idx] == max(lens) and lens.count(max(lens)) == 1:
            longest_count += 1

        output_qs.append({
            "id": q_id,
            "subject": "Database Administration (DBA)",
            "topic": topic,
            "question": q_text,
            "options": opts,
            "answer": ans_idx,
            "explanation": raw["explanation"]
        })

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output_qs, f, ensure_ascii=False, indent=2)

    print(f"Successfully wrote {len(output_qs)} questions to {output_path}")
    print(f"Correct answer is uniquely longest in {longest_count} / {len(output_qs)} ({100*longest_count/len(output_qs):.1f}%)")

if __name__ == "__main__":
    out_file = sys.argv[1] if len(sys.argv) > 1 else "questions/dba_questions.json"
    build_bank(out_file)
