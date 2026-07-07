class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        best_len = 0
        seen = {}
        curr_len = 0
        l, r = 0, 0

        # [1, 2, 3, 2, 2]  - fruit
        #  0  1  2  3  4   - i
        # l = 1
        # r = 3
        # curr_len = 3
        # best_len = 3
        # seen = {,2:3, 3:2, }

        while r < len(fruits):
            if fruits[r] in seen:
                pass
            elif fruits[r] not in seen and len(seen)==2:
                l = seen[min(seen, key = seen.get)] + 1
                del seen[min(seen, key = seen.get)]
            seen[fruits[r]] = r # last seen index stored
            curr_len = r - l + 1
            best_len = max(best_len, curr_len)
            r += 1
        return best_len

                






























        # l, r = 0, 0
        # seen = {}
        # best_len = 0

        # # 0 1 2 2
        # # seen =  1:1 2:2
        # # r = 2
        # # curr_len = 2
        # # best_len = 2

        # while r <len(fruits):
        #     fruit = fruits[r]
        #     if len(seen)<2 and fruit not in seen:
        #         seen[fruit] = r
        #     if len(seen)<=2 and fruit in seen:
        #         r += 1
        #     if len(seen)==2 and fruit not in seen:
        #         l = min(seen.values())+1
        #         del seen[min(seen, key=seen.get)]
        #         seen[fruit] = r
        #         r += 1
            
        #     curr_len = r - l
        #     best_len = max(best_len, curr_len)
        
        # return best_len



        # # def totalFruit(self, fruits: List[int]) -> int:
        # # l = 0
        # # seen = {}
        # # best_len = 0

        # # for r, fruit in enumerate(fruits):
        # #     seen[fruit] = seen.get(fruit, 0) + 1

        # #     while len(seen) > 2:
        # #         left_fruit = fruits[l]
        # #         seen[left_fruit] -= 1

        # #         if seen[left_fruit] == 0:
        # #             del seen[left_fruit]

        # #         l += 1

        # #     curr_len = r - l + 1
        # #     best_len = max(best_len, curr_len)

        # # return best_len

















        
        # # s, e = 0, 0
        # # seen = set()
        # # max_length = 0

        # # if fruits[e] not in seen:
        # #     if len(seen)<2:
        # #         seen.add(fruits[e])
        # #         e += 1
        # #         max_length = max(max_length, e-s+1)
        # #     else:
                
        # # else























        # # # 1 2 3 2 2
        # # # seen -> 1 2
        # # # current = 2
        # # # max = 2

        # # seen = deque()
        # # max_fruits = 0
        # # current_fruits = 0
        # # l, r = 0, len(fruits)-1

        # # for i in range(len(fruits)):
        # #     if fruits[i] not in seen:
        # #         if len(seen)<2:
        # #             seen.append(fruits[i])
        # #             current_fruits += 1
        # #             max_fruits = max(max_fruits, current_fruits)
        # #             r += 1
        # #         else:
        # #             seen.append(fruits[i])
        # #             seen.popleft()
        # #             l += 1
                    
        # #     else:
        # #         current_fruits += 1
        # #         max_fruits = max(max_fruits, current_fruits)
        # #         r += 1













        # # l, r = 0, len(fruits)-1
        # # storage = []
        # # count1 = 1
        # # count2 = 1
        # # while l<r:
        # #     if fruits[l+1]==fruits[l]:
        # #         count1 += 2
        # #         l += 1
        # #     if fruits[r-1]==fruits[r]:
        # #         count2 += 2
        # #         r -= 1
            