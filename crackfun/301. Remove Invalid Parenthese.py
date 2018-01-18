# This is a very good question
'''
BFS can be very useful
'''

# Learn about filter function
# Method 1: BFS
class Solution():
    def removeInvalidParentheses(self, s):
        def isvalid(s):
            ctr = 0
            for c in s:
                if c == '(':
                    ctr += 1
                elif c == ')':
                    ctr -= 1
                    if ctr < 0:
                        return False
            return ctr == 0
        level = {s}
        while True:
            valid = list(filter(isvalid, level))
            if valid:
                return valid
            level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

# Method 2:
# a special backtracking problem with pruning
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.helper(s, 0, 0, '()')
        return self.res

    def helper(self, s, Li, Lj, pair):
        cnt = 0
        # print(s +' '+ pair)
        for i in range(Li, len(s)):
            if s[i] == pair[0]:
                cnt += 1
            elif s[i] == pair[1]:
                cnt -= 1
            if cnt >= 0: continue
            for j in range(Lj, i + 1):
                if s[j] == pair[1] and (j == Lj or s[j - 1] != pair[1]):
                    self.helper(s[:j] + s[j + 1:], i, j, pair)
            return

        reversed_s = s[::-1]
        if pair[0] == '(':
            # print(reversed_s)
            self.helper(reversed_s, 0, 0, ')(')
        else:
            self.res.append(reversed_s)






