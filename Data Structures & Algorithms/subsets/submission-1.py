class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def helper(p, i):
            if i >= n:
                res.append(p.copy())
                return
            
            p.append(nums[i])
            helper(p, i+1)
            p.pop()
            helper(p, i+1)
            
        helper([],0)
        return res