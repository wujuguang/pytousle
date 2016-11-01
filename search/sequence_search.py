# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Sequence Search.
"""

import random


def for_sequence_search(sequence, item):
    """For Mode.
    """
    existed = False

    for i, v in enumerate(sequence):
        if v == item:
            print(i)
            existed = True
            break
    return existed


def while_sequence_search(sequence, item):
    """While Mode.
    """
    length = len(sequence)
    index, existed = 0, False

    while index < length and not existed:
        if sequence[index] == item:
            print(index)
            existed = True
        else:
            index += 1
    return existed


if __name__ == '__main__':
    data = [random.randint(0, 1000) for _ in range(0, 100)]

    value = data[60]
    print(data)
    print(value)

    for_sequence_search(data, value)
    while_sequence_search(data, value)
