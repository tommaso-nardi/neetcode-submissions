class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nonbit=set()
        nums=sorted(nums)
        i=0
        for n in nums:
            if n != i:
                return i
            else:
                i=i+1
        return i