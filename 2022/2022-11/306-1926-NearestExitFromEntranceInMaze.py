"""
Leetcode
1926. Nearest Exit from Entrance in Maze (medium)
2022-11-21

You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+'). You are also given the entrance of the maze, where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance. An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.

Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.

Example 1:
Input: maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
Output: 1
Explanation: There are 3 exits in this maze at [1,0], [0,2], and [2,3].
Initially, you are at the entrance cell [1,2].
- You can reach [1,0] by moving 2 steps left.
- You can reach [0,2] by moving 1 step up.
It is impossible to reach [2,3] from the entrance.
Thus, the nearest exit is [0,2], which is 1 step away.

Example 2:
Input: maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
Output: 2
Explanation: There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.

Example 3:
Input: maze = [[".","+"]], entrance = [0,0]
Output: -1
Explanation: There are no exits in this maze.
"""

from typing import List, Optional


# Time Limit Exceeded
# 156 / 194 test cases passed.
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        moveCount = 0
        seen = set()
        q = [entrance]
        while q:
            for _ in range(len(q)):
                r, c = q.pop(0)
                if (r == 0 or r == m-1 or c == 0 or c == n-1) and moveCount > 0:
                    return moveCount
                seen.add((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr = r + dr
                    nc = c + dc
                    if (0 <= nr < m) and \
                       (0 <= nc < n) and \
                       (maze[nr][nc] == ".") and \
                       ((nr, nc) not in seen):
                        q.append((nr, nc))
            moveCount += 1
        return -1


# leetcode solution
# Runtime: 936 ms, faster than 83.05% of Python3 online submissions for Nearest Exit from Entrance in Maze.
# Memory Usage: 14.5 MB, less than 68.60% of Python3 online submissions for Nearest Exit from Entrance in Maze.
class Solution1:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        start_r, start_c = entrance
        maze[start_r][start_c] = "+"
        q = [(start_r, start_c, 0)]
        while q:
            r, c, moves = q.pop(0)
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                if not (0 <= nr < rows) or not (0 <= nc < cols) or maze[nr][nc] == "+":
                    continue
                if nr == 0 or nr == rows-1 or nc == 0 or nc == cols-1:
                    return moves + 1
                maze[nr][nc] = "+"
                q.append((nr, nc, moves+1))
        return -1


s = Solution1()
tests = [
    (([["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]],
      [1, 2]),
        1),

    (([["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]],
      [1, 0]),
     2),

    (([[".", "+"]],
      [0, 0]),
     -1)
]
for inp, exp in tests:
    maze, entrance = inp
    res = s.nearestExit(maze, entrance)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
