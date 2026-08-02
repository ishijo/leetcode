class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]

# [4,5,6,4,5,6]
# [1,2,3]

# [1,2,3,2,5,6]
# [0,6,3]

        p1, p2 = m-1, n-1
        ins = m+n-1
        #n1, n2 = nums1[p1], nums2[p2]
        while p2>=0:
            if p1>=0 and nums1[p1]>=nums2[p2]:
                nums1[ins] = nums1[p1]
                #nums1[p1] = n2
                p1 -= 1
            else:
                nums1[ins] = nums2[p2]
                p2 -= 1
            ins -= 1
            


            























        # # insert num2s elements into num1
        # j = len(nums1)-1
        # for i in range(len(nums2)-1,-1,-1):
        #     nums1[j] = nums2[i]
        #     j -= 1
        # print(nums1)

        # L, R = 0, len(nums1)-1

        # while L<R:
        #     if nums1[L] < nums1[R]:
        #         L += 1
        #         R -= 1
        #     else:
        #         nums1[L], nums1[R] = nums1[R], nums1[L]

