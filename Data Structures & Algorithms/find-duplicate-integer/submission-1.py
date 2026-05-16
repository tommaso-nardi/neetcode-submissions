class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            indice = abs(nums[i])
            if nums[indice] < 0:
                return indice
            nums[indice] = nums[indice] * -1