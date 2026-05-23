class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def helper(path, o, c):
            if len(path) == 2*n:
                res.append(path)
                return
            
            if o < c or o > n:
                return

            if o == n:
                path += ")"
                helper(path, o, c+1)
                path = path[:-1]
                return
        
            path += "("
            helper(path, o+1, c)
            path = path[:-1]

            path += ")"
            helper(path, o, c+1)
            path = path[:-1]
        helper("",0,0)
        return res