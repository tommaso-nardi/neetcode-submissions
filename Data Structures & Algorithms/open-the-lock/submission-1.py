class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        #La logica sta nel voler fare una ricerca BFS visto che vogliamo vedere ogni volta
        #il numero minimo di mosse, la logica base è che se un valore è in deadends allora
        #lo scartiamo. Mentre se non lo è allora proviamo a vedere che succede
        #se spostiamo i suoi valori.
        #Con "visti" ci assicuriamo che un valore viene considerato una volta sola
        #Cosi evitiamo di loopare su roba già vista

        visti={}
        q = collections.deque()
        q.append("0000")
        mosse=0
        #Trasformandolo in set la ricerca è ora O(1)
        deadends=set(deadends)

        while q:
            #Per il livello attuale (lun(q) ha solo quelli del livello 'mosse' attuale)
            lunliv=len(q)
            #Prendi tutti i valori uno alla volta e vedi se è una condizione base
            for i in range(lunliv):
                val=q.popleft()
                if val == target:
                    return mosse
                if val in deadends:
                    continue
                #Se no, per ogni suo carattere prendi la cifra, vai avanti e indietro
                #E, se è valido e non è già stato visto, mettilo nella queue
                for j in range(4):
                    cifra = int(val[j])
                    avanti=((cifra+1)%10)
                    indietro=((cifra-1)%10)
                    combinazione_avanti = val[:j] + str(avanti) + val[j+1:]
                    combinazione_indietro = val[:j] + str(indietro) + val[j+1:]
                    if combinazione_avanti not in deadends and combinazione_avanti not in visti:
                        q.append(combinazione_avanti)
                        visti[combinazione_avanti] = combinazione_avanti
                    if combinazione_indietro not in deadends and combinazione_indietro not in visti:
                        q.append(combinazione_indietro)
                        visti[combinazione_indietro] = combinazione_indietro
            #Aumenta il numero di mosse necessarie e torna indietro
            mosse=mosse+1

        return -1
