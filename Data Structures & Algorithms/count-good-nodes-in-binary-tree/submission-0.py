# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ris = 0

        def ricorsione(albero,massimo):
            nonlocal ris
            if not albero:
                return
            if albero.val>=massimo:
                ris = ris+1
            massimo=max(massimo,albero.val)
            ricorsione(albero.left,massimo)
            ricorsione(albero.right,massimo)

        ricorsione(root,-101)
        return ris