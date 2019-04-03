"""
https://leetcode-cn.com/problems/house-robber-iii/

在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。

这个地区只有一个入口，我们称之为“根”。

除了“根”之外，每栋房子有且只有一个“父“房子与之相连。

一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。

如果两个直接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。

示例 1:

输入: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

输出: 7
解释: 小偷一晚能够盗取的最高金额 = 3 + 3 + 1 = 7.

示例 2:

输入: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

输出: 9
解释: 小偷一晚能够盗取的最高金额 = 4 + 5 = 9.

http://www.cnblogs.com/grandyang/p/5275096.html
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # 差点超时间，因为对于"不打劫"的讨论比较粗糙，导致可能出现多余的调用
        # 用上hash表之后才勉强通过
        # 我对于打劫/不打劫是用一个变量表示，然后调用两次，第二次调用中需要跑的一些步骤可能第一次就已经跑过了
        # 而下面的解法则是将两种结果一起传回来，减少函数调用次数，加快时间
        #
        # records = {}
        #
        # def dfs(node: TreeNode, can_rob: bool) -> int:
        #     try:
        #         return records[(node, can_rob)]
        #     except KeyError:
        #         if node is None:
        #             return 0
        #         result = dfs(node.left, True) + dfs(node.right, True)
        #         if can_rob:
        #             result = max(result, node.val + dfs(node.left, False) + dfs(node.right, False))
        #         records[(node, can_rob)] = result
        #         return result
        # return dfs(root, True)

        def dfs(node: TreeNode) -> [int]:
            if node is None:
                return [0, 0]

            l = dfs(node.left)
            r = dfs(node.right)

            not_rob = max(l) + max(r)
            rob = node.val + l[0] + r[0]
            return [not_rob, rob]

        return max(dfs(root))
