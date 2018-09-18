# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Fibonacci Array, 时间与空间优化最好.
"""


def fibonacci_more(n):
    """空间优化方案."""
    if n < 2:
        return n

    a, b = 1, 2
    for _ in range(1, n - 1):
        a, b = b, a + b
    return b


def fibonacci_try(n):
    """空间优化方案."""

    def generator():
        t, x, y = 1, 1, 2
        while True:
            yield t, x
            t, x, y = t + 1, y, x + y

    for (m, j) in generator():
        if m == n:
            return j


if __name__ == "__main__":

    fibonacci_data, fibonacci_list = [], []
    for i in range(1, 10):
        fibonacci_data.append(fibonacci_more(i))
        fibonacci_list.append(fibonacci_try(i))

    print(fibonacci_data)
    print(fibonacci_list)
