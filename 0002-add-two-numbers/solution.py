# Approach 1: Elementary Math

# Time: O(max(n, m))
# Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0

        while l1 != None or l2 != None or carry != 0:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0

            column_sum = l1val + l2val + carry
            carry = column_sum // 10
            
            new_node = ListNode(column_sum % 10)
            curr.next = new_node
            curr = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy_head.next

