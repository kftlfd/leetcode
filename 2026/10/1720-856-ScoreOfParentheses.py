"""
Leetcode
2026-10-05
856. Score of Parentheses
Medium

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

 

Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2

 

Constraints:

    2 <= s.length <= 50
    s consists of only '(' and ')'.
    s is a balanced parentheses string.
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 19.29MB Beats 55.73%
    """

    def scoreOfParentheses(self, s: str) -> int:
        total = cnt = 0
        prev_open = False

        for c in s:
            if c == "(":
                cnt += 1
                prev_open = True
            else:
                cnt -= 1
                if prev_open:
                    total += 2**cnt
                prev_open = False

        return total


class Solution1:
    """
    sample 0ms solution
    Runtime 0ms Beats 100.00%
    Memory 19.37MB Beats 17.13%
    """

    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:
            if char == '(':
                stack.append(0)
            else:
                value = max(2 * stack.pop(), 1)

                stack[-1] += value

        return stack.pop()
