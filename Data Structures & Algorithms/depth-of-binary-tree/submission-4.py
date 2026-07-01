# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return 1 + self.maxDepthRoot(root)

    def maxDepthRoot(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        if root.right == None:
            right = 0
        else:
            right = 1 + self.maxDepthRoot(root.right)
        
        if root.left == None:
            left = 0
        else:
            left = 1 + self.maxDepthRoot(root.left)
        
        return max(right, left)
        
        