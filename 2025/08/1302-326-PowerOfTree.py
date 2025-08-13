"""
Leetcode
2025-08-13
326. Power of Three
Easy

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

 

Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33

Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.

Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).

 

Constraints:

    -2^31 <= n <= 2^31 - 1

 
Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    """
    Runtime 18ms Beats 23.13%
    Memory 17.91MB Beats 25.52%
    """

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        i = 1

        while i <= n:
            if i == n:
                return True
            i *= 3

        return False


class Solution1:
    """
    https://leetcode.com/problems/power-of-three/solutions/7073228/100-fast-easy-power-of-three-check-lightning-fast-intuitive-solution
    Runtime 11ms Beats 48.06%
    Memory 17.70MB Beats 93.17%
    """

    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1
