#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 1.CoinsProblem.py
@time: 18-6-24 下午4:29
@version: v1.0 
"""

# 《凑硬币》
# 如果我们有面值为1元、3元和5元的硬币若干枚，如何用最少的硬币凑够11元？

# 基本思路：
#   用d(n)表示凑够n元所需的最少硬币数，其中d(1)、d(3)、d(5)为最小单位，均为1。
#   要计算11元，便是计算d(11)。
#   d(11)是根据 min{d(10) + d(1), d(8) + d(3), d(6) + d(5)}得到。
#   所以呢，先要计算前面的币值所需的硬币数目。

from Algorithms.LogDecorator import PrintfDecorator

coinsList = [1, 3, 5]  # 能使用的硬币枚举
coinsNeed = dict()  # 各币值所需的硬币数量记录


@PrintfDecorator
def CoinsCount(targetValue):
    """
    计算目标币值所需的最少的硬币数量
    :param targetValue: 目标币值
    :return: 目标币值所需的最少的硬币数量
    """
    coinsNeed[0] = 0  # 初始化0元所需的硬币数量为0
    for value in range(1, targetValue + 1):  # 从1元开始算起
        coinsNeed[value] = float("inf")  # 初始化该面值所需的硬币数为无穷大

        for coin in coinsList:  # 遍历枚举的硬币
            if value - coin >= 0 and coinsNeed[value - coin] + 1 < coinsNeed[value]:  # 如果满足条件，则更新该面值所需的最少硬币数
                coinsNeed[value] = coinsNeed[value - coin] + 1
    return coinsNeed[targetValue]


CoinsCount(11)
print(coinsNeed)
