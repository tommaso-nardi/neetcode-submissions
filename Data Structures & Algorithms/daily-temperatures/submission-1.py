class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        #Salvati la grandezza che ti serve con il default 0
        ris = [0] * len(temperatures)
        stack = []

        #Si risolve con lo stack, per ogni valore...
        for i in range(len(temperatures)):
            #Se ci sono elementi nello stack e il primissimo elemento è più piccolo (nell'array) di quello
            #che stiamo vedendo ora in posizione i...
            #allora togli tutto e salva come risultato la differenza negli indici (che è esplicitamente la richiesta)
            while stack and temperatures[stack[-1]] < temperatures[i]:
                rimuovi=stack.pop()
                ris[rimuovi] = i-rimuovi

            #In ogni caso aggiungi il nuovo elementi temperatures[i] all'append
            stack.append(i)
        return ris