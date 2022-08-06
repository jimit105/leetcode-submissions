# https://leetcode.com/problems/find-leaves-of-binary-tree/discuss/83815/Simple-Python-solution-using-dict/235834

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        def helper(root):
            if not root:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)
            
            level = max(left, right) + 1
            dic[level].append(root.val)
            
            return level
        
        dic = collections.defaultdict(list)
        helper(root)
        return list(dic.values())
