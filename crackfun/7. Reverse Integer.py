class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return x
        s = str(x)
        minus = False
        if s[0] == '-':
            minus = True
            s = s[1:]
        s = s[::-1]
        while s[0] == 0:
            s = s[1:]
        x = int(s)
        if x > 2 ** 31 - 1:
            x = 0
        if minus:
            x = -x
        return x

