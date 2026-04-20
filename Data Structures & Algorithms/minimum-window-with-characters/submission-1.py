class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, h = 0, 0
        seen = {}
        for c in t:
            seen[c] = 1 + seen.get(c, 0)
            n += 1

        have = {}
        res = ""
        min_l = 1e10
        l = 0

        for i in range(len(s)):
            c = s[i]
            if c in seen:
                have[c] = 1 + have.get(c, 0)
                h += 1 if have[c] <= seen[c] else 0
            
            while n == h:
                if i - l + 1 < min_l:
                    res = s[l:i+1]
                    min_l = i - l + 1
                
                r = s[l]
                if r in have:
                    have[r] -= 1
                    h -= 1 if have[r] < seen[r] else 0
                l += 1
        
        return res
        