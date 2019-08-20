#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr_node = dummy

        tmp_list = set()
        while head:
            if head.val in tmp_list:
                head = head.next
            else:
                tmp_list.add(head.val)
                curr_node.next = head
                curr_node = curr_node.next

        curr_node.next = None

        return dummy.next


if __name__ == '__main__':
    PrintListNode(Solution().deleteDuplicates(MakeListNodes([1, 1, 2])))
    PrintListNode(Solution().deleteDuplicates(MakeListNodes([1, 1, 2, 3, 3])))
