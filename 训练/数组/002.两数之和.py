"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        current = res
        carry = 0  # 数学上的进位

        while l1 is not None or l2 is not None:
            current.next = ListNode(0)
            current = current.next

            n1 = 0 if l1 is None else l1.val
            n2 = 0 if l2 is None else l2.val
            current.val = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10  # 向下取整

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        if carry != 0:
            current.next = ListNode(carry)

        return res.next
