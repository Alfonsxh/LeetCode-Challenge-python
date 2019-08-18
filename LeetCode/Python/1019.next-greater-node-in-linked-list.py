#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    # 递归方式，深度太深，python解释器报错
    def nextLargerNodes_recursion(self, head: ListNode) -> List[int]:
        import sys
        sys.setrecursionlimit(1000000)

        if head is None:
            return [0]

        next_larger_list = self.nextLargerNodes_recursion(head.next)
        if head.next:
            for i in next_larger_list:
                if head.val < head.next.val:
                    return [head.next.val] + next_larger_list
                elif head.val < i:
                    return [i] + next_larger_list
            else:
                return [0] + next_larger_list
        else:
            return [0]

    # 超时
    # def nextLargerNodes(self, head: ListNode) -> List[int]:
    #     next_larger_list = list()
    #
    #     while head:
    #         curr_val = head.val
    #         compare_node = head.next
    #         while compare_node:
    #             if curr_val < compare_node.val:
    #                 next_larger_list.append(compare_node.val)
    #                 break
    #             compare_node = compare_node.next
    #         else:
    #             next_larger_list.append(0)
    #         head = head.next
    #
    #     return next_larger_list

    def nextLargerNodes(self, head: ListNode) -> List[int]:
        next_larger_list = list()
        stack = list()      # 关键列表，记录了之前元素的索引信息！避免了时间复杂度为O(n^2)
        index = 0

        while head:
            next_larger_list.append(0)
            curr_val = head.val

            while stack and stack[-1][0] < curr_val:
                top_node = stack.pop()
                next_larger_list[top_node[1]] = curr_val

            stack.append((curr_val, index))
            index += 1
            head = head.next

        return next_larger_list


if __name__ == '__main__':
    print(Solution().nextLargerNodes(MakeListNodes([7, 2, 6, 6, 9, 4, 3])))
    print(Solution().nextLargerNodes(MakeListNodes([9, 7, 6, 7, 6, 9])))
    print(Solution().nextLargerNodes(MakeListNodes([2, 5, 5])))
    print(Solution().nextLargerNodes(MakeListNodes([2, 1, 5])))
    print(Solution().nextLargerNodes(MakeListNodes([2, 7, 4, 3, 5])))
    print(Solution().nextLargerNodes(MakeListNodes([1, 7, 5, 1, 9, 2, 5, 1])))

    # print("Use recursion")
    # print(Solution().nextLargerNodes_recursion(MakeListNodes([7, 2, 6, 6, 9, 4, 3])))
    # print(Solution().nextLargerNodes_recursion(MakeListNodes([9, 7, 6, 7, 6, 9])))
    # print(Solution().nextLargerNodes_recursion(MakeListNodes([2, 5, 5])))
    # print(Solution().nextLargerNodes_recursion(MakeListNodes([2, 1, 5])))
    # print(Solution().nextLargerNodes_recursion(MakeListNodes([2, 7, 4, 3, 5])))
    # print(Solution().nextLargerNodes_recursion(MakeListNodes([1, 7, 5, 1, 9, 2, 5, 1])))

    import json

    with open("./1019_big_data", "r") as f:
        data = json.loads(f.read())

    # print(Solution().nextLargerNodes_recursion(MakeListNodes(data)))
    print(Solution().nextLargerNodes(MakeListNodes(data)))
