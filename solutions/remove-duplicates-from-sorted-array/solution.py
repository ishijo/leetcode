class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        L, R = 1, 1
        while R < len(nums):
            if nums[R] == nums[R-1]: # unique value
                count += 1
            else:
                nums[L] = nums[R]
                L += 1
            R += 1
        return L
            
            























        #     if nums[i] in seen:
        #         n = i
        #         while nums[n] == nums[i]:
        #             count += 1
        #             n += 1





        #         count += 1
        #         n = i
        #         while n<len(nums)-1:
        #             nums[n] = nums[n+1]
        #             n += 1
        #         nums[n] = nums[i]
        #     seen.add(nums[i])
        # return count



