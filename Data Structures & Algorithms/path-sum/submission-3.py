# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        pathSum = [0]
        return self.backtrack(root, pathSum, targetSum)
    
    def backtrack(self, node, pathSum, target):
        if not node:
            return False
        pathSum[0] += node.val
    
        if not node.right and not node.left and pathSum[0] == target:
            return True
        if self.backtrack(node.left, pathSum, target):
            return True
        if self.backtrack(node.right, pathSum, target):
            return True
        
        pathSum[0] -= node.val
        return False
