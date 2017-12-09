# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x.start)
        last = intervals[0]
        res = []
        for x in intervals[1:]:
            if x.start <= last.end:
                last.end = max(x.end, last.end)
            else:
                res.append([last.start, last.end])
                last = x
        if res and last.end != res[-1][1]:
            res.append([last.start, last.end])
        if not res:
            res.append([last.start, last.end])
        return res

