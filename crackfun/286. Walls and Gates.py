#rooms = [[INF,-1,  0,  INF],[INF, INF, INF,  -1],[INF,  -1, INF,  -1],[0,  -1, INF, INF]]
class Solution(object):
    def wallsAndGates(self,rooms):
        if not rooms:
            return
        levelnodes = []
        level = 0
        INF = 2**31-1
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    levelnodes.append([i,j])
        dx = [1,0,-1,0]
        dy = [0,1,0,-1]
        while levelnodes:
            level+=1
            newlevelnodes = []
            for [x,y] in levelnodes:
                for dxx, dyy in zip(dx, dy):
                    nx,ny = x+dxx, y+dyy
                    if 0<=nx<len(rooms) and 0<=ny<len(rooms[0]):
                        if rooms[nx][ny] == INF:
                           rooms[nx][ny] = level
                           newlevelnodes.append([nx,ny])
            levelnodes = newlevelnodes


# Second Time 1/26/2018

class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        INF = 2 ** 31 - 1
        if not rooms or not rooms[0]:
            return
        m = len(rooms)
        n = len(rooms[0])
        queue = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for x in range(m):
            for y in range(n):
                if rooms[x][y] == 0:
                    queue += [(x, y)]
        val = 1
        while queue:
            newqueue = []
            for node in queue:
                for dxx, dyy in zip(dx, dy):
                    if 0 <= node[0] + dxx < m and 0 <= node[1] + dyy < n and rooms[node[0] + dxx][node[1] + dyy] == INF:
                        rooms[node[0] + dxx][node[1] + dyy] = val
                        newqueue += [(node[0] + dxx, node[1] + dyy)]
            queue = newqueue
            val += 1

