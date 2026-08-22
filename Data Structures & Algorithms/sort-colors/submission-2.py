class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        puntx=0
        puntm=0
        punty=len(nums)-1

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