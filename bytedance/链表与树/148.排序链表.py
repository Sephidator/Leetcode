# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1040/
#
# 排序链表
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
#
# 示例 1:
#
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 示例 2:
#
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        对于O(n log n)时间复杂度，可以选择快速排序和归并排序
        但是快排虽然通常更快，但是有最坏情况O(n)的可能，所以选择归并排序
        归并排序的思路如下：
            其思路是先将所有元素两两划分为一组，然后递归合并，
            合并就相当于将两个排序好的链表合并为一个。
            这样最终我们就可以将链表排序好了。
            关键所在就是先分裂，在合并。
            
        参考如下：https://blog.csdn.net/liuchonge/article/details/74394995
        
        然而更快的答案是把node的val提成一个数组，然后排序...
        """
        if head is None or head.next is None:
            return head

        # 分裂操作
        # fast的移动速度是slow的两倍
        # 所以当fast走到整个链表的结束处时，slow才指向链表中部
        #
        # slow和fast分别是要合并的两个链表的尾部
        # 所以可以由slow得到head2
        # 再将head和head2的两个链表排序（递归调用）并且合并两个有序链表
        #
        # 使用prev的原因是，必须保证l2不以null开头，不然l1和head开头的链表就是一模一样的
        # 这会导致无限递归
        # 假如没有prev，用head2 = slow.next，slow.next = None，且head链表只有2个数 1->3->None 的场合
        # head: 1->3->None,  l1: 1->3->None, l2: None
        # head == l1, 无限递归
        prev = slow = fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # merge操作，合并两个有序链表
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.merge(l1, l2)

    # 021.合并两个有序链表
    def merge(self, l1, l2):
        origin = ListNode(0)
        current = origin

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


d = ListNode(3)
c = ListNode(1)
b = ListNode(2)
a = ListNode(4)
c.next = d
b.next = c
a.next = b

s = Solution()
x = s.sortList(a)
print()




