'''
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
'''
class Solution:
    def getFactors(self, n):
        import math
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.n = n
        self.dfs(n, [])
        return self.res

    def dfs(self, n, temp):
        i = 2
        while i * i <= n:
            if not n % i:
                if (not temp or i >= temp[-1]) and i <= int(n / i):
                    self.res += [temp + [i, int(n / i)]]
                    self.dfs(n / i, temp + [i])
            i += 1
        return