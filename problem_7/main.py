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
[1,1,1,1], [11,1,1], [11,11], [1,11,1], [1,1,11]

{1234} = 3
[1,2,3,4], [12,3,4], [1,23,4]

{4321} = 2
[4,3,2,1], [4,3,21]

{11111}
[1,1,1,1,1],
[1,11,1,1],
[1,11,11],

[1,1,11,1],

[1,1,1,11],

[11,1,1,1],
[11,11,1],
[11,1,11]
'''
import sys;

cnt = 0
def perms(input_str, start, end):
    "count message permutations"
    global cnt
    cnt += 1
    for i in range(start, end-1):
        num = input_str[i:i + 2]
        if int(num) <= 26:
            perms(input_str, i + 2, end)


S = sys.stdin.read().rstrip() or '111'
print(f"Input: '{S}'")
breakpoint()
perms(S, 0, len(S))
print(cnt)


# ------ Stack 1 -------                                        ------ Stack 1' -------
# cnt = 1                                                       cnt = 3
# def perms(input_str='111', start=0, end=3):                   def perms(input_str='111', start=0, end=3):
#     global cnt                                                    global cnt
#     cnt += 1                    \i/                               cnt += 1                      \i/
#     for i in range(start, end): [0,1,2]                           for i in range(start, end): [0,1,2]
#         num = input_str[i:i + 2] '11'                                 num = input_str[i:i + 2] '11'
#         if int(num) <= 26:                                            if int(num) <= 26:
#             perms(input_str ='11,1', i + 2, end)                      perms(input_str ='1,11', i + 2, end)

# ------ Stack 2 -------                                        ------ Stack 2' -------
# cnt = 2                                                       cnt = 3
# def perms(input_str='11,1', start=2, end=3):                  def perms(input_str='1,11', start=1, end=3):
#     global cnt                                                    global cnt
#     cnt += 1                    \i/                               cnt += 1                      \i/
#     for i in range(start, end): [2]                               for i in range(start, end): [0,1,2]
#         num = input_str[i:i + 2] '1'                                  num = input_str[i:i + 2] '11'
#         if int(num) <= 26:                                            if int(num) <= 26:
#             perms(input_str ='11,1,', i + 2, end)                     perms(input_str ='1,11', i + 2, end)

# ------ Stack 3 -------
# cnt = 3
# def perms(input_str='11,1,', start=4, end=3):
#     global cnt
#     cnt += 1                    \i/
#     for i in range(start, end): []
#         num = input_str[i:i + 2] '1'
#         if int(num) <= 26:
#             perms(input_str ='11,1,', i + 2, end)
