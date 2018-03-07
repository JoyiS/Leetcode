'''
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3
Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:

All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
'''


class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def subseq(t, s):
            index = -1
            for c in t:
                index = s.find(c, index + 1)
                if index < 0:
                    return False
            return True

        res = list(map(lambda t: subseq(t, S), words))

        return res.count(True)


class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        count = 0
        dic = collections.defaultdict(list)

        for w in words:
            dic[w[0]].append(w)
        for c in S:
            newc = []
            for w in dic[c]:
                if len(w) == 1:
                    count += 1
                elif w[1] != c:
                    dic[w[1]].append(w[1:])
                elif w[1] == c:
                    newc.append(w[1:])
            dic[c] = newc
        return count