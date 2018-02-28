'''
There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12
Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.

Note:
There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''


class Solution:
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        if not maze or not maze[0]:
            return -1
        for row in maze:
            row.insert(0, 1)
            row.append(1)
        maze.append([1 for i in range(len(maze[0]))])
        maze.insert(0, [1 for i in range(len(maze[-1]))])
        start = (start[0] + 1, start[1] + 1)
        des = (destination[0] + 1, destination[1] + 1)
        d = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        cnt = 0
        for dd in d:
            if maze[des[0] + dd[0]][des[1] + dd[1]] == 1:
                cnt += 1
        if cnt != 3:
            return -1
        print(cnt)

        queue = [(start[0], start[1], 0)]
        while queue:
            oldi, oldj, curr = queue.pop(0)
            maze[oldi][oldj] = 2
            if oldi == des[0] and oldj == des[1]:
                return curr
                break
            for dx, dy in d:
                i = oldi
                j = oldj
                print(dx,dy)
                i += dx
                j += dy
                curr += 1
                while 1 <= i < len(maze) - 1 and 1 <= j < len(maze[0]) - 1 and maze[i][j] != 1:
                    i += dx
                    j += dy
                    curr += 1
                i -= dx
                j -= dy
                curr -= 1
                if maze[i][j] == 0:
                    queue.append((i, j, curr))
                    print(queue)
        return -1

