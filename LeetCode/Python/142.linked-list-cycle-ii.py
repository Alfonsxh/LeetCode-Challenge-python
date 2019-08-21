#
# @lc app=leetcode id=142 lang=python
#
# [142] Linked List Cycle II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution(object):
    # def detectCycle(self, head):
    #     """
    #     :type head: ListNode
    #     :rtype: ListNode
    #     """
    #     node_set = set()
    #
    #     while head:
    #         if head in node_set:
    #             return head
    #
    #         node_set.add(head)
    #         head = head.next
    #
    #     return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # python2 中set的实现还不是散列表的形式，效率上比dict慢
        node_dict = dict()

        while head:
            if head in node_dict:
                return head

            node_dict.update({head: 1})
            head = head.next

        return None


if __name__ == '__main__':
    node = MakeListNodes([1, 2, 3, 4, 5, 6, 7])
    node.next.next.next.next.next = node.next

    print(Solution().detectCycle(node).val)
