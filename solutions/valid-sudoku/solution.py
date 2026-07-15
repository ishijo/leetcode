class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    if val in rows[r]:
                        return False
                    if val in cols[c]:
                        return False
                    if val in boxes[(r//3,c//3)]:
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r//3,c//3)].add(val)
        print(rows)
        print(cols)
        print(boxes)
        return True









        #def get_box(r,c): # check for duplicates for r,c in box
        #     nr, nc = r%3, c%3

        # def get_row(r,c):

        # def get_column(r,c):

            
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] != ".":
        #             if not get_box(r,c) or not get_row(r,c) or not get_column(r,c):
        #                 return False
        # return True