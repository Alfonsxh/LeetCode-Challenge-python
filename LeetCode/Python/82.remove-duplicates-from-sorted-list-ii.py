#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 如果头部前两个数字相同，则去除从头开始的重复数字
        if head.val == head.next.val:
            while (head.next is not None) and (head.val == head.next.val):
                head = head.next

            return self.deleteDuplicates(head.next)
        else:
            # 如果头部前两个数字不相同，则头部的下一个节点为递归后的结果
            head.next = self.deleteDuplicates(head.next)
            return head


if __name__ == '__main__':
    PrintListNode(Solution().deleteDuplicates(MakeListNodes([1, 2, 2, 3, 3, 4, 5])))
