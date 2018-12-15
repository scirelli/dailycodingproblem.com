#!/usr/bin/env python3
"""
This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
"""
import sys

inpt = list(map(lambda x: x.split(' '), filter(lambda x: x, sys.stdin.read().split('\n'))))

# /////////////// ignore above this line ////////////////////


def largestSum(arr):
    """
    largestSum()
    """
    print('nothing', arr)


# od -vAd -N40 -tu1 < /dev/urandom | cut -c11- | tr -s [:space:] " " | tee input2.txt
def main():
    """
    main
    """
    print(inpt[0])


if __name__ == '__main__':
    main()
