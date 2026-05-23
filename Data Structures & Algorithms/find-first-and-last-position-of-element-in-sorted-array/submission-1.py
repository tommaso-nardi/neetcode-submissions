class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        sx=0
        dx=len(nums)-1
        #Se dovrei fare in teoria una ricerca binaria che poi continua richiamando due funzioni
        #Ci cerchiamo i nostri indici direttamente con le due funzioni ricorsive

        #Sx va a sinistra a ritroso salvandosi gli indici nums[mid]==target che trova per la via
        #restituendo l'ultimo trovato, quello più a sx di tutti grazie a dx=mid-1 quando trova
        def backupsx(sx,dx):
            indice=-1
            while dx>=sx:
                mid=(dx+sx)//2
                if nums[mid]>target:
                    dx=mid-1
                elif nums[mid]<target:
                    sx=mid+1
                if nums[mid]==target:
                    indice = mid
                    dx=mid-1
            return indice

        #Dx fa la cosa al contrario, va a destra a ritroso salvandosi gli indici nums[mid]==target che
        #trova per la via, resituendo l'ultimo trovato, più a dx di tutti grazie a sx=mid+1 quando trova
        def backupdx(sx,dx):
            indice=-1
            while dx>=sx:
                mid=(dx+sx)//2
                if nums[mid]>target:
                    dx=mid-1
                elif nums[mid]<target:
                    sx=mid+1
                if nums[mid]==target:
                    indice = mid
                    sx=mid+1
            return indice

        return[backupsx(0,len(nums)-1),backupdx(0,len(nums)-1)]
