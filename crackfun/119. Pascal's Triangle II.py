class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        level0 = [1]
        level1 = [1, 1]
        if rowIndex == 0:
            return level0
        if rowIndex == 1:
            return level1

        for i in range(1, rowIndex):
            newlevel = [1]
            for j in range(0, len(level1) - 1):
                newlevel += [level1[j] + level1[j + 1]]
            newlevel += [1]
            level1 = newlevel
        return newlevel