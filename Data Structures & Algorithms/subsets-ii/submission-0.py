class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ris = []
        attuale = []
        nums.sort()
        def ricorsione(i):
            #Se siamo all'ultimo step, ritorna quanto hai e fermati
            if i>=len(nums):
                ris.append(attuale.copy())
                return

            #Lato dove prendo l'elemento i
            attuale.append(nums[i])
            ricorsione(i+1)
            attuale.pop()

            #Lato dove non prendo l'elemento i
            indice = i+1
            while indice<len(nums) and nums[indice] == nums[i]:
                indice = indice+1
            ricorsione(indice)
        
        #Fai partire
        ricorsione(0)
        return ris