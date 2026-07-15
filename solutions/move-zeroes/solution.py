class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1

        L = 0
        for R in range(1,len(nums)):
            if nums[L] == 0:
                if nums[R]!=0:
                    nums[L], nums[R] = nums[R], nums[L]
                    L += 1
            else:
                L += 1


            
        # [0,1,0,3,12]
        #  L R

        # [1,0,0,3,12]
        #    L   R

        # [1,3,0,0,12]
        #      L   R


            # if nums[L]==0:
            #     if nums[R]!=0:
            #         nums[L], nums[R] = nums[R], nums[L]
            #     else:
            #         R -= 1
            # else:
            #     L += 1