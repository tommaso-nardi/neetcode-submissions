class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        sx=0
        dx=k-1
        mindiff=float("inf")
        while dx<len(nums):
            mindiff=min((nums[dx]-nums[sx]),mindiff)
            dx+=1
            sx+=1
        return mindiff