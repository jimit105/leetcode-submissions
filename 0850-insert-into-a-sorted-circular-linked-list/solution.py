# Time: O(n)
# Space: O(1)

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':

        # If the list is empty
        if not head:
            new_node = Node(insertVal)
            new_node.next = new_node
            return new_node
        
        curr = head

        while True:
            # Find a position between two nodes where insertVal fits
            if curr.val <= insertVal <= curr.next.val:
                break

            # When we reach the maximum value node (before minimum)
            elif curr.val > curr.next.val:
                if insertVal >= curr.val or insertVal <= curr.next.val:
                    break

            curr = curr.next

            # We've completed one full cycle
            if curr == head:
                break

        # Insert new node
        new_node = Node(insertVal)
        new_node.next = curr.next
        curr.next = new_node

        return head

