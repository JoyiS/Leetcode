'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''


class Solution(object):
    def addStrings(self, num1, num2):
        carry = 0
        out = ''
        while num1 or num2:
            if num1:
                a = ord(num1[-1]) - ord('0')
            else:
                a = 0
            if num2:
                b = ord(num2[-1]) - ord('0')
            else:
                b = 0
            res = (a + b + carry) % 10
            carry = (a + b + carry) / 10
            out = str(res) + out
            num1 = num1[:-1]
            num2 = num2[:-1]
        if carry:
            out = str(carry) + out
        return out

