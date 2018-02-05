class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m == 1 or n == 1:
            return 1
        dp = [[0] * n] * m
        dp[0] = [1] * n
        for i in range(1, m):
            dp[i][0] = 1
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]