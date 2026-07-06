class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        return ''.join([char.lower() for char in s if char.isalnum()]) == ''.join([char.lower() for char in s[::-1] if char.isalnum()])
        
