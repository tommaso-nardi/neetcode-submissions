class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        sx=0
        dx=len(nums)-1
        ris=0
        while dx>=sx:
            if nums[dx]+nums[sx]<=target:
                ris+=2**(dx-sx)
                sx+=1
            else:
                dx-=1
        return ris%(10**9+7)