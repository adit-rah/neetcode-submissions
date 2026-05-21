class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[-1] = 0

        for i in range(n-2,-1,-1):
            if nums[i] + i >= n-1:
                dp[i] = 1
            else:
                minj = 1e9
                for j in range(i, i + nums[i]+1):
                    if dp[j] == -1:
                        continue
                    minj = min(minj,dp[j] + 1)
                dp[i] = minj
        
        
        return dp[0]