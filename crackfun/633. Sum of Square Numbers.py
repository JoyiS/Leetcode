class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        if c == 0 or int(math.sqrt(c)) == math.sqrt(c):
            return True
        for i in range(int(math.sqrt(c)) + 1):

            if c - i ** 2 >= 0 and int(math.sqrt(c - i ** 2)) == math.sqrt(c - i ** 2):
                return True
        return False