# DP problem
# find the subproblem word of len(s) --> break down to length(0 to i)
# use dp to record the status of all subproblem

class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(0, len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for k in range(i):
                if dp[k] and s[k:i] in wordDict:
                    dp[i] = True
        return dp[-1]

# Second Time the time complexity if superior than the first one O(len(s)*len(dict))
class Solution(object):
    def wordBreak(self, s, words):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in words:
                if w == s[i-len(w)+1:i+1] and (i-len(w) == -1 or d[i-len(w)]):
                    d[i] = True
        return d[-1]