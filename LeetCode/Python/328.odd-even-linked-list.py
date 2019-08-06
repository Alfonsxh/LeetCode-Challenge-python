#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# Definition for singly-linked list.

from LeetCode.Python.BaseListNode import MakeListNodes, PrintListNode, ListNode


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if (not head) or (not head.next) or (not head.next.next):
            return head

        # 奇、偶节点
        odd_node = head
        even_node = head.next

        # 偶数头，最后连接用
        even_head = even_node

        # 偶数节点为末尾节点，所以判断其为None为结束标志
        while even_node:
            # 如果偶数节点存在，则奇数节点的next为偶数节点的next
            odd_node.next = even_node.next

            # 如果偶数节点的next(也就是下一个奇数节点)存在
            # 则奇数、偶数节点进行更新
            if even_node.next:
                odd_node = odd_node.next
                even_node.next = odd_node.next
            even_node = even_node.next

        # 奇数节点的末尾与偶数节点的头部连接
        odd_node.next = even_head

        return head


if __name__ == '__main__':
    PrintListNode(Solution().oddEvenList(MakeListNodes([1, 2, 3, 4, 5])))
    PrintListNode(Solution().oddEvenList(MakeListNodes([2, 1, 3, 5, 6, 4, 7])))
