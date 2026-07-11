# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        queue = deque([root])
        output = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                    #level.append(node.left.val)
                if node.right:
                    queue.append(node.right)
                    #level.append(node.right.val)

            output.append(level[-1])
        return output
        

        
        #return [root.val] + self.rightSideView(root.right)