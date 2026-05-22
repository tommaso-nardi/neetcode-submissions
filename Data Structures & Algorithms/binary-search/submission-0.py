class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sx=0
        dx=len(nums)-1
        while dx>sx:
            mid=(sx+dx)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                dx=mid-1
            else:
                sx=mid+1
        if nums[dx]==target:
            return dx
        return -1