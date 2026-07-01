class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        solution = []
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            L, R = i+1, len(nums)-1
            curr_sum = nums[i]
            while L<R:
                threesum = nums[i] + nums[L] + nums[R]
                if threesum>0:
                    R -= 1
                elif threesum<0:
                    L += 1
                else:
                    solution.append([nums[i],nums[L],nums[R]])
                    L += 1
                    while nums[L]==nums[L-1] and L<R:
                        L+=1
        return solution



            
