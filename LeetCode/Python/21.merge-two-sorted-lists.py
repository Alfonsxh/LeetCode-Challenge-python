#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr_node = dummy

        while l1 and l2:
            if l1.val > l2.val:
                curr_node.next = l2
                l2 = l2.next
            else:
                curr_node.next = l1
                l1 = l1.next

            curr_node = curr_node.next

        if l1 is None:
            curr_node.next = l2
        else:
            curr_node.next = l1

        return dummy.next


if __name__ == '__main__':
    PrintListNode(Solution().mergeTwoLists(MakeListNodes([1, 3, 4]), MakeListNodes([1, 2, 4])))
    PrintListNode(Solution().mergeTwoLists(None, None))
