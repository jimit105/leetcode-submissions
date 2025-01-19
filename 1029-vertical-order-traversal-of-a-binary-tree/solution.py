# Approach 2: BFS with Partition Sorting

# Time: O(n log n)
# Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        columnTable = defaultdict(list)        
        min_column = max_column = 0

        queue = deque([(root, 0, 0)])

        while queue:
            node, row, column = queue.popleft()
            if node is not None:
                columnTable[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                queue.append((node.left, row + 1, column - 1))
                queue.append((node.right, row + 1, column + 1))

        result = []
        for col in range(min_column, max_column + 1):
            result.append([val for row, val in sorted(columnTable[col])])

        return result
