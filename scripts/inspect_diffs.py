import sys
sys.path.append('scripts')
from build_batch1 import questions_batch1
from build_batch2 import questions_batch2
from build_batch3 import questions_batch3
from build_batch4 import questions_batch4

all_qs = questions_batch1 + questions_batch2 + questions_batch3 + questions_batch4

count = 0
for i, q in enumerate(all_qs):
    a = q['answer']
    ans_text = q['options'][a]
    dist_lens = [len(o) for idx, o in enumerate(q['options']) if idx != a]
    diff = len(ans_text) - max(dist_lens)
    if diff > 0:
        count += 1
        longest_dist_idx = max((idx for idx in range(4) if idx != a), key=lambda idx: len(q['options'][idx]))
        qid = q['id']
        dist_text = q['options'][longest_dist_idx]
        print(f"{qid} (diff={diff}):")
        print(f"  ANS [{len(ans_text)}]:  {ans_text}")
        print(f"  DIST[{len(dist_text)}]: {dist_text}")

print(f"\nTotal questions where answer is strictly longest: {count} / {len(all_qs)}")
