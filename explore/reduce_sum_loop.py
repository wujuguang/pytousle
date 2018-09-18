# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import six

"""
Reduce And Sum And Loop, 叠加运算技巧.
"""


def string_number_begin(str_number):
    total = 0
    for i in [int(n) for n in str(str_number)]:
        total += i
    return total


def string_number_first(str_number):
    return sum([int(n) for n in str(str_number)])


def string_number_second(str_number):
    return six.moves.reduce(lambda x, y: x + y,
                            [int(n) for n in str(str_number)])


def measure():
    from timeit import repeat, default_timer

    print(repeat("string_number_begin(number_test)",
                 "from __main__ import string_number_begin,number_test",
                 default_timer, 5, 100000))

    print(repeat("string_number_first(number_test)",
                 "from __main__ import string_number_first,number_test",
                 default_timer, 5, 100000))

    print(repeat("string_number_second(number_test)",
                 "from __main__ import string_number_second,number_test",
                 default_timer, 5, 100000))


if __name__ == "__main__":
    number_test = 123456789987654321

    print(string_number_begin(number_test))
    print(string_number_first(number_test))
    print(string_number_second(number_test))

    measure()

    # Output:
    # [2.2799589440001, 2.0079793410000093, 2.0750300690001495,
    # 2.0442105989998254, 2.076502313999981]
    # [1.8881973420000122, 1.7981703399998423, 2.125046164999958,
    # 2.2998939139999948, 2.221084977999908]
    # [12.539034508999976, 13.183137703000057, 11.469514520999837,
    # 11.372206390999963, 10.994613625000056]
