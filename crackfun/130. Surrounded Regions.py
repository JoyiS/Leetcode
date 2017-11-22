# This is a bfs problem:
# The idea is that all points 'O' on the boarder of the board should not be changed; and all the points conneting to the boarder 'O' cannot be changed as well.
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        queue = []
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        xlim = [0, len(board) - 1]
        ylim = [0, len(board[0]) - 1]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i in xlim or j in ylim) and board[i][j] == 'O':
                    board[i][j] = 'V'
                    queue.append([i, j])
        while queue:
            [x, y] = queue.pop()
            for dxx, dyy in zip(dx, dy):
                if 0 < x + dxx < len(board) - 1 and 0 < y + dyy < len(board[0]) - 1 and board[x + dxx][y + dyy] == 'O':
                    board[x + dxx][y + dyy] = 'V'
                    queue.append([x + dxx, y + dyy])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'