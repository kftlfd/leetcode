"""
Leetcode
212. Word Search II (hard)
2022-11-05

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:
Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
"""

from typing import List, Optional


# Time Limit Exceeded
# https://leetcode.com/problems/word-search-ii/discuss/59790/Python-dfs-solution-(directly-use-Trie-implemented).
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
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
        self.dfs(board, node, i+1, j, path+tmp, res)
        self.dfs(board, node, i-1, j, path+tmp, res)
        self.dfs(board, node, i, j-1, path+tmp, res)
        self.dfs(board, node, i, j+1, path+tmp, res)
        board[i][j] = tmp


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


# https://leetcode.com/problems/word-search-ii/discuss/2779789/PythonC++JavaRust-DFS-using-trie-with-removal-(with-detailed-comments)
# Runtime: 2899 ms, faster than 54.65% of Python3 online submissions for Word Search II.
# Memory Usage: 16.3 MB, less than 58.67% of Python3 online submissions for Word Search II.
class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        # trie is initialized with a list of words
        trie = Trie1(words)
        seen = set()                         # found words are being collected into a set

        # generator that yields (!) adjacent cells
        def adj(x, y):
            for i, j in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
                if 0 <= x+i < m and 0 <= y+j < n:
                    yield (x+i, y+j)

        # DFS search with prefix 'p', last cell (x,y) on board 'b'
        def dfs(p, b, x, y):

            # [1] mark used cell and save board state
            ch, b[x][y] = b[x][y], "#"

            if trie.search(p):
                seen.add(p)                   # [2] mark word as found and
                trie.remove(p)  # no longer search for it

            # [3] iterate over adjacent cells
            for i, j in adj(x, y):
                if b[i][j] != "#":  # which are still unused
                    pp = p + b[i][j]  # and extend the word
                    # [4] if the prefix exists in the trie,
                    if trie.starts(pp):
                        dfs(pp, b, i, j)  # we should check this branch

            b[x][y] = ch                      # [5] restore board state

        for i in range(m):                    # DFS procedure is initialized starting
            for j in range(n):                # from all possible cells (i,j)
                dfs(board[i][j], board, i, j)

        return seen


class Trie1:
    def __init__(self, words=[]):
        self.trie = {}
        for w in words:
            self.insert(w)

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#'

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def starts(self, prefix):
        t = self.trie
        for w in prefix:
            if w not in t:
                return False
            t = t[w]
        return True

    def remove(self, word):
        t = self.trie
        nodes = []
        for w in word:
            if w not in t:
                return False
            t = t[w]
            nodes.append((t, w))

        if '#' in t:
            p = '#'
            for n, w in nodes[::-1]:
                if len(n[p]) == 0 or p == '#':
                    del n[p]
                p = w


s = Solution1()
tests = [
    (([["o", "a", "a", "n"],
       ["e", "t", "a", "e"],
       ["i", "h", "k", "r"],
       ["i", "f", "l", "v"]],
      ["oath", "pea", "eat", "rain"]),
     ["eat", "oath"]),

    (([["a", "b"],
       ["c", "d"]],
      ["abcb"]),
     [])
]
for inp, exp in tests:
    board, words = inp
    res = s.findWords(board, words)
    res = [x for x in res]
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
