class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def check(x, y):
            if x >= 0 and x < m and y >= 0 and y < n and grid[x][y] == '1' and visit[x][y] == False:
                return True

        def dfs(x, y):
            nbrow = [1, 0, -1, 0]
            nbcol = [0, 1, 0, -1]
            for k in range(4):
                newx = x + nbrow[k]
                newy = y + nbcol[k]
                if check(newx, newy):
                    visit[newx][newy] = True
                    dfs(newx, newy)

        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        visit = [[False for i in range(n)] for j in range(m)]
        count = 0
        for row in range(m):
            for col in range(n):
                if check(row, col):
                    visit[row][col] = True
                    dfs(row, col)
                    count += 1
        return count



