"""
Leetcode
168. Excel Sheet Column Title (easy)
2023-08-22

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

Example 1:

Input: columnNumber = 1
Output: "A"

Example 2:

Input: columnNumber = 28
Output: "AB"

Example 3:

Input: columnNumber = 701
Output: "ZY"

Constraints:

    1 <= columnNumber <= 231 - 1
"""


class Solution:
    """
    leetcode solution
    Runtime: 42 ms, faster than 53.64% of Python3 online submissions for Excel Sheet Column Title.
    Memory Usage: 16.2 MB, less than 89.71% of Python3 online submissions for Excel Sheet Column Title.
    """

    def convertToTitle(self, columnNumber: int) -> str:
        ans = []
        rem = columnNumber
        while rem > 0:
            rem -= 1
            ans.insert(0, chr(rem % 26 + ord('A')))
            rem = rem // 26
        return "".join(ans)


s = Solution()
tests = [
    (1,
     'A'),

    (28,
     'AB'),

    (701,
     'ZY'),
]
for inp, exp in tests:
    res = s.convertToTitle(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
