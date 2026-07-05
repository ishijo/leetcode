class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t_lis = [char for char in t]
        for char in s:
            if char in t_lis:
                t_lis.remove(char)
            else:
                return False
        return len(t_lis)==0
