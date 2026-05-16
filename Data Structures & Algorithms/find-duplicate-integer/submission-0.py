class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dictt={}

        for i in range(len(nums)):
            if nums[i] in dictt:
                return nums[i]
            dictt[nums[i]] = nums[i]