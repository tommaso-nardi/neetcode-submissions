# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            # Il nodo si trova nel sottoalbero sinistro
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            # Il nodo si trova nel sottoalbero destro
            root.right = self.deleteNode(root.right, key)
        else:
            # Caso 1 & 2: Il nodo ha 0 figli o 1 solo figlio
            if not root.left:
                return root.right  # Se manca il sinistro, restituisco il destro (può essere None)
            if not root.right:
                return root.left   # Se manca il destro, restituisco il sinistro
            
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root