INF = 2 ** 31 - 1

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid), len(grid[0])
        q = deque()
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        while q:
            i, j = q.popleft()

            for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni, nj = i + di, j + dj

                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == INF:
                    grid[ni][nj] = grid[i][j] + 1
                    q.append((ni,nj))
