class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid), len(grid[0])

        def helper(i,j):
            if not (0 <= i < n and 0 <= j < m):
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            helper(i+1,j)
            helper(i-1,j)
            helper(i,j+1)
            helper(i,j-1)

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    helper(i,j)
                    res += 1
        return res


