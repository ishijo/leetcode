# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:

        if p.right:
            p_right = p.right
            while p_right.left:
                p_right = p_right.left
            return p_right

        traverse = root
        lowest_max = None
        
        while traverse:
            if traverse.val>p.val:
                lowest_max = traverse
                traverse = traverse.left
                #lowest_max = min(lowest_max,traverse.val)
            else:
                traverse = traverse.right
        return lowest_max

        