# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good = 0
        prev_max = root.val

        def count(root,prev_max):
            nonlocal good
            if not root:
                return 
            if root.val>=prev_max:
                good += 1
            prev_max = max(prev_max,root.val)
            if root.left:
                count(root.left,prev_max)
            if root.right:
                count(root.right,prev_max)


        count(root,root.val)
        return good

            
        