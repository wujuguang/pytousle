# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Binary Search.
"""

import random


def while_binary_search(sequence, item):
    """While Mode.
    """

    head_index = 0
    foot_index = len(sequence) - 1
    while head_index <= foot_index:
        middle = (foot_index + head_index) / 2
        if item == sequence[middle]:
            print("Found: %s; Index: %s.", (str(item), str(middle)))
            return middle
        elif item > sequence[middle]:
            head_index = middle + 1
        elif item < sequence[middle]:
            foot_index = middle - 1

    print("Not Found!")
    return -1


def recursion_binary_search(sequence, item):
    """Recursion Mode.
    """

    head_index = 0
    foot_index = len(sequence) - 1

    if head_index > foot_index:
        return -1

    middle = (foot_index + head_index) / 2
    if item == sequence[middle]:
        print("Found: %s; Index: %s.", (str(item), str(middle)))
        return middle
    elif item > sequence[middle]:
        return recursion_binary_search(sequence[middle + 1:foot_index], item)
    elif item < sequence[middle]:
        return recursion_binary_search(sequence[head_index:middle - 1], item)

    print("Not Found!")
    return -1


if __name__ == '__main__':
    data = [random.randint(0, 1000) for _ in range(0, 10)]

    data = sorted(data)
    value = data[6]

    print(data)
    print(value)

    print("-" * 40)
    # while_binary_search(data, value)
    print("-" * 40)
    recursion_binary_search(data, value)
