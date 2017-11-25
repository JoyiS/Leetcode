# I wrote a TLE version using DFS...
# Check the BFS solution.
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        i = 1
        lst = []
        while i ** 2 <= n:
            lst.append(i ** 2)
            i+=1
        levelnodes = [n]
        level = 0
        while levelnodes:
            level += 1
            newlevelnodes = []
            for node in levelnodes:
                for x in lst:
                    if node == x:
                        return level
                    if node < x:
                        break
                    newlevelnodes.append(node - x)
            levelnodes = newlevelnodes
        return level



