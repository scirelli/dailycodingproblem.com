#!/usr/bin/env python3


def longest_substring(string, k):
    """
    Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

    For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
    """
    longest_subString = 0
    ci = 0
    i = 0
    for i in range(len(string)):
        char_set = set()
        for ci in range(i, len(string)):
            c = string[ci]
            char_set.add(c)

            if len(char_set) > k:
                break
        if len(char_set) <= k:
            longest_subString = max(longest_subString, (ci + 1) - i)
        else:
            longest_subString = max(longest_subString, ci - i)
        print(char_set)

    return longest_subString


expected = 3
result = longest_substring('abcba', 2)
print('Result: ' + str(result))
assert expected == result

expected = 3
result = longest_substring('aabcba', 2)
print('Result: ' + str(result))
assert expected == result

expected = 4
result = longest_substring('aaabcba', 2)
print('Result: ' + str(result))
assert expected == result

expected = 4
result = longest_substring('caaabcba', 2)
print('Result: ' + str(result))
assert expected == result

expected = 3
result = longest_substring('caaabcba', 1)
print('Result: ' + str(result))
assert expected == result

expected = 3
result = longest_substring('vcaaabcba', 1)
print('Result: ' + str(result))
assert expected == result

expected = 4
result = longest_substring('vcabcbaaa', 2)
print('Result: ' + str(result))
assert expected == result

expected = 5
result = longest_substring('vcabcbaaab', 2)
print('Result: ' + str(result))
assert expected == result

expected = 4
result = longest_substring('vcabcbaaac', 2)
print('Result: ' + str(result))
assert expected == result

expected = 9
result = longest_substring('vcabcbaaac', 3)
print('Result: ' + str(result))
assert expected == result
