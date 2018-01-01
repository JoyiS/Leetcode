class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        b = n//5
        res = 0
        while b>=1:
            res +=b
            i += 1
            b = n//(5**i)
        return res