class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       # We can use greedy approach for this as well (similar to insert intervals)
       # Clarification: what is minimum number of intervals?
        # If 1, return that interval (Base Case)
       # Also, is array sorted? If not, we should sort
       # This time, we compare 2 intervals at a time
       # Scenario 1: Interval 1 comes before interval 2 completely
        # end1 < start2
        # append interval 1 to list and iterate to next i
       # Scenario 2: Interval 2 comes before interval 1 (impossible) b/c we sorted
       # Scenario 3: Overlap
        # Since start1 <= end1 at all times,
        # end1 >= start2 is when they overlap
        # then newInterval = min(start1, start2), max(end1, end2)
        # Since we processed this, we put this as i+1's interval and iterate next
       # At the end we need to add remaining intervals
        # Base Case
        if len(intervals) < 2:
            return intervals
        
        intervals.sort()
        res = []
        # When intervals is at least 2
        for i in range(1, len(intervals)):
            start1, end1 = intervals[i-1][0], intervals[i-1][1]
            start2, end2 = intervals[i][0], intervals[i][1]
            # Case 1
            if end1 < start2:
                res.append([start1, end1])
            else:
                newInterval = [min(start1, start2), max(end1, end2)]
                intervals[i] = newInterval
        res.append(intervals[-1])
        return res





