class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def helper(path, sum, i):
            if i >= len(candidates) or sum >= target: 
                if sum == target:
                    res.append(path.copy())
                return 
            
            path.append(candidates[i])
            helper(path,sum+candidates[i],i+1)
            path.pop()
            
            j = i + 1
            while j < len(candidates) and candidates[j-1] == candidates[j]:
                j += 1

            helper(path,sum,j)

        helper([],0,0)
        return res