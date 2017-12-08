# Bad TLE version......
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        maxlen = 0
        words.sort(key=lambda x: len(x))
        for p in words:
            for q in words:
                if self.nocommon(p, q):
                    maxlen = max(maxlen, len(p) * len(q))
        return maxlen

    def nocommon(self, wordp, wordq):
        setp = set(wordp)
        setq = set(wordq)
        if setp & setq == set():
            return True
        return False

# ----------------AC Solution
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        curr_max = 0
        while words:
            curr_word = set(words[0])
            curr_len = len(words[0])
            words = words[1:]   # REDUCE THE LENGTH OF WORDS In each iteration.
            for word in words:
                for char in curr_word:
                    if char in word:
                        break
                else:
                    curr_max = max(curr_max, curr_len*len(word))
        return curr_max

