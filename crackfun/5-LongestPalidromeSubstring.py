'''
This is a very good problem.
Method 1: Brute force O(n^3) first and second loops for get the substring (i,j), loop 3 for judging whether s[i,j] is a palindrome string
Method 2: DP. O(n^2) and space O(n^2)
(1) what are the initial states?
if there is only one char in the string. It is a palindrome
if there is two char, if they are the same. It is a palindrome.
(2) how to write the state transfer function?
tableij[i][j] = tableij[i+1][j-1] +(s[i]==s[j])
'''
class Solution(object):
    def longestPalindrome(self, s):
        tableij = [[0 for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            tableij[i][i] = True
        n = len(s)

        maxlength = 1
        start = 0
        i = 0
        while i < n - 1 :
            if (s[i] == s[i + 1]) :
                tableij[i][i + 1] = True
                start = i
                maxlength = 2
            i = i + 1

        k = 3
        while k <= n:
            i = 0
            while i < n - k + 1:
                j = i + k - 1
                if (tableij[i + 1][j - 1] and s[i] == s[j]):
                    tableij[i][j] = True
                    if k>maxlength:
                        maxlength = k
                        start = i
                i = i+1
            k=k+1
        if maxlength>1:
            return s[start:start+maxlength]
        else:
            return s[0]

# Solution 2: much faster
# constant Memory
# O(n^2)
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        p = s[0]
        for i in range(1, len(s)):
            if len(p) == len(s):
                return p
            l = (len(p) - 1) / 2
            if len(self.palin(s, i - l, i + l)) > len(p):
                p = self.palin(s, i - l, i + l)
            if len(self.palin(s, i - 1 - l, i + l)) > len(p):
                p = self.palin(s, i - 1 - l, i + l)
        return p

    def palin(self, s, begin, end):
        if (begin < 0) or (end > len(s)):
            return ''
        else:
            str1 = s[begin:end + 1]
            str2 = str1[::-1]
            if (str1 == str2):
                while (begin >= 0) and (end < len(s)) and (s[begin] == s[end]):
                    begin -= 1
                    end += 1
            else:
                return ''
        return s[begin + 1:end]