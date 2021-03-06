# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Quick Sort.
"""


def quick_sort(lists, left, right):
    if left >= right:
        return lists

    key = lists[left]
    low = left
    high = right

    while left < right:
        while left < right and lists[right] >= key:
            right -= 1

        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1

        lists[right] = lists[left]

    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, left + 1, high)

    return lists


if __name__ == "__main__":
    lst = [6, 5, 3, 9, 7, 2]

    print(quick_sort(lst, 0, len(lst) - 1))
