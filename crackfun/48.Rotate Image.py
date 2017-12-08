class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for l in range(n / 2):
            r = n - 1 - l
            for p in range(l, r):
                q = n - 1 - p
                cache = matrix[l][p]
                matrix[l][p] = matrix[q][l]
                matrix[q][l] = matrix[r][q]
                matrix[r][q] = matrix[p][r]
                matrix[p][r] = cache