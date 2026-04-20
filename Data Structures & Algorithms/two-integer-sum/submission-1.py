class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        for i, n in enumerate(nums):
            if target - n in sol:
                return [sol[target - n], i]
            sol[n] = i

        return [0,0]