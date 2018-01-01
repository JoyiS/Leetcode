class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def dfs(x, y, word, board):
            if len(word) == 0: return True
            # up
            if x > 0 and board[x - 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                dfs(x - 1, y, word[1:])
                board[x][y] = tmp
            # down
            if x < len(board) - 1 and board[x + 1][y] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                dfs(x + 1, y, word[1:])
                board[x][y] = tmp
            # left
            if y > 0 and board[x][y - 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                dfs(x, y - 1, word[1:])
                board[x][y] = tmp
            # right
            if y < len(board[0]) - 1 and board[x][y + 1] == word[0]:
                tmp = board[x][y]
                board[x][y] = '#'
                dfs(x, y + 1, word[1:])
                board[x][y] = tmp
            else:
                return False

        res = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                for word in words:
                    if board[i][j] == word[0] and dfs(i, j, word[1:]):
                        res += [word]
        return res

#--------------------------------
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False


class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord


class Solution(object):
    def findWords(self, board, words):
        res = []
        trie = Trie()
        node = trie.root
        for w in words:
            trie.insert(w)
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res

    def dfs(self, board, node, i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        tmp = board[i][j]
        node = node.children.get(tmp)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i + 1, j, path + tmp, res)
        self.dfs(board, node, i - 1, j, path + tmp, res)
        self.dfs(board, node, i, j - 1, path + tmp, res)
        self.dfs(board, node, i, j + 1, path + tmp, res)
        board[i][j] = tmp