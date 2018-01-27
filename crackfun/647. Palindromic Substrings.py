# O(N^2)
def countSubstrings(self, S):
    N = len(S)
    ans = 0
    for center in range(2*N - 1):
        left = center / 2
        right = left + center % 2
        while left >= 0 and right < N and S[left] == S[right]:
            ans += 1
            left -= 1
            right += 1
    return ans
# Manacher's Method

class Solution(object):
    def countSubstrings(self, s):
        n = len(s)
        dp = [[0] * n for i in range(n)]
        count = 0
        for end in range(n):
            dp[end][end] = 1
            count += 1
            for start in range(end):
                if s[start] == s[end] and (start+1 >= end-1 or dp[start+1][end-1]):
                    count += 1
                    dp[start][end] = 1
        return count