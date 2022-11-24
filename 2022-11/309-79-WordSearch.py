"""
Leetcode
79. Word Search (medium)
2022-11-24

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

from typing import List, Optional
from collections import Counter
from itertools import chain, product


# https://leetcode.com/problems/word-search/discuss/2843501/PythonC++-faster-than-99-DFS-(explained)
# Runtime: 87 ms, faster than 95.45% of Python3 online submissions for Word Search.
# Memory Usage: 14 MB, less than 52.49% of Python3 online submissions for Word Search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])

        if len(word) > m * n:
            # [a] trivial case to discard
            return False

        if not (cnt := Counter(word)) <= Counter(chain(*board)):
            # [b] there are not enough letters on the board
            return False

        if cnt[word[0]] > cnt[word[-1]]:
            # [c] inverse word if it's better to start from the end
            word = word[::-1]

        # recursive postfix search
        def dfs(i, j, s):

            if s == len(word):
                # [1] found the word
                return True

            if 0 <= i < m and 0 <= j < n and board[i][j] == word[s]:
                # [2] found a letter
                # [3] mark as visited
                board[i][j] = "#"
                # [4] iterate over adjacent cells...
                adj = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
                # [5] ...and try next letter
                dp = any(dfs(ii, jj, s+1) for ii, jj in adj)
                # [6] remove mark
                board[i][j] = word[s]
                # [7] return search result
                return dp

            # [8] this DFS branch failed
            return False

        # search starting from each position
        return any(dfs(i, j, 0) for i, j in product(range(m), range(n)))


s = Solution()
tests = [
    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"),
     True),

    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"),
     True),

    (([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"),
     False)
]
for inp, exp in tests:
    board, word = inp
    res = s.exist(board, word)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
