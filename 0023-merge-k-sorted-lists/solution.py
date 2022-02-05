import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = [(l.val, idx) for idx, l in enumerate(lists) if l]
        heapq.heapify(q)
        
        head = curr = ListNode(None)
        
        while q:
            val, idx = heapq.heappop(q)
            curr.next = ListNode(val)
            curr = curr.next
            node = lists[idx] = lists[idx].next
            if node:
                heapq.heappush(q, (node.val, idx))
            
        return head.next
