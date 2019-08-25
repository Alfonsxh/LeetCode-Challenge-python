#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        curr_node, prev_node = head, None
        while curr_node:
            # curr_node.next, curr_node, prev_node = prev_node, curr_node.next, curr_node   # 这种方式比较耗时
            tmp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = tmp

        return prev_node


if __name__ == '__main__':
    PrintListNode(Solution().reverseList(head=MakeListNodes([1, 3, 4])))
