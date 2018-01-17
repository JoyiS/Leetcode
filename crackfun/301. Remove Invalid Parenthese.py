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
