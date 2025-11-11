"""
Leetcode
2025-11-11
474. Ones and Zeroes
Medium

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

 

Example 1:

Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
Output: 4
Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

Input: strs = ["10","0","1"], m = 1, n = 1
Output: 2
Explanation: The largest subset is {"0", "1"}, so the answer is 2.

 

Constraints:

    1 <= strs.length <= 600
    1 <= strs[i].length <= 100
    strs[i] consists only of digits '0' and '1'.
    1 <= m, n <= 100

 
"""

from functools import cache
from typing import List


class Solution:
    """
    Runtime 871ms Beats 97.29%
    Memory 243.51MB Beats 27.19%
    """

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        strings = sorted([(len(string), string.count("1")) for string in strs])

        @cache
        def dfs(idx: int, zeroes: int, ones: int, cur_subset_len: int) -> int:
            if idx >= l:
                return cur_subset_len

            cur_len, cur_ones = strings[idx]

            if zeroes + ones + cur_len > m + n:
                return cur_subset_len

            cur_zeroes = cur_len - cur_ones

            pick = dfs(idx + 1, zeroes + cur_zeroes, ones + cur_ones, cur_subset_len + 1) \
                if zeroes + cur_zeroes <= m and ones + cur_ones <= n \
                else 0

            omit = dfs(idx + 1, zeroes, ones, cur_subset_len)

            return max(pick, omit)

        return dfs(0, 0, 0, 0)
