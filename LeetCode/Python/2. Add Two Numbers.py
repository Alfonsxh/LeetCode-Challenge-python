"""
@author: Alfons
@contact: alfons_xh@163.com
@file: 2. Add Two Numbers.py
@time: 19-1-9 下午8:54
@version: v1.0 
"""


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
        result = ListNode(0)
        result_tmp = result
        carry = 0
        while l1 is not None or l2 is not None:
            carry_tmp = carry
            if l1 is None:
                until = (l2.val + carry_tmp) % 10
                carry = (l2.val + carry_tmp) // 10
                l2 = l2.next
            elif l2 is None:
                until = (l1.val + carry_tmp) % 10
                carry = (l1.val + carry_tmp) // 10
                l1 = l1.next
            else:
                until = int(l1.val + l2.val + carry_tmp) % 10
                carry = int(l1.val + l2.val + carry_tmp) // 10
                l1 = l1.next
                l2 = l2.next

            result_tmp.val = until
            if l1 is None and l2 is None and int(carry) == 0:
                break

            result_tmp.next = ListNode(int(carry))
            result_tmp = result_tmp.next

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
