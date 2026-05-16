class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.append(0)
        nums.append(0)
        valore = [0] * (len(nums)+2)
        for i in range(len(nums)-1, -1, -1):
            valore[i] = max(nums[i] + valore[i+2], valore[i+1])
        return valore[0]