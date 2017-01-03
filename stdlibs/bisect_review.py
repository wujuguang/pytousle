# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Bisect Modules Review.
"""

import bisect


def bisect_test():
    def bisect_view(lst):
        print(lst)

        # 排序
        lst.sort()
        print(lst)

        # 插入排序.
        bisect.insort(lst, 5)
        print(lst)

        # 返回15要插入到的位置索引.
        print(bisect.bisect(lst, 15))
        print(lst)

    def bisect_show(lst):
        print(lst)

        # 排序
        lst.sort()
        print(lst)

        # # backward compatibility:
        # bisect.insort() == bisect.insort_right()
        # bisect.bisect() == bisect.bisect_right()

        # Overwrite above definitions with a fast C implementation

        # 遇到重复值时插前或插后.
        print(bisect.bisect_left(lst, 7))
        print(bisect.bisect_right(lst, 7))
        print(lst)

        bisect.insort_left(lst, 7)
        # bisect.insort_right(lst, 4)
        print(lst)

    data_lst = [1, 8, 7, 13, 9, 18]
    bisect_view(data_lst)
    bisect_show(data_lst)


if __name__ == "__main__":
    bisect_test()
