class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
#                        0 1 2
# Input: grid =       0 [2,1,1],
                    # 1 [1,1,0],
                    # 2 [0,1,1]

#                        0 1 2
# rotten grid =       0 [2,2,2],
                    # 1 [2,2,0],
                    # 2 [0,2,2]

# Output: 1+1
        rows = len(grid)
        cols = len(grid[0])
        queue = deque([])
        fresh = 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while queue and fresh>0:
            for _ in range(len(queue)):
                r,c = queue.popleft() # rotten orange

                for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                    nr, nc = dr+r, dc+c
                    if nr>=0 and nr<rows and nc>=0 and nc<cols and (grid[nr][nc]==1):
                        grid[nr][nc] = 2 ## rot this orange
                        fresh -= 1
                        print('rotten - ',nr,nc)
                        queue.append((nr,nc))
            minutes +=1 ## first layer (or minute) of fresh oranges rotted and added to queue

        return minutes if fresh == 0 else -1

                    
