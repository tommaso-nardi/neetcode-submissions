class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #Ci serve il max heap per vedere chi devo tentare ad inserire, quindi ricordiamo i numeri sono
        #negativi e il conteggio va al contrario, si fa +1
        max_heap=[]
        for conteggio, lettera in [(a, "a"), (b, "b"), (c, "c")]:
            if conteggio > 0:
                heapq.heappush(max_heap, (-conteggio, lettera))
        
        #Temp si usa per conservare una lettera se non inseribile
        ris=[]

        while max_heap:
            conteggio,lettera=heapq.heappop(max_heap)

            #Se non possiamo inserirla perchè sarebbero tre di fila...
            if len(ris)>=2 and ris[-1]==lettera and ris[-2]==lettera:
                #Se non ci sono altri elementi abbiamo finito
                if not max_heap:
                    break
                #Altrimenti prendiamo questo secondo elemento e lo inseriamo
                conttemp,lettemp=heapq.heappop(max_heap)
                ris.append(lettemp)
                conttemp+=1
                if conttemp<0:
                    heapq.heappush(max_heap,(conttemp,lettemp))
                heapq.heappush(max_heap,(conteggio,lettera))
            else:
                ris.append(lettera)
                conteggio+=1
                if conteggio<0:
                    heapq.heappush(max_heap,(conteggio,lettera))
        
        return "".join(ris)