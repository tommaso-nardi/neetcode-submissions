class Solution:
    def findMin(self, nums: List[int]) -> int:
        sx =0
        dx = len(nums)-1
        ris=nums[0]

        while sx<=dx:
            mid = (sx+dx)//2
            ris = min(ris,nums[mid])
            if nums[sx]<nums[dx]:
                ris=min(ris,nums[sx])

            if nums[mid]>=nums[sx]:
                sx=mid+1
            else:
                dx=mid-1
        return ris