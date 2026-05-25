class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ris = []
        i = 0
        n = len(intervals)

        # 1. Quelli che finiscono prima del nuovo (nessun contatto)
        while i < n and intervals[i][1] < newInterval[0]:
            ris.append(intervals[i])
            i += 1

        # 2. Quelli che hanno contatto (merge)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # ORA aggiungiamo il nuovo intervallo (fuso o originale)
        ris.append(newInterval)

        # 3. Quelli che iniziano dopo la fine del nuovo
        while i < n:
            ris.append(intervals[i])
            i += 1

        return ris