class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sx=0
        dx=len(nums)-1
        #Logica è che dobbiamo trovare la zona "ordinata" se non abbiamo già il nostro valore tra i puntatori
        while sx<=dx:
            mid=(sx+dx)//2
            if nums[mid]==target:
                return mid
            if nums[sx]==target:
                return sx
            if nums[dx]==target:
                return dx
            
        #Se il lato ordinato è a sinistra...
            if nums[sx]<nums[mid]:
                #Vedi se li si trova il nostro valore
                if target>nums[sx] and target<nums[mid]:
                    dx=mid-1
                else:
                    sx=mid+1
        #Altrimenti se il lato ordinato è a destra, vedi se si trova la
            else:
                if target>nums[mid] and target<nums[dx]:
                    sx=mid+1
                else:
                    dx=mid-1
        return -1