# Method 1: Straightforward method
class Solution(object):
    def lengthLongestPath(self, input):
        def countss(s, ss):
            count = 0
            lena = len(s)
            if ss in s:
                snew = s.split(ss)
                for a in snew:
                    if a == '':
                        count = count + 1
                    else:
                        lena = len(a)
            return count, lena

        newrow = '\n'
        newtab = '\t'
        fileid = '.'
        level = []
        lena = []
        res = 0
        k = 0
        for s in input.split(newrow):
            levelnew, lenanew = countss(s, newtab)
            level.append(levelnew)
            lena.append(lenanew)
            if fileid in s:
                j = k - 1
                lenall = lenanew
                currentlevel = levelnew
                # print(s + ' : current level : ' + str(currentlevel) + ' , value j :' + str(j))
                while j >= 0 and currentlevel >= 0:
                    if level[j] < currentlevel:
                        lenall += lena[j] + 1
                        # print('currentl level: ' + str(currentlevel) +', add str:' + str(j)+input.split(newrow)[j])
                        currentlevel = currentlevel - 1
                    j -= 1
                res = max(lenall, res)
            k = k + 1
        return res

# Method 2 : Same idea, use lstrip make the code looked clean and essy to maintain.
# This code is good!!
class Solution(object):
    def lengthLongestPath(self, input):
        maxlen = 0
        pathlen = {0: 0}
        for line in input.splitlines():
            name = line.lstrip('\t')    # what a surprise that len('\t') = 1
            depth = len(line) - len(name)
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            else:
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1 # plus 1 for '\' between different levels
        return maxlen