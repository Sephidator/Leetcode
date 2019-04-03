"""

445. 两数相加 II


题目描述
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carrier = 0
        next_node = None

        while stack1 or stack2:
            n1 = 0 if stack1 is None else stack1.pop()
            n2 = 0 if stack2 is None else stack2.pop()
            node = ListNode((n1 + n2 + carrier) % 10)
            carrier = (n1 + n2 + carrier) // 10
            node.next = next_node
            next_node = node

        if carrier is not 0:
            head = ListNode(carrier)
            head.next = next_node
            return head
        else:
            return next_node

