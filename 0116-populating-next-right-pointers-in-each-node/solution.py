# Approach 1 - Level Order Traversal

# Time: O(N)
# Space: O(N)

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        Q = deque([root])
        
        while Q:
            size = len(Q)
            
            for i in range(size):
                node = Q.popleft()
                
                if i < size - 1:
                    node.next = Q[0]
                    
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        
        return root
