class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        d = {}
        for i in range(len(s)-9):
            if s[i:i+10] not in d:
                d[s[i:i+10]]=1
            else:
                d[s[i:i+10]]+=1
        return [key for key,value in zip(d.keys(),d.values()) if value>=2]