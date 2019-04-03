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

    # Three static flags to keep track of post-order traversal.

    # Both left and right traversal pending for a node.
    # Indicates the nodes children are yet to be traversed.
    BOTH_PENDING = 2
    # Left traversal done.
    LEFT_DONE = 1
    # Both left and right traversal done for a node.
    # Indicates the node can be popped off the stack.
    BOTH_DONE = 0

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # nodes = [root]
        # parent = {root: None}
        #
        # while p not in parent or q not in parent:
        #     node = nodes.pop()
        #     if node.left:
        #         parent[node.left] = node
        #         nodes.append(node.left)
        #     if node.right:
        #         parent[node.right] = node
        #         nodes.append(node.right)
        #
        # records = set()
        # while p:
        #     records.add(p)
        #     p = parent[p]
        #
        # while q not in records:
        #     q = parent[q]
        #
        # return q

        stack = [(root, Solution.BOTH_PENDING)]
        one_node_found = False
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:
            parent_node, parent_state = stack[-1]
            if parent_state != Solution.BOTH_DONE:
                if parent_state == Solution.BOTH_PENDING:
                    if parent_node == p or parent_node == q:
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            one_node_found = True
                            LCA_index = len(stack) - 1
                    child_node = parent_node.left
                else:
                    child_node = parent_node.right
                stack.pop()
                stack.append((parent_node, parent_state - 1))
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None