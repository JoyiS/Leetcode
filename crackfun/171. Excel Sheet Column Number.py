class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        while s:
            i = s[0]
            num = 26 * num + ord(i) - ord('A') + 1
            s = s[1:]
        return num
