"""
Leetcode
844. Backspace String Compare (easy)
2023-10-19

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".

 

Constraints:

    1 <= s.length, t.length <= 200
    s and t only contain lowercase letters and '#' characters.
"""

from typing import List
from itertools import zip_longest


class Solution:
    """
    Runtime: 29 ms, faster than 97.01% of Python3 online submissions for Backspace String Compare.
    Memory Usage: 16.2 MB, less than 54.52% of Python3 online submissions for Backspace String Compare.
    """

    def backspaceCompare(self, s: str, t: str) -> bool:

        def type_str(string: str) -> List[str]:
            stack = []
            for c in string:
                if c == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            return stack

        return type_str(s) == type_str(t)


class Solution1:
    """
    leetcode solution: two pointers
    Time: O(m + n)
    Space: O(1)
    Runtime: 41 ms, faster than 43.68% of Python3 online submissions for Backspace String Compare.
    Memory Usage: 16.3 MB, less than 54.52% of Python3 online submissions for Backspace String Compare.
    """

    def backspaceCompare(self, s: str, t: str) -> bool:

        def f(string: str):
            skip = 0
            for c in reversed(string):
                if c == '#':
                    skip += 1
                elif skip > 0:
                    skip -= 1
                else:
                    yield c

        return all(c1 == c2 for c1, c2 in zip_longest(f(s), f(t)))


sol = Solution()
tests = [
    (("y#fo##f", "y#f#o##f"),
     True),
]
for inp, exp in tests:
    res = sol.backspaceCompare(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
