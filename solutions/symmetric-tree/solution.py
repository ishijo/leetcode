# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mirror(self,a,b) -> bool:
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val == b.val and self.mirror(a.left, b.right) and self.mirror(a.right, b.left):
            return True
        return False
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.mirror(root.left,root.right)
        

        
        # if root.left == root.right:
        #     return self.isSymmetric(root.left.left) == self.isSymmetric(root.right.right) and self.isSymmetric(root.left.right) == self.isSymmetric(root.right.left)