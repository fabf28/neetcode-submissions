# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        old = lists
        new = final = ListNode(0, None)

        while old:
            minIndex = self.findMin(old)
            new.next = ListNode(old[minIndex].val, None)
            new = new.next
            old[minIndex] = old[minIndex].next


            if old[minIndex] == None:
                old.pop(minIndex)
        
        return final.next
        
            
    def findMin(self, nodes):
        minn = nodes[0]
        index = 0
        n = len(nodes)

        for i in range(n):
            node = nodes[i]
            if node.val < minn.val:
                minn = node
                index = i
        return index
