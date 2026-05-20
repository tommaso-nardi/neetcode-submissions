# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ris=[]
        def ricorsione(root):
            if not root:
                return
            
            ricorsione(root.left)
            ris.append(root.val)
            ricorsione(root.right)

        ricorsione(root)
        return ris