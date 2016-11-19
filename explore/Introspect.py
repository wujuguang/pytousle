# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Introspect.
"""


def correct_type_check(n):
    """判断数据为int类型的方式.

        :param n:
        :return:
    """
    # print(n - int(n) == 0)  # 错误

    print("-" * 20)
    print(type(n))

    print(type(n) == int)
    print(type(n).__name__ == 'int')
    print(isinstance(n, int))


if __name__ == "__main__":
    for item in [8, 'v', None, True, False, (), [], {}]:
        correct_type_check(item)
