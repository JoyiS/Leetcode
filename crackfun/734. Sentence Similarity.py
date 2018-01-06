class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False

        def simiwords(p, q, pairs):
            for pair in pairs:
                if p in pair and q in pair:
                    return True
            return False

        for i, j in zip(words1, words2):
            if i != j and not simiwords(i, j, pairs):
                return False
        return True


