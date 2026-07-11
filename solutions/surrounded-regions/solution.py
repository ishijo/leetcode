class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        boundary_coords = [(0,c) for c in range(cols)] + [(rows-1,c) for c in range(cols)] + [(r,0) for r in range(rows)] + [(r,cols-1) for r in range(rows)]
        visit = set(boundary_coords)

        def move(r,c):
            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                row  = r + dr
                col = c + dc
                if (row,col) not in visit and row>=0 and row<rows and col>=0 and col<cols and board[row][col] == "O":
                    visit.add((row,col))
                    move(row,col)

        def moveX(r,c):
            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                row  = r + dr
                col = c + dc
                if (row,col) not in visit and board[row][col] == "O":
                    visit.add((row,col))
                    board[row][col] = "X"
                    moveX(row,col)

        for r,c in boundary_coords:
            if board[r][c]=="O":
                visit.add((r,c))
                move(r,c)

        for r in range(1,rows-1):
            for c in range(1,cols-1):
                if (r,c) not in visit and board[r][c] == "O":
                    visit.add((r,c))
                    board[r][c] = "X"


        