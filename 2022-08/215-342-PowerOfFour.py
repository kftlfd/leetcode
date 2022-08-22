"""
Leetcode
342. Power of Four (easy)
2022-08-22

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
"""


# Runtime: 34 ms, faster than 91.81% of Python3 online submissions for Power of Four.
# Memory Usage: 13.9 MB, less than 10.18% of Python3 online submissions for Power of Four.
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0:
            return False
        while n >= 1:
            if n == 1:
                return True
            n /= 4
        return False


# https://leetcode.com/problems/power-of-four/discuss/772269/Python-O(1)-oneliner-solution-explained
# Runtime: 37 ms, faster than 86.41% of Python3 online submissions for Power of Four.
# Memory Usage: 13.8 MB, less than 54.38% of Python3 online submissions for Power of Four.
class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and n & (n-1) == 0 and 0b1010101010101010101010101010101 & n == n


s = Solution()
tests = [
    16, 5, 1, 0, -64
]
for t in tests:
    print(t)
    print(s.isPowerOfFour(t))
    print()
