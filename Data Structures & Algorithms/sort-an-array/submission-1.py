class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        ordine=[]
        heapq.heapify(nums)
        while nums:
            ordine.append(heapq.heappop(nums))
        return ordine