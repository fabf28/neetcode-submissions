# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.traverse(root, values, k)
        return values[k - 1]

    def traverse(self, node, values,  k):
        if not node:
            return
        self.traverse(node.left, values, k)
        values.append(node.val)
        self.traverse(node.right, values, k)
        