class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid), len(grid[0])

        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i,j))

        res = 0

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni,nj = i+di, j+dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        q.append((ni,nj))
                
            res += 1
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        return max(res - 1, 0)