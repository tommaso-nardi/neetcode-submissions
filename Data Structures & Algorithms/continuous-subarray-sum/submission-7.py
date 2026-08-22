class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        visti={0:-1}
        sommaatt=0
        indiceatt=-1

        #È tutto un problema matematico, se dati due prefix sum si ripete
        #il resto modulo k allora matematicamente esiste da qualche parte
        #il "good subarray" cosi come richiesto dove la somma degli
        #elementi all'interno dello stesso è divisibile per k
        for i in nums:
            sommaatt+=i
            indiceatt+=1
            if sommaatt%k in visti:
                if indiceatt-visti[sommaatt%k]>=2:
                    return True
            else:
                visti[sommaatt%k]=indiceatt

        return False