#!/usr/bin/env python3
'''
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

Examples:
{111} = 3
[1,1,1], [11,1], [1,11]

{1111} = 4
[1,1,1,1], [11,1,1], [11,11], [1,11,1]

{1234} = 3
[1,2,3,4], [12,3,4], [1,23,4]

{4321} = 2
[4,3,2,1], [4,3,21]

{11111}
[1,1,1,1,1],
    [11,1,1,1],
        [11,11,1],
        [11,1,11],
    [1,1,11,1],
        [1,1,1,11],
    [1,11,1,1],
        [1,11,11],
    [1,1,1,11]

'''


def perms(input_str, start, end):
    "count message permutations"
    cnt = 0
    for i in range(start, end):
        print('start', start, ' i', i)
        if int(input_str[i:i + 2]) <= 26:
            perms(input_str, start + 2, end)
            cnt += 1
    return cnt


breakpoint()

S = '11111'
print(perms(S, 0, len(S)))
