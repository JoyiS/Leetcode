class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        self.res = []
        cnt1 = [0] * 26
        cnt2 = [0] * 26

        for c in p:
            cnt1[ord(c) - ord('a')] += 1

        for i in range(len(s)):
            cnt2[ord(s[i]) - ord('a')] += 1
            if i >= len(p):
                cnt2[ord(s[i - len(p)]) - ord('a')] -= 1
            if cnt2 == cnt1:
                self.res += [i - len(p) + 1]
        return self.res