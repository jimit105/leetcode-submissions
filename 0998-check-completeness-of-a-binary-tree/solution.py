# Approach: Breadth First Search
# https://leetcode.com/problems/check-completeness-of-a-binary-tree/solutions/2426611/python-simple-solution-using-queue-with-detailed-explanation-o-n/

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append(root)

        while q:
            node = q.popleft()
            if node is None:
                break
            q.append(node.left)
            q.append(node.right)

        for node in q:
            if node:
                return False

        return True
