class Solution(object):
    def isOneEditDistance(self, s, t):
        # The length comparison between s and t actually matters in the algorithm implementations.
        # use this way to make len(t) > len(s) as a valid assumption in the following code!! I like this concise way
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        # if the length diffs >2 false
        if len(t) - len(s) > 1:
            return False
        # if len(s) == len(t)
        cnt = 0
        if len(s) == len(t):
            for i in range(len(s)):
                if s[i] != t[i]:
                    cnt += 1
                    if cnt > 1:
                        return False
            return cnt == 1
        else:
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] != t[j]:
                    cnt += 1
                    if cnt > 1:
                        return False
                    j += 1
                else:
                    i += 1
                    j += 1
            return (cnt == 1 and i == len(s) and j == len(t)) or len(t) - j == 1