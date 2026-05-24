class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        
        dp = set()
        dp.add(0)
        t = s // 2

        for i in range(len(nums)-1,-1,-1):
            ndp = set()
            for sums in dp:
                ndp.add(sums)
                ndp.add(sums + nums[i])
            dp = ndp
        
        return t in dp
            