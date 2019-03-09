# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1038/
#
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Iteration
        # before = None
        # current = head
        # while current is not None:
        #     current.next, before, current = before, current, current.next
        # return before

        # Recursive
        def recursive_reverse(before, node_head):
            if node_head is None:
                return before, before
            else:
                head_, tail_ = recursive_reverse(node_head, node_head.next)
                tail_.next = before
                return head_, before

        return recursive_reverse(None, head)
