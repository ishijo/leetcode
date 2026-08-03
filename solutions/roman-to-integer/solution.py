class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
            "I": 1,
            "V": 5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        res = 0
        for i,ch in enumerate(s):
            if ch == 'V' and i!=0 and s[i-1]=="I":
                res+= 3
                continue
            elif ch == 'X' and i!=0 and s[i-1]=="I":
                res+= 8
                continue
            elif ch == 'L' and i!=0 and s[i-1]=="X":
                res+= 30
                continue
            elif ch == 'C' and i!=0 and s[i-1]=="X":
                res+= 80
                continue
            elif ch == 'D' and i!=0 and s[i-1]=="C":
                res+= 300
                continue
            elif ch == 'M' and i!=0 and s[i-1]=="C":
                res+= 800
                continue

            res+= hashmap[ch]
        return res
        