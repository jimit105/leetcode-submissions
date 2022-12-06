# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odds = ListNode(0)
        evens = ListNode(0)
        oddsHead = odds
        evensHead = evens

        is_odd = True
        while head:
            if is_odd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = head
                evens = evens.next
            is_odd = not is_odd
            head = head.next

        evens.next = None
        odds.next = evensHead.next

        return oddsHead.next
