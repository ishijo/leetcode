# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and q:
            return False
        elif p and not q:
            return False
        elif not p and not q:
            return True
        
            
        if p.val == q.val:
            
            if not self.isSameTree(p.left,q.left):
                return False
            elif not self.isSameTree(p.right,q.right):
                return False
            return True
        else:
            return False
