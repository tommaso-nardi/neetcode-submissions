# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ris = []
        q = collections.deque()
        q.append(root)

        while q:
            lun = len(q)
            ultimo = None
            for i in range(lun):
                nodo=q.popleft()
                ultimo=nodo
                if nodo:
                    if nodo.left:
                        q.append(nodo.left)
                    if nodo.right:
                        q.append(nodo.right)
            ris.append(ultimo.val)
        return ris