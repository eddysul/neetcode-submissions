class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # There are 3 cases of how a new interval can be added
        # 1. Comes before current interval
            # newIntervalEnd < curIntervalStart -> return newInterval + original array
            # As if it didn't overlap with curInterval it won't with future ones.
        # 2. Comes after current interval
            # currentIntervalEnd < newIntervalStart -> add currentInterval, keep newInterval for future comparisions
        # 3. Overlap
            # curIntervalEnd > newIntervalStart
            # Update newInterval = min(cur, new), max(cur, new)
            # But don't add any interval as the updated new interval can overlap with others

        res = []
        for i, (start, end) in enumerate(intervals):
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            elif end < newInterval[0]:
                res.append([start, end])
            else: # overlap
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        res.append(newInterval)
        return res




