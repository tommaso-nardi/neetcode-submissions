class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        punts=0
        puntd=0
        prodattuale=1
        prodvalidi=0
        while puntd<len(nums):
            prodattuale*=nums[puntd]
            puntd+=1
            while prodattuale>=k and punts<puntd:
                prodattuale//=nums[punts]
                punts+=1
            prodvalidi+=((puntd-1)-punts+1)

        return prodvalidi