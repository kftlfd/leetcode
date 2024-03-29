"""
Leetcode
2390. Removing Stars From a String (medium)
2023-04-11

You are given a string s, which contains stars *.

In one operation, you can:

    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.

Return the string after all stars have been removed.

Note:

    The input will be generated such that the operation is always possible.
    It can be shown that the resulting string will always be unique.

Example 1:
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".

Example 2:
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
"""


class Solution:
    """
    Runtime: 223 ms, faster than 81.22% of Python3 online submissions for Removing Stars From a String.
    Memory Usage: 15.7 MB, less than 40.09% of Python3 online submissions for Removing Stars From a String.
    """

    def removeStars(self, s: str) -> str:

        stack = []

        for c in s:
            if c == '*':
                stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)


sol = Solution()
tests = [
    ('leet**cod*e',
     'lecoe'),

    ('erase*****',
     ''),
]
for inp, exp in tests:
    res = sol.removeStars(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
