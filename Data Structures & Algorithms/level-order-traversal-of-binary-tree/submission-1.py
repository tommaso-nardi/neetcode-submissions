# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        #Come scritto sul quaderno, è un depth first, per questo esercizio ci serve una queue
        ris = []
        q = collections.deque()
        q.append(root)

        #finchè ci sono elementi...
        while q:
            #vediamo quanto è grande il livello cosi. Eviteremo quindi di includere i prossimi livelli in una
            #stessa lista
            lun = len(q)
            livello = []
            #prendi l'elemento con il pop, salvati il valore, fai append dei suoi valori per il prossimo livello
            #tanto se sono nulli non si salva nulla
            for i in range(lun):
                nodo = q.popleft()
                if nodo:
                    livello.append(nodo.val)
                    q.append(nodo.left)
                    q.append(nodo.right)
            if livello:
                ris.append(livello)
        return ris