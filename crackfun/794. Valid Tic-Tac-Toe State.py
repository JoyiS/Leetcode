'''
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.
Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true
'''


class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        m = 3
        n = 3
        cnt1 = 0
        cnt2 = 0

        def win(board, m, n):
            cnt = 0
            winx, winy = 0, 0
            for row in board:
                if row == 'OOO' or row == 'XXX':
                    cnt += 1
                    if row == 'OOO': winy = 1
                    if row == 'XXX': winx = 1

            for j in range(n):
                col = [board[i][j] for i in range(m)]
                col = ''.join(a for a in col)
                if col == 'OOO' or col == 'XXX':
                    cnt += 1
                    if col == 'OOO': winy = 1
                    if col == 'XXX': winx = 1

            diag1 = board[0][0] + board[1][1] + board[2][2]
            diag2 = board[0][2] + board[1][1] + board[2][0]
            if diag1 == 'OOO' or diag1 == 'XXX':
                cnt += 1
                if diag1 == 'OOO': winy = 1
                if diag1 == 'XXX': winx = 1
            if diag2 == 'OOO' or diag2 == 'XXX':
                cnt += 1
                if diag2 == 'OOO': winy = 1
                if diag2 == 'XXX': winx = 1
            return cnt, winx, winy

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    cnt1 += 1
                if board[i][j] == 'O':
                    cnt2 += 1
        if cnt1 < cnt2 or cnt1 - cnt2 > 1:
            return False
        wincnt, winx, winy = win(board, m, n)
        if wincnt > 1:
            return False
        if wincnt == 1 and winx == 1:
            return cnt1 - cnt2 == 1
        if wincnt == 1 and winy == 1:
            return cnt1 == cnt2
        return True