class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        heap = []
        for i, valore in enumerate(nums):
            heapq.heappush(heap, (valore, i))
        
        j=0
        #Per ogni iterazione prendi il valore più piccolo dall'heap
        #fai la moltiplicazione e aggiorna l'array nums in-place
        while j<k:
            (valore,i)=heapq.heappop(heap)
            nuovo=valore*multiplier
            nums[i]=nuovo
            heapq.heappush(heap,(nuovo,i))
            j+=1
        return nums