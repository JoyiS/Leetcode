class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x=1/x
            n = -n
        res = 1
        while n > 0:
            if n%2:
                res *= x
                n-=1
            else:
                x*=x
                n = n/2
        return res