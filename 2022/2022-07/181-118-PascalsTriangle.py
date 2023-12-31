"""
Leetcode
118. Pascal's Triangle (easy)
2022-07-19

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it 

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
"""

from typing import List


# iterative with memoization
# Runtime: 70 ms, faster than 5.19% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.9 MB, less than 66.48% of Python3 online submissions for Pascal's Triangle.
class Solution:
    rows = {1: [1], 2: [1, 1]}
    last = 2

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows not in self.rows:
            for i in range(self.last + 1, numRows + 1):
                self.rows[i] = self.new_row(self.rows[i - 1])
            self.last = numRows
        return [self.rows[i] for i in range(1, numRows + 1)]

    def new_row(self, prev_row: List[int]) -> List[int]:
        row = [1] + prev_row
        for i in range(1, len(row) - 1):
            row[i] += row[i + 1]
        return row


# recursive
# Runtime: 47 ms, faster than 52.25% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.8 MB, less than 66.48% of Python3 online submissions for Pascal's Triangle.
class Solution1:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        else:
            prev = self.generate(numRows - 1)
            row = [1] + prev[-1]
            for i in range(1, len(row) - 1):
                row[i] += row[i + 1]
            prev.append(row)
            return prev


# https://leetcode.com/problems/pascals-triangle/discuss/38128/Python-4-lines-short-solution-using-map.
# Runtime: 54 ms, faster than 32.11% of Python3 online submissions for Pascal's Triangle.
# Memory Usage: 13.8 MB, less than 97.62% of Python3 online submissions for Pascal's Triangle.
class Solution2:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows):
            res.append(
                list(map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])))
        return res[:numRows]


s = Solution2()
tests = [1, 5, 10]
for t in tests:
    print(t)
    print(s.generate(t))
    print()
