# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Get Prime Number From Range.
"""


def get_prime_range(lower, upper):
    result_list = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result_list.append(num)
    return result_list


if __name__ == "__main__":
    print(get_prime_range(0, 100))
