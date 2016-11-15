# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Fibonacci Array.
"""


def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":

    fibonacci_list = []
    for i in range(0, 10):
        fibonacci_list.append(fibonacci(i))
    print(fibonacci_list)
