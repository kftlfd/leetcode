"""
Leetcode
2024-10-19
1545. Find Kth Bit in Nth Binary String
Medium

Given two positive integers n and k, the binary string Sn is formed as follows:

    S1 = "0"
    Si = Si - 1 + "1" + reverse(invert(Si - 1)) for i > 1

Where + denotes the concatenation operation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

For example, the first four strings in the above sequence are:

    S1 = "0"
    S2 = "011"
    S3 = "0111001"
    S4 = "011100110110001"

Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

 

Example 1:

Input: n = 3, k = 1
Output: "0"
Explanation: S3 is "0111001".
The 1st bit is "0".

Example 2:

Input: n = 4, k = 11
Output: "1"
Explanation: S4 is "011100110110001".
The 11th bit is "1".

 

Constraints:

    1 <= n <= 20
    1 <= k <= 2n - 1
"""


class Solution:
    """
    Runtime: 540 ms, faster than 22.49% of Python3 online submissions for Find Kth Bit in Nth Binary String.
    Memory Usage: 65.7 MB, less than 5.33% of Python3 online submissions for Find Kth Bit in Nth Binary String.
    """

    def findKthBit(self, n: int, k: int) -> str:
        s = [0]

        for _ in range(n):
            s += [1] + [x ^ 1 for x in reversed(s)]

        return str(s[k - 1])


class Solution3:
    """
    leetcode solution 3: Iterative Divide and Conquer
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Kth Bit in Nth Binary String.
    Memory Usage: 16.6 MB, less than 72.78% of Python3 online submissions for Find Kth Bit in Nth Binary String.
    """

    def findKthBit(self, n: int, k: int) -> str:
        invert_count = 0
        len_n = (1 << n) - 1  # Length of Sn is 2^n - 1

        while k > 1:
            # If k is in the middle, return based on inversion count
            if k == len_n // 2 + 1:
                return "1" if invert_count % 2 == 0 else "0"

            # If k is in the second half, invert and mirror
            if k > len_n // 2:
                k = len_n + 1 - k  # Mirror position
                invert_count += 1  # Increment inversion count

            len_n //= 2  # Reduce length for next iteration

        # For the first position, return based on inversion count
        return "0" if invert_count % 2 == 0 else "1"


class Solution4:
    """
    leetcode solution 4: Bit Manipulation
    Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Kth Bit in Nth Binary String.
    Memory Usage: 16.5 MB, less than 72.78% of Python3 online submissions for Find Kth Bit in Nth Binary String.
    """

    def findKthBit(self, n: int, k: int) -> str:
        # Find the position of the rightmost set bit in k
        # This helps determine which "section" of the string we're in
        position_in_section = k & -k

        # Determine if k is in the inverted part of the string
        # This checks if the bit to the left of the rightmost set bit is 1
        is_in_inverted_part = ((k // position_in_section) >> 1 & 1) == 1

        # Determine if the original bit (before any inversion) would be 1
        # This is true if k is even (i.e., its least significant bit is 0)
        original_bit_is_one = (k & 1) == 0

        if is_in_inverted_part:
            # If we're in the inverted part, we need to flip the bit
            return "0" if original_bit_is_one else "1"
        else:
            # If we're not in the inverted part, return the original bit
            return "1" if original_bit_is_one else "0"
