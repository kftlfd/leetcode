"""
Leetcode
2024-11-22
1072. Flip Columns For Maximum Number of Equal Rows
Medium

You are given an m x n binary matrix matrix.

You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from 0 to 1 or vice versa).

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: matrix = [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:

Input: matrix = [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:

Input: matrix = [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 300
    matrix[i][j] is either 0 or 1.
"""

from collections import Counter
from typing import List


class Solution:
    """
    Runtime: 207 ms, faster than 18.52% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
    Memory Usage: 19.4 MB, less than 32.16% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
    """

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = Counter()

        # count occurences of row or its opposite/flip
        for row in matrix:
            cnt["".join(map(str, row))] += 1
            cnt["".join(map(str, map(lambda x: x ^ 1, row)))] += 1

        return max(cnt.values())


class Solution2:
    """
    leetcode solution 2
    Runtime: 64 ms, faster than 53.70% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
    Memory Usage: 19.5 MB, less than 32.16% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
    """

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # Dictionary to store frequency of each pattern
        pattern_frequency = {}

        for current_row in matrix:
            # Convert row to pattern using list comprehension and join
            # 'T' if element matches first element, 'F' otherwise
            row_pattern = "".join(
                "T" if num == current_row[0] else "F" for num in current_row
            )

            # Update pattern frequency using dict.get() with default value
            pattern_frequency[row_pattern] = (
                pattern_frequency.get(row_pattern, 0) + 1
            )

        # Return maximum frequency using max() with default of 0
        return max(pattern_frequency.values(), default=0)


class Solution3:
    """
    https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/solution/2732161
    Runtime: 47 ms, faster than 82.41% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
    Memory Usage: 20.1 MB, less than 20.60% of Python3 online submissions for Flip Columns For Maximum Number of Equal Rows.
    """

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        return max(Counter(tuple(r[0] ^ x for x in r) for r in matrix).values())
