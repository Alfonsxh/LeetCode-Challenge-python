"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 198. House Robber.py
@time: 18-12-19 下午9:37
@version: v1.0 
"""


class Solution(object):
    def rec_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)

        return max(self.rec_rob(nums[:-1]), self.rec_rob(nums[:-2]) + nums[len(nums) - 1])

    def dp_rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) <= 2:
            return max(nums)

        a = nums[0]
        b = nums[1]

        for i in range(len(nums) - 2):
            tmp = max(b, a + nums[i + 2])
            a = max(a, b)
            b = tmp

        return b


if __name__ == '__main__':
    sol = Solution()
    print(sol.rec_rob([2, 1, 1, 2]))
    print(sol.dp_rob([2, 1, 1, 2]))
