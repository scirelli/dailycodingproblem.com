#!/usr/bin/env python3
from random import randrange
from time import perf_counter_ns
from math import floor


tests = [
    [4, 3, 0, 1, 5],
    [1, 1],
    [4, 1, 4, 1, 4, 1, 4, 1, 5, 5],
    [4, 4, 4, 4, 5, 5],
    [2, 3, 1],
    [4, 4, 5, 6, 3],
    [5, 6],
    [randrange(100000) for x in range(10000)]
]


# O(n^2)
def determineHIndex(paper_citations: list) -> int:
    results = []

    for h in paper_citations:
        cnt = 0
        for c in paper_citations:
            if c >= h:
                cnt = cnt + 1
        if cnt >= h:
            results.append(h)

    if not results:
        return None

    return max(results)


# O(nlog(n)) + n/2
def determineHIndex_fastest(paper_citations: list) -> int:
    paper_citations = sorted(paper_citations)

    size = len(paper_citations)
    midIndex = floor(size / 2)
    rtn = None

    end = size
    i = midIndex
    while i >= 0:
        if paper_citations[i] <= (end - i):
            rtn = paper_citations[i]
            break
        i = i - 1

    return rtn


for f in (determineHIndex, determineHIndex_fastest):
    t = perf_counter_ns()
    r = map(f, tests)
    e = perf_counter_ns()
    print('\n'.join([str(x) for x in r]), (e - t) / 1000 / 1000, 's')
