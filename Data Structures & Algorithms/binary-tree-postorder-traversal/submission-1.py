# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ris=[]
        stack=[root]

        while stack:
            nodo=stack.pop()
            ris.append(nodo.val)

            if nodo.left:
                stack.append(nodo.left)
            if nodo.right:
                stack.append(nodo.right)
        
        return ris[::-1]