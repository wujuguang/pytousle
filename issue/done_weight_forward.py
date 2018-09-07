# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function
from collections import Counter

"""
Done Weight Forward, 按出现权重排序.
"""


def done_weight_forward(lst):
    """出现次数越多越靠前.
    """
    if not lst:
        return None

    counter = {}
    for i in lst:
        counter[i] = counter.get(i, 0) + 1

    counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    return "".join([k * v for k, v in counter])


def done_weight_another(lst):
    """可以使用Counter类实现.
    """
    if not lst:
        return None

    counter = Counter(lst)
    counter = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    return "".join([k * v for k, v in counter])


if __name__ == "__main__":
    print(done_weight_forward("meeting"))
    print(done_weight_forward("goodness"))
    print(done_weight_another("goodness"))
