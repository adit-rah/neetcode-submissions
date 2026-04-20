class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])
        def helper(path, i, j):
            if not path:
                return True
            
            if i >= n or j >= m or i < 0 or j < 0:
                return False
            
            if path[-1] != board[i][j]:
                return False
            
            c = path.pop()
            temp = board[i][j]
            board[i][j] = "#" 
            if helper(path,i-1,j) or helper(path,i,j-1) or helper(path,i+1,j) or helper(path,i,j+1):
                return True
            board[i][j] = temp
            path.append(c)

            return False
        
        for i in range(n):
            for j in range(m):
                if helper(list(reversed(list(word))), i, j):
                    return True

        return False