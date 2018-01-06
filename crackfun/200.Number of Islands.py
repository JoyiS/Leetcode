# 1/5/2018 Solution DFS version much faster
class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)

# 11/23 Update AC Solution
class Solution(object):
    def check(self, grid, x, y):
        if self.visit[x][y] != False:
            return False
        queue = [[x, y]]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        while queue:
            [px, py] = queue.pop()
            for dxx, dyy in zip(dx, dy):
                if 0 <= px + dxx < len(grid) and 0 <= py + dyy < len(grid[0]):
                    if grid[px + dxx][py + dyy] == '1' and self.visit[px + dxx][py + dyy] == False:
                        queue.append([px + dxx, py + dyy])
                        self.visit[px + dxx][py + dyy] = True
        return True

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        self.visit = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and self.check(grid, i, j):
                    count += 1
        return count
#---------------- OLD VERSIONS.

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



