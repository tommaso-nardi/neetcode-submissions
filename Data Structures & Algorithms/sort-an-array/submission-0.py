class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ordine=[]
        numeri=[]
        for i in range(len(nums)):
            heapq.heappush(ordine,nums[i])
        while ordine:
            numeri.append(heapq.heappop(ordine))
        return numeri