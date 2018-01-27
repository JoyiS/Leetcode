'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        # Step 1: Insert the newInterval in the intervals
        flag = 0
        for i in range(len(intervals)):
            if intervals[i].start >= newInterval.start:
                flag = 1
                break
        if flag==1:
            intervals = intervals[:i] + [newInterval] + intervals[i:]
        else:
            intervals = intervals + [newInterval]
        # Step 2: merge interval to the left
        j = i-1
        while j >= 0 and intervals[j].end >= intervals[i].start:
            j -= 1
        intervals[j+1].end = max(intervals[i].end, intervals[j+1].end)
        intervals = intervals[:j+2]+intervals[i+1:]
        # merge interval to the right
        q = j+2
        while q<len(intervals) and intervals[q].start<=intervals[j+1].end:
            q += 1
        intervals[j+1].end = max(intervals[q-1].end, intervals[j+1].end)
        intervals = intervals[:j+2]+intervals[q:]
        return intervals