"""
Leetcode
279. Perfect Squares (medium)
2022-11-22

Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""

from typing import List, Optional
import math


# Runtime: 3421 ms, faster than 48.58% of Python3 online submissions for Perfect Squares.
# Memory Usage: 57.7 MB, less than 6.36% of Python3 online submissions for Perfect Squares.
class Solution:
    def numSquares(self, n: int) -> int:

        squares = [x**2 for x in range(math.floor(n**0.5), 0, -1)]

        # BFS
        q = [(0, 0)]
        while q:
            currSum, currCount = q.pop(0)
            nextCount = currCount + 1
            for num in squares:
                nextSum = currSum + num
                if nextSum == n:
                    return nextCount
                elif nextSum < n:
                    q.append((nextSum, nextCount))


# https://leetcode.com/problems/perfect-squares/discuss/2837639/Python-3-oror-no-dp-just-mathematics-wbrief-explanation-oror-TM:-10084
# Runtime: 47 ms, faster than 98.34% of Python3 online submissions for Perfect Squares.
# Memory Usage: 14 MB, less than 71.48% of Python3 online submissions for Perfect Squares.
class Solution:
    def numSquares(self, n: int) -> int:

        i = 1
        while i*i <= n:
            if i*i == n:
                return 1
            i += 1

        def CheckTwo(c):
            while c % 2 == 0:
                c = c//2
            while c % 5 == 0:
                c = c//5
            while c % 9 == 0:
                c = c//9

            if c % 3 == 0:
                return False

            if c in (0, 1, 13, 17):
                return True

            i, j = 0, int(c**.5)

            while i <= j:
                if i*i + j*j == c:
                    return True
                if i*i + j*j < c:
                    i += 1
                if i*i + j*j > c:
                    j -= 1

            return False

        if CheckTwo(n):
            return 2

        while not n % 4:
            n //= 4
        if n % 8 != 7:
            return 3

        return 4


s = Solution()
tests = [
    (12,
     3),

    (13,
     2),

    (7168,
     4)
]
for inp, exp in tests:
    res = s.numSquares(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
