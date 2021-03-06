'''
Very good backtracking question + Memorization.
# Need to write a summary about this type of question
# The point of memorization is to avoid repeat the same subproblem many times.
How to define a subproblem is the key to choose the the data structure.
For example, in this problem, a hashtable is used to construct the subproblem.
For the hashtable, how to define the key and values are important.

Time complexity: It will need to solve O(2^n) subproblem.

'''

'''
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
'''


class Solution:
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        n = maxChoosableInteger + 1
        target = desiredTotal
        if n * (n - 1) / 2 < target:
            return False
        self.visited = ['0'] * n
        self.map = {}
        return self.dfs(n, target)

    def dfs(self, n, target):
        key = ''.join(self.visited)
        if key in self.map:
            return self.map[key]
        for i in range(1, n):
            if self.visited[i] == '0':
                self.visited[i] = '1'
                if target - i <= 0 or not self.dfs(n, target - i):
                    self.map[key] = True
                    self.visited[i] = '0'
                    return True
                self.visited[i] = '0'
        self.map[key] = False
        return False


