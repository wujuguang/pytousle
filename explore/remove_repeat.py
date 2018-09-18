# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Remove Repeat Value, 去重复值操作技巧.
"""


def remove_repeat_loop(lst):
    """传统去重.

        :param lst:
        :return:
    """
    result = []
    for item in lst:
        if item not in result:
            result.append(item)

    return result


def remove_repeat_set(lst):
    """Set去重.

        :param lst:
        :return:
    """

    result = list(set(lst))
    result.sort(key=lst.index)  # 保持原来的顺序
    return result


def remove_repeat_dict_keys(lst):
    """利用Dict的Key唯一性去重.

        :param lst:
        :return:
    """

    # print({}.fromkeys(lst))
    result = list({}.fromkeys(lst).keys())
    result.sort(key=lst.index)  # 保持原来的顺序
    return result


def measure():
    from timeit import repeat, default_timer

    print(repeat("remove_repeat_loop(data_test)",
                 "from __main__ import remove_repeat_loop,data_test",
                 default_timer, 5, 100000))

    print(repeat("remove_repeat_set(data_test)",
                 "from __main__ import remove_repeat_set,data_test",
                 default_timer, 5, 100000))


if __name__ == "__main__":
    data_test = [3, 2, 4, 5, 1, 3]
    print(remove_repeat_loop(data_test))
    print(remove_repeat_set(data_test))
    print(remove_repeat_dict_keys(data_test))

    measure()

    # Output:
    # [0.8181600299999445, 0.7662495469999158, 0.8624386200001481,
    # 0.7982522950001112, 0.7769615830000021]
    # [0.9371358149999196, 0.9058971229999315, 0.9129523950000475,
    # 0.9347492450001482, 0.9102671699999973]

    # 注释result.sort(key=lst.index)
    # [0.8478895690000172, 0.8177765360001104, 0.8040043600001354,
    # 0.8050430119999419, 0.867980063999994]
    # [0.7031611060001524, 0.6909822049999548, 0.6870315969999865,
    # 0.6852257990001362, 0.6912917110000762]
