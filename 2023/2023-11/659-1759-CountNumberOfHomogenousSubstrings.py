"""
Leetcode
1759. Count Number of Homogenous Substrings (medium)
2023-11-09

Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 109 + 7.

A string is homogenous if all the characters of the string are the same.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abbcccaa"
Output: 13
Explanation: The homogenous substrings are listed as below:
"a"   appears 3 times.
"aa"  appears 1 time.
"b"   appears 2 times.
"bb"  appears 1 time.
"c"   appears 3 times.
"cc"  appears 2 times.
"ccc" appears 1 time.
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13.

Example 2:

Input: s = "xy"
Output: 2
Explanation: The homogenous substrings are "x" and "y".

Example 3:

Input: s = "zzzzz"
Output: 15

 

Constraints:

    1 <= s.length <= 10^5
    s consists of lowercase letters.
"""


class Solution:
    """
    Runtime: 87 ms, faster than 96.04% of Python3 online submissions for Count Number of Homogenous Substrings.
    Memory Usage: 17.2 MB, less than 77.34% of Python3 online submissions for Count Number of Homogenous Substrings.
    """

    def countHomogenous(self, s: str) -> int:
        ans = 0
        cur_char = None
        cur_len = 0

        for c in s:
            if c == cur_char:
                cur_len += 1
            else:
                ans += self.getSum(cur_len)
                cur_char = c
                cur_len = 1

        ans += self.getSum(cur_len)

        return ans % (10**9 + 7)

    def getSum(self, n: int) -> int:
        return n * (n + 1) // 2
