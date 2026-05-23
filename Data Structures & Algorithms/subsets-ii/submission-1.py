class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def helper(path, i):
            if i >= len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            helper(path, i+1)
            path.pop()

            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(path, i+1)

        helper([],0)
        return res