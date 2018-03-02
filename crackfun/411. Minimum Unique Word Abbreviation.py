# This is a good question, combining 408 and 320
class Solution():
    def minAbbreviation(self, target, dictionary):
        self.res = []
        self.dfs(target, 0, '', 0)
        self.res.sort(key = lambda x: len(x))
        for x in self.res:
            for d in dictionary:
                if self.validWordAbbreviation(d, x):
                    break
            else:
                return x
        return ''

    def dfs(self,target, pos, line, num):
        if pos == len(target):
            if num!=0:
                line+=str(num)
            self.res.append(line)
            return
        self.dfs(target, pos+1, line, num+1)
        self.dfs(target, pos+1, line+('' if num==0 else str(num))+target[pos], 0)

    def validWordAbbreviation(word,abbr):
        digit = '0123456789'
        i = 0
        j = 0
        while i < len(abbr):
            num = 0
            while i < len(abbr) and abbr[i] in digit:
                num = num*10 + int(abbr[i])
                i += 1
            j = j+num
            print(j)
            if j==len(word):
                return True
            if j < len(word) and word[j] == abbr[i]:
                i += 1
                j += 1
            else:
                return False
        return True