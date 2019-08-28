#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        tmp_list = [0 for _ in range(len(nums))]
        for n in nums:
            tmp_list[n - 1] = 1

        res = list()
        for index, n in enumerate(tmp_list):
            if n == 0:
                res.append(index + 1)

        return res


if __name__ == '__main__':
    print(Solution().findDisappearedNumbers([]))
    print(Solution().findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
