# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Fibonacci Array.
"""


def more_less(func):
    cache = {}

    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrap


@more_less
def fibonacci_normal(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_normal(n - 1) + fibonacci_normal(n - 2)


def fibonacci_more(n):
    a, b = 0, 1
    for _ in range(0, n - 1):
        a, b = b, a + b
    return 0 if n <= 0 else b


if __name__ == "__main__":

    fibonacci_list, fibonacci_data = [], []
    for i in range(0, 10):
        fibonacci_list.append(fibonacci_normal(i))
        fibonacci_data.append(fibonacci_more(i))

    print(fibonacci_list)
    print(fibonacci_data)
