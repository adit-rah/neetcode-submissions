class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmax, cmin = nums[0], nums[0]
        n = len(nums)
        ans = nums[0]
        for i in range(1,n):
            x= nums[i]

            tmax = max(x,x*cmax,x*cmin)
            tmin = min(x,x*cmax,x*cmin)

            cmax = tmax
            cmin = tmin

            ans = max(ans, cmax)
        
        return ans
