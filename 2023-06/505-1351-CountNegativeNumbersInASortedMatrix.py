"""
Leetcode
1351. Count Negative Numbers in a Sorted Matrix (easy)
2023-06-08

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Example 1:

Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:

Input: grid = [[3,2],[1,0]]
Output: 0

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100
"""

from typing import List


class Solution:
    """
    Runtime: 128 ms, faster than 65.39% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    Memory Usage: 17.6 MB, less than 14.16% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        ans = 0

        prev_end = n - 1

        for row in grid:
            start, end = 0, prev_end

            while start <= end and start < n:
                mid = (start + end) // 2
                if row[mid] < 0:
                    end = mid - 1
                else:
                    start = mid + 1

            if end < 0:  # all negative numbers in row
                ans += n
            else:  # some or no negatives in row
                ans += n - start

            prev_end = start

        return ans


class Solution1:
    """
    leetcode solution: Binary search
    Runtime: 139 ms, faster than 21.47% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    Memory Usage: 17.5 MB, less than 14.16% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        row_end = n - 1

        for row in grid:
            left, right = 0, row_end

            while left <= right:
                mid = (left + right) // 2
                if row[mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1

            ans += n - left

        return ans


class Solution2:
    """
    leetcode solution: Linear traversal
    Runtime: 136 ms, faster than 32.21% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    Memory Usage: 17.4 MB, less than 44.05% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        n = len(grid[0])
        curr_row_negative_index = n - 1

        for row in grid:
            while curr_row_negative_index >= 0 and row[curr_row_negative_index] < 0:
                curr_row_negative_index -= 1
            ans += n - (curr_row_negative_index + 1)

        return ans


class Solution3:
    """
    https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/solution/1920556
    Runtime: 131 ms, faster than 53.17% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
    Memory Usage: 17.4 MB, less than 66.13% of Python3 online submissions for Count    Negative Numbers in a Sorted Matrix.
    """

    def countNegatives(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        r = len(grid) - 1
        c = 0
        count = 0

        while c < COLS and r >= 0:
            if grid[r][c] >= 0:
                c += 1
            else:
                count += COLS - c
                r -= 1

        return count


s = Solution()
tests = [
    ([[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]],
     8),

    ([[3, 2], [1, 0]],
     0),
]
for inp, exp in tests:
    res = s.countNegatives(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
