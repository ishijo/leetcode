class Solution:
    def climbStairs(self, n: int) -> int:
         # n = 2
         # 1,1 + 2

         # n = 3
         # 1,1,1 + 1,2 + 2,1

         # n = 4
         # 1,1,1,1 + 1,1,2 x 3 + 2,2
         # 1 + 1 + 

         # n = 5
         # 1,1,1,1,1 + 1,2,2 x 3 + 1,1,1,2 x 4
        
        # ways = 1

        # if n==1:
        #     return ways

        # # 5//2 = 2
        # if n%2==1:
        #     num_o_2s = n//2
        #     n - num_o_2s*2

        #     for i in range(num_o_2s):
        #         # when i is 1


        ways = [1, 1, 2]

        for i in range(3,n+1):
            ways.append(ways[i-1] + ways[i-2])
        return ways[n]

        

        
