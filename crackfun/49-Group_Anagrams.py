class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for i in strs:
            il = list(i)
            il = ''.join(x for x in sorted(il))
            if il not in d:
                d[il] = []
            d[il].append(i)
        res = []
        for key in d.keys():
            res.append(d[key])
        return res

