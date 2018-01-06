class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        res = 0
        for v in d.values():
            if v%2:
                res+=1
        return res<=1