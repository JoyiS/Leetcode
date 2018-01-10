class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = map(str, range(1, n+1))
        while n > 1:
            res = ["(" + res[i] + "," + res[n-1-i] + ")" for i in range(n >> 1)]
            print(res)
            n >>= 1
        return res[0]