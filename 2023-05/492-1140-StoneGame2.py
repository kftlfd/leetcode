"""
Leetcode
1140. Stone Game II (medium)
2023-05-26

Alice and Bob continue their games with piles of stones.  There are a number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].  The objective of the game is to end with the most stones. 

Alice and Bob take turns, with Alice starting first.  Initially, M = 1.

On each player's turn, that player can take all the stones in the first X remaining piles, where 1 <= X <= 2M.  Then, we set M = max(M, X).

The game continues until all the stones have been taken.

Assuming Alice and Bob play optimally, return the maximum number of stones Alice can get.

Example 1:
Input: piles = [2,7,9,4,4]
Output: 10
Explanation:  If Alice takes one pile at the beginning, Bob takes two piles, then Alice takes 2 piles again. Alice can get 2 + 4 + 4 = 10 piles in total. If Alice takes two piles at the beginning, then Bob can take all three piles left. In this case, Alice get 2 + 7 = 9 piles in total. So we return 10 since it's larger. 

Example 2:
Input: piles = [1,2,3,4,5,100]
Output: 104
"""

from typing import List


class Solution:
    """
    leetcode solution
    Runtime: 780 ms, faster than 32.72% of Python3 online submissions for Stone Game II.
    Memory Usage: 18.2 MB, less than 41.01% of Python3 online submissions for Stone Game II.
    """

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[[-1] * (n + 1) for i in range(n + 1)] for p in range(0, 2)]

        def f(p, i, m):
            if i == n:
                return 0
            if dp[p][i][m] != -1:
                return dp[p][i][m]
            res = 1000000 if p == 1 else -1
            s = 0
            for x in range(1, min(2 * m, n - i) + 1):
                s += piles[i + x - 1]
                if p == 0:
                    res = max(res, s + f(1, i + x, max(m, x)))
                else:
                    res = min(res, f(0, i + x, max(m, x)))
            dp[p][i][m] = res
            return res

        return f(0, 0, 1)


s = Solution()
tests = [
    ([2, 7, 9, 4, 4],
     10),

    ([1, 2, 3, 4, 5, 100],
     104),
]
for inp, exp in tests:
    res = s.stoneGameII(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
