# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return [] 

        res = []

        q = deque()
        q.append([root])

        while q:
            e = q.popleft()
            r = []
            new = []
            for n in e:
                r.append(n.val)
                if n.left: 
                    new.append(n.left)
                if n.right:
                    new.append(n.right)
            res.append(r)
            if new:
                q.append(new)

        return res

