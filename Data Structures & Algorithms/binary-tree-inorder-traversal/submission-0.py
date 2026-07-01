# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node, result):
            if not node:
                pass
            else:
                inorder(node.left, result)
                result.append(node.val)
                inorder(node.right, result)

            return result
        
        ans = inorder(root, [])
        return ans
            
