# Approach 2 - One Pass Algorithm

# Time: O(L), L = no. of nodes
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        
        first = dummy
        second = dummy
        
        # Advances first pointer so that the gap between first and second is n nodes apart
        for i in range(n+1):
            first = first.next
        
        # Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummy.next
        
