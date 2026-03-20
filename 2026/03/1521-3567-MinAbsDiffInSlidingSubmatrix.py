"""
Leetcode
2026-03-20
3567. Minimum Absolute Difference in Sliding Submatrix
Medium

You are given an m x n integer matrix grid and an integer k.

For every contiguous k x k submatrix of grid, compute the minimum absolute difference between any two distinct values within that submatrix.

Return a 2D array ans of size (m - k + 1) x (n - k + 1), where ans[i][j] is the minimum absolute difference in the submatrix whose top-left corner is (i, j) in grid.

Note: If all elements in the submatrix have the same value, the answer will be 0.
A submatrix (x1, y1, x2, y2) is a matrix that is formed by choosing all cells matrix[x][y] where x1 <= x <= x2 and y1 <= y <= y2.

 

Example 1:

Input: grid = [[1,8],[3,-2]], k = 2

Output: [[2]]

Explanation:

    There is only one possible k x k submatrix: [[1, 8], [3, -2]].
    Distinct values in the submatrix are [1, 8, 3, -2].
    The minimum absolute difference in the submatrix is |1 - 3| = 2. Thus, the answer is [[2]].

Example 2:

Input: grid = [[3,-1]], k = 1

Output: [[0,0]]

Explanation:

    Both k x k submatrix has only one distinct element.
    Thus, the answer is [[0, 0]].

Example 3:

Input: grid = [[1,-2,3],[2,3,5]], k = 2

Output: [[1,2]]

Explanation:

    There are two possible k*k submatrix:
        Starting at (0, 0): [[1, -2], [2, 3]].
            Distinct values in the submatrix are [1, -2, 2, 3].
            The minimum absolute difference in the submatrix is |1 - 2| = 1.
        Starting at (0, 1): [[-2, 3], [3, 5]].
            Distinct values in the submatrix are [-2, 3, 5].
            The minimum absolute difference in the submatrix is |3 - 5| = 2.
    Thus, the answer is [[1, 2]].

 

Constraints:

    1 <= m == grid.length <= 30
    1 <= n == grid[i].length <= 30
    -10^5 <= grid[i][j] <= 10^5
    1 <= k <= min(m, n)


"""

from typing import List


class Solution01:
    """
    Runtime 47ms Beats 37.10%
    Memory 19.40MB Beats 62.90%
    """

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        if k < 2:
            return ans

        def get_submat_min_diff(r: int, c: int) -> int:
            values = sorted(set(
                grid[rr][cc]
                for rr in range(r, r + k)
                for cc in range(c, c + k)
            ))
            if len(values) < 2:
                return 0
            cur = values[1] - values[0]
            for i in range(2, len(values)):
                cur = min(cur, values[i] - values[i - 1])
            return cur

        for r in range(m - k + 1):
            for c in range(n - k + 1):
                ans[r][c] = get_submat_min_diff(r, c)

        return ans


class Solution02:
    """
    without set
    Runtime 44ms Beats 43.55%
    Memory 19.48MB Beats 62.90%
    """

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        if k < 2:
            return ans

        def get_submat_min_diff(r: int, c: int) -> int:
            values = sorted(
                grid[rr][cc]
                for rr in range(r, r + k)
                for cc in range(c, c + k)
            )
            if len(values) < 2:
                return 0
            cur = None
            for i in range(1, len(values)):
                a, b = values[i], values[i - 1]
                if a != b:
                    if cur is None:
                        cur = a - b
                    else:
                        cur = min(cur, a - b)
            return cur if cur is not None else 0

        for r in range(m - k + 1):
            for c in range(n - k + 1):
                ans[r][c] = get_submat_min_diff(r, c)

        return ans


class Solution1:
    """
    leetcode solution: Sorting
    Runtime 44ms Beats 43.55%
    Memory 19.51MB Beats 40.32%
    """

    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                kgrid = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        kgrid.append(grid[x][y])
                kmin = float("inf")
                kgrid.sort()
                for t in range(1, len(kgrid)):
                    if kgrid[t] == kgrid[t - 1]:
                        continue
                    kmin = min(kmin, kgrid[t] - kgrid[t - 1])
                if kmin != float("inf") and not isinstance(kmin, float):
                    res[i][j] = kmin
        return res
