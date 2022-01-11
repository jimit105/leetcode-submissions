# Approach 2 - Recursive Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def preorder(root_, curr_number):
            nonlocal root_to_leaf
            if root_:
                curr_number = (curr_number << 1) | root_.val
                
                if not(root_.left or root_.right):
                    root_to_leaf += curr_number
                    
                preorder(root_.left, curr_number)
                preorder(root_.right, curr_number)
                
        root_to_leaf = 0
        preorder(root, 0)
        return root_to_leaf
        
