'''
Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
'''


class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """

        dis = []
        p = [p1, p2, p3, p4]
        for pp1 in p:
            for pp2 in p:
                dis += [(pp2[1] - pp1[1]) ** 2 + (pp2[0] - pp1[0]) ** 2]
        dis = [i for i in dis if i > 0]
        if len(dis) != 12: return False
        maxdis = max(dis)
        mindis = min(dis)
        cnt1 = 0
        cnt2 = 0
        if maxdis == 2 * mindis:
            for d in dis:
                if d == mindis:
                    cnt1 += 1
                if d == maxdis:
                    cnt2 += +1
            if cnt1 == 8 and cnt2 == 4:
                return True
        return False


class Solution(object):
    import collections
    def validSquare(self, p1, p2, p3, p4):
        points = [p1, p2, p3, p4]

        dists = collections.Counter()
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dists[self.getDistance(points[i], points[j])] += 1

        return len(dists.values()) == 2 and 4 in dists.values() and 2 in dists.values()

    def getDistance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2