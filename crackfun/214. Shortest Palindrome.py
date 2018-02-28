'''
Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

For example:

Given "aacecaaa", return "aaacecaaa".

Given "abcd", return "dcbabcd".
'''
class Solution:
    def shortestPalindrome(self, s):
        if not s:
            return ''
        n = len(s)
        if n % 2:
            center = 2 * (n // 2) + 1
        else:
            center = n
        for i in range(center, -1, -1):
            if i % 2:  # (' ')
                left = s[:(i + 1) // 2]
                right = s[(i + 1) // 2:]
                if left[::-1] == right[:len(left)]:
                    return right[::-1] + right
            else:
                left = s[:i // 2]
                right = s[i // 2 + 1:]
                if left[::-1] == right[:len(left)]:
                    return right[::-1] + s[i // 2] + right

