"""
Leetcode
224. Basic Calculator (hard)
2022-11-20

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
"""

from typing import List, Optional


# Time Limit Exceeded
# 43 / 44 test cases passed.
class Solution:
    def calculate(self, s: str) -> int:

        # recursively evaluate paranthese
        while s.find("(") > -1:
            start = s.find("(") + 1
            length = 0
            skip = 0
            for i, c in enumerate(s[start:]):
                if c == ")":
                    if skip == 0:
                        length = i
                        break
                    else:
                        skip -= 1
                elif c == "(":
                    skip += 1
            end = start + length
            s = s[:start - 1] + str(self.calculate(s[start:end])) + s[end + 1:]

        return self.myEval(s)

    digits = [str(n) for n in range(10)]

    def myEval(self, s):
        sign = 1
        currNum = ""
        l = len(s)
        nums = []
        for i, c in enumerate(s):
            if c in ["+", " "]:
                continue

            if c == "-":
                sign *= -1
            else:
                currNum += c

            if (i == l - 1) or (i + 1 < l and s[i+1] not in self.digits):
                if len(currNum) < 1:
                    continue

                num = int(currNum) * sign
                nums.append(num)

                sign = 1
                currNum = ""

        return sum(nums)


# https://leetcode.com/problems/basic-calculator/discuss/2831471/python3-Stack-Approach-with-Detailed-Explanations-O(n)
# Runtime: 219 ms, faster than 45.23% of Python3 online submissions for Basic Calculator.
# Memory Usage: 15.4 MB, less than 79.69% of Python3 online submissions for Basic Calculator.
class Solution1:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        stack = [0]

        for c in s:
            if c == " ":
                continue

            if c.isdigit():
                num = num * 10 + int(c)
                continue

            if c == "+" or c == "-":
                stack[-1] += num * sign

            elif c == "(":
                stack += [sign, 0]

            elif c == ")":
                lastNum = (stack.pop() + num * sign) * stack.pop()
                stack[-1] += lastNum

            num = 0
            sign = -1 if c == "-" else 1

        return stack[-1] + num * sign


s = Solution1()
tests = [
    "(1+(4+5+2)-3)+(6+8)",
    "510 + 432 - (334 - (234 - 54 + 223) - (23 + 446)) + (753 - (1234 - 343))",
    "1 + 1",
    " 2-1 + 2 ",
]
for inp in tests:
    exp = eval(inp)
    res = s.calculate(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
