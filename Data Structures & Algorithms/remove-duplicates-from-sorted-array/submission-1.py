class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        i=0
        j=i+1
        #Sostituisci tutti i numeri che sono uguali, j va avanti finchè non ha un valore diverso da i
        #e quando succede allora sposti avanti i
        while j in range(len(nums)):
            while j < len(nums) and nums[i] == nums[j]:
                j=j+1
            if j == len(nums):
                break
            nums[i+1]=nums[j]
            i=i+1
        return i+1
        