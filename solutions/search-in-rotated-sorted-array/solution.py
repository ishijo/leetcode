class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        k = (l+r)//2
        if l==r:
            return k if nums[k]==target else -1

        while l<=r:
            k = (l+r)//2
            if nums[k]==target:
                return k
            if nums[k]>=nums[l]:
                if target>=nums[l] and target<nums[k]:#left sorted
                #go left
                    r = k-1 
                else:#left sorted
                #go right
                    l = k+1
            else:
                if target<=nums[r] and target>nums[k]:#right sorted
                #go right
                    l = k+1
                else:#right sorted
                #go left
                    r = k-1
            
        return -1























            # if nums[k]>target and target>nums[l]:
            #     r = k
            # if nums[k]>target and target<nums[l]:
            #     l = k+1
            # if nums[k]<target and target<nums[r]:
            #     l = k+1
            # if nums[k]<target and target>nums[r]:
            #     r = k













        # l, r = 0, len(nums)-1
        # while l<r:
        #     k = (l+r)//2
        #     if target>nums[k] or target<nums[l]:
        #         l = k+1
        #     elif target<nums[k] or target>nums[r]:
        #         r = k

        # if nums[l]==target:
        #     return l
        # else:
        #     return -1