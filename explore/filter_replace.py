# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Filter And Replace.
"""


def done_filter(str_text, char):
    return ''.join(filter(lambda x: x != char, str_text))


def done_replace(str_text, char):
    return str_text.replace(char, '')


def measure():
    from timeit import repeat, default_timer

    print(repeat("done_filter(str_test,str_char)", "from __main__ import done_filter,str_char,str_test",
                 default_timer, 10, 1000))

    print(repeat("done_replace(str_test,str_char)", "from __main__ import done_replace,str_char,str_test",
                 default_timer, 10, 1000))


if __name__ == "__main__":
    str_char = ' '
    str_test = "One of my father’s greatest talents is his ability to see potential in people before they see it " \
               "in themselves. It was like that for us too, growing up. He taught us that potential vanishes into " \
               "nothing without effort. And that, like him, we each had a responsibility to work not just for " \
               "ourselves, but for the betterment of the world around us."

    print(done_filter(str_test, str_char))
    print(done_replace(str_test, str_char))

    measure()
