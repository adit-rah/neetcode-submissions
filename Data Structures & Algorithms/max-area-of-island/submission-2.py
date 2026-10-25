class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])

        def helper(i,j):
            if not (0 <= i < n and 0 <= j < m):
                return 0 
            
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return 1 + (
                helper(i-1,j) +
                helper(i+1,j) +
                helper(i,j-1) +
                helper(i,j+1)
            )
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, helper(i,j))
        
        return res