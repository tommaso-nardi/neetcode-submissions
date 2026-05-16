class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distanza = 0
        for x in range(len(nums)):
            if x > distanza:
                return False
            distanza = max(distanza,x+nums[x])
        return True