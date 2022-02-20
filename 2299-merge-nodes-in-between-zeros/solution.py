# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
       
        result = ListNode(0)
        result_list = result

        while head:
            next_node = head
            temp_sum = 0
            
            while next_node.next and next_node.val != 0:
                temp_sum += next_node.val
                next_node = next_node.next
                
            head = next_node.next
                
            node = ListNode(val = temp_sum)
            result_list.next = node
            result_list = result_list.next

        return result.next.next
                
