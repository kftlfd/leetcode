"""
Leetcode
70. Climbing Stairs
Easy
2024-01-18

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

 

Constraints:

    1 <= n <= 45
"""


class Solution:
    """
    Runtime: 41 ms, faster than 33.21% of Python3 online submissions for Climbing Stairs.
    Memory Usage: 17.5 MB, less than 15.77% of Python3 online submissions for Climbing Stairs.
    """

    def __init__(self):
        self.memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in self.memo:
            self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
