class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s1 = "++"
        s2 = "--"
        res = []
        residx = []
        for i in range(len(s)):
            idx1 = s.find(s1,i)
            if idx1>-1 and idx1 not in residx:
                residx.append(idx1)
                res+=[s[:idx1]+s2+s[idx1+2:]]
        return res