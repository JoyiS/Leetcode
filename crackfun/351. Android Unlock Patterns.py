# This is a good question for DFS.
# There are 5 different situations which involve potential jump therefore, special conditions are required to take care of these situations.
# Horizontal jump; vertical jump, diagonal cross, vertical cross, horizontal cross

class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        def dfs(m, n, prev, visited, length):
            if m <= length <= n:
                self.ans += 1

            if length == n:
                return

            for i in range(1, 10):
                if i not in visited:
                    x, y, xp, yp = (i - 1) / 3, (i - 1) % 3, (prev - 1) / 3, (prev - 1) % 3
                    if (5 not in visited and (x + xp, y + yp) == (2, 2)) or ((
                        (x == xp and abs(y - yp) == 2) or (y == yp and abs(x - xp) == 2)) and (
                        prev + i) / 2 not in visited) or (abs(x-xp)==2 and abs(y-yp)==1 and (5 not in visited or ((2 not in visited if y+yp==1) or (8 not in visited in y+yp==3))))
                        or (abs(x - xp) == 1 and abs(y - yp) == 2 and (5 not in visited or (
                        (4 not in visited if x + xp == 1) or (6 not in visited in x + xp == 3))):
                        continue
                    visited |= {i}
                    dfs(m, n, i, visited, length + 1)
                    visited.discard(i) # This is like temp.pop() for other dfs examples.

        visited = set()
        self.ans = 0
        dfs(m, n, -99, visited, 0)
        return self.ans



# 1/26/2018
class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        self.flags = [False] * 10
        self.rules = [[3, 7, 9], [8], [1, 7, 9], [6], [], [4], [1, 3, 9], [2], [1, 3, 7]]

        return sum(4 * self.dfs(1, i) + 4 * self.dfs(2, i) + self.dfs(5, i) for i in range(m, n + 1))

    def dfs(self, value, count):

        if count == 1:
            return 1

        ans = 0
        self.flags[value] = True
        for i in range(1, 10):
            if self.flags[i] is False and (i not in self.rules[value - 1] or self.flags[(i + value) / 2]):
                ans += self.dfs(i, count - 1)

        self.flags[value] = False
        return ans