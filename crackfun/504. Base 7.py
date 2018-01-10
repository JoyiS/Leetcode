class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        numbase = num
        cntmax = 0
        while numbase >= 1:
            numbase /= 7
            cntmax += 1
        cntmax -= 1
        res = ''
        while cntmax >= 0:
            res += str(int(num / (7 ** cntmax)))
            num =  num % (7 ** cntmax)
            cntmax -= 1
        return res
