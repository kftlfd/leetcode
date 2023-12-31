"""
Leetcode
20. Valid Parentheses (easy)
2023-04-10

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
"""


class Solution:
    """
    Runtime: 36 ms, faster than 39.98% of Python3 online submissions for Valid Parentheses.
    Memory Usage: 13.8 MB, less than 96.69% of Python3 online submissions for Valid Parentheses.
    """

    def isValid(self, s: str) -> bool:

        stack = []

        opposites = {
            ')': '(',
            ']': '[',
            '}': '{',
        }

        closing_brackets = opposites.keys()

        for c in s:
            if c in closing_brackets:
                if not stack or stack[-1] != opposites[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        return len(stack) == 0


sol = Solution()
tests = [
    ('()',
     True),

    ('()[]{}',
     True),

    ('(]',
     False),
]
for inp, exp in tests:
    res = sol.isValid(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
