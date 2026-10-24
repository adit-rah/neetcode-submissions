class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # make the trie
        root = {}

        for word in words:
            curr = root
            for i in range(len(word)):
                if word[i] not in curr:
                    curr[word[i]] = {}
                curr = curr[word[i]]
            curr['#'] = '#'
        
        n,m = len(board),len(board[0])
        res = set()
        def is_word(i,j,curr,path):
            if not (0 <= i < n and 0 <= j < m):
                return
            
            c = board[i][j]

            if c == '*' or c not in curr:
                return

            path.append(c)
            curr = curr[c]

            if '#' in curr:
                res.add("".join(path))

            board[i][j] = '*'  # Mark visited

            is_word(i + 1, j, curr, path)
            is_word(i - 1, j, curr, path)
            is_word(i, j + 1, curr, path)
            is_word(i, j - 1, curr, path)

            board[i][j] = c  # Restore cell
            path.pop() 

        for i in range(n):
            for j in range(m):
                is_word(i,j,root,[])
        
        return list(res)


