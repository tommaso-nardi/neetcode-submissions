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
        
        def ricorsione(node) -> Optional['Node']:
            nonlocal dictt
            if node in dictt:
                return dictt[node]
            attuale = Node(node.val)
            dictt[node] = attuale
            for n in node.neighbors:
                attuale.neighbors.append(ricorsione(n))
            return attuale

        return ricorsione(node)