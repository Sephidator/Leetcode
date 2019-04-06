"""
https://leetcode-cn.com/explore/interview/card/bytedance/244/linked-list-and-tree/1026/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        nodes = [root]
        parent = {root: None}

        while p not in parent or q not in parent:
            node = nodes.pop()
            if node.left:
                parent[node.left] = node
                nodes.append(node.left)
            if node.right:
                parent[node.right] = node
                nodes.append(node.right)

        records = set()
        while p:
            records.add(p)
            p = parent[p]

        while q not in records:
            q = parent[q]

        return q