# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ris = root

        while ris:
            if ris.val<p.val and ris.val<q.val:
                ris = ris.right
            elif ris.val>p.val and ris.val>q.val:
                ris = ris.left
            else:
                return ris