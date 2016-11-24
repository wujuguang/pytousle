# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Bucket Sorted.
"""

import random


def bucket_sort(lst, max_number):
    bucket_list = [None] * max_number
    print(bucket_list)
    # bucket_list = [None for _ in range(0, max_number + 1)]
    for i in range(0, len(lst)):
        bucket_list[lst[i]] = lst[i]
    return bucket_list


if __name__ == '__main__':
    def test_func():
        int_list = [random.randint(0, 10) for _ in range(0, 10)]
        max_number = max(int_list)

        print(int_list)
        bucket_data = bucket_sort(int_list, max_number)
        bucket_data = list(filter(lambda x: x, bucket_data))
        print(bucket_data)


    print("-" * 40)
    test_func()
    print("-" * 40)
