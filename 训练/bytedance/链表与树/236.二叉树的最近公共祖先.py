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

        # def isParent(p, node):
        #     if p == node:
        #         return True
        #     elif p is None:
        #         return False
        #     else:
        #         return isParent(p.left, node) or isParent(p.right, node)
        #
        # if root in [None, p, q]:
        #     return root
        # elif isParent(p, q):
        #     return p
        # elif isParent(q, p):
        #     return q
        #
        # while root:
        #     if isParent(root.left, p) and isParent(root.left, q):
        #         root = root.left
        #     elif isParent(root.right, p) and isParent(root.right, q):
        #         root = root.right
        #     else:
        #         return root
        # return None

        # def search(pfind, qfind, node, result):
        #     if pfind and qfind or node is None:
        #         return pfind, qfind, result
        #     else:
        #         pfind1, qfind1, result = search(pfind, qfind, node.left, result)
        #         pfind2, qfind2, result = search(pfind, qfind, node.right, result)
        #
        #         pfind = pfind1 or pfind2 or node == p
        #         qfind = qfind1 or qfind2 or node == q
        #         if pfind and qfind and result is None:
        #             result = node
        #
        #         return pfind, qfind, result
        #
        # pf, qf, res = search(False, False, root, None)
        # return res

        # Initialize the stack with the root node.
        stack = [(root, Solution.BOTH_PENDING)]

        # This flag is set when either one of p or q is found.
        one_node_found = False

        # This is used to keep track of LCA index.
        LCA_index = -1

        # We do a post order traversal of the binary tree using stack
        while stack:

            parent_node, parent_state = stack[-1]

            # If the parent_state is not equal to BOTH_DONE,
            # this means the parent_node can't be popped of yet.
            if parent_state != Solution.BOTH_DONE:

                # If both child traversals are pending
                if parent_state == Solution.BOTH_PENDING:

                    # Check if the current parent_node is either p or q.
                    if parent_node == p or parent_node == q:

                        # If one_node_found is set already, this means we have found both the nodes.
                        if one_node_found:
                            return stack[LCA_index][0]
                        else:
                            # Otherwise, set one_node_found to True,
                            # to mark one of p and q is found.
                            one_node_found = True

                            # Save the current top index of stack as the LCA_index.
                            LCA_index = len(stack) - 1

                    # If both pending, traverse the left child first
                    child_node = parent_node.left
                else:
                    # traverse right child
                    child_node = parent_node.right

                # Update the node state at the top of the stack
                # Since we have visited one more child.
                stack.pop()
                stack.append((parent_node, parent_state - 1))

                # Add the child node to the stack for traversal.
                if child_node:
                    stack.append((child_node, Solution.BOTH_PENDING))
            else:

                # If the parent_state of the node is both done,
                # the top node could be popped off the stack.

                # i.e. If LCA_index is equal to length of stack. Then we decrease LCA_index by 1.
                if one_node_found and LCA_index == len(stack) - 1:
                    LCA_index -= 1
                stack.pop()

        return None
