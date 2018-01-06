#[6,5,8,9,7,1,10,2,3,4]
#2
class BITree(object):
    def __init__(self, n):
        self.node = [0 for _ in range(n + 1)]

    def getSum(self, index):
        result = 0
        while index > 0:
            result += self.node[index]
            index -= index & -index
        return result

    def update(self, index, d):
        while index <= len(self.node):
            self.node[index] += d
            index += index & -index


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        bitree = BITree(len(flowers))
        bloomed = set()
        for day, index in enumerate(flowers):
            if index - k - 1 in bloomed and bitree.getSum(index) == bitree.getSum(index - k - 1):
                return day + 1
            elif index + k + 1 in bloomed and bitree.getSum(index) + 1 == bitree.getSum(index + k + 1):
                return day + 1
            else:
                bloomed.add(index)
                bitree.update(index, 1)
        return -1

    # TLE answer
import bisect

class Solution():
    def kEmptySlots(self, flowers, k):
        N = len(flowers)
        if N < 2:
            return -1
        i = 0
        l = []
        while i < N:
            x = flowers[i]
            idx = bisect.bisect_left(l,x)
            if l:
                if idx == 0:
                    newleftdis = None
                    newrightdis = l[idx]-x -1
                elif idx == len(l):
                    newleftdis = x - l[idx-1] -1
                    newrightdis  = None
                else:
                    newrightdis = l[idx]- x -1
                    newleftdis = x - l[idx-1] -1
                if newleftdis == k or newrightdis == k:
                    return i+1
            l = l[:idx]+[x]+l[idx:]
            i += 1
        return -1
