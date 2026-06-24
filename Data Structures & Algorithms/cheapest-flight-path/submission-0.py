class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costi=[float("inf")]*n
        costi[src]=0

        grafo = defaultdict(list)
        for u, v, w in flights:
            grafo[u].append((v, w))

        coda = deque([(src, 0)])
        stop = 0

        while coda and stop<=k:
            for _ in range(len(coda)):
                nodo,costo=coda.popleft()

                for vicino,prezzo in grafo[nodo]:
                    nuovo_costo=costo+prezzo

                    if nuovo_costo<costi[vicino]:
                        costi[vicino]=nuovo_costo
                        coda.append((vicino,nuovo_costo))
            stop+=1
        
        return costi[dst] if costi[dst]!=float("inf") else -1