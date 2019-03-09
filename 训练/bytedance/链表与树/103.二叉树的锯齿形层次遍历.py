# https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1027/
#
# 二叉树的锯齿形层次遍历
# 给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
# 例如：
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回锯齿形层次遍历如下：
#
# [
#   [3],
#   [20,9],
#   [15,7]
# ]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        """
        参考这个博客，二叉树的按层遍历可以用队列实现
        https://blog.csdn.net/sinat_20177327/article/details/78285495
        锯齿遍历使用两个栈来完成
        ps，数组的pop是pop最后一个，可以用来当栈
        """
        from collections import deque
        stack1 = deque([root])
        stack2 = []
        left_to_right = True

        result = []
        while stack1 or stack2:
            breadth = []
            if left_to_right:
                while stack1:
                    node = stack1.pop()
                    if node is not None:
                        breadth.append(node.val)
                        stack2.append(node.left)
                        stack2.append(node.right)
                left_to_right = False
            else:
                while stack2:
                    node = stack2.pop()
                    if node is not None:
                        breadth.append(node.val)
                        stack1.append(node.right)
                        stack1.append(node.left)
                left_to_right = True
            result.append(breadth)

        return result




