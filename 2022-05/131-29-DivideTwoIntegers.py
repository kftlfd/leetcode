"""
Leetcode
29. Divide Two Integers (medium)
2022-05-30

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-231, 231 - 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""



# https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code/148769
# Runtime: 45 ms, faster than 54.56% of Python3 online submissions for Divide Two Integers.
# Memory Usage: 13.9 MB, less than 76.13% of Python3 online submissions for Divide Two Integers.
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sig = (dividend < 0) == (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            x = 0
            while dividend >= (divisor << (x + 1)):
                x += 1
            res += (1 << x)
            dividend -= (divisor << x)
        return min(res if sig else -res, 2147483647)



s = Solution()
tests = [
    [10, 3],
    [7, -3],
]
for t in tests:
    print(t)
    print(s.divide(t[0], t[1]))
    print()
