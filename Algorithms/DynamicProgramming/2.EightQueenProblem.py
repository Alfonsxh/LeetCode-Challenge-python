#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 2.EightQueenProblem.py
@time: 18-6-24 下午4:29
@version: v1.0 
"""

# 八皇后问题
# 在一个N*N的棋盘上放置N个皇后，每行一个并使其不能互相攻击（同一行、同一列、同一斜线上的皇后都会自动攻击）。

# 基本思路:
# 将第N个皇后摆放在第N列，首先第一个皇后摆放在(1, 1)的位置，记录第一个皇后摆放的位置，然后开始摆放第二个皇后。
# 第二个皇后遍历第二列的行，找到合适的位置进行摆放，记录第二个皇后的位置，然后开始摆放第三个皇后的位置。
# 以此类推。
# 当能够摆放第N个皇后时，计数加一。假设当前位置为(x, y)，则继续下一行y + 1，直到第N行结束。
# 类似，处理完第N个皇后的N个位置后，返回上一层，第N - 1个皇后的位置，将第N - 1个皇后的位置下移，开始遍历第N个皇后的位置。
# 如此循环，知道所有的位置都已遍历。

count = 0                   # 摆放种类计数
queenStatusRecord = list()  # 皇后位置摆放记录


def IsValid(row, col):
    """
    判断插入的位置是否能够放置皇后
    :param row: 插入的行
    :param col: 插入的列
    :return: 可以插入返回True，不可以返回False
    """
    global queenStatusRecord

    for i, j in enumerate(queenStatusRecord):                       # 遍历皇后记录列表
        if i == row or j == col or abs(i - row) == abs(j - col):    # 判断该位置是否可以插入
            return False
    return True


def Parser(queen, targetQueenNumber):
    """
    N皇后问题递归函数
    :param queen: 将要处理的第几个皇后
    :param targetQueenNumber: 皇后的总数
    :return:
    """
    global count
    global queenStatusRecord

    if queen >= targetQueenNumber:      # 如果处理到了目标皇后的数量，则摆放方法计数加1
        count += 1
        return

    for col in range(targetQueenNumber):
        if IsValid(queen, col):                     # 判断次位置是否能够放置皇后
            queenStatusRecord.append(col)           # 能够放置，则将皇后位置记录
            Parser(queen + 1, targetQueenNumber)    # 处理下一皇后的摆放位置
            queenStatusRecord.pop()                 # 处理完后，将皇后位置状态恢复


def NQueenProblem(queenNmuber):
    """
    N皇后问题
    :param queenNmuber: 皇后的数量
    :return:
    """
    Parser(0, queenNmuber)


queenNum = 8
NQueenProblem(queenNum)
print("{n} queens has {total} ways!".format(n=queenNum, total=count))

