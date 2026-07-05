# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # 3, 9 20, null null 15 7 | null nulll null null 1 1 null null
        # 3, 20 9, null null 15 7 | null null 1 1 null null null null


        # 7 15 null null
        #  
        # [3] [20,9] []
        if not root:
            return []

        s1 = [root]
        s2 = []
        level = []
        result = []

        while s1 or s2:
            while s1:
                node = s1.pop()
                level.append(node.val)
                if node.left: s2.append(node.left)
                if node.right: s2.append(node.right)
            result.append(level)
            level = []

            while s2:
                node = s2.pop()
                level.append(node.val)
                if node.right: s1.append(node.right)
                if node.left: s1.append(node.left)
            if level!=[]: result.append(level)
            level = []

        return result
            

















        # queue = deque()
        # queue.append(root)
        # result = []

        # while queue:
        #     #stack = []
        #     for _ in range(len(queue)):
        #         level = []
        #         node = queue.popleft()
        #         #stack.append(node)
        #         if node:
        #             level.append(node.val)
        #             if node.left:
        #                 queue.append(node.left)
        #             if node.right:
        #                 queue.append(node.right)
                    
        #         result.append(level)
                
        # return result

