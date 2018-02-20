class Solution(object):
    def readBinaryWatch(self, n):
        """
        :type num: int
        :rtype: List[str]
        """
        hstr = [8, 4, 2, 1]
        mstr = [32, 16, 8, 4, 2, 1]
        hlimit = 11
        mlimit = 59
        timeres = []
        import itertools
        def timestr(n, string, maxlimit):
            res = []
            if n == 0:
                return [0]
            if n >= 1:
                for x in itertools.combinations(string, n):
                    if sum(list(x)) <= maxlimit:
                        res.append(sum(list(x)))
                if res == []:
                    return [-1]
            return res

        for i in range(0, n + 1):
            hourstr = timestr(i, hstr, hlimit)
            minstr = timestr(n - i, mstr, mlimit)
            for hh in hourstr:
                for mm in minstr:
                    if hh >= 0 and mm >= 0:
                        hh = str(hh)
                        if mm <= 9:
                            mm = '0' + str(mm)
                        else:
                            mm = str(mm)
                        timehm = hh + ':' + mm
                        timeres.append(timehm)

        return timeres

