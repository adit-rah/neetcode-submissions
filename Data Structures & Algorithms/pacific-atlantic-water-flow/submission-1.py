class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n,m = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def helper(i,j,h,visit):
            if (i,j) in visit or i < 0 or j < 0 or i >= n or j >= m or heights[i][j] < h:
                return
            
            visit.add((i,j))
            helper(i-1,j,heights[i][j],visit)
            helper(i,j-1,heights[i][j],visit)
            helper(i+1,j,heights[i][j],visit)
            helper(i,j+1,heights[i][j],visit)
        
        for i in range(n):
            helper(i, 0, heights[i][0], pac)
            helper(i, m-1, heights[i][m-1], atl) 
        
        for i in range(m):
            helper(0, i, heights[0][i], pac)
            helper(n-1, i, heights[n-1][i], atl) 
        
        for i in range(n):
            for j in range(m):
                if (i,j) in atl and (i,j) in pac:
                    res.append([i,j])
        
        return res
