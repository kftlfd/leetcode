"""
Leetcode
191. Number of 1 Bits (easy)
2022-05-26

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

Note:

 - Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
 - In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.
"""



# try 1
# Runtime: 35 ms, faster than 78.65% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.8 MB, less than 49.85% of Python3 online submissions for Number of 1 Bits.
class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count('1')


# https://leetcode.com/problems/number-of-1-bits/discuss/1044775/Python-n-and-(n-1)-trick-+-even-faster-explained
# Runtime: 42 ms, faster than 54.50% of Python3 online submissions for Number of 1 Bits.
# Memory Usage: 13.9 MB, less than 49.85% of Python3 online submissions for Number of 1 Bits.
class Solution1:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n &= n-1
            ans += 1
        return ans



s = Solution1()
tests = [
    0b00000000000000000000000000001011,
    0b00000000000000000000000010000000,
    0b11111111111111111111111111111101
]
for t in tests:
    print(t)
    print(s.hammingWeight(t))
    print()
