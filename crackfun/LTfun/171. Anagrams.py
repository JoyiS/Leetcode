'''
Given an array of strings, return all groups of strings that are anagrams.
'''


class Solution:
    """
    @param: strs: A list of strings
    @return: A list of strings
    """

    def anagrams(self, strs):
        # write your code here
        res = []
        d = {}
        for s in strs:
            x = ''.join(sorted(s))
            if x in d:
                d[x] += [s]
            else:
                d[x] = [s]
        for v in d.values():
            if len(v) > 1:
                res += v
        return res