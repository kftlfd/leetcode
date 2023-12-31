"""
Leetcode
1155. Number of Dice Rolls With Target Sum (medium)
2022-10-02

You have n dice and each die has k faces numbered from 1 to k.

Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice so the sum of the face-up numbers equals target. Since the answer may be too large, return it modulo 109 + 7.

Example 1:
Input: n = 1, k = 6, target = 3
Output: 1
Explanation: You throw one die with 6 faces.
There is only one way to get a sum of 3.

Example 2:
Input: n = 2, k = 6, target = 7
Output: 6
Explanation: You throw two dice, each with 6 faces.
There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:
Input: n = 30, k = 30, target = 500
Output: 222616187
Explanation: The answer must be returned modulo 109 + 7.
"""


# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355894/Python-DP-with-memoization-explained
# Runtime: 1554 ms, faster than 18.01% of Python3 online submissions for Number of Dice Rolls With Target Sum.
# Memory Usage: 19.8 MB, less than 31.10% of Python3 online submissions for Number of Dice Rolls With Target Sum.
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = {}

        def dp(d, target):
            if d == 0:
                return 0 if target > 0 else 1
            if (d, target) in memo:
                return memo[(d, target)]
            to_return = 0
            for i in range(max(0, target-k), target):
                to_return += dp(d-1, i)
            memo[(d, target)] = to_return
            return to_return

        return dp(n, target) % (10**9 + 7)


s = Solution()
tests = [
    (1, 6, 3),
    (2, 6, 7),
    (30, 30, 500),
]
for t in tests:
    print(t)
    n, k, target = t
    print(s.numRollsToTarget(n, k, target))
    print()
