"""
Leetcode
858. Mirror Reflection (medium)
2022-08-04

There is a special square room with mirrors on each of the four walls. Except for the southwest corner, there are receptors on each of the remaining corners, numbered 0, 1, and 2.

The square room has walls of length p and a laser ray from the southwest corner first meets the east wall at a distance q from the 0th receptor.

Given the two integers p and q, return the number of the receptor that the ray meets first.

The test cases are guaranteed so that the ray will meet a receptor eventually.

Example 1:
Input: p = 2, q = 1
Output: 2
Explanation: The ray meets receptor 2 the first time it gets reflected back to the left wall.

Example 2:
Input: p = 3, q = 1
Output: 1
"""

import math


# https://leetcode.com/problems/mirror-reflection/discuss/2376191/C++-Java-Python-or-Faster-then-100-or-Full-explanations-or
# Runtime: 54 ms, faster than 36.63% of Python3 online submissions for Mirror Reflection.
# Memory Usage: 14 MB, less than 16.83% of Python3 online submissions for Mirror Reflection.
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        while p % 2 == 0 and q % 2 == 0:
            p, q = p / 2, q / 2
        return int(1 - p % 2 + q % 2)


# https://leetcode.com/problems/mirror-reflection/discuss/2376355/Python3-oror-4-lines-geometry-w-explanation-oror-TM:-9281
# Runtime: 48 ms, faster than 57.43% of Python3 online submissions for Mirror Reflection.
# Memory Usage: 14 MB, less than 16.83% of Python3 online submissions for Mirror Reflection.
class Solution1:
    def mirrorReflection(self, p: int, q: int) -> int:
        L = math.lcm(p, q)

        if (L//q) % 2 == 0:
            return 2

        return (L//p) % 2


s = Solution()
tests = [
    (2, 1), (3, 1), (4, 2)
]
for p, q in tests:
    print(p, q)
    print(s.mirrorReflection(p, q))
    print()
