#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreeNode val={val}, left={left}, right={right}>".format(val=self.val, left=self.left, right=self.right)


from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        elif len(nums) == 1:
            return TreeNode(nums[0])

        mid_index = len(nums) // 2

        root = TreeNode(nums[mid_index])
        root.left = self.sortedArrayToBST(nums[0:mid_index])
        root.right = self.sortedArrayToBST(nums[mid_index + 1:])

        return root


if __name__ == '__main__':
    res = Solution().sortedArrayToBST([-93, -89, -85, -76, -56, -53, -20, -10, 20, 28, 41, 50, 66, 70, 87, 88, 91, 94])
    pass
