"""
Leetcode
2026-10-01
20. Valid Parentheses
Easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

    1 <= s.length <= 10^4
    s consists of parentheses only '()[]{}'.


"""


class Solution:
    """
    Runtime 1ms Beats 45.08%
    Memory 19.18MB Beats 91.62%
    """

    def isValid(self, s: str) -> bool:
        open_brackets = ["(", "[", "{"]
        close_bracket = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        stack = []

        for c in s:
            if c in open_brackets:
                stack.append(c)
                continue
            if not stack or c != close_bracket[stack[-1]]:
                return False
            stack.pop()

        return not stack


class Solution1:
    """
    sample 0ms solution
    Runtime 4ms Beats 11.63%
    Memory 19.31MB Beats 24.83%
    """

    def isValid(self, s: str) -> bool:
        i = 0
        a = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top = a.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False
        return len(a) == 0
