class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #Il problema si traduce in un problema di grafi, solo che invece di sommare bisogna
        #moltiplicare e dividere per i percorsi. "a,b" = 4 allora "b,a" = 0.25 perchè 1/valore originale
        ris=[]
        #Defaultdict si assicura che non esplode se qualcosa non c'è, la crea
        percorsi=defaultdict(dict)

        for (u, v), val in zip(equations, values):
            #u è la prima variabile (es. "a"), v è la seconda (es. "b")
            #val è il risultato numerico (es. 4.0)
            #Stessa cosa di un percorso normale solo che qui moltiplichiamo invece che sommare

            #Inseriamo la strada di andata: u -> v
            percorsi[u][v] = val

            #Inseriamo la strada di ritorno invertita: v -> u perchè è valida essendo non direzionato
            percorsi[v][u] = 1.0 / val
        
        #Se siamo arrivati, bene, ritorna 1, non serve fare altro
        def ricorsione(attuale,destinazione,visitati):
            if attuale==destinazione:
                return 1.0
            visitati.add(attuale)
            #Per ogni percorso che puoi fare, fallo. Se arrivi a destinazione parte
            #la ricorsione che moltiplica tutti i valori in catena usati per arrivare a destinazione
            #(sicuro si è fatto il percorso minimo) per logica DFS
            for valido,valore in percorsi[attuale].items():
                if valido not in visitati:
                    temp=ricorsione(valido,destinazione,visitati)
                    if temp!=-1:
                        return valore*temp
            return -1
        
        #Assicurati che i valori che cerchi dalla query esistono davvero
        for query in queries:
            if query[0] not in percorsi or query[1] not in percorsi:
                ris.append(-1)
            else:
                ris.append(float(ricorsione(query[0],query[1],set())))

        return ris