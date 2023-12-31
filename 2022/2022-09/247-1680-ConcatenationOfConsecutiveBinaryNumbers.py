"""
Leetcode
1680. Concatenation of Consecutive Binary Numbers (medium)
2022-09-23

Given an integer n, return the decimal value of the binary string formed by concatenating the binary representations of 1 to n in order, modulo 109 + 7.

Example 1:
Input: n = 1
Output: 1
Explanation: "1" in binary corresponds to the decimal value 1. 

Example 2:
Input: n = 3
Output: 27
Explanation: In binary, 1, 2, and 3 corresponds to "1", "10", and "11".
After concatenating them, we have "11011", which corresponds to the decimal value 27.

Example 3:
Input: n = 12
Output: 505379714
Explanation: The concatenation results in "1101110010111011110001001101010111100".
The decimal value of that is 118505380540.
After modulo 109 + 7, the result is 505379714.
"""


# Time Limit Exceeded
class Solution:
    def concatenatedBinary(self, n: int) -> int:

        def to_bin(n):
            if n == 1:
                return "1"
            else:
                return f"{to_bin(n-1)}{n:b}"

        return int(to_bin(n), 2) % (10**9 + 7)


# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/discuss/1037323/Python-O(n)-and-O(log2-n)-fast-and-short-explained
# Runtime: 4516 ms, faster than 14.17% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
# Memory Usage: 13.9 MB, less than 62.20% of Python3 online submissions for Concatenation of Consecutive Binary Numbers.
class Solution1:
    def concatenatedBinary(self, n: int) -> int:
        ans, M = 0, 10**9 + 7
        for x in range(n):
            ans = (ans * (1 << (len(bin(x+1)) - 2)) + x+1) % M
        return ans


s = Solution()
tests = [
    1,
    3,
    12,
]
for t in tests:
    print(t)
    print(s.concatenatedBinary(t))
    print()
