class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = [] 

        def helper(path, sum, i):
            if sum > target:
                return
            if sum == target:
                res.append(path.copy())
                return
            
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue

                path.append(candidates[j])
                helper(path, sum + candidates[j], j + 1)
                path.pop()

        helper([], 0, 0)
        return res