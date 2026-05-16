class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        mid = []
        i = 0
        for i in range(len(nums)-1):
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[j]+nums[k]+nums[i]==0:
                    mid.append(nums[i])
                    mid.append(nums[j])
                    mid.append(nums[k])
                    if mid not in sol:
                        sol.append(mid)
                    mid=[]
                    j=j+1
                    k=len(nums)-1
                elif nums[j]+nums[k]+nums[i]>0:
                    k=k-1
                elif nums[j]+nums[k]+nums[i]<0:
                    j=j+1
        return sol

