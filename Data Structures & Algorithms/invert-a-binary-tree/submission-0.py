# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        res = TreeNode()
        res.val = root.val 
        res.left = self.invertTree(root.right)
        res.right = self.invertTree(root.left)

        return res

