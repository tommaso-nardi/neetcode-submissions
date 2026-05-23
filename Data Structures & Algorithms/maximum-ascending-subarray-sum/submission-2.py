class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        tot=nums[0]
        massimo=nums[0]
        for dx in range(1,len(nums)):
            if nums[dx]<=nums[dx-1]:
                tot=0
            tot=tot+nums[dx]
            massimo=max(tot,massimo)
        return massimo