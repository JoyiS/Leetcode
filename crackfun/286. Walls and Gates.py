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

