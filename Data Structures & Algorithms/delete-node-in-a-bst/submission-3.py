# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = TreeNode(0, right=root)
        self.findKey(head.right, head, True, key)
        return head.right
    
    def findKey(self, node, prev, right, key):
        
        if not node:
            pass
        elif node.val == key:
            self.delete(node, prev, right)
        elif key > node.val:
            self.findKey(node.right, node, True, key)
        elif key < node.val:
            self.findKey(node.left, node, False, key)
        else:
            pass
    
    def delete(self, node, prev, right):
        if not node.right and not node.left:
            self.updatePrev(prev, right, None)
        elif node.right and not node.left:
            self.updatePrev(prev, right, node.right)
        elif node.left and not node.right:
            self.updatePrev(prev, right, node.left)
        elif node.right:
            minn = self.deleteMinimum(node.right, node)
            node.val = minn


                
    def updatePrev(self, prev, right, new):
        if right:
            prev.right = new
        else:
            prev.left = new

    def deleteMinimum(self, node, prev):
        right = True
        while node.left:
            right = False
            prev = node
            node = node.left
        
        minn = node.val
        if node.right:
            self.updatePrev(prev, right, node.right)
        else:
            self.updatePrev(prev, right, None)
        return minn
        
        