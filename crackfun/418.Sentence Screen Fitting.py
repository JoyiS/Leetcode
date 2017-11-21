# This is a google high frequency problem.
# The solution idea is straightforward. Scan from row 1 to end. at the end of the row, check if ' ' is met, if so, that's good, this ' ' can be ommited.
# if it is not met, start-- until a ' ' is met...

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        string = ''
        for word in sentence:
            string += word + ' '
        string = string[:-1]
        length = len(string)
        start = 0
        for i in range(rows):
            start += cols
            if string[start % length] == ' ':
                start += 1
                continue
            while start>0 and string[(start-1) % length] != ' ':
                start-=1
        return int(start/length)