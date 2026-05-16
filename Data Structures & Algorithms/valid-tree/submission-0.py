class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visitaattuale=set()
        preMap={i:[] for i in range(n)}
        for root,foglia in edges:
            preMap[root].append(foglia)
            preMap[foglia].append(root)

        def ricorsione(nodo,prima):
            if nodo in visitaattuale:
                return False
            visitaattuale.add(nodo)
            for vicino in preMap[nodo]:
                if vicino == prima:
                    continue
                if not ricorsione(vicino,nodo):
                    return False
            return True

        return ricorsione(0, -1) and len(visitaattuale) == n