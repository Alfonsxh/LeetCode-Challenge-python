#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        max_num = len(nums) + 1

        for i in range(1, max_num + 1):
            if i not in nums:
                return i
        return max_num


if __name__ == '__main__':
    print(Solution().firstMissingPositive([1, 2, 0]))
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([7, 8, 9, 11, 12]))
