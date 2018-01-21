'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

'''

class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        pos1 = -1
        pos2 = -1
        minlen = len(words) - 1
        for idx, word in enumerate(words):
            if word == word1:
                pos1 = idx

            if word == word2:
                pos2 = idx

            if pos1 > -1 and pos2 > -1:
                minlen = min(minlen, abs(pos1 - pos2))
        return minlen

