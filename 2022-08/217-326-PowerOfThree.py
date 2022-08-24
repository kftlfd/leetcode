"""
Leetcode
326. Power of Three (easy)
2022-08-24

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3**x.
"""


# Runtime: 101 ms, faster than 80.38% of Python3 online submissions for Power of Three.
# Memory Usage: 13.8 MB, less than 57.97% of Python3 online submissions for Power of Three.
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


# leetcode solution - Approach 4: Integer Limitations
# Runtime: 140 ms, faster than 45.13% of Python3 online submissions for Power of Three.
# Memory Usage: 13.8 MB, less than 57.97% of Python3 online submissions for Power of Three.
class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0


s = Solution()
tests = [
    27, 0, 9, -3
]
for t in tests:
    print(t)
    print(s.isPowerOfThree(t))
    print()
