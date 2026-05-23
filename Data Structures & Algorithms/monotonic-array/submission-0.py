class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]>nums[1]: segno="pos"
        else: segno="neg"
        
        if segno=="pos":
            for i in range(1,len(nums)-1):
                if nums[i]<nums[i+1]:
                    return False
        elif segno=="neg":
            for i in range(1,len(nums)-1):
                if nums[i]>nums[i+1]:
                    return False
        
        return True