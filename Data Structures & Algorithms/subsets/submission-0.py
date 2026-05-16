class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ris = []
        attuale = []
        def ricorsione(i):
            #Se siamo all'ultimo step, ritorna quanto hai e fermati
            if i>=len(nums):
                ris.append(attuale.copy())
                return

            #Lato dove prendo l'elemento i
            attuale.append(nums[i])
            ricorsione(i+1)

            #Lato dove non prendo l'elemento i
            attuale.pop()
            ricorsione(i+1)
        ricorsione(0)
        return ris