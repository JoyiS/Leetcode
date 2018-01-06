# My solution
# space O(mn), time add O(col), time sum O(row)
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.oldmatrix = matrix
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return
        m = len(matrix)
        n = len(matrix[0])
        self.matrix = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if j==0:
                    self.matrix[i][j] = matrix[i][j]
                else:
                    self.matrix[i][j] = matrix[i][j] + self.matrix[i][j-1]

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        oldval = self.oldmatrix[row][col]
        self.oldmatrix[row][col] = val
        diff = val - oldval
        for j in range(col, len(self.matrix[0])):
            self.matrix[row][j] += diff

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        res = 0
        for i in range(row1,row2+1):
            longsum = self.matrix[i][col2]
            if col1==0:
                shortsum = 0
            else:
                shortsum = self.matrix[i][col1-1]
            res+=(longsum-shortsum)
        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)

# Method 2:
class NumMatrix(object):
    def __init__(self, matrix):
        if not matrix:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.matrix, self.bit = [[0] * (self.n) for _ in range(self.m)], [[0] * (self.n + 1) for _ in range(self.m + 1)]
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])


    def update(self, row, col, val):
        diff, self.matrix[row][col], i = val - self.matrix[row][col], val, row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)


    def sumRegion(self, row1, col1, row2, col2):
        return self.sumCorner(row2, col2) + self.sumCorner(row1 - 1, col1 - 1) - self.sumCorner(row1 - 1,
                                                                                                col2) - self.sumCorner(row2,
                                                                                                                       col1 - 1)

    def sumCorner(self, row, col):
        res, i = 0, row + 1
        while i:
            j = col + 1
            while j:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res