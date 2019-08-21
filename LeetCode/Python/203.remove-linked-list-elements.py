#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node_list = list()

        while head:
            if head.val != val:
                node_list.append(head)

            head = head.next

        length = len(node_list)
        node_list.append(None)
        for index in range(length):
            node_list[index].next = node_list[index + 1] if node_list[index] else ...

        return node_list[0]


if __name__ == '__main__':
    # PrintListNode(Solution().removeElements(head=MakeListNodes([1, 3, 4, 6, 4, 8, 4]), val=4))
    # PrintListNode(Solution().removeElements(head=MakeListNodes([1, 3, 4, 6, 4, 8]), val=4))
    PrintListNode(Solution().removeElements(head=None, val=4))
