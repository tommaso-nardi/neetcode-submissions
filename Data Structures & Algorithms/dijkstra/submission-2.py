class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        dictt={}
        

        #1o valore : Punto Partenza
        #2o valore : Destinazione
        #3o valore : Costo tra 1 e 10

        #Idea: Salvo nel dizionario dictt l'attuale chiave-costo minore per ognuno con una navigazione che
        #se ho già visto il nodo e la distanza attuale è maggiore di quella salvata mi fermo
        #se è minore allora devo salvarla e ri-runnare la ricorsione. Una volta finito stampo i dizionari
        #(che manco avevo visto che l'output vuole un dizionario)

        #Una lista/dizionario per vedere chi raggiunge cosa con che costo di transito
        adj = defaultdict(list)
        for inizio, destinazione, costo in edges:
            adj[inizio].append((destinazione, costo))

        #La ricorsione, si capisce
        def ricorsione(nodo,costoatt):
            nonlocal dictt
            if nodo in dictt:
                if costoatt < dictt[nodo]:
                    dictt[nodo] = costoatt
                else:
                    return
            else:
                dictt[nodo] = costoatt
            for vicino, costo in adj[nodo]:
                ricorsione(vicino, costoatt+costo)
            return

        ricorsione(src,0)
        for i in range(n):
            if i not in dictt:
                dictt[i] = -1
        return dictt
        