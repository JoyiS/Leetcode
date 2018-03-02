'''
Write a function to generate the generalized abbreviations of a word.

Example:
Given word = "word", return the following list (order does not matter):
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''

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