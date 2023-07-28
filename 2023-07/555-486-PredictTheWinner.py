"""
Leetcode
486. Predict the Winner (medium)
2023-07-28

You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0. At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1]) which reduces the size of the array by 1. The player adds the chosen number to their score. The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, and you should also return true. You may assume that both players are playing optimally.

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2. 
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). 
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. 
Hence, player 1 will never be the winner and you need to return false.

Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Constraints:

    1 <= nums.length <= 20
    0 <= nums[i] <= 10^7
"""

from typing import List
from collections import defaultdict


class Solution:
    """
    leetcode solution 1: recursion
    Time: O(2^n)
    Space: O(n)
    Runtime: 2911 ms, faster than 25.24% of Python3 online submissions for Predict the Winner.
    Memory Usage: 16.3 MB, less than 88.23% of Python3 online submissions for Predict the Winner.
    """

    def PredictTheWinner(self, nums: List[int]) -> bool:

        def maxDiff(left, right):
            if left == right:
                return nums[left]

            score1 = nums[left] - maxDiff(left + 1, right)
            score2 = nums[right] - maxDiff(left, right - 1)

            return max(score1, score2)

        return maxDiff(0, len(nums) - 1) >= 0


class Solution1:
    """
    leetcode solution 2: dynamic programming (top-down)
    Time: O(n^2)
    Space: O(n^2)
    Runtime: 44 ms, faster than 92.84% of Python3 online submissions for Predict the Winner.
    Memory Usage: 16.6 MB, less than 31.92% of Python3 online submissions for Predict the Winner.
    """

    def PredictTheWinner(self, nums: List[int]) -> bool:
        memo = defaultdict(int)

        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]

            if left == right:
                return nums[left]

            score1 = nums[left] - maxDiff(left + 1, right)
            score2 = nums[right] - maxDiff(left, right - 1)

            memo[(left, right)] = max(score1, score2)
            return memo[(left, right)]

        return maxDiff(0, len(nums) - 1) >= 0


class Solution2:
    """
    leetcode solution 3: dynamic programming (bottom-up)
    Time: O(n^2)
    Space: O(n^2)
    Runtime: 38 ms, faster than 97.94% of Python3 online submissions for Predict the Winner.
    Memory Usage: 16.4 MB, less than 70.15% of Python3 online submissions for Predict the Winner.
    """

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = nums[i]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left][right] = max(
                    nums[left] - dp[left + 1][right], nums[right] - dp[left][right - 1])

        return dp[0][n - 1] >= 0


class Solution3:
    """
    leetcode solution 4: dynamic programming (bottom-up, space-optimized)
    Time: O(n^2)
    Space: O(n)
    Runtime: 44 ms, faster than 92.84% of Python3 online submissions for Predict the Winner.
    Memory Usage: 16.1 MB, less than 97.57% of Python3 online submissions for Predict the Winner.
    """

    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for diff in range(1, n):
            for left in range(n - diff):
                right = left + diff
                dp[left] = max(nums[left] - dp[left + 1],
                               nums[right] - dp[left])

        return dp[0] >= 0


s = Solution()
tests = [
    ([1, 5, 2],
     False),

    ([1, 5, 233, 7],
     True)
]
for inp, exp in tests:
    res = s.PredictTheWinner(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
