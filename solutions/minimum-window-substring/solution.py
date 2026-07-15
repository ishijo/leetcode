from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counts = {}
        for char in t:
            t_counts[char] = t_counts.get(char,0) + 1
        
        print(t_counts)
        start, end = 0, 0
        min_len = float("inf")
        curr_len = 0
        formed = 0
        required = len(t_counts)

        curr_counts = {}
    
        for end in range(len(s)):
            #while end < len(s) and formed < required:
            if s[end] in t_counts:
                curr_counts[s[end]] = curr_counts.get(s[end],0) + 1
                if curr_counts[s[end]] == t_counts[s[end]]:
                    formed += 1

            while formed == required:
                curr_len = end - start + 1
                if curr_len < min_len:
                    min_len = curr_len
                    best_start = start

                if s[start] in t_counts:
                    curr_counts[s[start]] -= 1
                    if curr_counts[s[start]] < t_counts[s[start]]:
                        formed -= 1
                start += 1

        if min_len == float("inf"):
            return ""
        return s[best_start:best_start+min_len]































        t_map = Counter(list(t))
        checker_map = {k: 0 for k, v in t_map.items()}

        need = sum([v for k, v in t_map.items()])
        have = 0

        start = 0
        end = 0

        store_str = {}

        for i in range(len(s)):
            char = s[i]
            if char in checker_map:
                checker_map[char] += 1
                if all(checker_map.get(key,0)>=t_map[key] for key in t_map):
                    store_str[s[start:end+1]] = len(s[start:end+1])
                    if s[start] in checker_map:
                        checker_map[s[start]] -= 1
                    start += 1
                    while start< len(s) and s[start] not in checker_map:
                        start += 1
            else:
                 pass
            end = i+1

        return store_str
