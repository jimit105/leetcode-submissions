# Approach 2: Recursive Preorder Traversal

# Time: O(N)
# Space: O(H)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def preorder(r, curr_num):
            nonlocal root_to_leaf

            if r:
                curr_num = curr_num * 10 + r.val
                if not (r.left or r.right):
                    root_to_leaf += curr_num

                preorder(r.left, curr_num)
                preorder(r.right, curr_num)

        root_to_leaf = 0
        preorder(root, 0)

        return root_to_leaf
