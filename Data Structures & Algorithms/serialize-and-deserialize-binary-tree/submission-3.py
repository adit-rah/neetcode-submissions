# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""
        def helper(node):
            nonlocal res
            if not node:
                res += "#N#"
                return
            
            res += "#"+str(node.val)+"#"
            helper(node.left)
            helper(node.right)
        helper(root)
        return res


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.i = 0

        def helper():
            
            c = data[self.i]
            j = self.i + 1
            while data[j] != "#":
                j += 1
            
            n = data[self.i+1:j]
            self.i = j + 1

            if n == "N":
                return None

            root = TreeNode(int(n))
            root.left = helper()
            root.right = helper()

            return root
        
        return helper()
