#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head

        node_list = list()
        while head:
            node_list.append(head)
            head = head.next

        index = len(node_list) - n
        if index == 0:
            return node_list[0].next
        else:
            node_list[index - 1].next = node_list[index + 1] if index + 1 < len(node_list) else None
            return node_list[0]


if __name__ == '__main__':
    PrintListNode(Solution().removeNthFromEnd(MakeListNodes([1]), 1))
    PrintListNode(Solution().removeNthFromEnd(MakeListNodes([1, 2]), 1))
    PrintListNode(Solution().removeNthFromEnd(MakeListNodes([1, 2]), 2))
    PrintListNode(Solution().removeNthFromEnd(MakeListNodes([1, 2, 3, 4, 5]), 2))
