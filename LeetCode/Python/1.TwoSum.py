#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 @Author  : Alfons
 @Contact: alfons_xh@163.com
 @File    : 1.TwoSum.py
 @Time    : 2018/5/28 10:55
"""


class Solution:
    # Runtime: 1092 ms
    def twoSum_1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # tmpNums = [target - num for num in nums]
        # for i in range(len(tmpNums)):
        #     tmpNum = tmpNums[i]
        #     if tmpNum in nums and nums.index(tmpNum) != i:
        #         return sorted([i, nums.index(tmpNum)])
        # return None

        for i in range(len(nums)):
            leftNum = nums[i]
            rightNum = target - leftNum
            if rightNum in nums and nums.index(rightNum) != i:
                return [i, nums.index(rightNum)]
        return None

    # Runtime: 40 ms
    def twoSum_2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if target % 2 == 0 and nums.count(target / 2) == 2:
            tmpNums = list(nums)
            tmpNums[nums.index(target / 2)] = target / 2 + 1
            return [nums.index(target / 2), tmpNums.index(target / 2)]
        tmpNums = [target - num for num in nums if target != 2 * num]
        numSet = set(nums) & set(tmpNums)
        return sorted([nums.index(list(numSet)[0]), nums.index(list(numSet)[1])])

    # Runtime:  3248 ms
    def twoSum_3(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            leftNum = nums[i]
            rightNum = target - leftNum
            for j in range(i + 1, len(nums)):
                if nums[j] == rightNum:
                    return [i, j]
        return None

    # Runtime: 1080 ms
    def twoSum_4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            leftNum = nums[i]
            rightNum = target - leftNum
            if rightNum in nums and i != nums.index(rightNum):
                return sorted([i, nums.index(rightNum)])
        return None


if __name__ == "__main__":
    sol = Solution()
    print("sol.twoSum_1:", sol.twoSum_1([1, 2, 3, 5, 5, 6], 10))
    print("sol.twoSum_2:", sol.twoSum_2([5, 5], 10))
    print("sol.twoSum_2:", sol.twoSum_2([-1, 2, 3, 4, 5, 12, 11], 10))
    print("sol.twoSum_3:", sol.twoSum_3([-1, 2, 3, 4, 5, 12, 11], 10))
    print("sol.twoSum_4:", sol.twoSum_4([3, 2, 4], 6))
