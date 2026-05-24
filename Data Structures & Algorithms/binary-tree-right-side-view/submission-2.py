# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            llen = len(q)
            last = None

            for _ in range(llen):
                node = q.popleft()
                if not node:
                    continue
                last = node

                q.append(node.left)
                q.append(node.right)
            if last:
                res.append(last.val)
        
        return res