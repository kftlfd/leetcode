"""
Leetcode
2025-05-31
909. Snakes and Ladders
Medium

You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

    Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
        This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
    If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
    The game ends when you reach the square n2.

A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

    For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.

Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:

Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.

Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1

 

Constraints:

    n == board.length == board[i].length
    2 <= n <= 20
    board[i][j] is either -1 or in the range [1, n2].
    The squares labeled 1 and n^2 are not the starting points of any snake or ladder.


"""

from collections import deque
from typing import List


class Solution00:
    """
    Wrong Answer
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_line = self.getBoardLine(board)
        end = len(board_line) - 1
        q = deque([0])
        rolls = 0

        while q:
            rolls += 1
            for _ in range(len(q)):
                cur = q.popleft()
                nxt_max = min(cur + 6, end)
                for nxt_pos in range(cur + 1, nxt_max + 1):
                    nxt = board_line[nxt_pos]
                    if nxt == end:
                        return rolls
                    if nxt > cur or nxt == nxt_max:
                        q.append(nxt)

        return -1

    def getBoardLine(self, board: List[List[int]]) -> List[int]:
        n = len(board)
        nn = n * n
        board_line = [-1] * nn
        i = 0
        reverse = 0
        for r in range(n - 1, -1, -1):
            row = reversed(board[r]) if reverse else board[r]
            reverse ^= 1
            for num in row:
                board_line[i] = num - 1 if num != -1 else i
                i += 1
        return board_line


class Solution01:
    """
    Time Limit Exceeded
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board_line = self.getBoardLine(board)
        end = len(board_line) - 1
        seen = [-1] * len(board_line)
        seen[0] = True
        q = deque([0])
        rolls = 0

        while q:
            rolls += 1
            for _ in range(len(q)):
                cur = q.popleft()
                nxt_max = min(cur + 6, end)
                for nxt_pos in range(cur + 1, nxt_max + 1):
                    nxt = board_line[nxt_pos]
                    if nxt == end:
                        return rolls
                    if seen[nxt] >= rolls:
                        continue
                    seen[nxt] = rolls
                    q.append(nxt)

        return -1

    def getBoardLine(self, board: List[List[int]]) -> List[int]:
        n = len(board)
        nn = n * n
        board_line = [-1] * nn
        i = 0
        reverse = 0
        for r in range(n - 1, -1, -1):
            row = reversed(board[r]) if reverse else board[r]
            reverse ^= 1
            for num in row:
                board_line[i] = num - 1 if num != -1 else i
                i += 1
        return board_line


class Solution1:
    """
    https://leetcode.com/problems/snakes-and-ladders/solutions/6797437/using-bfs-with-images-example-walkthrough-c-python-java
    Runtime 11ms Beats 95.60%
    Memory 17.85MB Beats 82.91%
    """

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        end = n * n
        min_rolls = [-1] * (end + 1)
        q = deque()
        min_rolls[1] = 0
        q.append(1)

        while q:
            x = q.popleft()
            for i in range(1, 7):
                t = x + i
                if t > end:
                    break
                row = (t - 1) // n
                col = (t - 1) % n
                v = board[n - 1 - row][(n - 1 - col)
                                       if (row % 2 == 1) else col]
                y = v if v > 0 else t
                if y == end:
                    return min_rolls[x] + 1
                if min_rolls[y] == -1:
                    min_rolls[y] = min_rolls[x] + 1
                    q.append(y)

        return -1


s = Solution01()
tests = [
    ([[-1, -1, -1, -1, 48, 5, -1], [12, 29, 13, 9, -1, 2, 32], [-1, -1, 21, 7, -1, 12, 49], [42, 37, 21, 40, -1, 22, 12], [42, -1, 2, -1, -1, -1, 6], [39, -1, 35, -1, -1, 39, -1], [-1, 36, -1, -1, -1, -1, 5]],
     3),

    ([[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1], [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]],
     4),
]
for inp, exp in tests:
    res = None
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
