# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        #Prendi la radice attuale
        root=TreeNode(preorder[0])
        #e salvati il suo indice per fare i range
        indice_root_inorder=inorder.index(preorder[0])
        #Sinistra ha come preorder tutto ciò che precede l'indice (0 escluso)
        #mentre inorder tutto ciò che lo sussegue
        root.left=self.buildTree(preorder[1:indice_root_inorder+1],inorder[:indice_root_inorder])
        #Destra ha entrambi come tutto ciò che sussegue l'indice
        root.right=self.buildTree(preorder[indice_root_inorder+1:],inorder[indice_root_inorder+1:])
        return root