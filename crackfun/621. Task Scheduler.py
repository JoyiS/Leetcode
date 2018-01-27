'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''


class Solution(object):
    import collections
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        TaskCounts = list(collections.Counter(tasks).values())
        MaxTaskCount = max(TaskCounts)
        NumofMaxTask = TaskCounts.count(MaxTaskCount)
        return max(len(tasks), (MaxTaskCount - 1) * (n + 1) + NumofMaxTask)


# Shally's genius method!!!
class Solution(object):
        import collections
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)

        dct = collections.Counter(tasks)
        dct1 = [i for i in dct.values() if i > 0]

        cnt = 0
        while len(dct1) > 0 and max(dct1) > 1:
            dct1 = sorted(dct1, reverse=True)
            cnt += n + 1
            if len(dct1) < n + 1:
                dct1 = [j - 1 for j in dct1 if j - 1 > 0]
            else:
                dct11 = dct1[:n + 1]
                dct12 = dct1[n + 1:]
                dct1 = [j - 1 for j in dct11 if j - 1 > 0]
                dct1.extend(dct12)

        return cnt + sum(dct1)

# 1/23 Third time:
class Solution(object):
    import collections
    def leastInterval(self, tasks, n):
    counts = collections.Counter(tasks)
    dct = [i for i in counts.values()]
    cnt = 0
    while len(dct) > 0 and max(dct) > 1:
        dct.sort(reverse=True)
        cnt += n + 1
        if len(dct) >= n + 1:
            dct[:n + 1] = [i - 1 for i in dct[:n + 1]]
            dct = [i for i in dct if i > 0]
        else:
            dct = [i - 1 for i in dct if i > 1]
    return cnt + len(dct)


# Method 2: Priority Queue # This method can generate the output OKay
from Queue import PriorityQueue
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        # get a dictionary of taks
        d = {}
        for item in tasks:
            if item not in d:
                d[item] = 1
            else:
                d[item]+=1
        q = []
        last = ['idle']*n
        output = []
        for key in d.keys():
            heapq.heappush(q,(-d[key], key)) # use the counts as a priority number
        while q:
            (Negcount, key) = heapq.heappop(q)
            if key not in last:
                output+=[key]
                count = -Negcount - 1
                last = last[1:] + [key]
                if count!=0:
                    heapq.heappush(q,(-count, key))
            else:
                tempout =[(Negcount, key)]
                tempkey = key
                while q and tempkey in last:
                    (tempNegcount, tempkey) = heapq.heappop(q)
                    tempout.append((tempNegcount, tempkey))
                if tempkey not in last:
                    (Negcount, key) = tempout.pop()
                    output += [key]
                    count = -Negcount - 1
                    last = last[1:] + [key]
                    if count != 0:
                        heapq.heappush(q, (-count, key))
                else:
                    output += ['idle']
                    last = last[1:] + ['idle']
                for x in tempout:
                    heapq.heappush(q, x)

        return len(output)
