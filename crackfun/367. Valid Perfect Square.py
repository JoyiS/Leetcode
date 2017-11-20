class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i=1
        while i**2<=num:
            if i**2==num:
                return True
            else:
                i+=1
        return False