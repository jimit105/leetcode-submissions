# Approach 3: One Pass

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first = second = head

        for _ in range(k - 1):
            first = first.next

        tail = first
        while tail.next:
            second = second.next
            tail = tail.next

        first.val, second.val = second.val, first.val
        return head

