#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return str(self.val)


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.length or self.head is None:
            return -1

        index_node = self.head
        for _ in range(index):
            index_node = index_node.next
        return index_node.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head
        self.length += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        tail_node = self.head
        if tail_node is None:
            self.head = ListNode(val)
        else:
            while tail_node.next:
                tail_node = tail_node.next
            tail_node.next = ListNode(val)

        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index <= 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        elif 0 <= index < self.length:
            index_node = self.head
            for _ in range(index - 1):
                index_node = index_node.next
            node = ListNode(val)
            node.next = index_node.next
            index_node.next = node
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head.next
        else:
            delete_pre_node = self.head
            for _ in range(index - 1):
                delete_pre_node = delete_pre_node.next
            delete_pre_node.next = delete_pre_node.next.next

        self.length -= 1


# Your MyLinkedList object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtIndex(0, 10)
    obj.addAtIndex(0, 20)
    obj.addAtIndex(1, 30)
    print(obj.get(0))
