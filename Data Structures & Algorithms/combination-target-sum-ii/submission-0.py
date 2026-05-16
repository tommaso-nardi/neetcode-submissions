class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ris = []
        attuale = []
        def ricorsione(i,sommaattuale): 
            #Se siamo all'ultimo step, vedi se la somma è buona e se si aggiungi
            if sommaattuale==target:
                ris.append(attuale.copy())
                return

            if i>=len(candidates) or sommaattuale>target:
                return
            
            #Lato dove prendo l'elemento i se non presente già
            attuale.append(candidates[i])
            ricorsione(i+1,sommaattuale+candidates[i])
            attuale.pop()

            #Lato dove non prendo l'elemento i e scorro
            numero = candidates[i]
            while i<len(candidates) and candidates[i] == numero:
                i=i+1
            if i>=len(candidates):
                return
            ricorsione(i,sommaattuale)
        
        #Fai partire
        ricorsione(0,0)
        return ris