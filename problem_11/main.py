#!/usr/bin/env python3
"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
"""

import sys

S = list(filter(lambda x: x, sys.stdin.read().split('\n')))
testSets = []

i = 0
while i < len(S):
    print(S)
    testSets.append((S[i], tuple(S[i + 1].split(' '))))
    i += 2


def autocomplete(string, dictionary):
    return list(filter(lambda x: x.startswith(string), dictionary))


for ts in testSets:
    print(autocomplete(ts[0], ts[1]))
