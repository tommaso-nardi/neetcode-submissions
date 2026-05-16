# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q) -> bool:
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
            
        if not subRoot:
            return True
        if not root:
            return False
        if isSameTree(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)