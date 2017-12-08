class Solution(object):
    def canAttendMeetings(self,intervals):
        if len(intervals)<2:
            return True
        intervals.sort(key = lambda x:x[0])
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0]<last:
                return False
            last = intervals[i][1]
        return True
