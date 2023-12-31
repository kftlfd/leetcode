"""
Leetcode
1531. String Compression II
Hard
2023-12-28

Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".

Notice that in this problem, we are not adding '1' after single characters.

Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.

Find the minimum length of the run-length encoded version of s after deleting at most k characters.

 

Example 1:

Input: s = "aaabcccd", k = 2
Output: 4
Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

Example 2:

Input: s = "aabbaa", k = 2
Output: 2
Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.

Example 3:

Input: s = "aaaaaaaaaaa", k = 0
Output: 3
Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.

 

Constraints:

    1 <= s.length <= 100
    0 <= k <= s.length
    s contains only lowercase English letters.

Hints
- Use dynamic programming.
- The state of the DP can be the current index and the remaining characters to delete.
- Having a prefix sum for each character can help you determine for a certain character c in some specific range, how many characters you need to delete to merge all occurrences of c in that range.
"""


from math import inf
from functools import cache


class Solution:
    """
    https://leetcode.com/problems/string-compression-ii/discuss/2704470/LeetCode-The-Hard-Way-Explained-Line-By-Line
    Runtime: 3425 ms, faster than 5.00% of Python3 online submissions for String Compression II.
    Memory Usage: 373.5 MB, less than 11.00% of Python3 online submissions for String Compression II.
    """

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @cache
        def dp(i, prev, prev_cnt, k):
            # set it to inf as we will take the min later
            if k < 0:
                return inf

            # we delete all characters, return 0
            if i == len(s):
                return 0

            # here we can have two choices, we either
            # 1. delete the current char
            # 2. keep the current char
            # we calculate both result and take the min one
            delete = dp(i + 1, prev, prev_cnt, k - 1)
            if s[i] == prev:
                # e.g. a2 -> a3
                keep = dp(i + 1, prev, prev_cnt + 1, k)
                # add an extra 1 for the following cases
                # since the length of RLE will be changed
                # e.g. prev_cnt = 1: a -> a2
                # e.g. prev_cnt = 9: a9 -> a10
                # e.g. prev_cnt = 99: a99 -> a100
                # otherwise the length of RLE will not be changed
                # e.g. prev_cnt = 3: a3 -> a4
                # e.g. prev_cnt = 8: a8 -> a9
                # alternative you can calculate `RLE(prev_cnt + 1) - RLE(cnt)`
                if prev_cnt in [1, 9, 99]:
                    keep += 1
            else:
                # e.g. a
                keep = dp(i + 1, s[i], 1, k) + 1

            return min(delete, keep)

        # dp(i, prev, prev_cnt, k) returns the length of RLE with k characters to be deleted
        # starting from index i
        # with previous character `prev`
        # with `prev_cnt` times repeated so far
        return dp(0, "", 0, k)
