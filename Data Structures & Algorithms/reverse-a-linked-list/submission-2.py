# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #one pass

        new = None
        dummy = head

        while dummy:
            new = ListNode(dummy.val, new)
            dummy = dummy.next
        
        return new

        