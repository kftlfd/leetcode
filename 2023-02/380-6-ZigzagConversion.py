"""
Leetcode
6. Zigzag Conversion (medium)
2023-02-03

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:
Input: s = "A", numRows = 1
Output: "A"
"""

from typing import List, Optional


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """
        Runtime: 66 ms, faster than 61.60% of Python3 online submissions for Zigzag Conversion.
        Memory Usage: 14.1 MB, less than 29.22% of Python3 online submissions for Zigzag Conversion.
        """

        if numRows < 2:
            return s

        rows = [[] for _ in range(numRows)]

        forwards = True
        currRow = 0
        lastRow = numRows - 1

        for c in s:
            rows[currRow].append(c)

            if currRow == lastRow:
                forwards = False
            elif currRow == 0:
                forwards = True

            currRow += 1 if forwards else -1

        return ''.join(c for row in rows for c in row)


s = Solution()
tests = [
    (("ABC", 1),
     "ABC"),

    (("PAYPALISHIRING", 3),
     'PAHNAPLSIIGYIR'),

    (("PAYPALISHIRING", 4),
     "PINALSIGYAHRPI"),

    (("A", 1),
     "A")
]
for inp, exp in tests:
    res = s.convert(*inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
