# Approach: Heap

# n = total number of nodes, k = no. of linked lists
# Time: O(n * log k)
# Space: O(k)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Add the first node from each list to the heap
        # We store (value, list_index, node) in heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst.val, i, lst))

        dummy = ListNode(0)
        current = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Add the node to our result list
            current.next = node
            current = current.next

            # If there are more nodes in the same list, add the next node to heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

