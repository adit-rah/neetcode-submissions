class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n,m = len(board), len(board[0])
        
        def dfs(i,j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != "O":
                return
            
            board[i][j] = "T"
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
    
        for i in range(n):
            for j in range(m):
                if board[i][j] and (i in [0,n-1] or j in [0,m-1]):
                    dfs(i,j)
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "T":
                    board[i][j] = "O"

