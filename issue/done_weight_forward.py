# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Done Weight Forward.
"""


def done_weight_forward(lst):
    """出现次数越多越靠前.

        :param lst:
        :return:
    """
    if not lst:
        return None

    counter = {}
    for i in lst:
        counter[i] = counter.get(i, 0) + 1

    counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    return "".join([k * v for k, v in counter])


if __name__ == "__main__":
    print(done_weight_forward("meeting"))
    print(done_weight_forward("goodness"))
