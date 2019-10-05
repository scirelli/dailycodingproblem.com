#!/usr/bin/env python3
"""
This problem was asked by Sumo Logic.

Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.

An element is considered a peak if it is greater than both its left and right neighbors.
It is guaranteed that the first and last elements are lower than all others.
[0, 3, 9, 2, 7, 6, 4, 5, 8, 100, 1]
[0, 2, 3, 4, 1]
[0, 3, 9, 5, 4, 1]
"""
from math import floor


def _is_peak(array, index):
    if 0 < index < len(array) - 1 and array[index - 1] <= array[index] >= array[index + 1]:
        return True

    return False


def _dnc_peak(array, low_index, high_index):
    """
    Sub-arrays are chosen by going toward the larger number on the left or right of the mid point.
    """
    sub_array_length = high_index - low_index
    mid_index = low_index + floor(sub_array_length / 2)

    if _is_peak(array, mid_index):
        return mid_index

    if 0 < mid_index < len(array) - 1 and array[mid_index - 1] >= array[mid_index]:
        return _dnc_peak(array, low_index, mid_index - 1)

    return _dnc_peak(array, mid_index + 1, high_index)


def find_peak(array):
    """
    An element is considered a peak if it is greater than both its left and
    right neighbors.
    """
    peak_index = _dnc_peak(array, 0, len(array) - 1)
    return (peak_index, (array[peak_index - 1], array[peak_index], array[peak_index + 1]))


def generate_peakable(number_of_elements=10, startNumber=2):
    """
    Peakable array is guaranteed that the first and last elements are lower than all others.
    """
    import random

    array = [x for x in range(startNumber, number_of_elements)]
    random.shuffle(array)
    array.insert(0, startNumber - 2)
    array.append(startNumber - 1)

    return array


def main():
    array = [0, 3, 9, 5, 4, 1]
    print(', '.join([str(x) for x in array]), 'Result', find_peak(array))

    array = generate_peakable()
    print('Random array')
    print(', '.join([str(x) for x in array]), 'Result', find_peak(array))


if __name__ == '__main__':
    main()
