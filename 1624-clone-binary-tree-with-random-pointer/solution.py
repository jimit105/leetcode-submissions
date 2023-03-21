# Approach 1: Depth First Search (2 Passes)

# Time: O(n)
# Space: O(n)

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def __init__(self):
        self.new_old_pairs = {None: None}


    def deep_copy(self, root):
        if not root:
            return None

        new_root = NodeCopy(root.val)
        new_root.left = self.deep_copy(root.left)
        new_root.right = self.deep_copy(root.right)
        
        self.new_old_pairs[root] = new_root
        return new_root

    
    def map_random_pointers(self, old_node):
        if not old_node:
            return
        
        new_node = self.new_old_pairs[old_node]
        new_node_random = self.new_old_pairs[old_node.random]
        new_node.random = new_node_random

        self.map_random_pointers(old_node.left)
        self.map_random_pointers(old_node.right)


    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        new_root = self.deep_copy(root)
        self.map_random_pointers(root)

        return new_root



