"""
Leetcode
2026-09-01
3568. Minimum Moves to Clean the Classroom
Medium

You are given an m x n grid classroom where a student volunteer is tasked with cleaning up litter scattered around the room. Each cell in the grid is one of the following:

    'S': Starting position of the student
    'L': Litter that must be collected (once collected, the cell becomes empty)
    'R': Reset area that restores the student's energy to full capacity, regardless of their current energy level (can be used multiple times)
    'X': Obstacle the student cannot pass through
    '.': Empty space

You are also given an integer energy, representing the student's maximum energy capacity. The student starts with this energy from the starting position 'S'.

Each move to an adjacent cell (up, down, left, or right) costs 1 unit of energy. If the energy reaches 0, the student can only continue if they are on a reset area 'R', which resets the energy to its maximum capacity energy.

Return the minimum number of moves required to collect all litter items, or -1 if it's impossible.

 

Example 1:

Input: classroom = ["S.", "XL"], energy = 2

Output: 2

Explanation:

    The student starts at cell (0, 0) with 2 units of energy.
    Since cell (1, 0) contains an obstacle 'X', the student cannot move directly downward.
    A valid sequence of moves to collect all litter is as follows:
        Move 1: From (0, 0) → (0, 1) with 1 unit of energy and 1 unit remaining.
        Move 2: From (0, 1) → (1, 1) to collect the litter 'L'.
    The student collects all the litter using 2 moves. Thus, the output is 2.

Example 2:

Input: classroom = ["LS", "RL"], energy = 4

Output: 3

Explanation:

    The student starts at cell (0, 1) with 4 units of energy.
    A valid sequence of moves to collect all litter is as follows:
        Move 1: From (0, 1) → (0, 0) to collect the first litter 'L' with 1 unit of energy used and 3 units remaining.
        Move 2: From (0, 0) → (1, 0) to 'R' to reset and restore energy back to 4.
        Move 3: From (1, 0) → (1, 1) to collect the second litter 'L'.
    The student collects all the litter using 3 moves. Thus, the output is 3.

Example 3:

Input: classroom = ["L.S", "RXL"], energy = 3

Output: -1

Explanation:

No valid path collects all 'L'.

 

Constraints:

    1 <= m == classroom.length <= 20
    1 <= n == classroom[i].length <= 20
    classroom[i][j] is one of 'S', 'L', 'R', 'X', or '.'
    1 <= energy <= 50
    There is exactly one 'S' in the grid.
    There are at most 10 'L' cells in the grid.


Hint 1
Use BFS with states (x, y, mask, e, steps), initializing with (sx, sy, 0, energy, 0), and for each move update e (-1 per step), update mask on 'L', reset e=energy on 'R', and return steps when mask == fullMask.
Hint 2
Maintain a 3D array bestEnergy[x][y][mask] storing the maximum e seen for each (x,y,mask) and skip any new state with e <= bestEnergy[x][y][mask] to prune.
"""

from collections import deque
from typing import List


class Solution:
    """
    Runtime 2938ms Beats 35.09%
    Memory 60.36MB Beats 38.60%
    """

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        l_mask = {}  # key=(row, col)
        nxt_l_mask = 1
        full_l_mask = 0

        srow, scol = 0, 0

        for row in range(m):
            for col in range(n):
                v = classroom[row][col]
                if v == "S":
                    srow, scol = row, col
                elif v == "L":
                    full_l_mask |= nxt_l_mask
                    l_mask[(row, col)] = nxt_l_mask
                    nxt_l_mask <<= 1

        # (row, col, litter_mask, energy, steps)
        q = deque([(srow, scol, 0, energy, 0)])
        best_energy = {}  # key=(row, col, litter_mask)
        dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def nxt_pos(row: int, col: int) -> list[tuple[int, int]]:
            return [
                (row + dr, col + dc)
                for dr, dc in dirs
                if 0 <= row + dr < m
                and 0 <= col + dc < n
                and classroom[row+dr][col+dc] != "X"
            ]

        while q:
            row, col, litter, enrg, steps = q.popleft()

            v = classroom[row][col]

            if v == "L":
                litter |= l_mask.get((row, col), 0)

            if litter == full_l_mask:
                return steps

            if v == "R":
                enrg = energy

            if energy < 1:
                continue

            for nr, nc in nxt_pos(row, col):
                ne = enrg - 1
                if best_energy.get((nr, nc, litter), -1) >= ne:
                    continue
                best_energy[(nr, nc, litter)] = ne
                q.append((nr, nc, litter, ne, steps + 1))

        return -1


class Solution1:
    """
    leetcode solution
    Runtime 1762ms Beats 87.72%
    Memory 25.12MB Beats 84.21%
    """

    def minMoves(self, classroom: List[str], energy: int) -> int:
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        m = len(classroom)
        n = len(classroom[0])
        l_id = [[0] * n for _ in range(m)]
        sx = sy = 0
        cnt = 0
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == "S":
                    sx, sy = i, j
                elif classroom[i][j] == "L":
                    l_id[i][j] = 1 << cnt
                    cnt += 1

        full = 1 << cnt
        bestEnergy = [
            [[-1 for _ in range(full)] for _ in range(n)] for _ in range(m)
        ]
        bestEnergy[sx][sy][0] = energy
        Info = deque()
        Info.append((sx, sy, 0, energy, 0))
        while Info:
            x, y, mask, e, steps = Info.popleft()
            if mask == full - 1:
                return steps
            if e == 0:
                continue
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if (
                    nx < 0
                    or nx >= m
                    or ny < 0
                    or ny >= n
                    or classroom[nx][ny] == "X"
                ):
                    continue
                ne = energy if classroom[nx][ny] == "R" else e - 1
                nmask = mask | l_id[nx][ny]
                if ne > bestEnergy[nx][ny][nmask]:
                    bestEnergy[nx][ny][nmask] = ne
                    Info.append((nx, ny, nmask, ne, steps + 1))
        return -1
