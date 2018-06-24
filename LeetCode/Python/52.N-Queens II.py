#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 52.N-Queens II.py
@time: 18-6-24 下午6:02
@version: v1.0 
"""

# 52. N-Queens II (https://leetcode.com/problems/n-queens-ii/description/)


class Solution:
    def __init__(self):
        self.__count = 0  # 摆放种类计数
        self.__queenStatusRecord = list()  # 皇后位置摆放记录

    def __IsValid(self, row, col):
        """
        判断插入的位置是否能够放置皇后
        :param row: 插入的行
        :param col: 插入的列
        :return: 可以插入返回True，不可以返回False
        """
        for i, j in enumerate(self.__queenStatusRecord):  # 遍历皇后记录列表
            if i == row or j == col or abs(i - row) == abs(j - col):  # 判断该位置是否可以插入
                return False
        return True

    def __Parser(self, queen, targetQueenNumber):
        """
        N皇后问题递归函数
        :param queen: 将要处理的第几个皇后
        :param targetQueenNumber: 皇后的总数
        :return:
        """
        if queen >= targetQueenNumber:  # 如果处理到了目标皇后的数量，则摆放方法计数加1
            self.__count += 1
            return

        for col in range(targetQueenNumber):
            if self.__IsValid(queen, col):  # 判断次位置是否能够放置皇后
                self.__queenStatusRecord.append(col)  # 能够放置，则将皇后位置记录
                self.__Parser(queen + 1, targetQueenNumber)  # 处理下一皇后的摆放位置
                self.__queenStatusRecord.pop()  # 处理完后，将皇后位置状态恢复

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.__Parser(0, targetQueenNumber=n)
        return self.__count


sol = Solution()
print(sol.totalNQueens(4))
