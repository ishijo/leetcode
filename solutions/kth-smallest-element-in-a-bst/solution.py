# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                heapq.heappush(heap,node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)

        for i in range(k-1):
            heapq.heappop(heap)
        
        return heapq.heappop(heap)
        

