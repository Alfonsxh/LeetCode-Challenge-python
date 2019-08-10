#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        # 先整个循环链表
        length = 1
        start = end = head
        while end.next:
            length += 1
            end = end.next
        end.next = start

        # 计算要移动的步数
        # 需要做一下转换
        right_step = length - k % length
        for _ in range(right_step):
            start = start.next
            end = end.next

        end.next = None
        return start


if __name__ == '__main__':
    PrintListNode(Solution().rotateRight(MakeListNodes([0, 1, 2]), 4))
    PrintListNode(Solution().rotateRight(MakeListNodes([1, 2, 3, 4, 5]), 2))
