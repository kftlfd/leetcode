"""
Leetcode
2026-03-26
3548. Equal Sum Grid Partition II
Hard

You are given an m x n matrix grid of positive integers. Your task is to determine if it is possible to make either one horizontal or one vertical cut on the grid such that:

    Each of the two resulting sections formed by the cut is non-empty.
    The sum of elements in both sections is equal, or can be made equal by discounting at most one single cell in total (from either section).
    If a cell is discounted, the rest of the section must remain connected.

Return true if such a partition exists; otherwise, return false.

Note: A section is connected if every cell in it can be reached from any other cell by moving up, down, left, or right through other cells in the section.

 

Example 1:

Input: grid = [[1,4],[2,3]]

Output: true

Explanation:

    A horizontal cut after the first row gives sums 1 + 4 = 5 and 2 + 3 = 5, which are equal. Thus, the answer is true.

Example 2:

Input: grid = [[1,2],[3,4]]

Output: true

Explanation:

    A vertical cut after the first column gives sums 1 + 3 = 4 and 2 + 4 = 6.
    By discounting 2 from the right section (6 - 2 = 4), both sections have equal sums and remain connected. Thus, the answer is true.

Example 3:

Input: grid = [[1,2,4],[2,3,5]]

Output: false

Explanation:

    A horizontal cut after the first row gives 1 + 2 + 4 = 7 and 2 + 3 + 5 = 10.
    By discounting 3 from the bottom section (10 - 3 = 7), both sections have equal sums, but they do not remain connected as it splits the bottom section into two parts ([2] and [5]). Thus, the answer is false.

Example 4:

Input: grid = [[4,1,8],[3,2,6]]

Output: false

Explanation:

No valid cut exists, so the answer is false.

 

Constraints:

    1 <= m == grid.length <= 10^5
    1 <= n == grid[i].length <= 10^5
    2 <= m * n <= 10^5
    1 <= grid[i][j] <= 10^5


Hint 1
In a grid (or any subgrid), when can a section be disconnected? Can disconnected components occur if the section spans more than one row and more than one column?
Hint 2
Handle single rows or single columns separately. For all other partitions, maintain the sums and value frequencies of each section to check whether removing at most one element from one section can make the two sums equal.
"""

from typing import Counter, List


class Solution:
    """
    Time Limit Exceeded
    935 / 942 testcases passed
    """

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = 0
        total_cnt: Counter[int] = Counter()

        for row in grid:
            for val in row:
                total_sum += val
                total_cnt[val] += 1

        return self.can_partition_rows(grid, total_sum, total_cnt) or self.can_partition_cols(grid, total_sum, total_cnt)

    def can_partition_rows(self, grid: List[List[int]], total_sum: int, total_cnt: Counter[int]) -> bool:
        m = len(grid)
        n = len(grid[0])
        cur_sum = 0
        cur_cnt = Counter()
        rest_sum = total_sum
        rest_cnt = Counter({k: v for k, v in total_cnt.items()})

        for r in range(m - 1):
            for c in range(n):
                val = grid[r][c]
                cur_sum += val
                cur_cnt[val] += 1
                rest_cnt[val] -= 1
            rest_sum = total_sum - cur_sum

            if cur_sum == rest_sum:
                return True

            if cur_sum > rest_sum:
                remove = [grid[0][0], grid[0][-1]] if r == 0 \
                    else [grid[0][0], grid[r][0]] if n == 1 \
                    else [k for k, v in cur_cnt.items() if v > 0]
                if cur_sum - rest_sum in remove:
                    return True
                continue

            remove = [grid[-1][0], grid[-1][-1]] if r + 1 == m - 1 \
                else [grid[r + 1][0], grid[-1][0]] if n == 1 \
                else [k for k, v in rest_cnt.items() if v > 0]
            if rest_sum - cur_sum in remove:
                return True

        return False

    def can_partition_cols(self, grid: List[List[int]], total_sum: int, total_cnt: Counter) -> bool:
        m = len(grid)
        n = len(grid[0])
        cur_sum = 0
        cur_cnt = Counter()
        rest_sum = total_sum
        rest_cnt = Counter({k: v for k, v in total_cnt.items()})

        for c in range(n - 1):
            for r in range(m):
                val = grid[r][c]
                cur_sum += val
                cur_cnt[val] += 1
                rest_cnt[val] -= 1
            rest_sum = total_sum - cur_sum

            if cur_sum == rest_sum:
                return True

            if cur_sum > rest_sum:
                remove = [grid[0][0], grid[-1][0]] if c == 0 \
                    else [grid[0][0], grid[0][c]] if m == 1 \
                    else [k for k, v in cur_cnt.items() if v > 0]
                if cur_sum - rest_sum in remove:
                    return True
                continue

            remove = [grid[0][-1], grid[-1][-1]] if c + 1 == n - 1 \
                else [grid[0][c + 1], grid[0][-1]] if m == 1 \
                else [k for k, v in rest_cnt.items() if v > 0]
            if rest_sum - cur_sum in remove:
                return True

        return False


class Solution1:
    """
    leetcode solution: Rotation Matrix + Hash Table + Enumeration of the Upper Matrix Sum
    Runtime 1003ms Beats 41.67%
    Memory 46.33MB Beats 97.22%
    """

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                total += grid[i][j]
        for _ in range(4):
            exist = set()
            exist.add(0)
            sum_val = 0
            m = len(grid)
            n = len(grid[0])
            if m < 2:
                grid = self.rotation(grid)
                continue
            if n == 1:
                for i in range(m - 1):
                    sum_val += grid[i][0]
                    tag = sum_val * 2 - total
                    if tag == 0 or tag == grid[0][0] or tag == grid[i][0]:
                        return True
                grid = self.rotation(grid)
                continue
            for i in range(m - 1):
                for j in range(n):
                    exist.add(grid[i][j])
                    sum_val += grid[i][j]
                tag = sum_val * 2 - total
                if i == 0:
                    if tag == 0 or tag == grid[0][0] or tag == grid[0][n - 1]:
                        return True
                    continue
                if tag in exist:
                    return True
            grid = self.rotation(grid)
        return False

    def rotation(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        tmp = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                tmp[j][m - 1 - i] = grid[i][j]
        return tmp


s = Solution()
tests = [
    ([[10, 5, 4, 5]], False),
    ([[253, 10, 10]], True),
    ([[1, 2, 4], [2, 3, 5]], False),
    ([[4, 1, 8], [3, 2, 6]], False),
    ([[1, 4], [2, 3]], True),
    ([[1, 2], [3, 4]], True),
]
for inp, exp in tests:
    res = s.canPartitionGrid(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
