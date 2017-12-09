# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        flag = 0
        for i in range(len(intervals)):
            if intervals[i].start >= newInterval.start:
                flag = 1
                break
        if flag==1:
            intervals = intervals[:i] + [newInterval] + intervals[i:]
        else:
            intervals = intervals + [newInterval]
        j = i-1
        while j >= 0 and intervals[j].end >= intervals[i].start:
            j -= 1
        intervals[j+1].end = max(intervals[i].end, intervals[j+1].end)
        intervals = intervals[:j+2]+intervals[i+1:]
        q = j+2
        while q<len(intervals) and intervals[q].start<=intervals[j+1].end:
            q += 1
        intervals[j+1].end = max(intervals[q-1].end, intervals[j+1].end)
        intervals = intervals[:j+2]+intervals[q:]
        return intervals