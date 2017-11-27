# Solution 1: TLE version bad

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.res = 0
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.dfs(matrix, i, j, [], visited)
        return self.res

    def dfs(self, matrix, x, y, path, visited):
        visited[x][y] = True
        for dir in self.directions:
            if 0 <= x + dir[0] < len(matrix) and 0 <= y + dir[1] < len(matrix[0]) and matrix[x + dir[0]][y + dir[1]] > \
                    matrix[x][y]:
                self.dfs(matrix, x + dir[0], y + dir[1], path + [[x, y]], visited)
        else:
            self.res = max(self.res, len(path) + 1)
            return


# Good Solution; use a Cache to reduce repeat recursions!!!!
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix: return 0
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(matrix)
        n = len(matrix[0])
        cache = [[-1 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                cur_len = self.dfs(i, j, matrix, cache, m, n)
                res = max(res, cur_len)
        return res

    def dfs(self, i, j, matrix, cache, m, n):
        if cache[i][j] != -1:
            return cache[i][j]
        res = 1
        for direction in self.directions:
            x, y = i + direction[0], j + direction[1]
            if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                continue
            length = 1 + self.dfs(x, y, matrix, cache, m, n)
            res = max(length, res)
        cache[i][j] = res
        return res