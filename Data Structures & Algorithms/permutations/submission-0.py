class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def helper(path):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for j in range(len(nums)):
                if used[j]:
                    continue
                
                used[j] = True
                path.append(nums[j])
                helper(path)
                path.pop()
                used[j] = False

        helper([])
        return res