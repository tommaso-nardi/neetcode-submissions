# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ris = []
        q = collections.deque()
        q.append(root)

        while q:
            lun = len(q)
            livello = []
            for i in range(lun):
                nodo = q.popleft()
                if nodo:
                    livello.append(nodo.val)
                    q.append(nodo.left)
                    q.append(nodo.right)
            if livello:
                ris.append(livello)
        return ris