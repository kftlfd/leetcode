"""
Leetcode
2025-08-10
869. Reordered Power of 2
Medium

You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true

Example 2:

Input: n = 10
Output: false

 

Constraints:

    1 <= n <= 10^9


"""

from collections import Counter


class Solution:
    """
    Runtime 5ms Beats 37.02%
    Memory 17.98MB Beats 17.56%
    """

    def reorderedPowerOf2(self, n: int) -> bool:
        cnt = Counter(str(n))
        n_ceil = self.getIntCeil(n)
        for i in range(32):
            num = 1 << i
            if num > n_ceil:
                break
            if Counter(str(num)) == cnt:
                return True
        return False

    def getIntCeil(self, n: int) -> int:
        out = 10
        while out < n:
            out *= 10
        return out


class Solution1:
    """
    sample 0ms submission
    Runtime 0ms Beats 100.00%
    Memory 17.64MB Beats 79.77%
    """

    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            return ''.join(sorted(str(x)))

        target = count_digits(n)

        # Precompute all powers of 2 within range
        for i in range(31):  # 2^0 to 2^30
            if count_digits(1 << i) == target:
                return True
        return False
