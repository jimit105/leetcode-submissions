# Approach 1 - Fixed-Range Sampling

import random

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.range = []
        
        while head:
            self.range.append(head.val)
            head = head.next
        

    def getRandom(self) -> int:
        selected = int(random.random() * len(self.range))
        return self.range[selected]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
