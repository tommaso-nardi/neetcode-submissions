class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if range(len(nums)) == 0:
            return True
        obj = len(nums)-1
        for x in range(len(nums)-2,-1,-1):
            if x + nums[x] >= obj:
                obj = x
        if (obj == 0):
            return True
        return False
                