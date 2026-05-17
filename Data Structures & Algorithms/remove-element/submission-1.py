class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        #Puntatore di destra che deve dirci la posizione dell'ultimo elemento valido
        slotdx=len(nums)-1
        #Condizione per spostare slotdx se è invalido
        while slotdx >= 0 and nums[slotdx]==val:
            slotdx=slotdx-1

        i=0
        while i<slotdx:
            #Se il numero visto da i è invalido, spostalo alla posizione di dx e fai tornare indietro dx
            if nums[i] == val:
                nums[i] = nums[slotdx]
                slotdx=slotdx-1
                while slotdx >= 0 and nums[slotdx]==val:
                    slotdx=slotdx-1
            #Altrimenti i+1
            else:
                i=i+1
        return slotdx+1