"""
Leetcode
2025-09-24
166. Fraction to Recurring Decimal
Medium

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, return any of them.

It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

 

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:

Input: numerator = 2, denominator = 1
Output: "2"

Example 3:

Input: numerator = 4, denominator = 333
Output: "0.(012)"

 

Constraints:

    -2^31 <= numerator, denominator <= 2^31 - 1
    denominator != 0


Hint 1
No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
Hint 2
Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
Hint 3
Notice that once the remainder starts repeating, so does the divided result.
Hint 4
Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.
"""


class Solution:
    """
    Runtime 43ms Beats 1.74%
    Memory 18.14MB Beats 20.31%
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        num_sign = numerator >= 0
        den_sign = denominator >= 0
        sign = "" if num_sign == den_sign else "-"
        if numerator < 0:
            numerator *= -1
        if denominator < 0:
            denominator *= -1

        d, r = divmod(numerator, denominator)
        if r == 0:
            return sign + str(d)

        rem = {}
        out = [sign, str(d), "."]

        def div(num: int):
            num *= 10
            zeroes = 0
            while num < denominator:
                num *= 10
                zeroes += 1
            d, r = divmod(num, denominator)
            return ("0" * zeroes + str(d), r)

        repeat_start = 0
        cur = r
        while cur:
            div_res = div(cur)
            if cur in rem:
                repeat_start = cur
                break
            rem[cur] = div_res
            cur = div_res[1]

        res = []
        cur = r
        rep_started = False
        while cur:
            if cur == repeat_start:
                if rep_started:
                    res.append(")")
                    break
                res.append("(")
                rep_started = True
            div_res = rem[cur]
            res.append(div_res[0])
            cur = div_res[1]

        return "".join(out + res)


class Solution1:
    """
    https://leetcode.com/problems/fraction-to-recurring-decimal/solutions/7218999/have-a-look-at-it-beat-100-anyone-screenshot-attached
    Runtime 44ms Beats 1.74%
    Memory 18.15MB Beats 20.31%
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator % denominator == 0:
            return str(numerator // denominator)

        negative = (numerator < 0) ^ (denominator < 0)
        numerator, denominator = abs(numerator), abs(denominator)

        integer_part = numerator // denominator
        result = "-" if negative else ""
        result += str(integer_part) + "."

        remainder = numerator % denominator
        remainders = {}
        decimal_part = []

        while remainder != 0:
            if remainder in remainders:
                repeat_index = remainders[remainder]
                decimal_part.insert(repeat_index, "(")
                decimal_part.append(")")
                break

            remainders[remainder] = len(decimal_part)
            remainder *= 10
            digit = remainder // denominator
            decimal_part.append(str(digit))
            remainder %= denominator

        return result + "".join(decimal_part)


class Solution2:
    """
    sample 0ms solution
    Runtime 0ms Beats 100.00%
    Memory 18.03MB Beats 39.42%
    """

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'

        ans = []
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
            ans.append('-')
        n, d = abs(numerator), abs(denominator)
        ans.append(str(n//d))
        remainder = n % d
        if remainder == 0:
            return ''.join(ans)

        ans.append('.')
        dict1 = {}
        while remainder != 0 and remainder not in dict1:
            dict1[remainder] = len(ans)
            remainder *= 10
            ans += str(remainder // d)
            remainder %= d
        if remainder in dict1:
            ans.insert(dict1[remainder], '(')
            ans.append(')')

        return ''.join(ans)
