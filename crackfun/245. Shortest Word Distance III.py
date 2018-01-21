class Solution:
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        d = {}
        minlen = len(words) - 1
        if word1 == word2:
            for idx, word in enumerate(words):
                if word == word1:
                    if word in d:
                        minlen = min(minlen, idx - d[word1][-1])
                        d[word1] += [idx]
                    else:
                        d[word1] = [idx]
            return minlen

        for idx, word in enumerate(words):
            if word == word1:
                if word1 in d:
                    d[word1] += [idx]
                else:
                    d[word1] = [idx]
            if word == word2:
                if word2 in d:
                    d[word2] += [idx]
                else:
                    d[word2] = [idx]

        m = len(d[word1])
        n = len(d[word2])
        i = 0
        j = 0
        while i < m and j < n:
            if d[word1][i] > d[word2][j]:
                minlen = min(minlen, d[word1][i] - d[word2][j])
                j += 1
            else:
                minlen = min(minlen, -d[word1][i] + d[word2][j])
                i += 1
        return minlen
