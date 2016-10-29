# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Obtain the round number from a float object.
"""

import math


def int_function(float_number):
    """直接取整数 -- 取小于等于的整数.
    """
    return int(float_number)


def round_function(float_number):
    """四舍五入后取整.
    """
    return int(round(float_number))


def floor_function(float_number):
    """使用math库取整 -- 取小于等于的整数.
    """
    return int(math.floor(float_number))


def up_int_function(float_number):
    """int_function的逆反, 小数点后有值都向上取整.
    """
    int_number = int(float_number)
    if float_number > int_number:
        return int_number + 1
    else:
        return int_number


def up_int_digit_function(float_number, digit=0):
    """up_int_function扩展, 按位数都向上取整.

        3872.49 ==> 3873
        3872.49 ==> 3880
        3872.49 ==> 3900
        3872.49 ==> 4000
    """

    # 先不考虑小数部分直接取整.
    digit_seq = str(int(float_number))
    digit_len = len(digit_seq)

    together_number = 0

    digit = 0 if digit > digit_len else digit
    start_index = -1 if not digit else -digit

    for n in range(start_index, -(digit_len + 1), -1):
        abs_n = abs(n)
        if digit == abs_n:
            together_number += (int(digit_seq[n]) + 1) * 10 ** (abs_n - 1)
        else:
            together_number += int(digit_seq[n]) * 10 ** (abs_n - 1)

    return together_number


if __name__ == '__main__':
    demo_lst = [3.21, 4.43, 5.65, 6.87, 3872.49]

    for i in demo_lst:
        # print(int_function(i))
        # print(round_function(i))
        # print(floor_function(i))
        # print(up_int_function(i))
        pass

    for i in range(0, 5):
        print(up_int_digit_function(3872.49, i))
