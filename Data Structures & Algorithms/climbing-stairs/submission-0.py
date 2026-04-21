class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [0] * n
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n):
            dp[i] = dp[i-1] + dp[i-2]
        
        print(dp)
        return dp[n-1] + dp[n-2]