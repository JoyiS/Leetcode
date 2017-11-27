class Solution():
    def generateAbbreviations(self, word):
        self.res = []
        self.dfs(word, 0, '', 0)
        return self.res
    def dfs(self, word, pos, line, num):
        if pos==len(word):
            if num!=0:
                line+=str(num)
            self.res.append(line)
            return
        self.dfs(word, pos+1, line, num + 1) # Generate abbreviation for word[pos]
        self.dfs(word, pos+1, line + ("" if num==0 else str(num)) + word[pos], 0) #Try to keep word[pos]