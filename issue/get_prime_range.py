# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

from math import sqrt

"""
Get Prime Number From Range. 质数大于等于2 不能被它本身和1以外的数整除
"""


def get_prime_range(lower, upper):
    """概念版.

        :param lower:
        :param upper:
        :return:
    """
    result_list = []
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                result_list.append(num)
    return result_list


def get_prime_range_mode(n):
    """网上另个思路.

        基本判断思路:
        在一般领域, 对正整数n, 如果用2到n的平方根之间的所有整数去除, 均无法整除,则n为质数.

        :param n:
        :return:
    """

    list_num = []
    for i in range(2, n):
        for num in range(2, int(sqrt(n)) + 1):
            if i % num == 0 and i != num:
                break
            elif i % num != 0 and num == int(sqrt(n)):
                list_num.append(i)
    return list_num


if __name__ == "__main__":
    print(get_prime_range(0, 100))
    print(get_prime_range_mode(100))
