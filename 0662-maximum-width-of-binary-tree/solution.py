# Approach 1: BFS Traversal

# Time: O(n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        max_width = 0
        # queue of elements [(node, col_index)]
        queue = collections.deque()
        queue.append((root, 0))

        while queue:
            level_length = len(queue)
            _, level_head_index = queue[0]

            # iterating the current level
            for _ in range(level_length):
                node, col_index = queue.popleft()

                # preparing for next level
                if node.left:
                    queue.append((node.left, 2 * col_index))
                if node.right:
                    queue.append((node.right, 2 * col_index + 1))

            max_width = max(max_width, col_index - level_head_index + 1)

        return max_width

