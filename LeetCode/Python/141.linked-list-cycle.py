#
# @lc app=leetcode id=141 lang=python
#
# [141] Linked List Cycle
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # 两个索引，一步和两步跳，如果两步跳追上了一步跳，则说明有回环
        one_step_node = two_step_node = head

        while one_step_node and two_step_node:
            try:
                one_step_node = one_step_node.next
                two_step_node = two_step_node.next.next

                if one_step_node == two_step_node:
                    return True
            except:
                return False

        return False
