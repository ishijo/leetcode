class Solution:
    def maxArea(self, height: List[int]) -> int:

        maxarea = 0
        Lmax, Rmax = height[0], height[len(height)-1]
        L, R = 0, len(height)-1 
        while L<R:
            Lmax = max(Lmax,height[L])
            Rmax = max(Rmax,height[R])
            maxarea = max(maxarea, (R-L)*min(height[L],height[R]))
            if height[L]<height[R]:
                L += 1
            else:
                R -= 1

        return maxarea

