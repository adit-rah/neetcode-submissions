class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def helper(l):
            n = len(l)
            if n == 1:
                return l[0]
            if n == 2:
                return max(l[0], l[1])
            
            l[1] = max(l[0], l[1])
            
            for i in range(2, n):
                l[i] = max(l[i] + l[i-2], l[i-1])
            
            return l[-1]
        
        return max(helper(nums[1:]), helper(nums[:-1]))