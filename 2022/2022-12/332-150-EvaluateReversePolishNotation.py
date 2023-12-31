"""
Leetcode
150. Evaluate Reverse Polish Notation (medium)
2022-12-17

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

Example 1:
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6

Example 3:
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""

from typing import List, Optional


# https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47444/Python-easy-to-understand-solution
# Runtime: 134 ms, faster than 62.19% of Python3 online submissions for Evaluate Reverse Polish Notation.
# Memory Usage: 14.3 MB, less than 60.84% of Python3 online submissions for Evaluate Reverse Polish Notation.
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for t in tokens:

            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))
                continue

            r, l = stack.pop(), stack.pop()

            if t == "+":
                stack.append(l + r)
            elif t == "-":
                stack.append(l - r)
            elif t == "*":
                stack.append(l * r)
            elif t == "/":
                stack.append(int(float(l) / r))

        return stack[-1]


s = Solution()
tests = [
    (["2", "1", "+", "3", "*"],
     9),

    (["4", "13", "5", "/", "+"],
     6),

    (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],
        22),
]
for inp, exp in tests:
    res = s.evalRPN(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
