# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = self.build(preorder, inorder)
        return root

    def build(self, preorder, inorder):
        if not preorder or not inorder:
            return None

        val = preorder[0]
        node = TreeNode(val)
        mid = inorder.index(val)

        node.left = self.build(preorder[1:1 + mid], inorder[:mid])
        node.right = self.build(preorder[1 + mid:], inorder[mid + 1: ])
        return node

        




