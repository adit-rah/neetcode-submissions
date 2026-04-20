# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def recurse(node):
            nonlocal res

            if not node:
                return 0
            
            left = recurse(node.left)
            right = recurse(node.right)

            if abs(left - right) > 1:
                res = False
            
            return 1 + max(left, right)

        recurse(root)
        return res
                