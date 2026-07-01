# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        final = self.addNodes(l1, l2, 0)
        return final

    
    def addNodes(self, l1, l2, carry):
        if not l1 and not l2 and not carry:
            return None
        elif not l1 and not l2:
            return ListNode(carry, None)
        elif l1 and l2:
            return self.findSum(l1, l2, carry)
        elif l1:
            carryNode = ListNode(carry, None)
            return self.findSum(l1, carryNode, 0)
        elif l2:
            carryNode = ListNode(carry, None)
            return self.findSum(l2, carryNode, 0)

    

    def findSum(self, l1, l2, carry):
        summ = str(l1.val + l2.val + carry)
        if len(summ) == 1:
            ones = int(summ)
            tenth = 0 
        else:
            ones = int(summ[1])
            tenth = int(summ[0])
        return ListNode(ones, self.addNodes(l1.next, l2.next, tenth))
    


