# Approach 2: Split Input List

# Time: O(N + k)
# Space: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        for N in range(1001):
            if not curr:
                break
            curr = curr.next

        width, remainder = divmod(N, k)

        ans = []
        curr = head

        for i in range(k):
            temp = curr
            for j in range(width + (i < remainder) - 1):
                if curr:
                    curr = curr.next
            if curr:
                curr.next, curr = None, curr.next
            ans.append(temp)
        return ans
