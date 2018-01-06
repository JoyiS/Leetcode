# TLE version
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        buildings = []
        res = float('inf')
        m = len(grid)
        n = len(grid[0])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    buildings.append([x, y])
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    cur_res = 0
                    for b in buildings:
                        cur_res += self.min_path([x, y], b, grid)
                    res = min(cur_res, res)
        return [-1,res][res!=float('inf')]

    def min_path(self, p, b, grid):
        queue = [(p, 0)]
        explored = []
        while queue:
            (cp, dis) = queue.pop(0)
            explored.append(cp)
            for dx,dy in zip([0,1,0,-1],[1,0,-1,0]):
                newpx  = cp[0]+dx
                newpy = cp[1]+dy
                if 0<=newpx<len(grid) and 0<=newpy<len(grid[0]):
                    if [newpx, newpy] not in explored and grid[newpx][newpy] == 0:
                        queue.append(([newpx, newpy], dis + 1))
                    if [newpx, newpy] == b:
                        return dis + 1
        return float('inf')

#AC version
# Time:  O(k * m * n), k is the number of the buildings
# Space: O(m * n)

class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        def bfs(grid, dists, cnts, x, y):
            dist, m, n = 0, len(grid), len(grid[0])
            visited = [[False for _ in range(n)] for _ in range(m)]

            pre_level = [(x, y)]
            visited[x][y] = True
            while pre_level:
                dist += 1
                cur_level = []
                for i, j in pre_level:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        I, J = i + dir[0], j + dir[1]
                        if 0 <= I < m and 0 <= J < n and grid[I][J] == 0 and not visited[I][J]:
                            cnts[I][J] += 1
                            dists[I][J] += dist
                            cur_level.append((I, J))
                            visited[I][J] = True

                pre_level = cur_level

        m, n, cnt = len(grid), len(grid[0]), 0
        dists = [[0 for _ in range(n)] for _ in xrange(m)]
        cnts = [[0 for _ in range(n)] for _ in xrange(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    cnt += 1
                    bfs(grid, dists, cnts, i, j)

        shortest = float("inf")
        for i in xrange(m):
            for j in xrange(n):
                if dists[i][j] < shortest and cnts[i][j] == cnt:
                    shortest = dists[i][j]

        return shortest if shortest != float("inf") else -1