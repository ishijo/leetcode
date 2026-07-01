class Solution:
    def isPalindrome(self, x: int) -> bool:
        stack = []
        x_char = str(x)
        l, r = 0, len(x_char)-1
        while l<r:
            if x_char[l]==x_char[r]:
                l += 1
                r -= 1
            else:
                return False
        return True