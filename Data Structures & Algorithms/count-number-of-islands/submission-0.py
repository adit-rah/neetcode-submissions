class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        n, m = len(grid), len(grid[0])
        
        def destroy(i,j):
            if i >= n or j >= m or i < 0 or j < 0:
                return
            
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            destroy(i, j - 1)
            destroy(i - 1, j)
            destroy(i + 1, j)
            destroy(i, j + 1)

        for i in range(n): 
            for j in range(m):
                if grid[i][j] == "1":
                    destroy(i,j)
                    res += 1
                    print(i,j)

        return res 
