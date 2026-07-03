class Solution:
    # def move_indices(self,i,j) -> list:
    #     directions = [[0,-1],[0,1],[-1,0],[1,0]]
    #     indices = [[i,j]]*4
    #     return [[x[0]+y[0],x[1]+y[1]] for x,y in zip(directions,indices)]


    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        islands = 0

        def dfs(r,c):

            if r<0 or r>=rows or c<0 or c>=cols:
                return None
            
            if grid[r][c]!="1":
                return None
            
            grid[r][c]="0"
            
            for dr,dc in [[0,-1],[0,1],[-1,0],[1,0]]:
                dfs(dr+r,dc+c)

            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)

        return islands





































        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         for x,y in self.move_indices(i,j):
        #             if x in range(len(grid)) and y in range(len(grid[0])):
        #                 print(grid[x][y])
        #             else: print('x')
        #         print('\n')












#         if not grid:
#             return 0

#         rows = len(grid)
#         cols = len(grid[0])
#         seen = set()
#         islands = 0

#         def is_island(i,j):
#             if (i,j) not in seen:
#                 seen.add((i,j))
#                 if grid[i][j]==0 or not grid[i][j]:
#                     return 0
#                 else:
#                     for m in range(i-1,i+2)
#                     return 1 + is_island(i+1,j)
#             else:


#         for i in range(rows)
#             for j in range(cols):
#                 if grid[i][j]==1:
#                     seen.add((i,j))

# # [i][j]
# # [i-1][j]
# # [i+1][j]
# # [i][j-1]
# # [i][j+1]