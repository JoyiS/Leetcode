class Solution():
    def validWordAbbreviation(self,word,abbr):
        digit = '0123456789'
        i = 0
        j = 0
        while i < len(abbr):
            num = 0
            if abbr[i] in digit[1:]:  # This is a tricky one
                while i<len(abbr) and abbr[i] in digit:
                    num = num*10 + int(abbr[i])
                    i += 1
            j = j+num
            if j==len(word) and i==len(abbr): # the second condition is a bit tricky too
                return True
            if i< len(abbr) and j < len(word) and word[j] == abbr[i]:
                i += 1
                j += 1
            else:
                return False
        return True