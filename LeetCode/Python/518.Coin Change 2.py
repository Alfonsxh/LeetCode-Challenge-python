#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 518.Coin Change 2.py
@time: 18-6-24 下午6:14
@version: v1.0 
"""


# 518. Coin Change 2 (https://leetcode.com/problems/coin-change-2/description/)

class Solution:
    def change(self, amount, coins):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        d = {key: 0 for key in range(1, amount + 1)}
        d[0] = 1

        for coin in coins:
            for value in range(1, amount + 1):

                if value - coin >= 0:
                    d[value] += d[value - coin]
        return d[amount]


sol = Solution()
print(sol.change(5, [1, 2, 5]))
