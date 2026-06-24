class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costi=[float("inf")]*n
        costi[src]=0

        #Per ogni viaggio in flights ci salviamo destinazione e prezzo alla key 'partenza'
        grafo = defaultdict(list)
        for u, v, w in flights:
            grafo[u].append((v, w))

        coda = deque([(src, 0)])
        stop = 0

        #Con la deque vediamo fin dove possiamo andare nei limiti di k
        while coda and stop<=k:
            #Finchè la coda non è vuota
            for _ in range(len(coda)):
                #Prendi il pirmo elemento in coda, sicuro è una mossa valida perchè siamo in range k
                nodo,costo=coda.popleft()

                #E per ogni nodo che possiamo raggiungere vediamo se ci conviene o no
                for vicino,prezzo in grafo[nodo]:
                    nuovo_costo=costo+prezzo

                    #Se si salva il costo e metti la destinazione in coda per la prossima iterazione
                    if nuovo_costo<costi[vicino]:
                        costi[vicino]=nuovo_costo
                        coda.append((vicino,nuovo_costo))
            stop+=1
        
        return costi[dst] if costi[dst]!=float("inf") else -1