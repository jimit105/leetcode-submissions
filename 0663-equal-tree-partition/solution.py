# Approach: Depth First Search

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        seen = []

        def sum_(node):
            if not node:
                return 0
            seen.append(sum_(node.left) + sum_(node.right) + node.val)
            return seen[-1]

        total = sum_(root)
        seen.pop()
        return total / 2.0 in seen
        
