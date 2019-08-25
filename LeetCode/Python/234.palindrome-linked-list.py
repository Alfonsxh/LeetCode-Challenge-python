#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node_list = list()
        while head:
            node_list.append(head.val)
            head = head.next

        return all([v1 == v2 for v1, v2 in zip(node_list, node_list[::-1])])


if __name__ == '__main__':
    print(Solution().isPalindrome(MakeListNodes([1])))
    print(Solution().isPalindrome(None))
    print(Solution().isPalindrome(MakeListNodes([1, 0, 0])))
    print(Solution().isPalindrome(MakeListNodes([1])))
    print(Solution().isPalindrome(MakeListNodes([1, 2])))
    print(Solution().isPalindrome(MakeListNodes([1, 2, 2, 1])))
