class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # First sort by start time
        # Overlap if end1 < start2
            # Greedy approach is always remove interval that has larger end time to minimize the risk of overlapping
            # So keep new interval as min(start1, start2), min(end1, end2)

        # Base Case
        if len(intervals) < 2:
            return 0

        intervals.sort(key=lambda x: x[1])
        count = 0
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if prevEnd > intervals[i][0]:
                count += 1
            else:
                prevEnd = intervals[i][1]
            
        return count





