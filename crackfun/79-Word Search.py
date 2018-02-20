# TLE...
class Solution(object):
    def dfs(self, word, temp, index, x, y, board):
        if len(temp) == len(word):
            self.res = True
            return
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for dxx, dyy in zip(dx, dy):
            if 0 <= x + dxx < len(board) and 0 <= y + dyy < len(board[0]) and board[x + dxx][y + dyy] == word[index]:
                temp.append(word[index])
                board[x + dxx][y + dyy] = 0
                self.dfs(word, temp, index + 1, x + dxx, y + dyy, board)
                # print(''.join(x for x in temp))
                temp.pop()
                board[x + dxx][y + dyy] = word[index]
        return False

    def exist(self, board, word):
        self.res = False
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == None:
            return True
        if board == None:
            return False

        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    board[x][y] = 0
                    self.dfs(word, [word[0]], 1, x, y, board)
                    if self.res == True:
                        return True
                    board[x][y] = word[0]
        return False

#------------------------------------AC Solution

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def dfs(x, y, word):
            if len(word) == 0: return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y];
                board[x][y] = '#'
                if dfs(x - 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y];
                board[x][y] = '#'
                if dfs(x + 1, y, word[1:]):
                    return True
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y];
                board[x][y] = '#'
                if dfs(x, y - 1, word[1:]):
                    return True
                board[x][y] = tmp
            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y];
                board[x][y] = '#'
                if dfs(x, y + 1, word[1:]):
                    return True
                board[x][y] = tmp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if (dfs(i, j, word[1:])):
                        return True
        return False

# 2/8/2018

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(position, board, word):
            if len(word) == 0:
                return True
            [x, y] = position
            for dx, dy in self.direction:
                if 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]) and board[x + dx][y + dy] == word[0]:
                    temp = word[0]
                    board[x + dx][y + dy] = 0
                    if dfs([x + dx, y + dy], board, word[1:]):
                        return True
                    board[x + dx][y + dy] = temp
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = word[0]
                    board[i][j] = 0
                    if dfs([i, j], board, word[1:]):
                        return True
                    board[i][j] = temp
        return False


