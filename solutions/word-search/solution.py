class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r,c,i):
            
            if i== len(word):
                return True

            temp = board[r][c] 
            board[r][c] = ""

            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                if r+dr>=0 and r+dr<rows and c+dc>=0 and c+dc<cols:
                    if i<len(word):
                        if board[r+dr][c+dc] == word[i]:
                            if dfs(r+dr,c+dc,i+1):
                                board[r][c] = temp
                                return True
            board[r][c] = temp
            return False

        i = 0
        for r in range(rows):
            for c in range(cols):
                if i<len(word) and board[r][c] == word[i]:
                    if dfs(r,c,i+1):
                        return True
        return False
