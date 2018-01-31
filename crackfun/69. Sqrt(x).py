class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        upper = int(x / 2 + 1)
        lower = 1
        while lower <= upper:
            mid = int((upper + lower) / 2)
            if mid ** 2 <= x and (mid + 1) ** 2 > x:
                return mid
            if mid ** 2 > x:
                upper = mid - 1
            else:
                lower = mid + 1

#1/29/2018 Second time binary search and also Newton's method