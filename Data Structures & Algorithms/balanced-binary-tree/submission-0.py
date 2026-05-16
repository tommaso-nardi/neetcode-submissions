# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balanced(root):
            if not root:
                return [True,0]

            sx=balanced(root.left)
            dx=balanced(root.right)
            bal=sx[0] and dx[0] and abs(sx[1] - dx[1]) <= 1
                
            return [bal,1+max(sx[1],dx[1])]
        return balanced(root)[0]