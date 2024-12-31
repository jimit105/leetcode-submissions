# Approach 1: Recursive

# Time: O(n)
# Space: O(h), h = height of the tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or root is one of the nodes we're looking for
        if root is None or root == p or root == q:
            return root

        # Recursively search in left and right subtrees
        left = self.lowestCommonAncestor(root.left, p , q)
        right= self.lowestCommonAncestor(root.right, p, q)

        # If both left and right return non-null values,
        # then current node is the LCA
        if left and right:
            return root

        # If only one side returns a non-null value,
        # return that value up the tree
        return left if left else right
        
