# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q:
            return True
        
        def lato(sx,dx):
            if sx == None and dx == None:
                return True
            if not sx or not dx or sx.val != dx.val:
                return False
            
            return lato(sx.left,dx.left) and lato(sx.right,dx.right)

        if lato(p,q):
            return True
        else:
            return False