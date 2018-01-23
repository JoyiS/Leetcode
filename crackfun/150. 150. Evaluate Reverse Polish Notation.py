'''
Very important knowledge: '-4'.isdigit() will return False!!!!!!!

about the division operation the Leetcode and python 2.x version gives differnet results/
'''
'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

'''

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return 0
        stack = []
        stack.append(int(tokens[0]))
        tokens = tokens[1:]
        opt = '+-*/'
        while tokens:
            if tokens[0] not in opt:
                stack.append(int(tokens[0]))
            if tokens[0] in opt:
                opt2 = stack.pop()
                opt1 = stack.pop()
                if tokens[0] == '+':
                    stack.append(opt1 + opt2)
                if tokens[0] == '-':
                    stack.append(opt1 - opt2)
                if tokens[0] == '*':
                    stack.append(opt1 * opt2)
                if tokens[0] == '/':
                    if opt1 * opt2 < 0 and opt1 % opt2 != 0:
                        stack.append(opt1 / opt2 + 1)
                    else:
                        stack.append(opt1 / opt2)
            tokens = tokens[1:]
        return int(stack[0])

# Method 2:
class Solution:
    import operator
    # @param {string[]} tokens
    # @return {integer}
    def __init__(self):
        self.operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(operator.truediv(x, y))
        }

    def evalRPN(self, tokens):
        if not tokens:
            return 0
        stack = []
        for token in tokens:
            if token in self.operators:
                stack.append(self.operators[token](stack.pop(), stack.pop()))
            else:
                stack.append(int(token))
        return stack[0]


        return int(stack[-1])