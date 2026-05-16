# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #Un nodo è "buono" se è maggiore o uguale del nodo più grande del suo ramo all'insù
    #ovviamente se è maggiore allora sovrascriverà il massimo da comparare per quel ramo
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
                massimo=albero.val
            ricorsione(albero.left,massimo)
            ricorsione(albero.right,massimo)

        ricorsione(root,float('-inf'))
        return ris