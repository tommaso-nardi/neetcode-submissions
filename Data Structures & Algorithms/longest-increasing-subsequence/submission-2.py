class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        valori = [1] * len(nums)
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]<nums[i]:
                    valori[i] = max(valori[i],valori[j]+1)
        return max(valori)