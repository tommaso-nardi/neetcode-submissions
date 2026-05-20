class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if len(tasks)==1:
            return [0]
        ris = []
        prio = []
        #Serve anche una lista dei task che tiene conto del loro i (quello che vuole in caso di parità)
        #che verrà richiamato praticamente solo nel push, si aggiunge il tempo richiesto e l'indice i
        tasks_indice = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        tasks_indice.sort()
        processati=0
        momento=0
        indiceattuale=0
        ultimoindice=0

        while processati!=len(tasks):
            if not prio:
                momento=max(momento,tasks_indice[ultimoindice][0])
            # Usiamo un while dinamico al posto del for
            while ultimoindice < len(tasks_indice) and tasks_indice[ultimoindice][0] <= momento:
                heapq.heappush(prio, (tasks_indice[ultimoindice][1], tasks_indice[ultimoindice][2]))
                # Se non si tiene traccia di questo si perde tutto
                ultimoindice += 1
            y,x = heapq.heappop(prio)
            ris.append(x)
            processati+=1
            momento+=y
        
        return ris