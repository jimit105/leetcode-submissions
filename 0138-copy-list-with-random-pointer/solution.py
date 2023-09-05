# Approach 1: Recursive

# Time: O(n)
# Space: O(n)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self) -> None:
        self.visited_hash = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None

        if head in self.visited_hash:
            return self.visited_hash[head]

        node = Node(head.val, None, None)

        self.visited_hash[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

        
