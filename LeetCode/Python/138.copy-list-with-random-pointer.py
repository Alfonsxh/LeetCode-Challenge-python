#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        curr_node = head
        deepcopy_dict = dict()

        while curr_node:
            # 1、节点不在copy字典中，则将其添加进去
            if curr_node not in deepcopy_dict:
                deepcopy_dict[curr_node] = Node(curr_node.val, None, None)

            # 2、处理next节点，next节点如果不在，则添加。并且将当前节点的下一个节点添加进字典
            if curr_node.next:
                if curr_node.next not in deepcopy_dict:
                    deepcopy_dict[curr_node.next] = Node(curr_node.next.val, None, None)
                deepcopy_dict[curr_node].next = deepcopy_dict[curr_node.next]

            # 3、类似于next节点的处理random节点
            if curr_node.random:
                if curr_node.random not in deepcopy_dict:
                    deepcopy_dict[curr_node.random] = Node(curr_node.random.val, None, None)
                deepcopy_dict[curr_node].random = deepcopy_dict[curr_node.random]

            curr_node = curr_node.next

        return deepcopy_dict.get(head, None)
