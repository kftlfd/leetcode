"""
Leetcode
79. Word Search
Medium
2024-04-03

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

 

Constraints:

    m == board.length
    n = board[i].length
    1 <= m, n <= 6
    1 <= word.length <= 15
    board and word consists of only lowercase and uppercase English letters.

 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""

from typing import List


class Solution:
    """
    Runtime: 2854 ms, faster than 88.04% of Python3 online submissions for Word Search.
    Memory Usage: 16.6 MB, less than 71.59% of Python3 online submissions for Word Search.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        starting_points = []

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    starting_points.append((row, col))

        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        seen = [[False] * n for _ in range(m)]

        def dfs(r, c, word_i):
            if word_i >= len(word):
                return True

            for dx, dy in moves:
                nxt_r = r + dx
                nxt_c = c + dy
                if 0 <= nxt_r < m and 0 <= nxt_c < n and not seen[nxt_r][nxt_c] and board[nxt_r][nxt_c] == word[word_i]:
                    seen[nxt_r][nxt_c] = True
                    if dfs(nxt_r, nxt_c, word_i + 1):
                        return True
                    seen[nxt_r][nxt_c] = False

            return False

        for r, c in starting_points:
            seen[r][c] = True
            if dfs(r, c, 1):
                return True
            seen[r][c] = False

        return False
