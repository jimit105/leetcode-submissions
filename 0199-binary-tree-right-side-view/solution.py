# Approach 3: BFS: One Queue + Level Size Measurements

# Time: O(n)
# Space: O(d), d = tree diameter

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque([root])
        rightside = []

        while queue:
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                if i == level_length - 1:
                    rightside.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return rightside

