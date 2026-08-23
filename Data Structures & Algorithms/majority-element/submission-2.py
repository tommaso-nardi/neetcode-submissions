class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        visti={}

        for n in nums:
            if n in visti:
                visti[n]+=1
                if visti[n]>(len(nums)/2):
                    return n
            else:
                visti[n]=1
        
        return nums[0]