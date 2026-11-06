"""Validate a question bank: count, duplicates, answer position balance, longest-option bias."""
import json, sys, re
from collections import Counter

def norm(t):
    return re.sub(r'[^a-z0-9 ]', '', t.lower()).strip()

def check(path, expected=200):
    qs = json.load(open(path, encoding='utf-8'))
    problems = []
    if len(qs) != expected:
        problems.append(f'count={len(qs)} (expected {expected})')
    seen = {}
    longest = 0
    for i, q in enumerate(qs):
        for k in ('id', 'subject', 'topic', 'question', 'options', 'answer', 'explanation'):
            if k not in q:
                problems.append(f'#{i} missing {k}')
        opts = q.get('options', [])
        if len(opts) != 4 or len(set(map(norm, opts))) != 4:
            problems.append(f'#{i} bad/duplicate options')
            continue
        a = q.get('answer')
        if not isinstance(a, int) or not 0 <= a < 4:
            problems.append(f'#{i} bad answer index')
            continue
        lens = [len(o) for o in opts]
        if lens[a] == max(lens) and lens.count(max(lens)) == 1:
            longest += 1
        n = norm(q['question'])
        if n in seen:
            problems.append(f'#{i} duplicate of #{seen[n]}')
        seen[n] = i
    pos = Counter(q.get('answer') for q in qs)
    print(f'{path}: {len(qs)} qs | answer positions {dict(sorted(pos.items()))} | correct=longest {longest} ({100*longest/max(len(qs),1):.0f}%)')
    for p in problems[:30]:
        print('  -', p)
    return not problems and longest / max(len(qs), 1) <= 0.30

if __name__ == '__main__':
    ok = all(check(p) for p in sys.argv[1:])
    sys.exit(0 if ok else 1)
