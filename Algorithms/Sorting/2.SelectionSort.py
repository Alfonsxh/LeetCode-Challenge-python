#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 2.SelectionSort.py
@time: 18-6-3 下午3:15
@version: v1.0 
"""

from Algorithms.LogDecorator import PrintfDecorator


# 选择排序

def FindMinNumber(srcList: list) -> (int, int):
    minIndex = 0
    minValue = srcList[0]
    for index, value in enumerate(srcList):
        if minValue > value:
            minIndex = index
            minValue = value
    return minIndex, minValue


@PrintfDecorator
def SelectionSort(srcList: list) -> list:
    for i in range(len(srcList)):
        minIndex, minValue = FindMinNumber(srcList[i:])
        srcList[i], srcList[i + minIndex] = srcList[i + minIndex], srcList[i]
    return srcList


if __name__ == "__main__":
    srcList_1 = [3, 1, 5, 5, 5, 5, 5, 7, 2, 4, 9, 6]
    SelectionSort(srcList_1)
    # print("SelectionSort({srcList_1}) ----> ".format(srcList_1=srcList_1), SelectionSort(srcList_1))
