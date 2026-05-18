"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key=lambda x: x.start)
        prec = float("-inf")
        for i in range(len(intervals)):
            if intervals[i].start < prec:
                return False
            prec=intervals[i].end
        return True