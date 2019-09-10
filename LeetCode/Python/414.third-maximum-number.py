#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_set = set(nums)

        if len(nums_set) < 3:
            return max(nums_set)

        max_num = 0
        for i in range(3):
            max_num = max(nums_set)
            nums_set.remove(max_num)

        return max_num


if __name__ == '__main__':
    print(Solution().thirdMax([3, 2, 1]))
    print(Solution().thirdMax([2, 1]))
    print(Solution().thirdMax([3, 2, 2, 1]))
    print(Solution().thirdMax([3, 4, 5, 2, 1]))
