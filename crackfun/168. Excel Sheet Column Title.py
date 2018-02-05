class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        vol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n > 0:
            res+= vol[(n - 1) % 26]
            n = (n-1)//26
        return res[::-1]