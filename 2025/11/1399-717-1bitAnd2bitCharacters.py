"""
Leetcode
2025-11-18
717. 1-bit and 2-bit Characters
Easy

We have two special characters:

    The first character can be represented by one bit 0.
    The second character can be represented by two bits (10 or 11).

Given a binary array bits that ends with 0, return true if the last character must be a one-bit character.

 

Example 1:

Input: bits = [1,0,0]
Output: true
Explanation: The only way to decode it is two-bit character and one-bit character.
So the last character is one-bit character.

Example 2:

Input: bits = [1,1,1,0]
Output: false
Explanation: The only way to decode it is two-bit character and two-bit character.
So the last character is not one-bit character.

 

Constraints:

    1 <= bits.length <= 1000
    bits[i] is either 0 or 1.

 
"""

from typing import List


class Solution:
    """
    Runtime 1ms Beats 21.56%
    Memory 17.89MB Beats 40.84%
    """

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits) - 1
        i = 0

        while i < n:
            i += 2 if bits[i] == 1 else 1

        return i == n


class Solution2:
    """
    leetcode solution 2: Greedy
    Runtime 0ms Beats 100.00%
    Memory 17.67MB Beats 91.02%
    """

    def isOneBitCharacter(self, bits: List[int]) -> bool:
        bits = bits[:]
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0
