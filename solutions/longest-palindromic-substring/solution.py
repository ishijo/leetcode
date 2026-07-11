class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        max_len = 0

        def expand (l,r):
            nonlocal res, max_len
            while l>=0 and r <len(s) and s[l]==s[r] :
                l -= 1
                r += 1
            curr = s[l+1:r]
            if len(curr)>max_len:
                res = curr
                max_len = len(curr)

        for mid in range(len(s)):
            expand(mid,mid)
            expand(mid,mid+1)
        return res

























        # for l in range(len(s)):
        #     r = l+1
        #     while s[l]!=s[r] or r<len(s):
        #         r += 1
            
        #     l0, r0 = l, r
        #     while s[l0]==s[r0] and l0<r0:
        #         l0 += 1
        #         r0 -= 1
            
        # return s[l:r+1]
            



            