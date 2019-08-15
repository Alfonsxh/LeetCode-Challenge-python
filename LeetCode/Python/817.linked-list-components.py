#
# @lc app=leetcode id=817 lang=python3
#
# [817] Linked List Components
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        node_list = list()
        insert_node = None
        G_set = set(G)  # 性能提升的关键啊！set为散列结构，查找速度为o(1);列表为链式结构，查找速度为o(n)
        while head:
            if head.val in G_set:
                if insert_node is None:
                    insert_node = head
            else:
                if insert_node is not None:
                    node_list.append(insert_node)
                    insert_node = None

            head = head.next
        else:
            if insert_node is not None:
                node_list.append(insert_node)

        return len(node_list)

    def numComponents_2(self, head: ListNode, G: List[int]) -> int:
        prev_node = None
        component_num = 0
        G_set = set(G)  # 性能提升的关键啊！
        while head:
            if head.val in G_set:
                if prev_node is None or prev_node.val not in G_set:
                    component_num += 1
            prev_node = head
            head = head.next

        return component_num


if __name__ == '__main__':
    # print(Solution().numComponents(head=MakeListNodes([0, 1, 2, 3]), G=[0, 1, 3]))
    print(Solution().numComponents_2(head=MakeListNodes([0, 1, 2, 3]), G=[0, 1, 3]))
