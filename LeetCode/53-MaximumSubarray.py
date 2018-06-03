#!/usr/bin/env python
# encoding: utf-8
"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 53-MaximumSubarray.py
@time: 18-6-4 上午12:16
@version: v1.0 
"""


class Solution:
    def maxSubArray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxNum = nums[0]
        for i in range(len(nums)):
            n = i + 1
            sonMaxNum = sum(nums[:n])
            for index, value in enumerate(nums):
                sonMaxNum = max(sonMaxNum, sum(nums[index: index + n]))
            maxNum = max(maxNum, sonMaxNum)
        return maxNum

    def maxSubArray_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sonMaxNum = maxNum = nums[0]
        for i in nums[1:]:
            sonMaxNum = max(i, sonMaxNum + i)
            maxNum = max(maxNum, sonMaxNum)
        return maxNum


if __name__ == "__main__":
    srcList_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    srcList_2 = [-64, 78, 56, 10, -8, 26, -18,
                 47, -31, 75, 89, 13, 48, -19,
                 -69, 36, -39, 55, -5, -4, -15,
                 -37, -27, -8, -5, 35, -51, 83,
                 21, -47]
    sol = Solution()
    print(sol.maxSubArray_1(srcList_1))
    print(sol.maxSubArray_1(srcList_2))

    print(sol.maxSubArray_2(srcList_1))
    print(sol.maxSubArray_2(srcList_2))
