#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from typing import List
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        # 算个节点总个数
        length = 0
        root_head = root
        while root:
            length += 1
            root = root.next

        # 平均每个块的节点数，多余的节点往前面的节点上放
        average = length // k
        div = length % k

        result = list()
        for i in range(k):
            # 1、如果有余数
            #   前面节点的个数 = 平均个数 + 1
            part_len = average + 1 if div else average
            div = div - 1 if div else div

            # 添加对应块的节点
            result.append(root_head)

            if root_head is None:
                continue

            for j in range(part_len - 1):
                root_head = root_head.next

            # 各块结束后，将末尾的节点的下一跳指向None
            root_pre = root_head
            root_head = root_head.next
            root_pre.next = None

        return result


if __name__ == '__main__':
    for part in Solution().splitListToParts(root=MakeListNodes([1, 2, 3, 4, 5, 6, 7, 8, 9]), k=10):
        PrintListNode(part)
