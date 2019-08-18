#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head

        less_part = list()
        great_part = list()

        while head:
            if head.val < x:
                less_part.append(head)
            else:
                great_part.append(head)

            head = head.next

        part_list = less_part + great_part + [None]
        for i in range(len(part_list) - 1):
            part_list[i].next = part_list[i + 1]

        return part_list[0]


if __name__ == '__main__':
    PrintListNode(Solution().partition(MakeListNodes([1, 4, 3, 2, 5, 2]), 3))
