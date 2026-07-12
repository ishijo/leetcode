class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal_t = []
        for n in range(1,numRows+1):
            level = [1]*n
            if n>2:
                print('n: ',n)
                mid = n//2
                for mid in range(1,n-1):
                    print(mid)
                    level[mid] = pascal_t[-1][mid] + pascal_t[-1][mid-1]

            pascal_t.append(level)
        return pascal_t


#        0
#       0 1
#      0 1 2
#     0 1 2 3
#    0 1 2 3 4
    
        