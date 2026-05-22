class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)==1:
            return 0
        intervals.sort(key=lambda x: x[1])
        cont=0
        fine_prec=float("-inf")

        for inv in intervals:
            if inv[0] < fine_prec:
                cont+=1
            else:
                fine_prec=inv[1]
        
        return cont