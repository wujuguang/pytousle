# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Bit By Bit, 知识的点点滴滴.
"""


def lookup_data_type():
    """推导式相关, 容易tuple/set混淆.

    常见的几种推导式：
        列表推导式： x = [i for i in range(5)]
        字典推导式： y = {i: i**2 for i in range(5)}
        生成器推导： z = (i for i in range(5))

        集合非字典：　{0, 1, 2, 3, 4}

    知识点: 特别注意地方(i for i in range(5))不是个元组,是个生成器.
    """
    x = (0, 1, 2, 3, 4)
    print("x", type(x))

    y = {0, 1, 2, 3, 4}
    print("y", type(y))

    z = (i for i in range(5))
    print("z", type(z))


def lookup_data_multiple():
    """3的倍数输出Fizz, 5的倍数输出Bizz, 否则输出原始数字.
    """

    result = []
    for i in range(101):
        result.append("Fizz"[i % 3 * 4::] + "Bizz"[i % 5 * 4::] or i)

    return result


if __name__ == "__main__":
    lookup_data_type()
    print(lookup_data_multiple())
