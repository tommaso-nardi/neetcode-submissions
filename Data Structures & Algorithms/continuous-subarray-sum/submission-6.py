class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visti={0:-1}
        sommaatt=0
        indiceatt=-1

        for i in nums:
            sommaatt+=i
            indiceatt+=1
            if sommaatt%k in visti:
                if indiceatt-visti[sommaatt%k]>=2:
                    return True
            else:
                visti[sommaatt%k]=indiceatt

        return False