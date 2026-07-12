class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, mid, R = 0, 0, len(nums)-1
        while mid<=R:
            if nums[mid]==1:
                mid = mid+1
            elif nums[mid]==0:
                nums[L], nums[mid] = nums[mid], nums[L]
                mid += 1
                L += 1
            elif nums[mid]==2:
                nums[R], nums[mid] = nums[mid], nums[R]
                R -= 1

