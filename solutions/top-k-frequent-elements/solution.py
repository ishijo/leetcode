#from Collections import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num,0) + 1

        k_target = k

        for k,v in counts.items():
            if len(heap)<k_target or v>heap[0][0]:
                heapq.heappush(heap, [v,k])
            if len(heap)>k_target:
                heapq.heappop(heap)
        
        return [k for v,k in heap]
