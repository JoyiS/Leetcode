class Solution(object):
    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

#2/9/2018
# TLE but great solution!!!
class Solution(object):
    def longestSubstring(self, s, k):
        i = 0
        n = len(s)
        res = 0
        while i + k <= n:
            mask = 0
            m = [0] * 26
            start = i
            for j in range(i, n):
                t = ord(s[j]) - ord('a')
                m[t] += 1
                if m[t] < k:
                    mask |= (1 << t)
                else:
                    mask &= (~(1 << t))
                if mask == 0:
                    res = max(res, j - i + 1)
                    start = j
            i = start + 1
        return res
