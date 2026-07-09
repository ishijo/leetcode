class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        if target == "0000":
            return 0

        def helper(combination):
            res = []
            for i in range(4):
                added_dig = str((int(combination[i]) + 1)%10)
                res.append(combination[:i] + added_dig + combination[i+1:])
                sub_dig = str((int(combination[i]) + 9)%10)
                res.append(combination[:i] + sub_dig + combination[i+1:])
            return res

        visit = set(deadends)
        queue = deque()
        queue.append(['0000',0])

        while queue:
            combination, turns = queue.popleft()
            for comb in helper(combination):
                if comb not in visit:
                    if comb == target:
                        return turns+1
                    queue.append([comb,turns+1])
                    visit.add(comb)
        return -1
            
                        


        
