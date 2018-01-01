from collections import OrderedDict


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = OrderedDict()
        for i in s:
            if ord(i) - ord('a') not in d:
                d[ord(i) - ord('a')] = 1
            else:
                d[ord(i) - ord('a')] += 1
        for i in d.keys():
            if d[i] == 1:
                return s.index(chr(i + ord('a')))
        return -1


