'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
'''


class Solution:
    def palindromePairs(self, words):
        words = {word: i for i, word in enumerate(words)}

        def valid(s):
            return s == s[::-1]

        res = []
        for word in words:
            k = words[word]
            n = len(word)
            for i in range(n + 1):
                pre = word[:i]
                suf = word[i:]
                if valid(pre):
                    back = suf[::-1]
                    if back != word and back in words:
                        res += [[words[back], k]]


                if i != n and valid(suf):
                    back = pre[::-1]
                    if back != word and back in words:
                        res += [[k, words[back]]]

        return res