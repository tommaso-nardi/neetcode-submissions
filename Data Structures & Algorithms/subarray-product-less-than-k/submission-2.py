class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        punts=0
        puntd=0
        prodattuale=1
        prodvalidi=0
        #Logica che se c'è un subarray che va da X a Y che va bene allora
        #tutti i subarray (che sono in tutto "(y-1)-x+1") al suo interno vanno bene a loro volta
        #l'aggiornamento prodvalidi+=((puntd-1)-punts+1) segue proprio questa regola
        while puntd<len(nums):
            prodattuale*=nums[puntd]
            puntd+=1
            while prodattuale>=k and punts<puntd:
                prodattuale//=nums[punts]
                punts+=1
            prodvalidi+=((puntd-1)-punts+1)

        return prodvalidi