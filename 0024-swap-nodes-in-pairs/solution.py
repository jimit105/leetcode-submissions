# Approach 2 - Iterative Approach

# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(val=-1, next=head)
        
        prev_node = dummy
        
        while head and head.next:
            first_node = head
            second_node = head.next
            
            # Swap
            prev_node.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node
            
            # Reinitializing the head and prev_node for next swap
            prev_node = first_node
            head = first_node.next
            
        return dummy.next
        
