# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def ricorsione(albero,mis,mad) -> bool:
            if not albero:
                return True
            if not (mis<albero.val<mad):
                return False
            return (ricorsione(albero.left,mis,albero.val) and ricorsione(albero.right,albero.val,mad))
        
        return ricorsione(root,-1001,1001)