'''
Classic Recursion Problem

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

'''


class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.d_below_20 = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven',
                           8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                           15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}
        self.d_below_100 = {20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy',
                            80: 'Eighty', 90: 'Ninety'}

        if num == 0:
            return 'Zero'
        else:
            return self.trans(num)

    def trans(self, num):
        if num < 20:
            return self.d_below_20[num]
        if num < 100:
            return self.d_below_100[(num // 10) * 10] + (' ' + self.trans(num % 10) if num % 10 else '')
        if num < 10 ** 3:
            return self.trans(num // 100) + ' Hundred' + (' ' + self.trans(num % 100) if num % 100 else '')
        if num < 10 ** 6:
            return self.trans(num // 1000) + ' Thousand' + (' ' + self.trans(num % 1000) if num % (10 ** 3) else '')
        if num < 10 ** 9:
            return self.trans(num // (10 ** 6)) + ' Million' + (' ' + self.trans(num % (10 ** 6)) if num % (10 ** 6) else '')
        else:
            return self.trans(num // (10 ** 9)) + ' Billion' + (' ' + self.trans(num % (10 ** 9)) if num % (10 ** 9) else '')