#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    # def reorderList(self, head: ListNode):
    #     """
    #     Do not return anything, modify head in-place instead.
    #     """
    #     node_list = list()
    #     while head:
    #         node_list.append(head)
    #         head = head.next
    #
    #     odd_num = int(len(node_list) / 2 + 1) if len(node_list) % 2 else int(len(node_list) / 2)
    #     odd_node_list = node_list[:odd_num]
    #     even_node_list = node_list[odd_num:][::-1]
    #     even_node_list.append(None) if len(odd_node_list) > len(even_node_list) else ...
    #
    #     new_node_list = list()
    #     for odd_node, even_node in zip(odd_node_list, even_node_list):
    #         new_node_list.append(odd_node)
    #         new_node_list.append(even_node)
    #
    #     new_node_list.append(None) if new_node_list and new_node_list[-1] is not None else ...
    #     length = len(new_node_list) - 1 if new_node_list else 0
    #
    #     for i in range(length):
    #         new_node_list[i].next = new_node_list[i + 1]
    #
    #     head = new_node_list[0] if new_node_list else None
    #     return head

    def reorderList(self, head: ListNode):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr_node, prev_node = slow, None
        while curr_node:
            curr_node.next, prev_node, curr_node = prev_node, curr_node, curr_node.next

        odd_head = head
        even_head = prev_node
        while even_head.next:
            odd_head.next, odd_head = even_head, odd_head.next
            even_head.next, even_head = odd_head, even_head.next
        return head


if __name__ == '__main__':
    PrintListNode(Solution().reorderList(None))
    PrintListNode(Solution().reorderList(MakeListNodes([1, 2, 3, 4])))
    PrintListNode(Solution().reorderList(MakeListNodes([1, 2, 3, 4, 5])))
