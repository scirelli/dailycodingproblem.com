#!/usr/bin/env python3


def unique_climbs(N, X={1, 2}):
    """
    Brought force method. Try out all possible combinations.
    """
    result = 0

    if N == 0:
        return 1
    if N < 0:
        return 0

    for cnt in X:
        result += unique_climbs(N-cnt, X)

    return result

print(unique_climbs(4))

print(unique_climbs(4, {1, 3, 5}))

print(unique_climbs(4, {1}))

print(unique_climbs(5, {1, 2}))
