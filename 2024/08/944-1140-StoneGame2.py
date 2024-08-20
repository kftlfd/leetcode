"""
Leetcode
1140. Stone Game II
Medium
2024-08-20

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

 

Constraints:

    1 <= piles.length <= 100
    1 <= piles[i] <= 10^4

Hints:
- Use dynamic programming: the states are (i, m) for the answer of piles[i:] and that given m.
"""

from functools import cache
from typing import List


class Solution:
    """
    Runtime: 313 ms, faster than 65.92% of Python3 online submissions for Stone Game II.
    Memory Usage: 20.3 MB, less than 39.18% of Python3 online submissions for Stone Game II.
    """

    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        @cache
        def dp(i: int, m: int, is_alice: bool) -> int:
            # reurn Alice's score

            # always take all remaining piles if you can
            if i + 2*m >= n:
                if is_alice:
                    return sum(piles[i:i+2*m])
                return 0

            if is_alice:
                # take the X piles that will maximize Alice's score
                max_score = 0
                for x in range(1, 2*m + 1):
                    max_score = max(
                        max_score,
                        sum(piles[i:i+x]) + dp(i+x, max(m, x), False)
                    )
                return max_score

            # is_bob: take X piles that will minimize Alice's score
            min_score = float('inf')
            for x in range(1, 2*m + 1):
                min_score = min(min_score, dp(i+x, max(m, x), True))
            return min_score

        return dp(0, 1, True)


class Solution2:
    """
    leetcode solution 2: Dynamic Programming (Tabulation)
    Runtime: 1437 ms, faster than 8.16% of Python3 online submissions for Stone Game II.
    Memory Usage: 17 MB, less than 83.47% of Python3 online submissions for Stone Game II.
    """

    def stoneGameII(self, piles: List[int]) -> int:
        length = len(piles)
        dp = [[0 for _ in range(length + 1)] for _ in range(length + 1)]

        # Store suffix sum for all possible suffix
        suffix_sum = [0 for _ in range(length + 1)]
        for i in range(length - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]

        # Initialize the dp array.
        for i in range(length + 1):
            dp[i][length] = suffix_sum[i]

        # Start from the last index to store the future state first.
        for index in range(length - 1, -1, -1):
            for max_till_now in range(length - 1, 0, -1):
                for X in range(1, min(2 * max_till_now, length - index) + 1):
                    dp[index][max_till_now] = max(
                        dp[index][max_till_now],
                        suffix_sum[index] -
                        dp[index + X][max(max_till_now, X)],
                    )

        return dp[0][1]


s = Solution()
tests = [
    ([4], 4),
    ([4, 4], 8),
    ([4, 4, 4], 8),
    ([2, 7, 9, 4, 4], 10),
    ([1, 2, 3, 4, 5, 100], 104),
]
for inp, exp in tests:
    res = s.stoneGameII(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
