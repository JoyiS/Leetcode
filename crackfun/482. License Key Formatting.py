# My bad TLE solution
class Solution(object):
    def licenseKeyFormatting(self, s, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        s = s.replace('-', '').upper()
        n = len(s)
        if n < K:
            first = n
        else:
            first = n % K or K
        s0 = s[:first]
        s = s[first:]
        while s:
            s0 += '-'
            s0 += s[:K]
            s = s[K:]
        return s0

# AC solution:
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace('-', '').upper()
        if len(S) % K:
            S = '#' * (K - len(S) % K) + S
        return '-'.join(S[x:x + K] for x in range(0, len(S), K)).replace('#', '')