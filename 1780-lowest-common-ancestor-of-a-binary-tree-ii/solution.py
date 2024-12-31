# Approach 1: Depth First Search

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, target):
            # Base case: target found
            if node == target:
                return True
            # Base case: reached null, target not found
            if node is None:
                return False
            # Recursive case: search target in left or right subtree
            return dfs(node.left, target) or dfs(node.right, target)

        def LCA(node, p, q):
            if node is None or node == p or node == q:
                return node

            left = LCA(node.left, p, q)
            right = LCA(node.right, p, q)

            # If p and q are found in different subtrees, current node is their LCA
            if left and right:
                return node
            elif left:
                return left
            else:
                return right
        
        # Step 1: Find the lowest common ancestor of nodes p and q
        ans = LCA(root, p, q)

        # Step 2: Check if the LCA is p, meaning q must be in p's subtree
        if ans == p:
            return p if dfs(p, q) else None

        # Step 3: Check if the LCA is q, meaning p must be in q's subtree
        elif ans == q:
            return q if dfs(q, p) else None

        # Step 4: If neither p nor q is the ancestor of the other, return the LCA
        return ans
