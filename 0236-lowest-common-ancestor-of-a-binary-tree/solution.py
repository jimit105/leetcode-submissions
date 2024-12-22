# Approach 1: Recursive

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def recurse_tree(curr_node) -> bool:
            # If reached end of branch, return False
            if not curr_node:
                return False

            left = recurse_tree(curr_node.left)
            right = recurse_tree(curr_node.right)

            # If the current node is one of p or q
            mid = curr_node == p or curr_node == q

            # If any two of the three flags (left, right, mid) become True
            if mid + left + right >= 2:
                self.ans = curr_node

            # Return true if either of the three bool values is True
            return mid or left or right

        recurse_tree(root)
        return self.ans

