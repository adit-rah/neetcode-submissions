class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums[0] if n >= 1 else 0, nums[1] if n >= 2 else 0)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2,n):
            nums[i] = max(nums[i]+nums[i-2],nums[i-1])
        
        return max(nums)