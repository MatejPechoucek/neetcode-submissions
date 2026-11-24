"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        inter = []
        for interval in intervals:
            inter.append(tuple((interval.start, interval.end)))
        
        sorted_intervals = sorted(inter, key=lambda tup: tup[0])
        
        print(sorted_intervals)
        prev_interval = (0,0)
        for interval in sorted_intervals:
            if interval[0] < prev_interval[1]:
                print(f"{interval[0]} > {prev_interval[1]}")
                return False
            prev_interval = interval
        return True