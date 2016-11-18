# !/usr/bin/env python
# coding: utf-8

from __future__ import print_function

"""
Get Days From Date.
"""

import datetime


def get_days_from_date(str_date):
    """计算某日期为当前年中的第几天.

        :param str_date:
        :return:
    """

    date_data, format_list = None, ["%Y-%m-%d", "%Y.%m.%d", "%Y/%m/%d"]
    for fmt in format_list:
        try:
            date_data = datetime.datetime.strptime(str_date, fmt).date()
        except Exception as ex:
            print(ex)

        if date_data:
            break

    # 计算是否为闰年.
    leap_year = False
    if (date_data.year % 4 == 0 and date_data.year % 100 != 0) or date_data.year % 400 == 0:
        leap_year = True

    # 初始当前月的天数.
    total_days = date_data.day
    big_months = [1, 3, 5, 7, 8, 10, 12]

    for month in range(date_data.month - 1, 0, -1):
        # 闰年与平年二月天数.
        if month == 2:
            total_days += 29 if leap_year else 28
            continue

        # 大月与小月的天数.
        if month in big_months:
            total_days += 31
        else:
            total_days += 30

    return total_days


if __name__ == "__main__":
    print(get_days_from_date("2016-04-16"))
    print(get_days_from_date("2015/03/16"))
    print(get_days_from_date("2014.02.16"))
