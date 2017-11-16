class Solution(object):
    import math
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        if len(matrix) < 2:
            return int("1" in matrix[0])

        dp = [[0 for y in range(len(matrix[0]))] for x in range(len(matrix))]

        maxval = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = 1
                    maxval = 1

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if dp[i][j]:
                    if dp[i - 1][j - 1] and dp[i - 1][j] and dp[i][j - 1]:
                        dp[i][j] = (math.sqrt(min([dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]])) + 1) ** 2
                        maxval = int(max(maxval, dp[i][j]))
        return maxval