# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Bubble Sort.
"""


def bubble_sort(lists):
    print(lists)
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                print(lists)

    return lists


if __name__ == "__main__":
    lst = [6, 5, 3, 9, 7, 2]

    bubble_sort(lst)
