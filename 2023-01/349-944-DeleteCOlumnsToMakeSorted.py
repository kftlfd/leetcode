"""
Leetcode
944. Delete Columns to Make Sorted (easy)
2023-01-03

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Example 1:
Input: strs = ["cba","daf","ghi"]
Output: 1
Explanation: The grid looks as follows:
  cba
  daf
  ghi
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

Example 2:
Input: strs = ["a","b"]
Output: 0
Explanation: The grid looks as follows:
  a
  b
Column 0 is the only column and is sorted, so you will not delete any columns.

Example 3:
Input: strs = ["zyx","wvu","tsr"]
Output: 3
Explanation: The grid looks as follows:
  zyx
  wvu
  tsr
All 3 columns are not sorted, so you will delete all 3.
"""

from typing import List, Optional


# Runtime: 488 ms, faster than 31.16% of Python3 online submissions for Delete Columns to Make Sorted.
# Memory Usage: 14.9 MB, less than 13.05% of Python3 online submissions for Delete Columns to Make Sorted.
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        to_del = 0

        for col in zip(*strs):
            for i in range(1, len(col)):
                if col[i] < col[i-1]:
                    to_del += 1
                    break

        return to_del


# Runtime: 324 ms, faster than 51.58% of Python3 online submissions for Delete Columns to Make Sorted.
# Memory Usage: 14.5 MB, less than 100.00% of Python3 online submissions for Delete Columns to Make Sorted.
class Solution1:
    def minDeletionSize(self, strs: List[str]) -> int:

        to_del = 0

        for row in range(len(strs[0])):
            for col in range(1, len(strs)):
                if strs[col][row] < strs[col-1][row]:
                    to_del += 1
                    break

        return to_del


s = Solution1()
tests = [
    (["cba", "daf", "ghi"],
     1),
    (["a", "b"],
     0),
    (["zyx", "wvu", "tsr"],
     3),
]
for inp, exp in tests:
    res = s.minDeletionSize(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
