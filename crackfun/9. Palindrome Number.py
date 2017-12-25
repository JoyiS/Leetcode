class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if 0 <= (x) <= 2 ** 31 - 1:
            x = str(x)
            if x == x[::-1]:
                return True
        return False


# Method 2:
# Get the reverse number using the % 10 method
class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x>=0:
            return True if x == self.reverse(x) else False
        else:
            return False
    def reverse(self, x):
        answer = 0
        while x > 0 :
            answer = answer * 10 + x % 10
            x /= 10
        answer = answer if (answer < pow(2,31)-1) else 0
        return answer