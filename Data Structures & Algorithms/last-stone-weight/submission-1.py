class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-s for s in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            val1=(heapq.heappop(maxHeap))*-1
            val2=(heapq.heappop(maxHeap))*-1
            if (val1-val2) > 0:
                heapq.heappush(maxHeap,(val1-val2)*-1)

        if not maxHeap:
            heapq.heappush(maxHeap,0)
        return (maxHeap[0])*-1