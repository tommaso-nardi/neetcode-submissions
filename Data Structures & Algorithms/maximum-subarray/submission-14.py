class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return -1
        sommamax=nums[0]
        somma=nums[0]
        i=1
        while i <= len(nums)-1:
            if nums[i] > somma+nums[i]:
                somma=nums[i]
                if nums[i]>sommamax:
                    sommamax=nums[i]
            else:
                somma=somma+nums[i]
                if somma>sommamax:
                    sommamax=somma
            i=i+1
        return sommamax