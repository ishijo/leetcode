class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        def is_diff_one(word1,word2):
            i, count = 0, 0
            while i < len(word1):
                if word1[i]!=word2[i]:
                    count += 1
                i += 1
            return count==1

        queue = deque([(beginWord,1)])
        visit = set()
        while queue:
            cur_word, c = queue.popleft()
            if cur_word == endWord:
                return c
            for word in wordList:
                if word not in visit and is_diff_one(cur_word,word):
                    visit.add(word)
                    queue.append((word, c+1))
        return 0

        