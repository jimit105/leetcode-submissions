# Approach 2 - Floyd's Cycle Finding Algorithm

# Time: O(n), Space: O(1)


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def get_intersect(self, head):
        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
            
        return None
    
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        intersect = self.get_intersect(head)
        if intersect is None:
            return None
        
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1
   
