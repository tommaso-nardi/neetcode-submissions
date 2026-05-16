# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        ris = root
        lis = []

        while ris or lis:
            while ris:
                lis.append(ris)
                ris=ris.left

            ris = lis.pop()
            count=count+1
            if count==k:
                return ris.val
            ris = ris.right