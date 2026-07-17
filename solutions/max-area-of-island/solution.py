class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        def dfs(r,c,count):
            count+=1
            for dr, dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                nr, nc = r+dr, c+dc
                if nr>=0 and nr<rows and nc>=0 and nc<cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 'X'
                        count = dfs(nr,nc,count)
            return count
            
                
        max_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid[r][c] = 'X'
                    max_count = max(max_count, dfs(r,c,0))
        return max_count



        