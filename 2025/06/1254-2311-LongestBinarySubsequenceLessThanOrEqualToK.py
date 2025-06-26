"""
Leetcode
2025-06-26
2311. Longest Binary Subsequence Less Than or Equal to K
Medium

You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

    The subsequence can contain leading zeroes.
    The empty string is considered to be equal to 0.
    A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.

Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.

 

Constraints:

    1 <= s.length <= 1000
    s[i] is either '0' or '1'.
    1 <= k <= 109


Hint 1
Choosing a subsequence from the string is equivalent to deleting all the other digits.
Hint 2
If you were to remove a digit, which one should you remove to reduce the value of the string?
"""


class Solution:
    """
    Runtime 1ms Beats 75.61%
    Memory 17.71MB Beats 66.67%
    """

    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        ans = n
        val = int(s, 2)
        msb_idx = 0

        while val > k:
            while msb_idx < n and s[msb_idx] != "1":
                msb_idx += 1
            val -= 1 << (n - msb_idx - 1)
            ans -= 1
            msb_idx += 1

        return ans


class Solution1:
    """
    leetcode solution: Greedy
    Runtime 0ms Beats 100.00%
    Memory 17.76MB Beats 66.67%
    """

    def longestSubsequence(self, s: str, k: int) -> int:
        sm = 0
        cnt = 0
        bits = k.bit_length()
        for i, ch in enumerate(s[::-1]):
            if ch == "1":
                if i < bits and sm + (1 << i) <= k:
                    sm += 1 << i
                    cnt += 1
            else:
                cnt += 1
        return cnt
