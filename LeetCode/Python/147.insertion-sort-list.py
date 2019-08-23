#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        node_list = list()
        while head:
            node_list.append((head.val, head))
            head = head.next

        node_list.sort(key=lambda x: x[0])

        length = len(node_list)
        node_list.append((0, None))

        for index in range(length):
            node_list[index][1].next = node_list[index + 1][1]

        return node_list[0][1]


if __name__ == '__main__':
    PrintListNode(Solution().insertionSortList(None))
    PrintListNode(Solution().insertionSortList(MakeListNodes([4, 2, 1, 3])))
