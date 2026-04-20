class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(path, open, closed):
            if open == n and closed == n:
                res.append(path)
                return
            
            if open < n:
                helper(path + "(", open + 1, closed)
            
            if open > closed:
                helper(path + ")", open, closed + 1)

        helper("", 0, 0)
        return res