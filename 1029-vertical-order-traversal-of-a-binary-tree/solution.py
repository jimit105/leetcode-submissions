# Approach 1: BFS/DFS with Global Sorting

# Time: O(N log N)
# Space: O(N)
    
# BFS

from collections import deque, OrderedDict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        node_list = []
        
        def BFS(root):
            queue = deque([(root, 0, 0)])
            
            while queue:
                node, row, col = queue.popleft()
                if node is not None:
                    node_list.append((col, row, node.val))
                    queue.append((node.left, row + 1, col - 1))
                    queue.append((node.right, row + 1, col + 1))
                    
        BFS(root)
        
        node_list.sort()
        
        result = OrderedDict()
        for col, row, value in node_list:
            if col in result:
                result[col].append(value)
            else:
                result[col] = [value]
                
        
        return result.values()
        
