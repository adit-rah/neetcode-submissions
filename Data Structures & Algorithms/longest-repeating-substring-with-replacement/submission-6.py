class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        l = 0 
        res = 0

        for r in range(len(s)):
            if s[r] not in dic:
                dic[s[r]] = 0
            dic[s[r]] += 1

            while (r-l+1) - max(dic.values()) > k:
                dic[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)
        
        return res 