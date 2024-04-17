from typing import Sequence
import itertools


def generate_all_subsequences(s: str, easy_mode: bool | None = False) -> list[str]:
    if easy_mode:
        subseqs = []
        for i in range(len(s) + 1):
            for subseq in itertools.combinations(s, i):
                subseqs.append("".join(subseq))
        return sorted(set(subseqs))

    subseqs = []
    word_end_index = len(s)

    def backtrack(index: int, sequence: Sequence):
        if index == word_end_index:
            subseqs.append("".join(sequence))
            return

        for include_char in {True, False}:
            if include_char:
                sequence.append(s[index])
                backtrack(index + 1, sequence)
                sequence.pop()
            else:
                backtrack(index + 1, sequence)

    backtrack(0, [])
    return sorted(set(subseqs))

def bfs(s: str) -> list[str]:
    q = set([s])
    seen = set()
    while q:
        new_q = set()
        for subseq in q:
            seen.add(subseq)
            for i in range(len(subseq)):
                cand = subseq[:i] + subseq[i+1:]
                if cand not in new_q:
                    new_q.add(cand)
        
        q = new_q
    return seen


subs = generate_all_subsequences("123", easy_mode=False)
subs2 = bfs('abcc')
print(subs2, len(subs2))
print(subs, len(subs))
