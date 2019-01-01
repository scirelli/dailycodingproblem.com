#!/usr/bin/env python3
import random

count = 0

def choose_from_stream(item):
    global count
    rtn = None

    count += 1

    if count == 1:
        rtn = item
    else:
        choice = random.randrange(count + 1)
        if choice == count:
            rtn = item

    return rtn

range_size = 100
for s in range(range_size):
    lst = []
    count = 0
    for n in range(range_size):
        c = choose_from_stream(n)
        if c is not None:
            lst.append(c)
    print(f'Chose from {range_size} items of stream.')
    print(lst)
