# Time: O(h), h = height of the tree
# Space: O(h)

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()

        while q:
            visited.add(q.val)
            q = q.parent

        while p:
            if p.val in visited:
                return p
            visited.add(p.val)
            p = p.parent

        return None
        
