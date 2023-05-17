# Approach 1: List of Integers

# Time: O(n)
# Space: O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        values = []

        while current:
            values.append(current.val)
            current = current.next

        i = 0
        j = len(values) - 1
        max_sum = 0

        while i < j:
            max_sum = max(max_sum, values[i] + values[j])
            i += 1
            j -= 1

        return max_sum
