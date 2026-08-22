class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1 or nums[0]!=nums[1]:
            return nums[0]
        i=1
        while i<len(nums)-1:
            if nums[i]!=nums[i-1] and nums[i]!=nums[i+1]:
                return nums[i]
            i+=1
        return nums[len(nums)-1]
        