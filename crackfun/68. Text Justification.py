# AC solution on line
class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' ' # This is a smart line!!! to add space!!!
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]



# My bad/not working solution.......
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        if maxWidth < 1:
            return [""]
        par = ''
        for word in words:
            par += word
            par += ' '
        par = par[:-1]
        if len(par) <= maxWidth:
            return par
        line = ''
        allline = []
        resline = []
        while par:
            if len(par)<=maxWidth:
                line = par
                allline += line
                break
            if par[maxWidth - 1] == ' ':
                line = par[:maxWidth - 1]
                par = par[maxWidth:]
            elif maxWidth<len(par) and par[maxWidth] == ' ':
                line = par[:maxWidth]
                par = par[maxWidth + 1:]
            else:
                k = maxWidth - 1
                while 0<=k<len(par) and par[k] != ' ':
                    k -= 1
                line = par[:k]
                par = par[k + 1:]
            allline += line
        for line in allline[:-1]:
            count = 0
            for a in line:
                if a == ' ':
                    count += 1
            morespaces = maxWidth - len(line)
            if count>0:
                addspaces, left = divmod(morespaces, count)
            else:
                resline += line
                continue
            c = 0
            for a in line:
                c += 1
                if a == ' ':
                    a += ' ' * addspaces
                if c == count:
                    a += ' ' * left
            resline += line
        resline += allline[-1]
        return resline


