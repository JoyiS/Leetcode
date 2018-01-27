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

# Newton's method
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 0: return False
        if num <= 1: return True
        n = num/2  # start guessing using n = num/2
        while n*n!= num:
            inc = (num-n*n)/(2*n)
            n += inc
            if -1 <= inc <= 1: break
        if n*n < num: n+=1
        if n*n > num: n-=1
        return n*n == num