# Approach 1: Breadth First Search

# Time: O(n)
# Space: O(n)

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float('-inf'), 0, 0

        q = deque()
        q.append(root)

        while q:
            level += 1
            sum_at_curr_level = 0

            for _ in range(len(q)):
                node = q.popleft()
                sum_at_curr_level += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            
            if sum_at_curr_level > max_sum:
                max_sum, ans = sum_at_curr_level, level

        return ans

