# Approach 1: Top Down Depth-first Search
    
# Time: O(N)
# Space: O(N)
    
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        def dfs(curr, parent, length):
            if curr is None:
                return length
            
            if (parent is not None) and curr.val == (parent.val + 1):
                length += 1
            else:
                length = 1
                                
            return max(length, dfs(curr.left, curr, length), dfs(curr.right, curr, length))
        
        return dfs(root, None, 0)
