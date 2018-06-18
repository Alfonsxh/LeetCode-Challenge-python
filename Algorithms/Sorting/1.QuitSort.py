#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.QuitSort.py
@time: 18-6-3 下午3:05
@version: v1.0 
"""
from Algorithms.LogDecorator import PrintfDecorator


# 快速排序
@PrintfDecorator
def QuitSorting(srcList: list):
    if len(srcList) < 2:
        return srcList

    mid = (0 + len(srcList)) // 2
    midValue = srcList[mid]

    lowList = list()
    highList = list()
    midList = []                # 对于重复的mid都放在一起
    for i in srcList:
        if i < midValue:
            lowList.append(i)
        elif i > midValue:
            highList.append(i)
        else:
            midList.append(i)

    lst1 = QuitSorting(lowList)
    lst2 = QuitSorting(highList)
    return lst1 + midList + lst2


if __name__ == "__main__":
    srcList_1 = [3, 1, 5, 5, 5, 5, 5, 7, 2, 4, 9, 6]
    QuitSorting(srcList_1)
    # print("QuitSorting({srcList_1}) ----> ".format(srcList_1=srcList_1), QuitSorting(srcList_1))
