"""
Leetcode
2025-12-20
944. Delete Columns to Make Sorted
Solved

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid.

    For example, strs = ["abc", "bce", "cae"] can be arranged as follows:

abc
bce
cae

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

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

 

Constraints:

    n == strs.length
    1 <= n <= 100
    1 <= strs[i].length <= 1000
    strs[i] consists of lowercase English letters.


"""

from typing import List


class Solution:
    """
    Runtime 47ms Beats 78.45%
    Memory 18.07MB Beats 99.28%
    """

    def minDeletionSize(self, strs: List[str]) -> int:
        def is_sorted(arr: List[str]) -> bool:
            for a, b in zip(arr, arr[1:]):
                if a > b:
                    return False
            return True

        return sum(not is_sorted(col) for col in zip(*strs))  # type: ignore


class Solution1:
    """
    sample 27ms solution
    Runtime 27ms Beats 95.11%
    Memory 18.31MB Beats 52.44%
    """

    def minDeletionSize(self, strs: List[str]) -> int:
        return sum(col != sorted(col) for col in map(list, zip(*strs)))
