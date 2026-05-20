# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ris=[]
        def ricorsione(root):
            if not root:
                return
            
            ricorsione(root.left)
            ricorsione(root.right)
            ris.append(root.val)

        ricorsione(root)
        return ris