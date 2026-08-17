"""
Leetcode
2026-08-17
1563. Stone Game V
Hard

There are several stones arranged in a row, and each stone has an associated value which is an integer given in the array stoneValue.

In each round of the game, Alice divides the row into two non-empty rows (i.e. left row and right row), then Bob calculates the value of each row which is the sum of the values of all the stones in this row. Bob throws away the row which has the maximum value, and Alice's score increases by the value of the remaining row. If the value of the two rows are equal, Bob lets Alice decide which row will be thrown away. The next round starts with the remaining row.

The game ends when there is only one stone remaining. Alice's score is initially zero.

Return the maximum score that Alice can obtain.

 

Example 1:

Input: stoneValue = [6,2,3,4,5,5]
Output: 18
Explanation: In the first round, Alice divides the row to [6,2,3], [4,5,5]. The left row has the value 11 and the right row has value 14. Bob throws away the right row and Alice's score is now 11.
In the second round Alice divides the row to [6], [2,3]. This time Bob throws away the left row and Alice's score becomes 16 (11 + 5).
The last round Alice has only one choice to divide the row which is [2], [3]. Bob throws away the right row and Alice's score is now 18 (16 + 2). The game ends because only one stone is remaining in the row.

Example 2:

Input: stoneValue = [7,7,7,7,7,7,7]
Output: 28

Example 3:

Input: stoneValue = [4]
Output: 0

 

Constraints:

    1 <= stoneValue.length <= 500
    1 <= stoneValue[i] <= 10^6


Hint 1
We need to try all possible divisions for the current row to get the max score.
Hint 2
As calculating all possible divisions will lead us to calculate some sub-problems more than once, we need to think of dynamic programming.
"""

from functools import cache
from typing import List


class Solution:
    """
    Runtime 8398ms Beats 27.84%
    Memory 86.30MB Beats 7.84%
    """

    def stoneGameV(self, stoneValue: List[int]) -> int:

        @cache
        def ans(l: int, r: int) -> int:
            if r - l <= 1:
                return 0

            out = 0
            left_sum = 0
            right_sum = sum(stoneValue[l:r])
            for i in range(l, r):
                num = stoneValue[i]
                left_sum += num
                right_sum -= num
                if left_sum < right_sum:
                    out = max(out, left_sum + ans(l, i + 1))
                elif left_sum > right_sum:
                    out = max(out, right_sum + ans(i + 1, r))
                else:
                    out = max(out,
                              left_sum + ans(l, i + 1),
                              right_sum + ans(i + 1, r))

            return out

        return ans(0, len(stoneValue))


class Solution2:
    """
    leetcode solution 2: Dynamic Programming Optimization
    Runtime 641ms Beats 76.08%
    Memory 32.92MB Beats 68.63%
    """

    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        f = [[0] * n for _ in range(n)]
        maxl = [[0] * n for _ in range(n)]
        maxr = [[0] * n for _ in range(n)]

        for left in range(n - 1, -1, -1):
            maxl[left][left] = maxr[left][left] = stoneValue[left]
            total = stoneValue[left]
            suml = 0
            i = left - 1
            for right in range(left + 1, n):
                total += stoneValue[right]
                while i + 1 < right and (suml + stoneValue[i + 1]) * 2 <= total:
                    suml += stoneValue[i + 1]
                    i += 1
                if left <= i:
                    f[left][right] = max(f[left][right], maxl[left][i])
                if i + 1 < right:
                    f[left][right] = max(f[left][right], maxr[i + 2][right])
                if suml * 2 == total:
                    f[left][right] = max(f[left][right], maxr[i + 1][right])
                maxl[left][right] = max(
                    maxl[left][right - 1], total + f[left][right]
                )
                maxr[left][right] = max(
                    maxr[left + 1][right], total + f[left][right]
                )

        return f[0][n - 1]
