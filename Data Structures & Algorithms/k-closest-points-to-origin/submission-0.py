class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for x,y in points:
            distanza = (x**2 + y**2)
            heapq.heappush(maxHeap, (-distanza, [x, y]))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        return [p[1] for p in maxHeap]