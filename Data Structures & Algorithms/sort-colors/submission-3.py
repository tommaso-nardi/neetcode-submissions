class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        puntx=0
        puntm=0
        punty=len(nums)-1

        #Puntx funge da ancora mediana visto che i colori sono 3.
        #Se puntm è 0 allora deve appartenere al range di puntx, quindi scambiamo e mandiamo avanti entrambi
        #Se puntm è 1 allora sta già bene
        #Se puntm è 2 allora deve scambiarsi con punty, range dei 2, e si manda indietro punty
        while puntm<=punty:
            if nums[puntm]==0:
                nums[puntx], nums[puntm] = nums[puntm], nums[puntx]
                puntx+= 1
                puntm+= 1
            elif nums[puntm]==1:
                puntm+=1
            else:
                nums[punty],nums[puntm]=nums[puntm],nums[punty]
                punty-=1