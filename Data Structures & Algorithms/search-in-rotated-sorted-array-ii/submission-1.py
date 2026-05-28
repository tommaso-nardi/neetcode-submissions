class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        sx=0
        dx=len(nums)-1
        while sx<=dx:
            mid=(sx+dx)//2
            if nums[mid]==target:
                return True
            if nums[sx]==target:
                return True
            if nums[dx]==target:
                return True
            #Uguale al caso precedente solo con il controllo del loop
            if nums[sx]==nums[mid]==nums[dx]:
                sx+=1
                dx-=1
                continue
            
            if nums[sx]<=nums[mid]:
                if target>=nums[sx] and target<=nums[mid]:
                    dx=mid-1
                else:
                    sx=mid+1
            else:
                if target>=nums[mid] and target<=nums[dx]:
                    sx=mid+1
                else:
                    dx=mid-1
        return False