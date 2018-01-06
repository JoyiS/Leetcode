class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        wall = 'W'
        enemy = 'E'
        empty = '0'

        numRows = len(grid)
        numCols = len(grid[0])
        maxres = 0
        rowcount = [[0] * numCols] * numRows
        colcount = [[0] * numCols] * numRows
        for i in range(numRows):
            for j in range(numCols):
                if i==0 or grid[i-1][j]==wall:
                    rowcount[i][j]=0
                    k=i
                    while k<numRows and grid[k][j]!=wall:
                        rowcount[i][j] += grid[k][j]==enemy
                        k+=1
                else:
                    rowcount[i][j] = rowcount[i-1][j]

                if j==0 or grid[i][j-1]==wall:
                    colcount[i][j] = 0
                    k = j
                    while k<numCols and grid[i][k]!=wall:
                        colcount[i][j] += grid[i][k]==enemy
                        k+=1
                else:
                    colcount[i][j] = colcount[i][j-1]
                if grid[i][j] == empty:
                    maxres = max(maxres, rowcount[i][j]+colcount[i][j])
        return maxres

