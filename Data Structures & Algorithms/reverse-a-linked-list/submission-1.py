# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #two pass


        new = None
        values = []

        dummy = head

        while dummy:
            values.append(dummy.val)
            dummy = dummy.next
        print(values)
        while values:
            new = ListNode(values.pop(0), new)
        
        return new

        