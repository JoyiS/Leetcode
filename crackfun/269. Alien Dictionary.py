'''
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
'''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Corner case: all word in words are the same
        if all(word==words[0] for word in words):
            return words[0]

        # construct graph self.d based on the words
        self.d = {}
        for pair in zip(words, words[1:]):
            for a,b in zip(*pair):
                if a != b:
                    if a not in self.d:
                        self.d[a] = [b]
                        break
                    else:
                        self.d[a] += [b]
                        break

        # Corner Case 2: if the dictionary is empty
        if not self.d:
            return words[-1][::-1]

        # Construct all the vertexes
        self.v = set()
        for word in words:
            self.v |= set(word)
        self.v = list(self.v)

        # Call topological sort
        res = self.topologicalSort()
        if res:
            return ''.join(a for a in res)
        else:
            return res

    # Topological sort # DFS
    def topologicalSortUtil(self, v, visited, stack, key):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        if v in self.d:
            for i in self.d[v]:
                if i in key:
                    self.flag = 1
                    return
                if visited[i] == False:
                    self.topologicalSortUtil(i, visited, stack, key+[i])

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = {}
        for i in self.v:
            visited[i] = False
        stack = []
        self.flag = 0
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in self.v:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack, [i])
            if self.flag == 1:
                return ''

        return stack