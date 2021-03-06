# Matching problem, using DP method
# Why using DP method, 1) State Transition; 2) Initial State dp[0][0] =  True
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1, len(p)+1):
            if p[i-1] == '*':
                if i >= 2:
                    dp[0][i] = dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == '.': # the index means current position.
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*': # analyze the different conditions
                    dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else: # if current p[j-1] is a digit/char
                    dp[i][j] = (dp[i-1][j-1] and s[i-1]==p[j-1]) # this is a cleaner way to avoid too many if conditions
        return dp[len(s)][len(p)]

# analyze the three conditions:
# dp[i][j] = dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
# 1. * does not count
# 2. preceding element does not count: dp[i][j-2]
# 3. one or more of preceding element
        # (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))