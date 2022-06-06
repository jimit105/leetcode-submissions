# Approach 2 - Hash Table

# Time: O(N + M)
# Space: O(M)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        b_nodes = set()
        
        # Add all nodes of B Linked List to set (hash set)
        while headB is not None:
            b_nodes.add(headB)
            headB = headB.next
            
        # Check whether node from A Linked List exists in the set
        while headA is not None:
            if headA in b_nodes:
                return headA
            headA = headA.next
            
        return None
