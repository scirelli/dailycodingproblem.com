#!/usr/bin/env python3
"""
This problem was asked by Twitter.

Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try pre-processing the dictionary into a more efficient data structure to speed up queries.
"""

import random
# import sys

# S = list(filter(lambda x: x, sys.stdin.read().split('\n')))
# S = list(filter(lambda x: x, '''de
# dog deer deal'''.split('\n')))
# testSets = []

# i = 0
# while i < len(S):
#     testSets.append((tuple(S[i].split(' ')), tuple(S[i + 1].split(' '))))
#     i += 2


class Tri():
    def __init__(self, dictionary):
        self.tri = {}
        self.buildTri(dictionary)

    def buildTri(self, dictionary):
        for word in dictionary:
            node = self.tri
            for letter in word:
                childNode = node.get(letter, {})
                wordSet = childNode.get('wordSet', set())
                wordSet.add(word)
                childNode['wordSet'] = wordSet
                node[letter] = childNode
                node = childNode

    def autocomplete(self, query_string):
        node = self.tri
        for letter in query_string:
            node = node.get(letter)
            if node is None:
                return []
        return list(node['wordSet'])


words_txt = open('./words.txt', 'r')
dictionary = list(map(lambda x: x.lower(), filter(lambda x: x, words_txt.read().split('\n'))))
words_txt.close()
ALPHABET = list('abcdefghijklmnopqrstuvwxyz')
random.shuffle(ALPHABET)
TEST_SETS = 10000
MAX_PREFIX_LEN = 4

def randomQuery():
    query = ''
    for _ in range(random.randint(1, MAX_PREFIX_LEN)):
        query += random.choice(ALPHABET)
    return query

print('Building tri...')
tri = Tri(dictionary)
print('Done!')

for i in range(TEST_SETS):
    query = randomQuery()
    print(f"Query: {query}")
    tri.autocomplete(query)
