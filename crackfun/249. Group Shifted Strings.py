'''
Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]
'''
class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        d={}
        for a in strings:
            if len(a)==1:
                d['zero'] = d.get('zero',[]) + [a]
                continue
            res = [(ord(y) - ord(x)+26)%26 for x,y in zip(a[:-1], a[1:])]
            res = ''.join(str(x) for x in res)
            d[res] = d.get(res,[])+[a]
        result = []
        for i in d.keys():
            result += [d[i]]
        return result