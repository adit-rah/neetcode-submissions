# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Ortional[TreeNode], subRoot: Ortional[TreeNode]) -> bool:
        def helper(r,sr):
            if not r and not sr:
                return True
            if not r and sr or not sr and r:
                return False
            else:
                return (r.val == sr.val 
                and helper(r.left,sr.left) 
                and helper(r.right,sr.right))
        
        found = False
        if not root:
            return False
        if root.val == subRoot.val:
            found = helper(root, subRoot)
        
        return found or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
