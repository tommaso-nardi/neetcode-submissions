class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sx=0
        dx=len(nums)-1
        while sx<=dx:
            mid=(sx+dx)//2
            if nums[mid]==target:
                return mid
            if nums[sx]==target:
                return sx
            if nums[dx]==target:
                return dx
            
            if nums[sx]<nums[mid]:
                if target>nums[sx] and target<nums[mid]:
                    dx=mid-1
                else:
                    sx=mid+1
            else:
                if target>nums[mid] and target<nums[dx]:
                    sx=mid+1
                else:
                    dx=mid-1
        return -1