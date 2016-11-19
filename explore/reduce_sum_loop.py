# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

import six

"""
Reduce And Sum And Loop.
"""


def string_number_begin(str_number):
    total = 0
    for i in [int(n) for n in str(str_number)]:
        total += i
    return total


def string_number_first(str_number):
    return sum([int(n) for n in str(str_number)])


def string_number_second(str_number):
    return six.moves.reduce(lambda x, y: x + y, [int(n) for n in str(str_number)])


def measure():
    from timeit import repeat, default_timer

    print(repeat("string_number_begin(number_test)", "from __main__ import string_number_begin,number_test",
                 default_timer, 5, 10000))

    print(repeat("string_number_first(number_test)", "from __main__ import string_number_first,number_test",
                 default_timer, 5, 100000))

    print(repeat("string_number_second(number_test)", "from __main__ import string_number_second,number_test",
                 default_timer, 5, 100000))


if __name__ == "__main__":
    number_test = 123456789987654321

    print(string_number_begin(number_test))
    print(string_number_first(number_test))
    print(string_number_second(number_test))

    measure()

    # Output:
    # [0.24294102600015322, 0.21061783799996192, 0.20670399099981296, 0.2043759729995145, 0.23155067100015003]
    # [1.8176962969992019, 1.8886838720000014, 1.778694713000732, 1.8508639309993669, 1.7824996339995778]
    # [10.833690077000028, 10.729063573999156, 10.708194968000498, 10.786578866000127, 10.897213588999875]
