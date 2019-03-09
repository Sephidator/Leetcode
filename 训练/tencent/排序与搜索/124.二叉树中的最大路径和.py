"""
https://leetcode-cn.com/explore/interview/card/tencent/224/sort-and-search/931/

  二叉树中的最大路径和
给定一个非空二叉树，返回其最大路径和。

本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。

示例 1:

输入: [1,2,3]

       1
      / \
     2   3

输出: 6
示例 2:

输入: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

输出: 42
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.result = root.val

        # dfs中返回的是这个节点能为别人提供的maxPathSum
        # 而self.result存放的是真正用来计算的maxPathSum
        def dfs(node: TreeNode) -> int:
            if node is None:
                return 0
            else:
                left_path_sum = dfs(node.left)
                right_path_sum = dfs(node.right)
                self.result = max(self.result, node.val + max(left_path_sum, 0) + max(right_path_sum, 0))
                return node.val + max(left_path_sum, right_path_sum, 0)

        dfs(root)
        return self.result
