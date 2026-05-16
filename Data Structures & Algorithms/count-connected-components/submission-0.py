class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cont = 0
        visitaattuale=set()
        preMap={i:[] for i in range(n)}
        for root,foglia in edges:
            preMap[root].append(foglia)
            preMap[foglia].append(root)

        def ricorsione(nodo,prima):
            if nodo in visitaattuale:
                return
            visitaattuale.add(nodo)
            for vicino in preMap[nodo]:
                if vicino == prima:
                    continue
                ricorsione(vicino,nodo)
        
        for i in range(n):
            if i not in visitaattuale:
                cont = cont+1
                ricorsione(i,-1)
        return cont