# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1048/
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
#
# 示例：
#
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        origin = ListNode(0)
        current = origin

        # 注意这里是直接修改指针，而不是新建Node，可以减少开销
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        if l2 is None:
            current.next = l1
        elif l1 is None:
            current.next = l2
        return origin.next

