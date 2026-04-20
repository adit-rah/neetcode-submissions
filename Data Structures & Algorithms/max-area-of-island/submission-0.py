class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        n,m = len(grid), len(grid[0])

        def bfs(i,j):
            if i >= n or j >= m or i < 0 or j < 0:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            grid[i][j] = 0

            return 1 + bfs(i-1,j) + bfs(i,j-1) + bfs(i+1,j) + bfs(i,j+1)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    res = max(res, bfs(i,j))

        return res
