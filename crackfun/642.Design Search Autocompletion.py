class AutocompleteSystem():
    class Node():
        def __init__(self,st,t):
            self.sentence = st
            self.times = t

    def AutocompleteSystem(self, sentences, times):
        d = {}
        for i in range(len(sentences)):
            key = ord(sentences[i][0]) - ord('a')
            d[key] = d.get(key,[])+[[sentences[i], times[i]]]

    cur_sent = ''
    def input(self, c):
        if c == '#':
            return []
        else:
            cur_sent += c
            
