class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(path, i):
            res.append(path.copy())

            for j in range(i, len(nums)):
                path.append(nums[j])
                helper(path, j + 1)
                path.pop() 

        helper([], 0)
        return res
            
        