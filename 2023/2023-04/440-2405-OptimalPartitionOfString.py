"""
Leetcode
2405. Optimal Partition of String (medium)
2023-04-04

Given a string s, partition the string into one or more substrings such that the characters in each substring are unique. That is, no letter appears in a single substring more than once.

Return the minimum number of substrings in such a partition.

Note that each character should belong to exactly one substring in a partition.

Example 1:
Input: s = "abacaba"
Output: 4
Explanation:
Two possible partitions are ("a","ba","cab","a") and ("ab","a","ca","ba").
It can be shown that 4 is the minimum number of substrings needed.

Example 2:
Input: s = "ssssss"
Output: 6
Explanation:
The only valid partition is ("s","s","s","s","s","s").
"""


class Solution:
    """
    Runtime: 113 ms, faster than 72.30% of Python3 online submissions for Optimal Partition of String.
    Memory Usage: 14.7 MB, less than 19.39% of Python3 online submissions for Optimal Partition of String.
    """

    def partitionString(self, s: str) -> int:
        parts = 1
        curr_part = set()
        for c in s:
            if c not in curr_part:
                curr_part.add(c)
            else:
                parts += 1
                curr_part = set(c)
        return parts


class Solution1:
    """
    https://leetcode.com/problems/optimal-partition-of-string/solution/1853073
    Runtime: 157 ms, faster than 33.77% of Python3 online submissions for Optimal Partition of String.
    Memory Usage: 14.6 MB, less than 90.90% of Python3 online submissions for Optimal Partition of String.
    """

    def partitionString(self, s: str) -> int:
        parts = 1
        bitmask = 0
        for c in s:
            char_bit = 1 << (ord(c) - 97)  # ord('a') == 97
            if bitmask & char_bit:  # have seen char
                parts += 1
                bitmask = 0
            bitmask |= char_bit
        return parts


sol = Solution()
tests = [
    ("abacaba",
     4),

    ("ssssss",
     6),
]
for inp, exp in tests:
    res = sol.partitionString(inp)
    if res != exp:
        print('input:  ', inp)
        print('expect: ', exp)
        print('output: ', res)
        print()
print('Completed testing')
