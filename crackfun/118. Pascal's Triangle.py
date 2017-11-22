class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        level0 = [1]
        level1 = [1, 1]
        if numRows == 0:
            return []
        if numRows == 1:
            return [level0]
        if numRows == 2:
            return [level0, level1]
        self.res = [level0, level1]
        for i in range(2, numRows):
            newlevel = [1]
            for j in range(0, len(level1) - 1):
                newlevel += [level1[j] + level1[j + 1]]
            newlevel += [1]
            level1 = newlevel
            self.res += [level1]
        return self.res