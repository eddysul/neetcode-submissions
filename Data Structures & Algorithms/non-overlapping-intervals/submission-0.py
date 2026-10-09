class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # First sort by start time
        # Overlap if end1 < start2
            # Greedy approach is always remove interval that has larger end time to minimize the risk of overlapping
            # So keep new interval as min(start1, start2), min(end1, end2)

        # Base Case
        if len(intervals) < 2:
            return 0

        intervals.sort()
        count = 0
        for i in range(1, len(intervals)):
            start1, end1 = intervals[i-1][0], intervals[i-1][1]
            start2, end2 = intervals[i][0], intervals[i][1]
        
            if end1 > start2:
                if end1 > end2:
                    intervals[i] = [start2, end2]
                else:
                    intervals[i] = [start1, end1]
                count += 1
        return count





