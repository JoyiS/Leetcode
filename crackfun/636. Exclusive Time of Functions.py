'''
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

Example 1:
Input:
n = 2
logs =
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
Note:
Input logs will be sorted by timestamp, NOT log id.
Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
Two functions won't start or end at the same time.
Functions could be called recursively, and will always end.
1 <= n <= 100
'''


class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack = []
        res = [0] * n
        lastStatus = None
        lastid = None
        for log in logs:
            task, status, t_stamp = self.ReadLog(log)
            # print(stack, res)
            if status == 'start':
                if stack:
                    (lastid, stamp, duration) = stack.pop()
                    stack.append((lastid, stamp, t_stamp - lasttime - int(laststatus == 'end') + duration))
                stack.append((task, t_stamp, 0))
            if status == 'end':
                (lastid, stamp, duration) = stack.pop()
                res[int(lastid)] += duration + t_stamp - lasttime + int(laststatus == 'start')
            lasttime = t_stamp
            laststatus = status
        return res

    def ReadLog(self, log):
        task, status, t_stamp = log.split(':')
        return task, status, int(t_stamp)
