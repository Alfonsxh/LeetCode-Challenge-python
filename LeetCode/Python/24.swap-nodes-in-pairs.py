#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        node_list = list()
        while head:
            node_list.append(head)
            head = head.next

        # 分为奇列表和偶列表,末尾节点补None为了方便
        odd_list = node_list[::2] + [None]
        even_list = node_list[1::2] + [None]

        # 头为偶列表的第一个节点
        # 重排的顺序为： even[0] -> odd[0] -> even[1] -> odd[1] -> ....
        result = even_list[0]
        for i in range(len(even_list) - 1):
            even_list[i].next = odd_list[i]
            odd_list[i].next = even_list[i + 1] if even_list[i + 1] else (odd_list[i + 1] if odd_list[i + 1] else None)

        return result


if __name__ == '__main__':
    PrintListNode(Solution().swapPairs(MakeListNodes([1, 2, 3, 4])))
    PrintListNode(Solution().swapPairs(MakeListNodes([1, 2, 3])))
