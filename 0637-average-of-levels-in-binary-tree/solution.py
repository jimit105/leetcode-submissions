# Approach: Breadth-first Search
    
# https://leetcode.com/problems/average-of-levels-in-binary-tree/discuss/1094405/JS-Python-Java-C++-or-Easy-BFS-Solution-w-Explanation

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q, ans = [root], []
        
        while len(q):
            q_len, row = len(q), 0
            for i in range(q_len):
                curr = q.pop(0)
                row += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            ans.append(row/q_len)
            
        return ans
            
        
