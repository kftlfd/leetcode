"""
Leetcode
880. Decoded String at Index (medium)
2023-09-27

You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

    If the character read is a letter, that letter is written onto the tape.
    If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.

Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".

Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".

 

Constraints:

    2 <= s.length <= 100
    s consists of lowercase English letters and digits 2 through 9.
    s starts with a letter.
    1 <= k <= 10^9
    It is guaranteed that k is less than or equal to the length of the decoded string.
    The decoded string is guaranteed to have less than 2^63 letters.
"""


class Solution:
    """
    Memory Limit Exceeded
    """

    def decodeAtIndex(self, s: str, k: int) -> str:
        tape = ""

        for c in s:
            if c.isdigit():
                tape *= int(c)
            else:
                tape += c

            if len(tape) >= k:
                return tape[k - 1]


class Solution1:
    """
    https://leetcode.com/problems/decoded-string-at-index/discuss/156747/JavaC++Python-O(N)-Time-O(1)-Space
    Runtime: 37 ms, faster than 59.60% of Python3 online submissions for Decoded String at Index.
    Memory Usage: 16.2 MB, less than 65.15% of Python3 online submissions for Decoded String at Index.
    """

    def decodeAtIndex(self, s: str, k: int) -> str:
        N = 0

        for i, c in enumerate(s):
            N = N * int(c) if c.isdigit() else N + 1
            if k <= N:
                break

        for j in range(i, -1, -1):
            c = s[j]
            if c.isdigit():
                N /= int(c)
                k %= N
            else:
                if k == N or k == 0:
                    return c
                N -= 1
