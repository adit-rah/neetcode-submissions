class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            seen = {}
            for j in range(i, len(s)):
                if s[j] in seen:
                    break
                else:
                    seen[s[j]] = True

            res = max(res, len(seen.items()))

        return res
        