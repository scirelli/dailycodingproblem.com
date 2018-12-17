#!/usr/bin/env python3
"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?


Examples:

[15, 100, -10, 100, 1]
[15, 100, 1000, 100, -10, 100, 1]
[15, 100, 1000, 5000, -10, 100, 1]
[15, 100, 1000, 500, -10, 100, 1]

[1015, 600, 990, 600, -9, 100, 1]

[1006, ]



  0, 1, 2, 3, 4, 5, 6, 7, 8, 9
0    -  .  .  .  .  .  .  .  .
1 -     -  .  .  .  .  .  .  .
2 -  -     -  .  .  .  .  .  .
3 -  -  -     -  .  .  .  .  .
4 -  -  -  -     -  .  .  .  .
5 -  -  -  -  -     -  .  .  .
6 -  -  -  -  -  -     -  .  .
7 -  -  -  -  -  -  -     -  .
8 -  -  -  -  -  -  -  -     -
9 -  -  -  -  -  -  -  -  -

(0,0), (0,2), (2,4), (4,6), (6,8)
(1,1), (1,3), (3,5), (5,7), (7,9)
(2,2), (2,4), (4,6), (6,8)
(3,3), (3,5), (5,7), (7,9)
(4,4), (4,6), (6,8)
(5,5), (5,7), (7,9)
(6,6), (6,8)
(7,7), (7,9)
(8,8)
(9,9)

(0,0), (0,3), (3,5), (5,7), (7,9)
5 1 1 5
1 1 1 5
1 1 1 5
5 1 1 5

(0,0) + (0,2) = 5 + 1 = 6
(1,1) + (1,3) = 1 + 5 = 6
"""
import sys

inpt = list(
    map((lambda x: list(map(int, x.split(' ')))), filter(lambda x: x, sys.stdin.read().split('\n')))
)

# /////////////// ignore above this line ////////////////////


def find_max_sum(arr):
    """
    M(-1) = 0,
    M(0) = A[0], and
    M(i) = max(M(i - 1), M(i - 2) + A[i])
    for i = 1, ..., n. M(n)


    A = [5, 5, 10, 40, 50, 35]
         ^
    M(0) = 5
    M(1) = max(M(0), M(-1) + A[1])
         = max(5   , 0     + 5   )
         = 5

    M(2) = max(M(1), M(0) + A[2])
         = max(5   , 5    + 10  )
         = 15
    """
    incl = 0
    excl = 0

    for i in arr:
        tmp = incl
        incl = max(incl, excl + i)
        excl = tmp

    return max(excl, incl)


# od -vAd -N40 -tu1 < /dev/urandom | cut -c11- | tr -s [:space:] " " | tee input2.txt
def main():
    """
    main
    """
    print('Input:', inpt[0])
    print('Max sum = ', find_max_sum(inpt[0]))


if __name__ == '__main__':
    main()
