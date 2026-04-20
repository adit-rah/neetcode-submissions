class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(path, sum, i):
            if i == len(nums) or sum > target:
                return
            if sum == target:
                res.append(path.copy())
                return
            
            for j in range(i, len(nums)):
                path.append(nums[j])
                helper(path, sum + nums[j], j)
                path.pop()  
        
        helper([], 0, 0)
        return res