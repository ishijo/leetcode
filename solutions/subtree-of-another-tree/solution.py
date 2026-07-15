# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def check_same(root,subroot):
            if not root and not subroot:
                return True
            if not root or not subroot:
                return False
            if root.val != subroot.val:
                return False
            return check_same(root.left,subroot.left) and check_same(root.right,subroot.right)

        return check_same(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        
        