class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        vol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        res = ''
        while n > 0:
            res= vol[(n - 1) % 26] + res
            n = (n-1)//26
        return res


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        vol = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        res = ''
        while n > 0:
            res = vol[(n - 1) % 62] + res
            n = (n-1)//62
        return res