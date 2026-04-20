class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i,n in enumerate(nums):
            res[n] = i
        
        print(res)
        for i,n in enumerate(nums):
            if target - n in res and res[target - n] != i:
                return [min(i,res[target - n]),max(i,res[target - n])]
        
        return [-1,-1]
