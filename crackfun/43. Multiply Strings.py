class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        m = len(num1)
        n = len(num2)
        s = 0
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                position = m+n-i-j-2
                s+=int(num1[i])*int(num2[j])*(10**position)
        return str(s)