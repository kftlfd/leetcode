"""
Leetcode
2025-11-08
1611. Minimum One Bit Operations to Make Integers Zero
Hard

Given an integer n, you must transform it into 0 using the following operations any number of times:

    Change the rightmost (0th) bit in the binary representation of n.
    Change the ith bit in the binary representation of n if the (i-1)th bit is set to 1 and the (i-2)th through 0th bits are set to 0.

Return the minimum number of operations to transform n into 0.

 

Example 1:

Input: n = 3
Output: 2
Explanation: The binary representation of 3 is "11".
"11" -> "01" with the 2nd operation since the 0th bit is 1.
"01" -> "00" with the 1st operation.

Example 2:

Input: n = 6
Output: 4
Explanation: The binary representation of 6 is "110".
"110" -> "010" with the 2nd operation since the 1st bit is 1 and 0th through 0th bits are 0.
"010" -> "011" with the 1st operation.
"011" -> "001" with the 2nd operation since the 0th bit is 1.
"001" -> "000" with the 1st operation.

 

Constraints:

    0 <= n <= 10^9


Hint 1
The fastest way to convert n to zero is to remove all set bits starting from the leftmost one. Try some simple examples to learn the rule of how many steps are needed to remove one set bit.
Hint 2
consider n=2^k case first, then solve for all n.
"""


class Solution1:
    """
    leetcode solution 1: Math and Recursion
    Runtime 0ms Beats 100.00%
    Memory 17.62MB Beats 81.52%
    """

    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        k = 0
        curr = 1
        while (curr * 2) <= n:
            curr *= 2
            k += 1

        return 2 ** (k + 1) - 1 - self.minimumOneBitOperations(n ^ curr)


class Solution2:
    """
    leetcode solution 2: Iteration
    Runtime 0ms Beats 100.00%
    Memory 17.71MB Beats 46.74%
    """

    def minimumOneBitOperations(self, n: int) -> int:
        ans = 0
        k = 0
        mask = 1

        while mask <= n:
            if n & mask:
                ans = 2 ** (k + 1) - 1 - ans

            mask <<= 1
            k += 1

        return ans


class Solution3:
    """
    leetcode solution 3: Gray Code
    Runtime 0ms Beats 100.00%
    Memory 17.91MB Beats 11.96%
    """

    def minimumOneBitOperations(self, n: int) -> int:
        ans = n
        ans ^= ans >> 16
        ans ^= ans >> 8
        ans ^= ans >> 4
        ans ^= ans >> 2
        ans ^= ans >> 1
        return ans
