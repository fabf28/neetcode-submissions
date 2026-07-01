# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]: 
        vals = []
        queue = [root]

        if not root:
            return []

        while len(queue) > 0:
            curr = []
            for i in range(len(queue)): #snapshot of queue
                node = queue.pop(0)
                curr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            vals.append(curr)
        return vals
                


