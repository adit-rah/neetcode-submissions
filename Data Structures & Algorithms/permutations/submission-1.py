class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = [False] * n

        def helper(path):
            if len(path) == n:
                res.append(path.copy())
                return
            
            for i in range(n):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])

                helper(path)

                path.pop()
                used[i] = False
        
        helper([])
        return res
