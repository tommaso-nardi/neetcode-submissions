"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        dictt={}

        def ricorsione(node):
            nonlocal dictt
            if node in dictt:
                return dictt[node]
            copia = Node(node.val)
            dictt[node] = copia
            for n in node.neighbors:
                copia.neighbors.append(ricorsione(n))
            return copia

        return ricorsione(node)