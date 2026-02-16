"""
Leetcode
2026-02-16
190. Reverse Bits
Easy

Reverse bits of a given 32 bits signed integer.

 

Example 1:

Input: n = 43261596

Output: 964176192

Explanation:
Integer	Binary
43261596	00000010100101000001111010011100
964176192	00111001011110000010100101000000

Example 2:

Input: n = 2147483644

Output: 1073741822

Explanation:
Integer	Binary
2147483644	01111111111111111111111111111100
1073741822	00111111111111111111111111111110

 

Constraints:

    0 <= n <= 2^31 - 2
    n is even.

 

Follow up: If this function is called many times, how would you optimize it?

"""


class Solution:
    """
    Runtime 47ms Beats 37.74%
    Memory 19.28MB Beats 48.27%
    """

    def reverseBits(self, n: int) -> int:
        return int(f"{n:032b}"[::-1], 2)


class Solution1:
    """
    sample 36ms solution
    Runtime 40ms Beats 74.42%
    Memory 19.30MB Beats 22.24%
    """

    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1

        return res
