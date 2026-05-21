class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        conteggio = collections.Counter(tasks)

        #Salvati tutte le frequenze, ci interessano solo loro, in una MAXHEAP
        max_heap = [-freq for freq in conteggio.values()]
        heapq.heapify(max_heap)

        #Una lista per il cooldown dei vari task
        cooldown=collections.deque()
    
        tempo=0

        #Finchè ci sono elementi
        while max_heap or cooldown:
            #Avanza il tempo
            tempo=tempo+1
            #Prendi un task
            if max_heap:
                task=heapq.heappop(max_heap)
                #Se devi farlo ancora (+1 < 0 perchè sono salvati in negativo per via della MAXHEAP)
                #Allora salva il suo cooldown con tempo+n
                if task+1 < 0:
                    cooldown.append([task+1,tempo+n])
            #Se devi sbloccare qualcosa, sblocca poppando e prendendo il valore, rimettilo in queue
            if cooldown and cooldown[0][1] == tempo:
                task=cooldown.popleft()
                heapq.heappush(max_heap,task[0])
        return tempo