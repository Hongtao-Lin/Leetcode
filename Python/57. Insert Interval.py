# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Idea:
# Find left merge boundary by trying to insert 'start' in end seq
#   Similar to bisect.bisect_left(ends, start)
# Find right merge bounday by trying to insert 'end' in start seq
#   Similar to bisect.bisect(starts, end)

class Solution(object):
    def insert(self, intervals, newInterval):
        s, e, n = newInterval.start, newInterval.end, len(intervals)
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if intervals[mid].end < s: # note that here's '<' instead of '<=', consider the input: [[1, 5]], insert [5, 7]
                lo = mid + 1
            else:
                hi = mid
        if lo == n:
            return intervals + [newInterval]
        l = lo
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if intervals[mid].start <= e:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0:
            return [newInterval] + intervals
        r = lo
        return intervals[:l] + [Interval(min(s, intervals[l].start), max(e, intervals[r-1].end))] + intervals[r:]