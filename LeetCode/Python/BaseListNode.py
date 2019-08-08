"""
@author: Alfons
@contact: alfons_xh@163.com
@file: BaseListNode.py
@time: 2019/8/6 上午7:46
@version: v1.0 
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)


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


if __name__ == '__main__':
    PrintListNode(MakeListNodes([1, 2, 3, 4, 5, 6]))
