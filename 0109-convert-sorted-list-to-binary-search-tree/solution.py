# Approach 1: Recursion

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMiddle(self, head):
        prev_ptr = None
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if prev_ptr:
            prev_ptr.next = None

        return slow_ptr


    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        mid = self.findMiddle(head)

        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)

        return node

