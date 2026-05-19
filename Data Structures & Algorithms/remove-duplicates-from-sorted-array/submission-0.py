class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        i=0
        j=i+1
        while j in range(len(nums)):
            while j < len(nums) and nums[i] == nums[j]:
                j=j+1
            if j == len(nums):
                break
            nums[i+1]=nums[j]
            i=i+1
        return i+1
        