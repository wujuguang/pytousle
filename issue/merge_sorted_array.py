# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Merge Sorted Array.
"""

import random


def merge_sorted_array(list_one, list_two):
    sum_array = sum([len(item) for item in (list_one, list_two)])
    one_index, two_index, merge_list = 0, 0, []

    for i in range(0, sum_array):
        try:
            if list_one[one_index] < list_two[two_index]:
                merge_list.append(list_one[one_index])
                one_index += 1
            elif list_one[one_index] > list_two[two_index]:
                merge_list.append(list_two[two_index])
                two_index += 1
            else:
                merge_list.append(list_one[one_index])
                merge_list.append(list_two[two_index])
                one_index += 1
                two_index += 1

        except IndexError:
            array_dict = {one_index: list_one, two_index: list_two}
            start_index = min((one_index, two_index))
            merge_list.extend(array_dict[start_index][start_index:])
            break

    return merge_list


def merge_array(list_one, list_two):
    list_one = sorted(list_one)
    list_two = sorted(list_two)
    return merge_sorted_array(list_one, list_two)


def merge_sorted_more(*args):
    try:
        from functools import reduce
    except ImportError:
        pass

    return reduce(merge_sorted_array, args)


if __name__ == '__main__':
    def test_func():
        array_one = [random.randint(0, 1000) for _ in range(0, 10)]
        array_two = [random.randint(0, 1000) for _ in range(0, 10)]

        print("array_one: ", array_one)
        print("array_two: ", array_two)

        array_one = sorted(array_one)
        array_two = sorted(array_two)

        print("array_one sorted: ", array_one)
        print("array_two sorted: ", array_two)

        merged_data = merge_sorted_array(array_one, array_two)
        print("Merged Length:", len(merged_data))
        print("Merged Data:", merged_data)


    def test_merge():
        merged_data = merge_sorted_more(sorted([1, 7, 2]), sorted([3, 8, 5]), sorted([0, 6, 9]))
        print("More Merged Length:", len(merged_data))
        print("More Merged Data:", merged_data)


    print("-" * 40)
    test_func()
    test_merge()
    print("-" * 40)
