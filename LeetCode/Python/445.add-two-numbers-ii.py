#
# @lc app=leetcode id=445 lang=python
#
# [445] Add Two Numbers II
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def MakeListNodes(l: list):
    header = ListNode(l[0])
    header_tmp = header
    for val in l[1:]:
        second = ListNode(val)
        header_tmp.next = second
        header_tmp = second

    return header


def PrintListNode(l: ListNode):
    l_tmp = list()

    while l is not None:
        l_tmp.append(str(l.val))
        l = l.next

    print(" -> ".join(l_tmp))


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = list()
        l2_list = list()
        while l1 is not None or l2 is not None:
            if l1 is not None:
                l1_list.append(l1)
                l1 = l1.next
            if l2 is not None:
                l2_list.append(l2)
                l2 = l2.next

        carry = 0
        result = None
        while l1_list or l2_list or carry:
            p = l1_list.pop().val if l1_list else 0
            q = l2_list.pop().val if l2_list else 0
            sum_tmp = p + q + carry
            carry = int(sum_tmp // 10)
            result_tmp = ListNode(sum_tmp % 10)
            result_tmp.next = result

            result = result_tmp

        return result


if __name__ == '__main__':
    s = Solution()

    l_1 = MakeListNodes([2, 4, 3])
    l_2 = MakeListNodes([5, 6, 4])

    PrintListNode(s.addTwoNumbers(l_1, l_2))
    PrintListNode(s.addTwoNumbers(ListNode(5), ListNode(5)))

    l_1 = MakeListNodes([2, 4])
    l_2 = MakeListNodes([5])
    PrintListNode(s.addTwoNumbers(l_1, l_2))
