#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i, n in enumerate(nums):
            if n != 0:
                nums[i], nums[index], index = nums[index], nums[i], index + 1


if __name__ == '__main__':
    nums = [0, 1, 0, 3, 12]
    # nums = [0, 0, 0, 1]
    Solution().moveZeroes(nums)
    print(nums)
