"""
Leetcode
1799. Maximize Score After N Operations (hard)
2023-05-14

You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

    Choose two elements, x and y.
    Receive a score of i * gcd(x, y).
    Remove x and y from nums.

Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.

Example 1:
Input: nums = [1,2]
Output: 1
Explanation: The optimal choice of operations is:
(1 * gcd(1, 2)) = 1

Example 2:
Input: nums = [3,4,6,8]
Output: 11
Explanation: The optimal choice of operations is:
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

Example 3:
Input: nums = [1,2,3,4,5,6]
Output: 14
Explanation: The optimal choice of operations is:
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
"""

from typing import List
import math


class Solution:
    """
    leetcode solution 1: recursive DP with bitmasking
    Runtime: 3087 ms, faster than 29.75% of Python3 online submissions for Maximize Score After N Operations.
    Memory Usage: 16.8 MB, less than 74.05% of Python3 online submissions for Maximize Score After N Operations.
    """

    def backtrack(self, nums: List[int], mask: int, pairsPicked: int, memo: List[int]) -> int:
        # If we have picked all the numbers from 'nums' array, we can't get more score.
        if 2 * pairsPicked == len(nums):
            return 0

        # If we already solved this sub-problem then return the stored result.
        if memo[mask] != -1:
            return memo[mask]

        maxScore = 0

        # Iterate on 'nums' array to pick the first and second number of the pair.
        for firstIndex in range(len(nums)):
            for secondIndex in range(firstIndex + 1, len(nums)):

                # If the numbers are same, or already picked, then we move to next number.
                if (mask >> firstIndex) & 1 == 1 or (mask >> secondIndex) & 1 == 1:
                    continue

                # Both numbers are marked as picked in this new mask.
                newMask = mask | (1 << firstIndex) | (1 << secondIndex)

                # Calculate score of current pair of numbers, and the remaining array.
                currScore = (pairsPicked + 1) * \
                    math.gcd(nums[firstIndex], nums[secondIndex])
                remainingScore = self.backtrack(
                    nums, newMask, pairsPicked + 1, memo)

                # Store the maximum score.
                maxScore = max(maxScore, currScore + remainingScore)
                # We will use old mask in loop's next interation,
                # means we discarded the picked number and backtracked.

        # Store the result of the current sub-problem.
        memo[mask] = maxScore
        return maxScore

    def maxScore(self, nums: List[int]) -> int:
        memoSize = 1 << len(nums)  # 2^(nums array size)
        memo = [-1] * memoSize
        return self.backtrack(nums, 0, 0, memo)


class Solution2:
    """
    leetcode solution 2: iterative DP with bitmasking
    Runtime: 2858 ms, faster than 34.81% of Python3 online submissions for Maximize Score After N Operations.
    Memory Usage: 16.7 MB, less than 74.05% of Python3 online submissions for Maximize Score After N Operations.
    """

    def maxScore(self, nums: List[int]) -> int:
        maxStates = 1 << len(nums)  # 2^(nums array size)
        finalMask = maxStates - 1

        # 'dp[i]' stores max score we can get after picking remaining numbers represented by 'i'.
        dp = [0] * maxStates

        # Iterate on all possible states one-by-one.
        for state in range(finalMask, -1, -1):
            # If we have picked all numbers, we know we can't get more score as no number is remaining.
            if state == finalMask:
                dp[state] = 0
                continue

            numbersTaken = bin(state).count('1')
            pairsFormed = numbersTaken // 2
            # States representing even numbers are taken are only valid.
            if numbersTaken % 2:
                continue

            # We have picked 'pairsFormed' pairs, we try all combinations of one more pair now.
            # We iterate on two numbers using two nested for loops.
            for firstIndex in range(len(nums)):
                for secondIndex in range(firstIndex + 1, len(nums)):
                    # We only choose those numbers which were not already picked.
                    if (state >> firstIndex & 1) == 1 or (state >> secondIndex & 1) == 1:
                        continue
                    currentScore = (pairsFormed + 1) * \
                        math.gcd(nums[firstIndex], nums[secondIndex])
                    stateAfterPickingCurrPair = state | (
                        1 << firstIndex) | (1 << secondIndex)
                    remainingScore = dp[stateAfterPickingCurrPair]
                    dp[state] = max(dp[state], currentScore + remainingScore)

        # Returning score we get from 'n' remaining numbers of array.
        return dp[0]


s = Solution2()
tests = [
    ([1, 2],
     1),

    ([3, 4, 6, 8],
     11),

    ([1, 2, 3, 4, 5, 6],
     14),
]
for inp, exp in tests:
    res = s.maxScore(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
