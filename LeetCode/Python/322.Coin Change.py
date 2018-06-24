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
        d = dict()
        d[0] = 0

        for value in range(1, amount + 1):
            d[value] = float("inf")

            for coin in coins:
                if value - coin >= 0 and d[value - coin] + 1 < d[value]:
                    d[value] = d[value - coin] + 1
        return d[amount] if d[amount] != float("inf") else -1


sol = Solution()
print(sol.coinChange([2, 5], 3))
