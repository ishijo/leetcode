# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # if not root:
        #     return True
        # left,right = True,True
        # if root.left and root.left.val >= root.val:
        #     left = False
        # if root.right and root.right.val <= root.val:
        #     right = False

        # if left and right:
        #     return self.isValidBST(root.left) and self.isValidBST(root.right)

        curr = root
        stack = []
        to_validate = []
        prev = None
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
                
            node = stack.pop()
            if prev:
                if node.val <= prev.val:
                    return False
            prev = node
            if node.right:
                curr = node.right
        return True
            
















            # if node.right:
            #     curr = prev.right
            
            # if curr.val <= prev.val:
            #     return False
            






            # to_validate.append(node)

            # if to_validate[-1].val >= stack[-1].val:
            #     return False

            # curr = stack[-1].right
            # to_validate.append(stack.pop())

            # if to_validate[-1].val >= curr.val:
            #     return False
            
            


         














        # if not root:
        #     return True
        
        # if (root.left and (root.val < root.left.val or root.val==root.left.val) ) or (root.right and (root.val > root.right.val or root.val ==root.right.val) ):
        #     return False
        
        # return self.isValidBST(root.left) and self.isValidBST(root.right)
        
        