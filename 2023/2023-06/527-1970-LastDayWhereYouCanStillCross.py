"""
Leetcode
1970. Last Day Where You Can Still Cross (hard)
2023-06-30

There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

Example 1:

Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

Example 2:

Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

Example 3:

Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.

Constraints:

    2 <= row, col <= 2 * 10^4
    4 <= row * col <= 2 * 10^4
    cells.length == row * col
    1 <= ri <= row
    1 <= ci <= col
    All the values of cells are unique.
"""

from typing import List


class Solution:
    """
    Runtime: 3987 ms, faster than 15.21% of Python3 online submissions for Last Day Where You Can Still Cross.
    Memory Usage: 27.7 MB, less than 47.83% of Python3 online submissions for Last Day Where You Can Still Cross.
    """

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        moves = ((-1, 0), (0, -1), (0, 1), (1, 0))

        def can_cross(day: int) -> bool:
            nonlocal row, col, cells

            matrix = [[0] * col for _ in range(row)]
            for i in range(day):
                r, c = cells[i]
                matrix[r-1][c-1] = 1

            q = [(0, c) for c in range(col) if matrix[0][c] == 0]
            visited = set(q)
            while q:
                cur_r, cur_c = q.pop(0)
                for dr, dc in moves:
                    nxt_r, nxt_c = cur_r + dr, cur_c + dc
                    if not (0 <= nxt_r < row and
                            0 <= nxt_c < col and
                            matrix[nxt_r][nxt_c] == 0 and
                            (nxt_r, nxt_c) not in visited):
                        continue
                    if nxt_r == row - 1:
                        return True
                    visited.add((nxt_r, nxt_c))
                    q.append((nxt_r, nxt_c))

            return False

        l = 0
        r = len(cells) - 1
        while l <= r:
            m = (l + r) // 2
            if can_cross(m):
                l = m + 1
            else:
                r = m - 1

        return r


class Solution1:
    """
    leetcode solution: DFS + Binary Search
    Time: O(row * col * log(row*col))
    Space: O(row * col)
    Runtime: 3423 ms, faster than 20.65% of Python3 online submissions for Last Day Where You Can Still Cross.
    Memory Usage: 45.9 MB, less than 5.43% of Python3 online submissions for Last Day Where You Can Still Cross.
    """

    moves = ((-1, 0), (0, -1), (0, 1), (1, 0))

    def canCross(self, row, col, cells, day):
        grid = [[0] * col for _ in range(row)]

        for r, c in cells[:day]:
            grid[r-1][c-1] = 1

        def dfs(r, c):
            if not (0 <= r < row and
                    0 <= c < col and
                    grid[r][c] == 0):
                return False
            if r == row - 1:
                return True
            grid[r][c] = -1
            for dr, dc in self.moves:
                if dfs(r+dr, c+dc):
                    return True
            return False

        for i in range(col):
            if grid[0][i] == 0 and dfs(0, i):
                return True

        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left = 1
        right = len(cells)

        while left < right:
            mid = right - (right - left) // 2
            if self.canCross(row, col, cells, mid):
                left = mid
            else:
                right = mid - 1

        return left


class DSU:
    def __init__(self, n):
        self.root = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.root[root_x] = root_y
        self.size[root_y] = self.size[root_x]


class Solution2:
    """
    leetcode solution 3: Disjoint Set Union (on land cells)
    Time: O(row * col)
    Space: O(row * col)
    Runtime: 1968 ms, faster than 70.11% of Python3 online submissions for Last Day Where You Can Still Cross.
    Memory Usage: 25.2 MB, less than 90.76% of Python3 online submissions for Last Day Where You Can Still Cross.
    """

    moves = ((-1, 0), (0, -1), (0, 1), (1, 0))

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + 2)
        grid = [[1] * col for _ in range(row)]

        for i in range(len(cells) - 1, -1, -1):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 0
            index1 = r * col + c + 1
            for dr, dc in self.moves:
                new_r, new_c = r + dr, c + dc
                index2 = new_r * col + new_c + 1
                if 0 <= new_r < row and \
                        0 <= new_c < col and \
                        grid[new_r][new_c] == 0:
                    dsu.union(index1, index2)
            if r == 0:
                dsu.union(0, index1)
            if r == row - 1:
                dsu.union(row * col + 1, index1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return i


class Solution3:
    """
    leetcode solution 3: Disjoint Set Union (on water cells)
    Time: O(row * col * a(row*col))
    alpha(T) -- is the inverse Ackermann function that grows so slowly, that it doesn't exceed 4 for all reasonable T (approximately T<10^600)
    https://en.wikipedia.org/wiki/Disjoint-set_data_structure#Time_complexity
    Space: O(row * col)
    Runtime: 1475 ms, faster than 99.46% of Python3 online submissions for Last Day Where You Can Still Cross.
    Memory Usage: 25.3 MB, less than 73.91% of Python3 online submissions for Last Day Where You Can Still Cross.
    """

    moves = ((-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1))

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        dsu = DSU(row * col + 2)
        grid = [[0] * col for _ in range(row)]

        for i in range(row * col):
            r, c = cells[i][0] - 1, cells[i][1] - 1
            grid[r][c] = 1
            index1 = r * col + c + 1
            for dr, dc in self.moves:
                new_r, new_c = r + dr, c + dc
                index2 = new_r * col + new_c + 1
                if 0 <= new_r < row and \
                        0 <= new_c < col and \
                        grid[new_r][new_c] == 1:
                    dsu.union(index1, index2)
            if c == 0:
                dsu.union(0, index1)
            if c == col - 1:
                dsu.union(row * col + 1, index1)
            if dsu.find(0) == dsu.find(row * col + 1):
                return i


s = Solution()
tests = [
    ((2, 2, [[1, 1], [2, 1], [1, 2], [2, 2]]),
     2),

    ((2, 2, [[1, 1], [1, 2], [2, 1], [2, 2]]),
     1),

    ((3, 3, [[1, 2], [2, 1], [3, 3], [2, 2], [1, 1], [1, 3], [2, 3], [3, 2], [3, 1]]),
     3),
]
for inp, exp in tests:
    res = s.latestDayToCross(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
