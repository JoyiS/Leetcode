# find a prefix
# for all other strings, check whether the prefix works for them all...
# Time Complex O(M*N) M: len(str) N(len(str[0]))
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:
            return ''
        stra = strs[0]
        for i in range(len(stra)): # find a prefix
            prefix = stra[:i + 1]
            for strb in strs[1:]: # all other strs
                if prefix != strb[:i + 1]:
                    return prefix[:-1]
        return prefix

# Method 2: use enumerate and zip
# O(N): N = min(len(str))
class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            #print(letter_group)
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)