# Approach 1: Recursion

# Time: O(n)
# Space: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def helper(node):
            # Inorder traversal
            nonlocal first, last
            if node:
                helper(node.left)

                if last:
                    # Link the previous node (last) with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # Keep the smallest node to close Doubly Linked List later on
                    first = node
                last = node

                helper(node.right)

        if not root:
            return None
            
        first, last = None, None
        helper(root)

        # Close DLL
        last.right = first
        first.left = last

        return first
        
        
