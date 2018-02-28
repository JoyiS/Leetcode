'''
Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = “eceba”,

T is "ece" which its length is 3.


'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start,end = 0,0
        res = 0
        last = None
        while end<len(s):
            while end<len(s) and len(d.keys())<=2:
                if s[end] not in d:
                    d[s[end]] = end
                    last = s[end]
                elif s[end]!=last:
                    d[s[end]] = end
                    last = s[end]
                end+=1
            if len(d.keys())==3:
                res = max(res,end-1-start)
                for key in d.keys():
                    if key==s[end-2]:
                        start = d[s[end-2]]
                    elif key!=s[end-1]:
                        popkey = key
                d.pop(popkey)
        res = max(res,end-start)
        return res