#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 322.Coin Change.py
@time: 18-6-24 下午6:12
@version: v1.0 
"""


# 322. Coin Change (https://leetcode.com/problems/coin-change/description/)

class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = {key: float("inf") for key in range(1, amount + 1)}     # 初始化币值所需最少币数字典，初始值为infity
        d[0] = 0    # 0元需要的币数为0

        for value in range(1, amount + 1):          # 从1开始遍历所有币值

            for coin in coins:              # 遍历所有可选币值
                if value - coin >= 0 and d[value - coin] + 1 < d[value]:   # 如果币值大于可选币值并且所用的币数更少，则更新对应的币数
                    d[value] = d[value - coin] + 1
        return d[amount] if d[amount] != float("inf") else -1


sol = Solution()
print(sol.coinChange([2, 5], 3))
