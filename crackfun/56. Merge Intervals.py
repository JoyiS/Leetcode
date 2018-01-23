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

# 1/21/2018
# Second time:
'''
The key point is that the last inteval will need to be added in the end
'''
# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        if len(intervals) < 2:
            return intervals
        res = []
        intervals.sort(key=lambda x: x.start)
        newstart = intervals[0].start
        lastend = intervals[0].end
        for interval in intervals[1:]:
            if interval.start > lastend:
                res += [[newstart, lastend]]
                newstart = interval.start
            lastend = max(lastend, interval.end)
        res += [[newstart, lastend]]
        return res