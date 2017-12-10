class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'M'
                    for q in range(m):
                        if matrix[q][j] != 0:
                            matrix[q][j] = 'M'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'M':
                    matrix[i][j] = 0


