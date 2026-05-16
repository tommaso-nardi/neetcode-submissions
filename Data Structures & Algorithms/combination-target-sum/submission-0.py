class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ris = []
        attuale = []
        def ricorsione(i,sommaattuale): 
            #Se siamo all'ultimo step, vedi se la somma è buona e se si aggiungi
            if sommaattuale==target:
                ris.append(attuale.copy())
                return

            if i>=len(nums) or sommaattuale>target:
                return
            
            #Lato dove riprendo questo elemento (scelta valida)
            attuale.append(nums[i])
            ricorsione(i,sommaattuale+nums[i])

            #Lato dove non riprendo l'elemento e scorro
            attuale.pop()
            ricorsione(i+1,sommaattuale)
        
        #Fai partire
        ricorsione(0,0)
        return ris