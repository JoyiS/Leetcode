class Solution(object):
    def hasPath(self, maze, start, destination):

            Q = [start]
            n = len(maze)
            m = len(maze[0])
            dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))

            while Q:
                # Use Q.pop() as DFS or Q.popleft() with deque from collections library for better performance. Kudos to @whglamrock
                i, j = Q.pop(0)
                maze[i][j] = 2

                if i == destination[0] and j == destination[1]:
                    return True

                for x, y in dirs:
                    row = i + x
                    col = j + y
                    while 0 <= row < n and 0 <= col < m and maze[row][col] != 1:
                        row += x
                        col += y
                    row -= x
                    col -= y
                    if maze[row][col] == 0:
                        Q.append([row, col])

            return False



# TLE version
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0]:
            return False
        explored = []
        queue = []
        alldir = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m = len(maze)
        n = len(maze[0])
        for drt in alldir:
            queue.append([start, drt])
        while queue:
            [pos, drt] = queue.pop(0)
            if [pos, drt] not in explored:
                explored += [[pos, drt]]
            while 0 <= pos[0] < m and 0 <= pos[1] < n and maze[pos[0]][pos[1]] != 1:
                pos = [pos[0] + drt[0], pos[1] + drt[1]]
            pos = [pos[0] - drt[0], pos[1] - drt[1]]
            if pos == destination:
                return True
            for d in alldir:
                if d!=drt and [pos, d] not in explored:
                    queue += [[pos, d]]
        return False
