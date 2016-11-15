# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Obtain the repeat data from a list object.
"""


def get_repeat_loop_cmp(lst):
    """取出重复数据(先排序,后遍历,比较相邻数).

        :param lst:
        :return:
    """

    if not lst:
        return None

    x, result = None, []
    lst = sorted(lst)
    for i in lst:
        if x is not None and i == x:
            result.append(i)
        x = i
    return result


def get_repeat_loop_count(lst):
    """取出重复数据(先去重,后遍历,使用count计算原序列中该元素数量).

        :param lst:
        :return:
    """

    if not lst:
        return None

    result = []
    only_lst = set(lst)
    for i in only_lst:
        if lst.count(i) > 1:
            result.append(i)
    return result


def get_repeat_loop_in(lst):
    """取出重复数据(小时候捡豆法,先遍历,往好坏两个容器分别扔).

        :param lst:
        :return:
    """

    if not lst:
        return None

    repeat_lst, unique_lst = [], []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
            continue
        repeat_lst.append(i)
    return repeat_lst


def test(data_lst):
    print(get_repeat_loop_cmp(data_lst))
    print(get_repeat_loop_count(data_lst))
    print(get_repeat_loop_in(data_lst))


def measure():
    from timeit import repeat, default_timer

    print(repeat("get_repeat_loop_cmp(demo_lst)", "from __main__ import get_repeat_loop_cmp,demo_lst",
                 default_timer, 10, 10000))

    print(repeat("get_repeat_loop_count(demo_lst)", "from __main__ import get_repeat_loop_count,demo_lst",
                 default_timer, 10, 10000))

    print(repeat("get_repeat_loop_in(demo_lst)", "from __main__ import get_repeat_loop_in,demo_lst",
                 default_timer, 10, 10000))


if __name__ == '__main__':
    demo_lst = [1, 2, 7, 2, 3, 4, 5, 5, 6]
    test(demo_lst)
    # measure()
