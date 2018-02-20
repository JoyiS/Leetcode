# If a string contains '[]' for word processing, stack is the right data structure to use.

class Solution(object):
    def decodeString(self, s):
        stack = []
        stack.append(["", 1]) # This is very important
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]