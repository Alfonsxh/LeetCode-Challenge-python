#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 将节点按k个一组，分成若干大小的列表。
        # [ [l1,l2], [l3,l4], [l5] ]
        part_list = list()
        while head:
            part = list()
            for _ in range(k):
                if head:
                    part.append(head)
                else:
                    break
                head = head.next
            part_list.append(part)

        # 反转各个组内的元素，最后一组补None，方便后续链接
        # [ [l2, l1], [l4, l3], [l5, None] ]
        for part in part_list:
            if len(part) == k:
                part.reverse()
            else:
                part.append(None)

        # 将各组元素解开，最后一个元素如果不为None，则将其next元素指向None，防止构成循环链表
        part_list_new = list()
        for part in part_list:
            part_list_new.extend(part)
        if part_list_new and part_list_new[-1] is not None:
            part_list_new[-1].next = None

        # 链接前后各个元素
        for index in range(len(part_list_new)):
            if part_list_new[index] is not None and index + 1 < len(part_list_new):
                part_list_new[index].next = part_list_new[index + 1]

        return part_list_new[0] if part_list_new else None


if __name__ == '__main__':
    PrintListNode(Solution().reverseKGroup(MakeListNodes([1, 2]), k=2))
    PrintListNode(Solution().reverseKGroup(MakeListNodes([1, 2, 3, 4, 5]), k=1))
    PrintListNode(Solution().reverseKGroup(MakeListNodes([1, 2, 3, 4, 5]), k=2))
    PrintListNode(Solution().reverseKGroup(MakeListNodes([1, 2, 3, 4, 5]), k=3))
