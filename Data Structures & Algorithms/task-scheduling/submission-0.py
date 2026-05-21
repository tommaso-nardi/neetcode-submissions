class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        conteggio = collections.Counter(tasks)

        max_heap = [-freq for freq in conteggio.values()]
        heapq.heapify(max_heap)
        cooldown=collections.deque()
    
        tempo=0

        while max_heap or cooldown:
            tempo=tempo+1
            if max_heap:
                task=heapq.heappop(max_heap)
                if task+1 < 0:
                    cooldown.append([task+1,tempo+n])
            if cooldown and cooldown[0][1] == tempo:
                task=cooldown.popleft()
                heapq.heappush(max_heap,task[0])
        return tempo