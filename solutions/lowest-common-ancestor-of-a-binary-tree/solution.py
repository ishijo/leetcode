# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return None

        if root==p or root ==q:
            return root
        
        left_lca = self.lowestCommonAncestor(root.left,p,q)
        right_lca = self.lowestCommonAncestor(root.right,p,q)
        
        if left_lca and right_lca:
            return root
        elif left_lca and not right_lca:
            return left_lca
        elif right_lca and not left_lca:
            return right_lca
        else:
            return None 

            


            

        