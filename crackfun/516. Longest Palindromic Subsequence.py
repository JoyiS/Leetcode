# DP : Space O(n^2):
def longestPalindromeSubseq(self, s):
    if s == s[::-1]:
        return len(s)

    n = len(s)
    dp = [[0 for j in range(n)] for i in range(n)]
    for i in range(n - 1, -1, -1):  # Pay attention to the reverse order here.
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


# Recursion TLE:
class Solution(object):
    def longestPalindromeSubseq(self, s):
        res = self.helper(s, 0, len(s) - 1)
        return res

    def helper(self, s, start, end):
        if start < 0 or end >= len(s):
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            if end == start + 1:
                return 2
            else:
                return self.helper(s, start + 1, end - 1) + 2
        else:
            return max(self.helper(s, start + 1, end), self.helper(s, start, end - 1))