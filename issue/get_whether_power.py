# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Get Whether Power.
"""
import sys

sys.setrecursionlimit(10000)


def get_whether_power(number, base):
    if number == 1 or number == base:
        result = True
    elif 1 < number < base:
        result = False
    else:
        result = get_whether_power(number / base, base)

    return result


if __name__ == "__main__":
    print(get_whether_power(1, 3))
    print(get_whether_power(3, 3))
    print(get_whether_power(9, 3))
    print(get_whether_power(27, 3))
    print(get_whether_power(36, 3))
    print(get_whether_power(37, 3))
    print(get_whether_power(81, 3))
    print(get_whether_power(28, 3))
