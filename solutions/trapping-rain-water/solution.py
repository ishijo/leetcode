class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        L = 0
        R = len(height)-1
        maxL = height[L]
        maxR = height[R]
        water_vol = 0
        
        while L<R:

            if maxL < maxR:
                L += 1
                maxL = max(maxL,height[L])
                water_vol += maxL - height[L]
                
            else:
                R -= 1
                maxR = max(maxR,height[R])
                water_vol += maxR-height[R]

        return water_vol
            