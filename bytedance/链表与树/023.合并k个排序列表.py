# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1025/
#
# 合并K个排序链表
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
#
# 示例:
#
# 输入:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# 输出: 1->1->2->3->4->4->5->6


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        """
        就是把东西拿出来排一下序
        我顺手复习了一下堆排序
        https://www.jianshu.com/p/21bef3fc3030
        """
        from heapq import heappush, heappop
        origin = ListNode(None)
        current = origin
        min_heap = []
        for linked_list in lists:
            for node in linked_list:
                heappush(min_heap, node.val)
        while min_heap:
            current.next = ListNode(heappop(min_heap))
            current = current.next
        return origin.next

