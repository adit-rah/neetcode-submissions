class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(path, sum, i):
            if i >= len(nums) or sum >= target:
                if sum == target: 
                    res.append(path.copy())
                return
            
            path.append(nums[i])
            helper(path, sum + nums[i], i)
            path.pop()

            helper(path, sum, i + 1)
        
        helper([], 0, 0)
        return res
            