class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visti={}
        for i in range(len(nums)):
            if nums[i] in visti:
                if abs(i-visti[nums[i]]) <=k:
                    return True 
            visti[nums[i]] = i
        return False