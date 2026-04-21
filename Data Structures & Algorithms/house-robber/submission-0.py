class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 3:
            return max(nums[0] if n >= 1 else 0, nums[1] if n >= 2 else 0)
        
        nums[2] = max(
                nums[0] + nums[2],
                nums[1]
            )
        if n == 3:
            return nums[n-1]
        
        for i in range(3,n):
            nums[i] = nums[i] + max(nums[i-2],nums[i-3])
        
        print(nums)
        return max(nums)