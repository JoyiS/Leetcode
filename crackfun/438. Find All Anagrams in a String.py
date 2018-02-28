class Solution(object):
    def findAnagrams(self, s, p):

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

# 2/27/2018
class Solution(object):
    from collections import Counter

    def findAnagrams(self, s, p):
        pCounter = collections.Counter(p)
        sCounter = collections.Counter(s[:len(p)])
        res = [0] if pCounter == sCounter else []
        for i in range(len(p), len(s)):
            sCounter[s[i]] = sCounter.get(s[i], 0) + 1
            sCounter[s[i - len(p)]] -= 1
            if sCounter[s[i - len(p)]] == 0:
                del sCounter[s[i - len(p)]]
            if sCounter == pCounter:
                res += [i - len(p) + 1]

        return res