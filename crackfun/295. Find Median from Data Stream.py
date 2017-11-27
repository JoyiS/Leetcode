# My code: TLE bad version
class MedianFinder(object):
    def __init__(self):
        self.items = []
        self.length = 0

    def addNum(self, num):
        if self.length == 0:
            self.items = [num]
            self.length = 1
            return
        l = 0
        h = self.length - 1
        while l <= h:
            mid = int((l + h) / 2)
            if self.items[mid] == num:
                self.items = self.items[:mid] + [num] + self.items[mid:]
                self.length += 1
                return
            if self.items[mid] < num:
                l = mid + 1
            elif self.items[mid] > num:
                h = mid - 1
        self.items = self.items[:l] + [num] + self.items[l:]
        self.length += 1
        return

    def findMedian(self):
        if self.length == 0:
            return None
        if self.length % 2:
            return self.items[int(self.length / 2)]
        else:
            return 0.5 * (self.items[self.length / 2] + self.items[self.length / 2 - 1])


#------------- AC solution with heap....
from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])