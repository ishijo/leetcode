class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = [0]*len(nums)
        jumps[0] = 1
        for i,num in enumerate(nums):
            if jumps[i]==1:
                # if num!=-1 and num!=0:
                if i+num >= len(nums)-1:
                    return True
                else:
                    for n in range(i,i+num+1):
                        jumps[n] = 1
        return False
            


        