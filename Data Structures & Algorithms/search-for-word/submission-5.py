class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board), len(board[0])

        def helper(i,j,k):
            if k == len(word):
                return True
            
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            
            if board[i][j] != word[k]:
                return False
            
            prev = word[k]
            board[i][j] = "#"
            res = (
                helper(i-1,j,k+1) or
                helper(i,j-1,k+1) or
                helper(i+1,j,k+1) or
                helper(i,j+1,k+1)
            )
            board[i][j] = prev

            return res

        for i in range(n):
            for j in range(m):
                if helper(i,j,0):
                    return True
        
        return False