"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        old = old2 = head
        mirror = dict()
        newPassed = dict()
        
        final = new = new2 = newNode(head)

        while old:
            mirror[old] = new
            old = old.next
            new = new.next
        
        while old2:
            if old2.random == None:
                new2.random = None
            else:
                new2.random = mirror[old2.random]
            old2 = old2.next
            new2 = new2.next    

        return final

def newNode(old):
    if old == None:
        return None
    else:
        return Node(old.val, newNode(old.next), None)

        

    
            
