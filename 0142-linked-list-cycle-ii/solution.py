# Approach 2: Floyd's Tortoise and Hare Algorithm

# Time: O(n)
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # Found intersection, find cycle start
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
        
