# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
        
#         return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        def max_ht(root):
            if not root:
                return 0
            return 1 + max(max_ht(root.left), max_ht(root.right))

        if not root:
            return 0

        if not root.left and not root.right:
            val = 0
        elif root.left and root.right:
            val = max_ht(root.left) + max_ht(root.right)
            #return max( max_ht(root.left) , max_ht(root.right) , max_ht(root.left) + max_ht(root.right) )
        elif root.left or root.right:
            if root.left:
                val = max_ht(root.left)
            elif root.right:
                val = max_ht(root.right)
        return max(val, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
            
























        
        # if not root.left and not root.right:
        #     return 0
        # if root.left and root.right:
        #     return 2 + max_ht(root.left) + max_ht(root.right)
        # if root.left or root.right:
        #     if root.left:
        #         diameterOfBinaryTree(root.left)
        #     if root.right:
        #         diameterOfBinaryTree(root.right)
        