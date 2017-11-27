class Solution():
    def validWordAbbreviation(self,word,abbr):
        digit = '0123456789'
        i = 0
        j = 0
        while i < len(abbr):
            num = 0
            while i<len(abbr) and abbr[i] in digit:
                num += num*10 + int(abbr[i])
                i += 1
            j = j+num
            if j==len(word):
                return True
            if j < len(word) and word[j] == abbr[i]:
                i += 1
                j += 1
            else:
                return False
        return True