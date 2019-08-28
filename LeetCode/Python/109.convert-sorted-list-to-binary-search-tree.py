#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "<TreeNode val={val}, left={left}, right={right}>".format(val=self.val, left=self.left, right=self.right)


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        elif head.next is None:         # head的下一个节点为None，则它为叶子节点
            return TreeNode(head.val)

        fast_node = slow_node = pre_node = head     # pre_node用来记录中间那个节点的前一个节点
        while fast_node and fast_node.next:
            pre_node = slow_node
            fast_node, slow_node = fast_node.next.next, slow_node.next

        pre_node.next = None        # 将中间节点父节点的子节点截断

        root = TreeNode(slow_node.val)      # root节点为中间节点
        root.left = self.sortedListToBST(head)      # 递归左节点
        root.right = self.sortedListToBST(slow_node.next)   # 递归右节点

        return root


if __name__ == '__main__':
    # res = Solution().sortedListToBST(None)
    # res = Solution().sortedListToBST(MakeListNodes([-10, -3, 0, 5, 9]))
    res = Solution().sortedListToBST(MakeListNodes([-93, -89, -85, -76, -56, -53, -20, -10, 20, 28, 41, 50, 66, 70, 87, 88, 91, 94]))
    pass
