class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string: 1 way
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, n + 1):
            one = s[i-1]
            two = s[i-2:i]

            if one != '0':
                dp[i] += dp[i-1]

            if 10 <= int(two) <= 26:
                dp[i] += dp[i-2]

        print(dp)
        return dp[n]