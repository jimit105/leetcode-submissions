# Approach 1 - Top Down Merge Sort

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        mid = slow.next
        slow.next = None
        l, r = self.sortList(head), self.sortList(mid)
        return self.merge(l, r)
    
    
    def merge(self, l, r):
        if l is None:
            return r
        elif r is None:
            return l
        
        dummy = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
                
            else:
                p.next = r
                r = r.next
                
            p = p.next
            
        p.next = l if r is None else r
        
        return dummy.next
    
