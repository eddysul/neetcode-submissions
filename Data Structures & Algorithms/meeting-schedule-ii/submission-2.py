"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = [], []

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        s, e = 0, 0
        count, max_count = 0, 0
        while s < len(start) and e < len(end):
            if start[s] < end[e]:
                s+=1
                count+=1
                max_count = max(count, max_count)
            else:
                e+=1
                count-=1
        return max_count
        
                



