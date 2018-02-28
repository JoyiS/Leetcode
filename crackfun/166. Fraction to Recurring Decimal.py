'''
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

Given numerator = 1, denominator = 2, return "0.5".
Given numerator = 2, denominator = 1, return "2".
Given numerator = 2, denominator = 3, return "0.(6)".
'''


class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        res = ""

        if numerator / denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator // denominator)

        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator // denominator)

        res += "."

        numerator %= denominator
        i = len(res)
        table = {}

        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator // denominator)
            numerator %= denominator
            i += 1
        return res

# -------------- I memorized it.
class Solution:
    # @return a string
    def fractionToDecimal(self, numerator, denominator):
        res = ""
        up = numerator
        down = denominator
        if up * down < 0:
            res += '-'
        up = abs(up)
        down = abs(down)
        if not up % down:
            res += str(up // down)
            return res

        a = up // down
        res += str(a)
        res += '.'
        up %= down
        d = {}
        i = len(res)

        while up != 0:
            if up not in d:
                d[up] = i
            else:
                i = d[up]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            up = up * 10
            res += str(up // down)
            up = up % down
            i += 1
        return res
