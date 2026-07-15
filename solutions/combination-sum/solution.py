class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        result = []
        def dfs(i,curr_sum,total):

            if total == target:
                result.append(curr_sum.copy())
                return 
            
            if i>=len(candidates) or total>target:
                return 
            
            curr_sum.append(candidates[i])
            dfs(i,curr_sum,total+candidates[i])
            curr_sum.pop()
            dfs(i+1,curr_sum,total)
        
        dfs(0,[],0)

        return result

































            # for i in range(start,len(candidates)):
                
            #     path.append(nums[i])
            #     while sum(path)<target:
            #         path.append(nums[i])
            #     if sum(path) == target:
            #         return result.append(backtrack())
                

                
                

        # [ 2,  3,  6,  7 ]
        # [ 2 ]