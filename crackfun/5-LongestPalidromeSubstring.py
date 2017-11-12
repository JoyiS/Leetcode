'''
This is a very good problem.
Method 1: Brute force O(n^3) first and second loops for get the substring (i,j), loop 3 for judging whether s[i,j] is a palindrome string
Method 2: DP. O(n^2) and space O(n^2)
(1) what are the inital states?
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
