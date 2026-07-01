# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        path = []
        return self.backtrack(root, path, targetSum)
    
    def backtrack(self, node, path, target):
        if not node:
            return False
        path.append(node.val)
    
        if not node.right and not node.left and sum(path) == target:
            return True
        if self.backtrack(node.left, path, target):
            return True
        if self.backtrack(node.right, path, target):
            return True
        
        path.pop()
        return False
