class Solution(object):
    import math
    def maximalSquare(self, matrix):
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

# 2/15/2018
# AC solution but really slow
class Solution:
    def maximalSquare(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        heights = [0] * len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            for val in range(0,max(heights)+1):
                hres = [height - val for height in heights]
                cnt = 0
                for k in range(len(matrix[0])):
                    if hres[k]>=0 and cnt<=val:
                        cnt += 1
                        if cnt==val:
                            res = max(res,val**2)
                            break
                    else:
                        cnt = 0
        return res
