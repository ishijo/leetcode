class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        def has_duplicate(start,end,str):
            substr = str[start:end]
            seen = set()

            for ch in substr:
                if ch in seen:
                    return True
                seen.add(ch)
            return False
    
        start = 0
        lengths = []
        for i,ch in enumerate(s):
            end = i+1

            while has_duplicate(start,end,s):
                start += 1
            
            lengths.append(len(s[start:end]))
        
        return max(lengths) if lengths else 0




            