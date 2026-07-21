class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #L = 0
        max_prod = nums[0]
        min_prod = nums[0]
        curr_max,curr_min = 1,1
        for i in range(len(nums)):
            # if nums[i]==0:
            #     curr = 1
            #     continue
            old_max = curr_max 
            old_min = curr_min 
            curr_max = max(nums[i],old_max*nums[i],old_min*nums[i])
            curr_min = min(nums[i],old_max*nums[i],old_min*nums[i])

            max_prod = max(max_prod,curr_max)
            

        return max_prod
        