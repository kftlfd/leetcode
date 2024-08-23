"""
Leetcode
592. Fraction Addition and Subtraction
Medium
2024-08-23

Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

 

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"

 

Constraints:

    The input string only contains '0' to '9', '/', '+' and '-'. So does the output.
    Each fraction (input and output) has the format ±numerator/denominator. If the first input fraction or the output is positive, then '+' will be omitted.
    The input only contains valid irreducible fractions, where the numerator and denominator of each fraction will always be in the range [1, 10]. If the denominator is 1, it means this fraction is actually an integer in a fraction format defined above.
    The number of given fractions will be in the range [1, 10].
    The numerator and denominator of the final result are guaranteed to be valid and in the range of 32-bit int.
"""

import re
from typing import List, Tuple


class Solution01:
    """
    Runtime: 577 ms, faster than 6.98% of Python3 online submissions for Fraction Addition and Subtraction.
    Memory Usage: 16.7 MB, less than 26.36% of Python3 online submissions for Fraction Addition and Subtraction.
    """

    def fractionAddition(self, expression: str) -> str:
        nums = self.parse_expr(expression)

        numer = nums[0][0]
        denom = nums[0][1]

        for nxt_num, nxt_den in nums[1:]:
            if nxt_den != denom:
                cur_denom = denom
                denom *= nxt_den
                numer *= nxt_den
                numer += nxt_num * cur_denom
            else:
                numer += nxt_num

        continue_iter = True
        while continue_iter:
            continue_iter = False

            if numer % denom == 0:
                numer //= denom
                denom = 1
                continue

            for i in range(denom // 2, 1, -1):
                if numer % i == 0 and denom % i == 0:
                    numer //= i
                    denom //= i
                    continue_iter = True
                    break

        return str(numer) + "/" + str(denom)

    def parse_expr(self, expr: str) -> List[Tuple[int, int]]:
        out = []
        n = len(expr)
        cur_start = 0
        for cur_end in range(1, n + 1):
            if cur_end >= n or expr[cur_end] in ["+", "-"]:
                nums = expr[cur_start:cur_end].split("/")
                out.append((int(nums[0]), int(nums[1])))
                cur_start = cur_end
        return out


class Solution02:
    """
    Runtime: 44 ms, faster than 12.02% of Python3 online submissions for Fraction Addition and Subtraction.
    Memory Usage: 16.5 MB, less than 89.53% of Python3 online submissions for Fraction Addition and Subtraction.
    """

    def fractionAddition(self, expression: str) -> str:
        nums = self.parse_expr(expression)

        numer = nums[0][0]
        denom = nums[0][1]

        for nxt_num, nxt_den in nums[1:]:
            if nxt_den != denom:
                cur_denom = denom
                denom *= nxt_den
                numer *= nxt_den
                numer += nxt_num * cur_denom
            else:
                numer += nxt_num

        gcd = abs(self.find_gcd(numer, denom))

        # reduce fractions
        numer //= gcd
        denom //= gcd

        return f"{numer}/{denom}"

    def find_gcd(self, a, b):
        if a == 0:
            return b
        return self.find_gcd(b % a, a)

    def parse_expr(self, expr: str) -> List[Tuple[int, int]]:
        out = []
        n = len(expr)
        cur_start = 0
        for cur_end in range(1, n + 1):
            if cur_end >= n or expr[cur_end] in ["+", "-"]:
                nums = expr[cur_start:cur_end].split("/")
                out.append((int(nums[0]), int(nums[1])))
                cur_start = cur_end
        return out


class Solution1:
    """
    leetcode solution 1: Manual Parsing + Common Denominator
    Runtime: 37 ms, faster than 48.84% of Python3 online submissions for Fraction Addition and Subtraction.
    Memory Usage: 16.5 MB, less than 89.53% of Python3 online submissions for Fraction Addition and Subtraction.
    """

    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1

        i = 0
        while i < len(expression):
            curr_num = 0
            curr_denom = 0

            is_negative = False

            # check for sign
            if expression[i] == "-" or expression[i] == "+":
                if expression[i] == "-":
                    is_negative = True
                # move to next character
                i += 1

            # build numerator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_num = curr_num * 10 + val
                i += 1

            if is_negative:
                curr_num *= -1

            # skip divisor
            i += 1

            # build denominator
            while i < len(expression) and expression[i].isdigit():
                val = int(expression[i])
                curr_denom = curr_denom * 10 + val
                i += 1

            # add fractions together using common denominator
            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        # reduce fractions
        num //= gcd
        denom //= gcd

        return f"{num}/{denom}"

    def _find_gcd(self, a, b):
        if a == 0:
            return b
        return self._find_gcd(b % a, a)


class Solution2:
    """
    leetcode solution 2: Parsing with Regular Expressions
    Runtime: 36 ms, faster than 53.88% of Python3 online submissions for Fraction Addition and Subtraction.
    Memory Usage: 16.4 MB, less than 98.84% of Python3 online submissions for Fraction Addition and Subtraction.
    """

    def fractionAddition(self, expression: str) -> str:
        num = 0
        denom = 1

        # separate expression into signed numbers
        nums = re.split("/|(?=[-+])", expression)
        nums = list(filter(None, nums))

        for i in range(0, len(nums), 2):
            curr_num = int(nums[i])
            curr_denom = int(nums[i + 1])

            num = num * curr_denom + curr_num * denom
            denom = denom * curr_denom

        gcd = abs(self._find_gcd(num, denom))

        num //= gcd
        denom //= gcd

        return str(num) + "/" + str(denom)

    def _find_gcd(self, a: int, b: int) -> int:
        if a == 0:
            return b
        return self._find_gcd(b % a, a)
