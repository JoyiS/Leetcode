class Solution():
    def isMatch(self, s, p):
        if not p:
            return not s
        countstar = 0
        for i in p:
            if i=='*':
                countstar +=1
        if len(p)-countstar>len(s):
            return False
        pp = 0
        sp = 0
        star = -1
        match = 0
        while sp < len(s):
            if pp < len(p) and (p[pp] == s[sp] or p[pp]=='?'):
                pp += 1
                sp += 1
            elif pp < len(p) and p[pp] == '*':
                star = pp
                match = sp
                pp +=1
            elif star != -1:
                 pp = star + 1
                 match += 1
                 sp = match
            else:
                return False
        while pp<len(p) and p[pp]=='*':
            pp+=1
        return pp==len(p)

# Method 2: DP
class Solution():
    def isMatch(self, s, p):
        dp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        dp[0][0] = True

        for i in range(1, len(p)+1):
            dp[i][0]=dp[i-1][0] and p[i-1]=='*'
            for j in range(1, len(s)+1):
                if p[i-1]!='*':
                    dp[i][j] = dp[i-1][j-1] and (p[i-1]=='?' or p[i-1]==s[j-1])
                else:
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[len(p)][len(s)]



# This is wrong? BUT WHY??!!
class Solution():
    def isMatch(self, s, p):
        dp = [[False for j in range(len(s)+1)] for i in range(len(p)+1)]
        dp[0][0] = True

        for i in range(1, len(p)+1):
            dp[i][0]=dp[i-1][0] and p[i-1]=='*'
            for j in range(1, len(s)+1):
                if p[i-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                if p[i-1]=='*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = (dp[i-1][j-1] and p[i-1] == s[j-1])

        return dp[len(p)][len(s)]
