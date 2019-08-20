#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def __repr__(self):
        return str(self.val)


class Solution:
    def flatten(self, head: Node) -> Node:
        dummy = Node(0, None, None, None)
        res = dummy

        stack = list()
        while head:
            res.next = head
            res = res.next

            if head.child:
                if head.next:
                    stack.append(head.next)

                head.next = head.child
                head.child.prev = head
                head = head.child
                head.prev.child = None
                continue

            if head.next is None:
                if not stack:
                    head.next = None
                    head.child = None
                    break
                else:
                    n = stack.pop()
                    head.next = n
                    head.child = None
                    n.prev = head
                    head = n
                continue

            head = head.next

        return dummy.next


def create_node():
    node_1 = Node(1, None, None, None)
    node_2 = Node(2, None, None, None)
    node_3 = Node(3, None, None, None)
    node_4 = Node(4, None, None, None)
    node_5 = Node(5, None, None, None)
    node_6 = Node(6, None, None, None)
    node_7 = Node(7, None, None, None)
    node_8 = Node(8, None, None, None)
    node_9 = Node(9, None, None, None)
    node_10 = Node(10, None, None, None)
    node_11 = Node(11, None, None, None)
    node_12 = Node(12, None, None, None)

    node_1.next = node_2

    node_2.prev = node_1
    node_2.next = node_3

    node_3.prev = node_2
    node_3.next = node_4
    node_3.child = node_7

    node_4.prev = node_3
    node_4.next = node_5

    node_5.prev = node_4
    node_5.next = node_6

    node_6.prev = node_5

    node_7.next = node_8

    node_8.prev = node_7
    node_8.next = node_9
    node_8.child = node_11

    node_9.prev = node_8
    node_9.next = node_10

    node_10.prev = node_9

    node_11.next = node_12

    node_12.prev = node_11

    return node_1


if __name__ == '__main__':
    Solution().flatten(create_node())
