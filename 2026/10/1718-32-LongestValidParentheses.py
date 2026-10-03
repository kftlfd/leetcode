"""
Leetcode
2026-10-03
32. Longest Valid Parentheses
Hard

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

 

Constraints:

    0 <= s.length <= 3 * 10^4
    s[i] is '(', or ')'.


"""


class Solution:
    """
    sample 7ms solution
    Runtime 7ms Beats 90.33%
    Memory 20.56MB Beats 39.73%
    """

    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0

        for i, c in enumerate(s):

            if c == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])

        return max_length
