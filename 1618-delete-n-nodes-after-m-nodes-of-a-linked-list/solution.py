# Approach 1: Traverse Linked List and Delete In Place

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        current = head
        last = head

        while current:
            m_count = m
            n_count = n

            while current and m_count != 0:
                last = current
                current = current.next
                m_count -= 1

            while current and n_count != 0:
                current = current.next
                n_count -= 1

            last.next = current

        return head
        
