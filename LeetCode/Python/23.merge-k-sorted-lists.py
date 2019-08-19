#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     node_heapq = list()
    #
    #     # 将k组节点的头节点加入堆中
    #     for head in lists:
    #         node_heapq.append(head) if head else ...
    #
    #     res_head, res = None, None
    #     while node_heapq:
    #         small_one = min(node_heapq, key=lambda n: n.val)        # 自己模拟了小顶堆的实现
    #         node_heapq.remove(small_one)
    #
    #         if res is None:
    #             res = small_one
    #             res_head = res
    #         else:
    #             res.next = small_one
    #             res = res.next
    #
    #         # 堆中加入出堆节点的下一个节点
    #         node_heapq.append(small_one.next) if small_one.next is not None else ...
    #
    #     return res_head

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue

        node_queue = PriorityQueue()
        for index, node in enumerate(lists):
            node_queue.put((node.val, index, node)) if node else ...

        dummy = ListNode(0)
        curr_node = dummy
        while not node_queue.empty():
            _, index, tmp_node = node_queue.get()       # 使用优先队列

            curr_node.next = tmp_node
            curr_node = curr_node.next

            node_queue.put((tmp_node.next.val, index, tmp_node.next)) if tmp_node.next else ...

        return dummy.next


if __name__ == '__main__':
    PrintListNode(Solution().mergeKLists([
        MakeListNodes([1, 4, 5]),
        MakeListNodes([1, 3, 4]),
        MakeListNodes([2, 6])
    ]))

    PrintListNode(Solution().mergeKLists([
        None
    ]))
