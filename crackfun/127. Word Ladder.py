# This is a good practice problem for BFS.
# The objective is to find te minimum steps it takes for a transition from begin word to end word.
# This is similar to traverse a tree from level to next level. That is why BFS is preferred over DFS.
# For BFS, whenever a solution is reached -> GOT THE RESULT, RETURN.
# For DFS, traverse the tree in different ways -> and compare all the results for minimum level tranversed.
# DFS is doable, but may results in Time Limit Exceeds.
from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(wordList + [beginWord])
        return bfs_words(beginWord, endWord, d)