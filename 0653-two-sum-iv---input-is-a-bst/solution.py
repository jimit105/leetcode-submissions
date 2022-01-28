# Approach 1 - Using HashSet

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def find(root, k, nodes):
            if not root:
                return False
            complement = k - root.val
            if complement in nodes:
                return True
            nodes.add(root.val)
            
            return find(root.left, k, nodes) or find(root.right, k, nodes)
        
        
        return find(root, k, set())
        
