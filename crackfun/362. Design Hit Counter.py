# Time:  O(1), amortized
# Space: O(k), k is the count of seconds.

from collections import deque

class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timelimit = 300     # 5 min
        self.queue = deque()

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.queue.append(timestamp)

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """

        # It is important to popleft the queue because it help
        # to reduce the size of the queue and this will help to maintain
        # high efficiency even a large number of hits
        while (self.queue and self.queue[0] < timestamp - self.timelimit):
            self.queue.popleft()
        return len(self.queue)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)