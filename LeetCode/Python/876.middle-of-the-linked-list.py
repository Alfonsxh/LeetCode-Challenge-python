#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return

        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == '__main__':
    PrintListNode(Solution().middleNode(MakeListNodes([1])))
    PrintListNode(Solution().middleNode(MakeListNodes([1, 2, 3, 4])))
    PrintListNode(Solution().middleNode(MakeListNodes([1, 2, 3, 4, 5])))
