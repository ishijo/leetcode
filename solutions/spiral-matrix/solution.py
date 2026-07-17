class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # r = 0             0
        # c = 0, 1, 2

        # c = 2.            cols -1
        # r = 1, 2

        # r = 2             rows - 1
        # c = 1, 0 #rev

        # c = 0             0
        # r = 2, 1 $ rev

        # r = 1 ...

        rows = len(matrix) ## 3 2
        cols = len(matrix[0]) ## 3 2
        output = []
        r,c = 0,0
        while rows>0 and cols>0:

            for c in range(c,c+cols):
                output.append(matrix[r][c])
            rows -= 1
            if rows == 0:
                break
            r += 1

            for r in range(r,r+rows):
                output.append(matrix[r][c])
            cols -=1
            if cols == 0:
                break
            c -= 1

            for c in range(c,c-cols,-1):
                output.append(matrix[r][c])
            rows -= 1
            if rows == 0:
                break
            r -= 1
            
            for r in range(r,r-rows,-1):
                output.append(matrix[r][c])
            cols -= 1
            if cols == 0:
                break
            c+= 1
        return output

        