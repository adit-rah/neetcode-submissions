# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        iio = {v:i for i,v in enumerate(inorder)}
        n = len(preorder)
        self.i = 0

        def helper(l,r):
            if l > r:
                return None
            
            root_val = preorder[self.i]
            root = TreeNode(root_val)
            self.i += 1
            ni = iio[root_val]
            root.left = helper(l, ni-1)
            root.right = helper(ni+1, r)

            return root
        
        return helper(0,n-1)
            

            