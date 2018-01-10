class Solution(object):
    def wordsAbbreviation(self, dict):
        """
        :type dict: List[str]
        :rtype: List[str]
        """
        d = {}
        for idx, word in enumerate(dict):
            if len(word) > 3:
                abr = (word[0], str(len(word) - 2), word[-1])
                if abr in d:
                    d[abr] += [(word, idx)]
                else:
                    d[abr] = [(word, idx)]

        # similar word
        def similar(wds, word):
            i = 1
            wds.remove(word)
            while i < len(word):
                wpi = word[i]
                flag = 0
                for wq in wds:
                    if wq[i] == wpi:
                        flag = 1
                        break
                if flag == 1:
                    i += 1
                else:
                    print(i)
                    return i

        # output
        res = []
        for word in dict:
            if len(word) <= 3:
                res += [word]
            else:
                if len(d[(word[0], str(len(word) - 2), word[-1])]) == 1:
                    res += [word[0] + str(len(word) - 2) + word[-1]]
                else:
                    idx = similar(d[(word[0], str(len(word) - 2), word[-1])], word)
                    if len(word) - idx - 2 >= 2:
                        res += [word[:idx + 1] + str(len(word) - idx - 1) + word[-1]]
                    else:
                        res += [word]
        return res
