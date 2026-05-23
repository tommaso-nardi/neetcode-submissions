class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums)==0:
            return [-1,-1]
        sx=0
        dx=len(nums)-1

        def backupsx(sx,dx):
            indice=-1
            while dx>=sx:
                mid=(dx+sx)//2
                if nums[mid]>target:
                    dx=mid-1
                elif nums[mid]<target:
                    sx=mid+1
                if nums[mid]==target:
                    indice = mid
                    dx=mid-1
            return indice

        def backupdx(sx,dx):
            indice=-1
            while dx>=sx:
                mid=(dx+sx)//2
                if nums[mid]>target:
                    dx=mid-1
                elif nums[mid]<target:
                    sx=mid+1
                if nums[mid]==target:
                    indice = mid
                    sx=mid+1
            return indice

        return[backupsx(0,len(nums)-1),backupdx(0,len(nums)-1)]
