#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        node_list = list()
        while head:
            node_list.append(head)
            head = head.next

        node_list.sort(key=lambda x: x.val)

        length = len(node_list)
        node_list.append(None)

        for index in range(length):
            node_list[index].next = node_list[index + 1]

        return node_list[0]


if __name__ == '__main__':
    PrintListNode(Solution().sortList(None))
    PrintListNode(Solution().sortList(MakeListNodes([4, 2, 1, 3])))
