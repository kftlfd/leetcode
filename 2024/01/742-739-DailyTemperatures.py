"""
Leetcode
739. Daily Temperatures
Medium
2024-01-31

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

 

Constraints:

    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100

Hints:
- If the temperature is say, 70 today, then in the future a warmer temperature must be either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.
"""

from typing import List


class Solution:
    """
    https://leetcode.com/problems/daily-temperatures/discuss/1574808/C++Python-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for cur, cur_tmp in enumerate(temperatures):
            while stack and cur_tmp > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = cur - last
            stack.append(cur)

        return ans
