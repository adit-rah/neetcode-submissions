class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n 

        for i in range(n):
            sub = [dp[j] for j in range(i) if nums[j] < nums[i]] + [0]
            dp[i] += max(sub)
        
        return max(dp)