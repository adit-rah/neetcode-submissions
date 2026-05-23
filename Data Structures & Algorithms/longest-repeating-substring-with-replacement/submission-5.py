class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 0 
        l = 0

        maxe = s[l]
        seen = {s[l]:1}
        c = 0
        for r in range(1,len(s)):
            seen[s[r]] = seen.get(s[r],0) + 1
            if s[r] != maxe:
                c += 1
                
            if seen[s[r]] > seen[maxe]:
                c = c - seen[s[r]] + seen[maxe]
                maxe = s[r]
            
            if c > k:
                seen[s[l]] -= 1
                if s[l] != maxe:
                    c -= 1
                l += 1
            
            maxl = max(maxl, r-l+1)
        
        return maxl
        
                
            
