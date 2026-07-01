# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new = None
        current = head

        while current:
            data = current.val
            new = ListNode(data, new)
            current = current.next
        
        return new
            
