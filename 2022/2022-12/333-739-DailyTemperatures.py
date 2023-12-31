"""
Leetcode
739. Daily Temperatures (medium)
2022-12-18

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
"""

from typing import List, Optional


# https://leetcode.com/problems/daily-temperatures/discuss/1574808/C++Python-3-Simple-Solutions-w-Explanation-Examples-and-Images-or-2-Monotonic-Stack-Approaches
# Runtime: 1418 ms, faster than 89.84% of Python3 online submissions for Daily Temperatures.
# Memory Usage: 28.5 MB, less than 63.31% of Python3 online submissions for Daily Temperatures.
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for cur, cur_tmp in enumerate(temperatures):
            while stack and cur_tmp > temperatures[stack[-1]]:
                last = stack.pop()
                ans[last] = cur - last
            stack.append(cur)
        return ans


s = Solution()
tests = [
    ([73, 74, 75, 71, 69, 72, 76, 73],
     [1, 1, 4, 2, 1, 1, 0, 0]),

    ([30, 40, 50, 60],
     [1, 1, 1, 0]),

    ([30, 60, 90],
     [1, 1, 0])
]
for inp, exp in tests:
    res = s.dailyTemperatures(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
