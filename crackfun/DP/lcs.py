'''
http://www.techiedelight.com/longest-common-subsequence/
'''

# if solve this problem using recursion, this problem shows repeated subproblem/overlapping.
# therefore, dp method is used to solve this kind of problem.

class Solution():
    def lcs(self, s,p):
        m = len(s)
        n = len(p)
        dp = [[0]*(n+1)]*(m+1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if s[i]==p[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]