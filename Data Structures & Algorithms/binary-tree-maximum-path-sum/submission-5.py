# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = -1e9

        def helper(node):
            if not node:
                return -1e9
            
            left = helper(node.left)
            right = helper(node.right)

            res = node.val + max(0, left, right)
            self.res = max(self.res, left + right + node.val, res)

            return res
        
        helper(root)
        return self.res