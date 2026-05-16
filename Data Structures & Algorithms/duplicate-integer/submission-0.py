class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appoggio = nums
        for n in range(len(nums)):
            for k in range(len(nums)):
                if (appoggio[k]==nums[n]):
                    if (k!=n):
                        return True
        return False