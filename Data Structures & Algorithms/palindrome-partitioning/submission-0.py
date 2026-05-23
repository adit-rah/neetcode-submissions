class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isp(s):
            for i in range(len(s)):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        
        def helper(path, i):
            if i >= len(s):
                res.append(path.copy())
                return 

            w = ""
            for j in range(i,len(s)):
                w += s[j]
                if isp(w):
                    path.append(w)
                    helper(path, j+1)
                    path.pop()

        helper([],0)
        return res


