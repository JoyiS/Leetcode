class Solution:
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        def computeDis(a, b):
            ax, ay = a[0], a[1]
            bx, by = b[0], b[1]
            return abs(ax - bx) + abs(ay - by)

        dis = computeDis(target, (0, 0))

        for g in ghosts:
            gdis = computeDis(target, g)
            print(gdis)
            if gdis <= dis:
                return False
        return True
