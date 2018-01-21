'''
This is a follow up of Shortest Word Distance. The only difference is now you are given the list of words and your method will be called repeatedly many times with different parameters. How would you optimize it?

Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.d = {}
        for idx, word in enumerate(words):
            if word in self.d:
                self.d[word] += [idx]
            else:
                self.d[word] = [idx]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        i = 0
        j = 0
        m = len(self.d[word1])
        n = len(self.d[word2])
        minlen = max(self.d[word1][m - 1] - self.d[word2][0], self.d[word2][n - 1] - self.d[word1][0])
        while i < m and j < n:
            if self.d[word1][i] > self.d[word2][j]:
                minlen = min(minlen, self.d[word1][i] - self.d[word2][j])
                j += 1
            else:
                minlen = min(minlen, -self.d[word1][i] + self.d[word2][j])
                i += 1
        return minlen



        # Your WordDistance object will be instantiated and called as such:
        # obj = WordDistance(words)
        # param_1 = obj.shortest(word1,word2)