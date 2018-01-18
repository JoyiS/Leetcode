'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
'''

'''
For this problem, the DFS/recursion method is not efficient. Because there are overlaps between s[:-2] and s[:-1] conditions.
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.prohibited = ['30', '40', '50', '60', '70', '80', '90', '00']
        n = len(s)
        if n < 1 or s == '0' or s[0] == '0':
            return 0
        if n == 1:
            return 1
        for a in self.prohibited:
            if a in s:
                return 0
        if n == 2:
            if s[0] == '0':
                return 1
            elif s[1]!= '0' and 10 < int(s) < 27:
                return 2
            else:
                return 1

        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2 if 10<int(s[:2])<27 else 1
        for i in range(2, n):
            dp[i] = dp[i - 1] * int(s[i] != '0') + dp[i - 2] * (9 < int(s[i - 1:i+1]) < 27)
        return dp[-1]