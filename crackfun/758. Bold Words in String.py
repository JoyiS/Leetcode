'''
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.

The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:

words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
'''


class Solution:
    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        res = []

        for word in words:
            k = S.find(word)
            if k > -1:
                res += [[k, k + len(word)]]
                # print(word, k)
                for i in range(k + 1, len(S) - len(word) + 1):
                    k = S.find(word, i)
                    if k >= 0:
                        res += [[k, k + len(word)]]
                    else:
                        break
        if not res:
            return S
        res.sort(key=lambda x: x[0])

        laststart = res[0][0]
        lastend = res[0][1]
        newres = []
        # Merge res
        for start, end in res[1:]:
            if start <= lastend:
                lastend = max(lastend, end)
            else:
                newres += [[laststart, lastend]]
                laststart = start
                lastend = end
        newres += [[laststart, lastend]]
        print(newres)
        slist = list(S)
        flag = 0
        for start, end in newres:
            if start >= 1:
                slist[start - 1] += '<b>'
            else:
                flag = 1
            slist[end - 1] += '</b>'
        if flag:
            slist.insert(0, '<b>')
        return ''.join(a for a in slist)