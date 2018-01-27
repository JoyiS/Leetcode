# This is a two pointer problem:
# 一个 dictionary 来记录T中出现字母的次数
# 双指针 ：end and start;
# 双counter : 一个是cnt[], 用来记录s[start:end+1]中对应T中字母出现的次数
# 一个是n--, 用来表示
# 1/25/2018 revisited

class Solution:
    # @return a string
    def minWindow(self, S, T):
        m, n = len(S), len(T)
        dic, cnt = [0] * 129, [0] * 129
        for i in T:
            cnt[ord(i)] += 1
            dic[ord(i)] += 1

        start, L, dis = 0, 0, m + 1
        for i in range(m):
            if dic[ord(S[i])] > 0:
                cnt[ord(S[i])] -= 1
                if cnt[ord(S[i])] >= 0:
                    n -= 1
            if n == 0:
                while start <= i:
                    if dic[ord(S[start])] > 0:
                        if cnt[ord(S[start])] < 0:
                            cnt[ord(S[start])] += 1
                        else:
                            break
                    start += 1
                if i - start + 1 < dis:
                    dis = i - start + 1
                    L = start

        if dis != m + 1:
            return S[L:L + dis]
        return ""

# My Solution: TLE 266/268 Pass
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(s) < len(t):
            return ""
        snew = s
        for tt in t:
            if tt not in snew:
                return ""
            idx = snew.index(tt)
            snew = snew[:idx]+snew[idx+1:]

        self.res = []
        for i in range(len(s)):
            if s[i] in t:
                idx = t.index(s[i])
                self.dfs(t[:idx] + t[idx+1:], i, i+1, s)
        return min(self.res, key = len)

    def dfs(self, tstr, start, end, s):
        if not tstr:
            self.res += [s[start:end]]
            return
        if end >= len(s):
            return
        if s[end] in tstr:
            idx = tstr.index(s[end])
            tstr = tstr[:idx]+tstr[idx+1:]
        self.dfs(tstr, start, end+1, s)
