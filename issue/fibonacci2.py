# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Fibonacci Array, python2下传统实现.
"""


def more_less(func):
    """装饰器缓存中间重复计算."""
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@more_less
def fibonacci_normal(n):
    """基本形式, 可加缓存改良."""
    if n < 2:
        return n
    else:
        return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)


if __name__ == "__main__":
    fibonacci_list = []
    for i in range(0, 10):
        fibonacci_list.append(fibonacci_normal(i))

    print(fibonacci_list)
