"""
Leetcode
2025-01-15
2429. Minimize XOR
Medium
Topics
Companies
Hint

Given two positive integers num1 and num2, find the positive integer x such that:

    x has the same number of set bits as num2, and
    The value x XOR num1 is minimal.

Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.

Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.

 

Constraints:

    1 <= num1, num2 <= 10^9

Hint 1
To arrive at a small xor, try to turn off some bits from num1
Hint 2
If there are still left bits to set, try to set them from the least significant bit
"""


class Solution:
    """
    Runtime 0ms Beats 100.00%
    Memory 17.85MB Beats 23.20%
    """

    def minimizeXor(self, num1: int, num2: int) -> int:
        bits = num2.bit_count()
        ans = 0

        mask = 1 << (num1.bit_length() - 1)
        while mask > 0 and bits > 0:
            if num1 & mask == mask:
                ans |= mask
                bits -= 1
            mask = mask >> 1

        mask = 1
        while bits > 0:
            if ans & mask != mask:
                ans |= mask
                bits -= 1
            mask <<= 1

        return ans


class Solution1:
    """
    leetcode solution 1: From Optimal to Valid
    Runtime 2ms Beats 22.40%
    Memory 17.95MB Beats 14.40%
    """

    def minimizeXor(self, num1: int, num2: int) -> int:
        # Initialize result to num1. We will modify result.
        result = num1

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = bin(result).count("1")

        # Start with the least significant bit (bit 0).
        current_bit = 0

        # Add bits to result if it has fewer set bits than the target.
        while set_bits_count < target_set_bits_count:
            # If the current bit in result is not set (0), set it to 1.
            if not self._is_set(result, current_bit):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            # Move to the next bit.
            current_bit += 1

        # Remove bits from result if it has more set bits than the target.
        while set_bits_count > target_set_bits_count:
            # If the current bit in result is set (1), unset it (make it 0).
            if self._is_set(result, current_bit):
                result = self._unset_bit(result, current_bit)
                set_bits_count -= 1
            # Move to the next bit.
            current_bit += 1

        return result

    # Helper function to check if the given bit position in result is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in result to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)

    # Helper function to unset the given bit position in x (set it to 0).
    def _unset_bit(self, x: int, bit: int):
        return x & ~(1 << bit)


class Solution2:
    """
    leetcode solution 2: Building the Answer
    Runtime 4ms Beats 4.00%
    Memory 18.02MB Beats 14.40%    
    """

    def minimizeXor(self, num1: int, num2: int) -> int:
        result = 0

        target_set_bits_count = bin(num2).count("1")
        set_bits_count = 0
        current_bit = 31  # Start from the most significant bit.

        # While result has fewer set bits than num2
        while set_bits_count < target_set_bits_count:
            # If the current bit of num1 is set or we must set all remaining bits in result
            if self._is_set(num1, current_bit) or (
                target_set_bits_count - set_bits_count > current_bit
            ):
                result = self._set_bit(result, current_bit)
                set_bits_count += 1
            current_bit -= 1  # Move to the next bit.

        return result

    # Helper function to check if the given bit position in x is set (1).
    def _is_set(self, x: int, bit: int) -> bool:
        return (x & (1 << bit)) != 0

    # Helper function to set the given bit position in x to 1.
    def _set_bit(self, x: int, bit: int):
        return x | (1 << bit)
