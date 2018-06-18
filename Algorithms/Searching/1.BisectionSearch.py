#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.BisectionSearch.py
@time: 18-6-3 下午2:36
@version: v1.0 
"""

from Algorithms.LogDecorator import PrintfDecorator


# 二分法查找

# 非递归方式
@PrintfDecorator
def Bisection_1(targetList: list, target: int):
    if target < targetList[0] or target > targetList[-1]:
        return None

    low = 0
    high = len(targetList)
    while True:
        mid = (low + high) // 2
        if targetList[mid] < target:
            low = mid
        elif targetList[mid] > target:
            high = mid
        else:
            return mid


# 递归方式
@PrintfDecorator
def Bisection_2(targetList: list, target: int):
    if target < targetList[0] or target > targetList[-1]:
        return None

    low = 0
    high = len(targetList)
    mid = (low + high) // 2
    midValue = targetList[mid]
    if midValue < target:
        res = mid + Bisection_2(targetList[mid:], target)
        return res
    elif midValue > target:
        res = mid - Bisection_2(targetList[:mid], target)
        return res
    else:
        return mid


if __name__ == "__main__":
    intLst_1 = [3, 5, 11, 17, 21, 23, 28, 30, 32, 50, 64, 78, 81, 95, 101]
    intLst_2 = [3]
    print("*" * 32 + "使用非递归方式" + "*" * 32)
    Bisection_1(intLst_1, 81)
    Bisection_1(intLst_2, 81)

    print("*" * 32 + "使用递归方式" + "*" * 32)
    Bisection_2(intLst_1, 81)
    Bisection_2(intLst_2, 81)
