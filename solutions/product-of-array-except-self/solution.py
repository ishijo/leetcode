class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_nums = [1]
        val = 1
        #prefix nums
        for i in range(1,len(nums)):
            val = prefix_nums[-1]*nums[i-1]
            prefix_nums.append(val)

        val = 1
        for j in range(len(prefix_nums)-2,-1,-1):
            val = val*nums[j+1]
            prefix_nums[j] = prefix_nums[j]*val

        return prefix_nums



