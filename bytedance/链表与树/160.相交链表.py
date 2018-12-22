# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1024/
#
# 相交链表
# 编写一个程序，找到两个单链表相交的起始节点。
#
# 如下面的两个链表：
#
#
#
# 在节点c1开始相交。
#
# 示例1：
#
#
# 输入：intersectVal = 8, listA = [4, 1, 8, 4, 5], listB = [5, 0, 1, 8, 4, 5], skipA = 2, skipB = 3
# 输出：Reference of the node with value = 8
# 输入解释：相交节点的值为8 （注意，如果两个列表相交则不能为0）。从各自的表头开始算起，链表A为[4, 1, 8, 4, 5]，链表B
# 为[5, 0, 1, 8, 4, 5]。在A中，相交节点前有2个节点；在B中，相交节点前有3个节点。
#
#
# 示例2：
#
#
# 输入：intersectVal = 2, listA = [0, 9, 1, 2, 4], listB = [3, 2, 4], skipA = 3, skipB = 1
# 输出：Reference of the node with value = 2
# 输入解释：相交节点的值为2 （注意，如果两个列表相交则不能为0）。从各自的表头开始算起，链表A为[0, 9, 1, 2, 4]，链表
# B为[3, 2, 4]。在A中，相交节点前有3个节点；在B中，相交节点前有1个节点。
#
#
# 示例3：
#
#
# 输入：intersectVal = 0, listA = [2, 6, 4], listB = [1, 5], skipA = 3, skipB = 2
# 输出：null
# 输入解释：从各自的表头开始算起，链表A为[2, 6, 4]，链表B为[1, 5]。由于这两个链表不相交，所以intersectVal
# 必须为0，而skipA和skipB可以是任意值。
# 解释：这两个链表不相交，因此返回null。
#
#
# 注意：
#
# 如果两个链表没有交点，返回null.
# 在返回结果后，两个链表仍须保持原有的结构。
# 可假定整个链表结构中没有循环。
# 程序尽量满足O(n)时间复杂度，且仅用O(1)内存。

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 如果跑完了会去另一边从头跑
        # 也就是说p1会先跑headA然后跑headB，p2会先跑headB然后跑headA
        # 最后他们总能够碰头
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
        return p1

        # 我这个计算长度的方法是可行的，但是不够优雅
#         lenA = lenB = 0
#         a = headA
#         b = headB
#         while headA:
#             lenA += 1
#             headA = headA.next
#         while headB:
#             lenB += 1
#             headB = headB.next

#         while lenA > lenB:
#             a = a.next
#             lenA -= 1
#         while lenB > lenA:
#             b = b.next
#             lenB -= 1

#         while lenA > 0:
#             if a == b:
#                 return a
#             else:
#                 a = a.next
#                 b = b.next
#                 lenA -= 1

#         return None