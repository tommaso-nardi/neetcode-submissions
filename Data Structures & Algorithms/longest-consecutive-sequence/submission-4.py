class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        contattuale=1
        contmax=1
        last=nums[0]
        for i in range(1, len(nums)):
            if nums[i] == last:
                continue
            if nums[i] == last+1:
                contattuale = contattuale+1
                if contattuale > contmax:
                    contmax=contattuale
            else:
                contattuale=1
            last=nums[i]
        return contmax