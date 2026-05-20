class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        if len(tasks)==1:
            return [0]
        ris = []
        prio = []
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
                # Avanzi l'indice di 1 per passare al prossimo compito del nastro
                ultimoindice += 1
            y,x = heapq.heappop(prio)
            ris.append(x)
            processati+=1
            momento+=y
        
        return ris