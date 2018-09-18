# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
sorted skill, 排序相关小技巧.
"""


def demo():
    """
    Python排序题，排序从小写,大写,奇数,偶数.
    https://ask.csdn.net/questions/391802

    sorted是根据key函数来排序. key函数返回元组, 元组前面的元素越大, 就排在越后.
    例如:(False,True,False)就排在(False,False,True)后面(True(1) > False(0))

    两种方法还是有些区别: lambda x:(x.isdigit() and int(x)%2==0, x.isdigit(),x.isupper(),x.islower(),x)))
    这个的含义是: 数字中的偶数为大, 数字为大, 大写字母为大,小写字母为大, 根据字符串比较.

    lambda c: (c.isdigit() - c.islower(), c in '02468', c))
    这种是: 数字为大,小写字母最小, 偶数为大, 根据字符串比较.
    只有数字和字母两种是一样的结果.
    如果还有其他字符,就有区别,第2种小写字母总会排前面.第1种小写字母会排在其他非数字字母字符后面.
    """
    print(sorted(input(), key=lambda x: (x.isdigit() and int(x) % 2 == 0, x.isdigit(), x.isupper(), x.islower(), x)))
    print(sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')


def done_number_sorted():
    """原始/朴素/低效方式.
    整数混合有正负0, 实现如下输入排序：[0, 2, 3, 4, -2, -3, -4]
    """

    lst = [3, -2, 0, 2, -3, -4, 4]

    x = list(sorted(filter(lambda i: i >= 0, lst)))
    y = list(sorted(filter(lambda i: i < 0, lst), reverse=True))
    return x + y


def done_number_simple():
    """利用key函数技巧方式.
    整数混合有正负0, 实现如下输入排序：[0, 2, 3, 4, -2, -3, -4]

    知识点: key函数返回的可是个元组,其顺序是排序规则.
    """

    lst = [3, -2, 0, 2, -3, -4, 4]
    return sorted(lst, key=lambda i: (i < 0 and abs(i) ** 2, i >= 0 and i))


if __name__ == "__main__":
    print(done_number_simple())
