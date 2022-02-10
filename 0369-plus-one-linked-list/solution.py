# Approach 1 - Sentinel Head + Textbook Addition

# Time: O(N)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        
        # if input is all 9s e.g. 99, then we need additional node
        sentinel = ListNode(val = 0, next = head)
        not_nine = sentinel
        
        # find the rightmost not-nine
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next
        
        # add 1 to the value and move to next node
        not_nine.val += 1
        not_nine = not_nine.next
        
        # set following 9s to zero e.g. 1299 -> 1300
        while not_nine:
            not_nine.val = 0
            not_nine = not_nine.next
            
        return sentinel if sentinel.val else sentinel.next
        
        
