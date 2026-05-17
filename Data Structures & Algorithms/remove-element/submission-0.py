class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        slotdx=len(nums)-1
        while slotdx >= 0 and nums[slotdx]==val:
            slotdx=slotdx-1

        i=0
        k=0
        while i<slotdx:
            if nums[i] == val:
                nums[i] = nums[slotdx]
                k=k+1
                slotdx=slotdx-1
                while slotdx >= 0 and nums[slotdx]==val:
                    slotdx=slotdx-1
            else:
                i=i+1
        return slotdx+1